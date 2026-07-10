import { getCollection } from 'astro:content';

export const typeLabels = {
  essay: '随笔',
  research: '研究',
  system: '系统',
  signal: '信号',
  project: '项目',
  failure: '复盘',
  experiment: '实验',
  journal: '记录',
} as const;

export const statusLabels = {
  draft: '草稿',
  active: '活跃',
  stable: '稳定',
  archived: '归档',
  ongoing: '进行中',
} as const;

export const fieldLabels = {
  research: '研究',
  systems: '系统',
  signals: '信号',
  essays: '随笔',
  projects: '项目',
  experiments: '实验',
} as const;

function getObjectTimeValue(object: { data: { updated?: Date; date: Date } }) {
  return (object.data.updated ?? object.data.date).valueOf();
}

export function sortArchiveObjects<T extends { id: string; data: { featured: boolean; priority: number; updated?: Date; date: Date } }>(
  objects: T[],
) {
  return [...objects].sort((a, b) => {
    if (a.data.featured !== b.data.featured) return Number(b.data.featured) - Number(a.data.featured);

    const priorityDelta = a.data.priority - b.data.priority;
    if (priorityDelta !== 0) return priorityDelta;

    const dateDelta = getObjectTimeValue(b) - getObjectTimeValue(a);
    if (dateDelta !== 0) return dateDelta;

    return a.id.localeCompare(b.id);
  });
}

export async function getArchiveObjects() {
  const objects = await getCollection('archive', ({ data }) => !data.draft);
  return sortArchiveObjects(objects);
}

export async function getFeaturedObjects(limit = 8) {
  const objects = await getArchiveObjects();
  return sortArchiveObjects(objects.filter((object) => object.data.featured)).slice(0, limit);
}

export function formatDate(date: Date) {
  return new Intl.DateTimeFormat('zh-CN', {
    year: 'numeric',
    month: '2-digit',
    day: '2-digit',
  }).format(date);
}
