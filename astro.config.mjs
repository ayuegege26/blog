import { defineConfig } from 'astro/config';
import mdx from '@astrojs/mdx';
import sitemap from '@astrojs/sitemap';

export default defineConfig({
  site: process.env.SITE_URL ?? 'https://ayue-observatory.local',
  integrations: [mdx(), sitemap()],
  output: 'static',
});
