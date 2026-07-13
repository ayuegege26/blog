import {
  validateNasHistory,
  validateNasSnapshot,
  type Envelope,
  type NasHistoryData,
  type NasSnapshotData,
} from './schema';

export type DataState = 'loading' | 'fresh' | 'stale' | 'partial' | 'empty' | 'unavailable' | 'incompatible' | 'offline';
export type SimulationState = Exclude<DataState, 'loading'> | null;

export interface LoadedNasData {
  state: DataState;
  snapshot?: Envelope<NasSnapshotData>;
  history?: Envelope<NasHistoryData>;
  message?: string;
}

function clone<T>(value: T): T {
  return JSON.parse(JSON.stringify(value)) as T;
}

function applySimulation(snapshot: Envelope<NasSnapshotData>, simulation: SimulationState) {
  const next = clone(snapshot);
  if (!simulation || simulation === 'fresh') {
    next.generatedAt = new Date().toISOString();
    return next;
  }
  if (simulation === 'stale') next.generatedAt = new Date(Date.now() - next.staleAfterSeconds * 2000).toISOString();
  if (simulation === 'partial') next.sourceStatus = 'partial';
  if (simulation === 'empty') next.data.services = [];
  if (simulation === 'incompatible') next.schemaVersion = '2.0';
  return next;
}

export function resolveDataState(snapshot: Envelope<NasSnapshotData>): DataState {
  if (snapshot.sourceStatus === 'partial') return 'partial';
  if (snapshot.data.services.length === 0) return 'empty';
  const expiresAt = Date.parse(snapshot.generatedAt) + snapshot.staleAfterSeconds * 1000;
  return Date.now() > expiresAt ? 'stale' : 'fresh';
}

async function fetchJson(url: string) {
  const response = await fetch(url, { headers: { Accept: 'application/json' } });
  if (!response.ok) throw new Error(`gateway_${response.status}`);
  return response.json() as Promise<unknown>;
}

export async function loadNasData(options: {
  fixtureSnapshot: unknown;
  fixtureHistory: unknown;
  mode: 'fixture' | 'gateway';
  range: '24h' | '7d';
  simulation?: SimulationState;
}): Promise<LoadedNasData> {
  const { mode, range, simulation = null } = options;
  try {
    if (simulation === 'offline') throw new TypeError('simulated network failure');
    if (simulation === 'unavailable') throw new Error('gateway_503');
    const snapshotValue = mode === 'gateway'
      ? await fetchJson('/api/lab/v1/nas/snapshot')
      : applySimulation(options.fixtureSnapshot as Envelope<NasSnapshotData>, simulation);
    const historyValue = mode === 'gateway'
      ? await fetchJson(`/api/lab/v1/nas/history?range=${range}`)
      : options.fixtureHistory;
    validateNasSnapshot(snapshotValue);
    validateNasHistory(historyValue);
    return {
      state: resolveDataState(snapshotValue),
      snapshot: snapshotValue,
      history: historyValue,
    };
  } catch (error) {
    const message = error instanceof Error ? error.message : String(error);
    if (message.includes('unsupported schema major')) return { state: 'incompatible', message };
    if (error instanceof TypeError) return { state: 'offline', message: '无法连接数据网关。' };
    return { state: 'unavailable', message: '当前没有可用的公开 NAS 快照。' };
  }
}
