export type VS002ClickPoint = readonly [number, number, number];
export type VS002ClickNodeRole = 'standard' | 'exit';

export interface VS002ClickNodeConfig {
  id: string;
  proximityId: string;
  number: string;
  label: string;
  region: string;
  position: VS002ClickPoint;
  role?: VS002ClickNodeRole;
  actionLabel?: string;
  actionHref?: string;
  placeholderTitle: string;
  placeholderBody: string;
}

const placeholder = (number: string, region: string): Pick<VS002ClickNodeConfig, 'placeholderTitle' | 'placeholderBody'> => ({
  placeholderTitle: `Content Placeholder ${number}`,
  placeholderBody: `此处预留给「${region}」节点的正式信息。当前只用于验证信息展开、节点切换与收起逻辑。`,
});

export const VS002_FORMAL_CLICK_NODES: readonly VS002ClickNodeConfig[] = [
  {
    id: 'node-01-core',
    proximityId: 'core',
    number: '01',
    label: 'CORE CROWN',
    region: '核心主塔顶部',
    position: [0, 59, 0],
    ...placeholder('01', '核心主塔顶部'),
  },
  {
    id: 'node-02-upper-ring',
    proximityId: 'upper-ring',
    number: '02',
    label: 'UPPER RING',
    region: '上层环',
    position: [26, 32.2, 26],
    ...placeholder('02', '上层环'),
  },
  {
    id: 'node-03-main-ring',
    proximityId: 'upper-ring-east',
    number: '03',
    label: 'UPPER RING / EAST',
    region: '上层环 / 东段',
    position: [35.8, 32, 0],
    ...placeholder('03', '上层环 / 东段'),
  },
  {
    id: 'node-04-well-a',
    proximityId: 'well-a',
    number: '04',
    label: 'VERTICAL WELL A',
    region: '垂直井 A 顶端',
    position: [-42, 36.1, 42],
    ...placeholder('04', '垂直井 A 顶端'),
  },
  {
    id: 'node-05-well-b',
    proximityId: 'well-b',
    number: '05',
    label: 'VERTICAL WELL B',
    region: '垂直井 B 顶端',
    position: [42, 36.1, -42],
    ...placeholder('05', '垂直井 B 顶端'),
  },
  {
    id: 'node-06-floating-group',
    proximityId: 'floating-group',
    number: '06',
    label: 'FLOATING GROUP',
    region: '悬浮建筑群',
    position: [50, 43, 42.5],
    role: 'exit',
    actionLabel: '返回 Visual Systems',
    actionHref: '/lab/visual-systems',
    ...placeholder('06', '悬浮建筑群'),
    placeholderTitle: 'World Exit',
    placeholderBody: '此节点暂作世界出口。点击下方返回链接才会离开地图；再次点击节点、点击其他位置或按 ESC 只会收起信息。',
  },
  {
    id: 'node-07-upper-ring-north',
    proximityId: 'upper-ring-north',
    number: '07',
    label: 'UPPER RING / NORTH',
    region: '上层环 / 北段',
    position: [0, 32, 35.8],
    ...placeholder('07', '上层环 / 北段'),
  },
  {
    id: 'node-08-upper-ring-west',
    proximityId: 'upper-ring-west',
    number: '08',
    label: 'UPPER RING / WEST',
    region: '上层环 / 西段',
    position: [-35.8, 32, 0],
    ...placeholder('08', '上层环 / 西段'),
  },
  {
    id: 'node-09-upper-ring-south',
    proximityId: 'upper-ring-south',
    number: '09',
    label: 'UPPER RING / SOUTH',
    region: '上层环 / 南段',
    position: [0, 32, -35.8],
    ...placeholder('09', '上层环 / 南段'),
  },
] as const;
