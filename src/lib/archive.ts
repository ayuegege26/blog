import { getCollection } from 'astro:content';

export const typeLabels = {
  essay: 'Essay / 随笔',
  research: 'Research / 研究',
  system: 'System / 系统',
  signal: 'Signal / 信号',
  project: 'Project / 项目',
  failure: 'Failure / 复盘',
  experiment: 'Experiment / 实验',
  journal: 'Journal / 记录',
} as const;

export const statusLabels = {
  draft: 'draft',
  active: 'active',
  stable: 'stable',
  archived: 'archived',
  ongoing: 'ongoing',
} as const;

export const fieldLabels = {
  research: 'Research',
  systems: 'Systems',
  signals: 'Signals',
  essays: 'Essays',
  projects: 'Projects',
  experiments: 'Experiments',
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
