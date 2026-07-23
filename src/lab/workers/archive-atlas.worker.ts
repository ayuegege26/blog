import type { ArchiveAtlasNode } from '../data/archive-atlas';

type FilterMessage = {
  type: 'filter';
  nodes: ArchiveAtlasNode[];
  query: string;
  contentType: string;
  status: string;
  field: string;
};

self.addEventListener('message', (event: MessageEvent<FilterMessage>) => {
  if (event.data.type !== 'filter') return;
  const { nodes, query, contentType, status, field } = event.data;
  const normalized = query.trim().toLocaleLowerCase('zh-CN');
  const ids = nodes
    .filter((node) => contentType === 'all' || node.type === contentType)
    .filter((node) => status === 'all' || node.status === status)
    .filter((node) => field === 'all' || node.field === field)
    .filter((node) => {
      if (!normalized) return true;
      return [node.title, node.summary, node.objectId, ...node.tags]
        .join(' ')
        .toLocaleLowerCase('zh-CN')
        .includes(normalized);
    })
    .map((node) => node.id);

  self.postMessage({ type: 'filtered', ids });
});
