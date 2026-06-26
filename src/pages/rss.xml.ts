import rss from '@astrojs/rss';
import type { APIContext } from 'astro';
import { getArchiveObjects } from '@lib/archive';

export async function GET(context: APIContext) {
  const objects = await getArchiveObjects();

  return rss({
    title: 'Ayue Observatory',
    description: '一个关于研究、系统、信号、随笔与实验的长期个人观测站。',
    site: context.site ?? new URL('https://ayue-observatory.local'),
    items: objects.map((object) => ({
      title: object.data.title,
      description: object.data.summary,
      pubDate: object.data.updated ?? object.data.date,
      link: `/archive/${object.id}/`,
      categories: [object.data.type, object.data.field, ...object.data.tags],
    })),
  });
}
