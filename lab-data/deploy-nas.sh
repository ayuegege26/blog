#!/bin/sh
set -eu

PROJECT=/vol2/projects/ayue-observatory
ARCHIVE=/home/ayuegege26/ayue-observatory-deploy.tgz
SERVICE_USER=com.dustinky.qwenpaw
SERVICE_GROUP=com.dustinky.qwenpaw
STAMP=$(date +%Y%m%d-%H%M%S)
BACKUP_ROOT=/vol2/projects/ayue-observatory-backups
BACKUP="$BACKUP_ROOT/$STAMP"
NGINX_SITE=/etc/nginx/sites-available/ayue-observatory

mkdir -p "$BACKUP"
if [ -d "$PROJECT/dist" ]; then
  cp -a "$PROJECT/dist" "$BACKUP/dist"
fi
if [ -f "$NGINX_SITE" ]; then
  cp -a "$NGINX_SITE" "$BACKUP/nginx-ayue-observatory"
fi

tar -xzf "$ARCHIVE" -C "$PROJECT"
chown -R "$SERVICE_USER:$SERVICE_GROUP" "$PROJECT"

runuser -u "$SERVICE_USER" -- /usr/bin/python3 "$PROJECT/lab-data/collector.py"

install -m 0644 "$PROJECT/lab-data/ayue-lab-gateway.service" /etc/systemd/system/ayue-lab-gateway.service
systemctl daemon-reload
systemctl enable --now ayue-lab-gateway.service

python3 - "$NGINX_SITE" <<'PY'
from pathlib import Path
import sys

path = Path(sys.argv[1])
text = path.read_text()
marker = "# ayue-lab-data-gateway"
if marker not in text:
    block = """    # ayue-lab-data-gateway
    location /api/lab/v1/ {
        proxy_pass http://127.0.0.1:18101;
        proxy_http_version 1.1;
        proxy_set_header Host $host;
        proxy_set_header X-Forwarded-Proto $scheme;
        proxy_connect_timeout 2s;
        proxy_read_timeout 5s;
    }

"""
    needle = "    location / {"
    if needle not in text:
        raise SystemExit(f"cannot find insertion point in {path}")
    path.write_text(text.replace(needle, block + needle, 1))
PY

if nginx -t; then
  systemctl reload nginx
  # This NAS also runs /usr/trim/nginx, which can own the shared PID file.
  # Explicitly signal the Debian nginx master that serves port 8818.
  SITE_NGINX_MASTER=$(pgrep -f '^nginx: master process /usr/sbin/nginx' || true)
  if [ -n "$SITE_NGINX_MASTER" ]; then
    kill -HUP "$SITE_NGINX_MASTER"
  fi
else
  cp "$BACKUP/nginx-ayue-observatory" "$NGINX_SITE"
  nginx -t
  exit 1
fi

CRON_TMP=$(mktemp)
trap 'rm -f "$CRON_TMP"' EXIT
crontab -u "$SERVICE_USER" -l 2>/dev/null | grep -v 'ayue-observatory/lab-data/collector.py' > "$CRON_TMP" || true
printf '%s\n' '0 * * * * /usr/bin/python3 /vol2/projects/ayue-observatory/lab-data/collector.py >> /vol2/projects/ayue-observatory/lab-data/collector.log 2>&1' >> "$CRON_TMP"
crontab -u "$SERVICE_USER" "$CRON_TMP"

printf 'BACKUP=%s\n' "$BACKUP"
systemctl --no-pager --full status ayue-lab-gateway.service | sed -n '1,12p'
crontab -u "$SERVICE_USER" -l
