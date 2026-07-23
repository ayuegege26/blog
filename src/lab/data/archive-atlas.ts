export type AtlasType =
  | 'essay'
  | 'research'
  | 'system'
  | 'signal'
  | 'project'
  | 'failure'
  | 'experiment'
  | 'journal'
  | 'unknown';

export type AtlasField = 'research' | 'systems' | 'signals' | 'essays' | 'projects' | 'experiments';
export type AtlasStatus = 'draft' | 'active' | 'stable' | 'archived' | 'ongoing' | 'future';

export interface ArchiveAtlasNode {
  id: string;
  objectId: string;
  title: string;
  summary: string;
  date: string;
  dateLabel: string;
  updated: string | null;
  updatedLabel: string | null;
  type: AtlasType;
  field: AtlasField;
  status: AtlasStatus;
  tags: string[];
  readingMinutes: number;
  readingLabel: string;
  readingWeight: number;
  timePosition: number;
  related: string[];
  href: string;
}
