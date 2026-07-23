import { defineConfig } from 'astro/config';
import mdx from '@astrojs/mdx';
import sitemap from '@astrojs/sitemap';

export default defineConfig({
  site: process.env.SITE_URL ?? 'http://blog.ayuegege26.xyz',
  integrations: [mdx(), sitemap()],
  output: 'static',
});
