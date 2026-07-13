import { createServer } from 'node:http';
import { readFile, stat } from 'node:fs/promises';
import { extname, resolve, sep } from 'node:path';

const host = process.env.LOCAL_SITE_HOST ?? '127.0.0.1';
const port = Number(process.env.LOCAL_SITE_PORT ?? 4321);
const gatewayOrigin = process.env.NAS_LAB_ORIGIN ?? 'http://192.168.1.60:8818';
const distRoot = resolve(process.cwd(), 'dist');

const contentTypes = {
  '.css': 'text/css; charset=utf-8',
  '.html': 'text/html; charset=utf-8',
  '.ico': 'image/x-icon',
  '.js': 'text/javascript; charset=utf-8',
  '.json': 'application/json; charset=utf-8',
  '.png': 'image/png',
  '.svg': 'image/svg+xml; charset=utf-8',
  '.webp': 'image/webp',
  '.xml': 'application/xml; charset=utf-8',
};

function send(response, status, body, headers = {}) {
  response.writeHead(status, { 'Cache-Control': 'no-cache', ...headers });
  response.end(body);
}

async function proxyLabData(request, response, url) {
  try {
    const upstream = await fetch(new URL(url.pathname + url.search, gatewayOrigin), {
      headers: { Accept: request.headers.accept ?? 'application/json' },
      signal: AbortSignal.timeout(5000),
    });
    const body = Buffer.from(await upstream.arrayBuffer());
    send(response, upstream.status, body, {
      'Content-Type': upstream.headers.get('content-type') ?? 'application/json; charset=utf-8',
      'X-Local-Proxy': 'nas-lab-gateway',
    });
  } catch {
    send(response, 502, JSON.stringify({ error: 'nas_gateway_unavailable' }), {
      'Content-Type': 'application/json; charset=utf-8',
    });
  }
}

async function resolveStaticPath(pathname) {
  const decoded = decodeURIComponent(pathname);
  const relative = decoded.replace(/^\/+/, '');
  const candidate = resolve(distRoot, relative);
  if (candidate !== distRoot && !candidate.startsWith(distRoot + sep)) return null;
  try {
    const info = await stat(candidate);
    if (info.isDirectory()) return resolve(candidate, 'index.html');
    return candidate;
  } catch {
    if (!extname(candidate)) {
      const htmlCandidate = `${candidate}.html`;
      try {
        if ((await stat(htmlCandidate)).isFile()) return htmlCandidate;
      } catch { /* use the static 404 page */ }
    }
    return null;
  }
}

createServer(async (request, response) => {
  const url = new URL(request.url ?? '/', `http://${request.headers.host ?? host}`);
  if (url.pathname.startsWith('/api/lab/v1/')) {
    await proxyLabData(request, response, url);
    return;
  }

  const file = await resolveStaticPath(url.pathname);
  if (!file) {
    const notFound = await readFile(resolve(distRoot, '404.html'));
    send(response, 404, notFound, { 'Content-Type': 'text/html; charset=utf-8' });
    return;
  }

  try {
    const body = await readFile(file);
    send(response, 200, request.method === 'HEAD' ? undefined : body, {
      'Content-Type': contentTypes[extname(file)] ?? 'application/octet-stream',
    });
  } catch {
    send(response, 500, 'Internal Server Error', { 'Content-Type': 'text/plain; charset=utf-8' });
  }
}).listen(port, host, () => {
  console.log(`Ayue Observatory local QA: http://${host}:${port}`);
  console.log(`Lab data proxy: ${gatewayOrigin}/api/lab/v1/`);
});
