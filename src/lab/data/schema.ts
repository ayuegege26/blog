export const LAB_API_MAJOR = 1;

export type SourceStatus = 'ok' | 'partial' | 'unavailable';
export type SystemStatus = 'online' | 'degraded' | 'offline' | 'unknown';
export type ServiceStatus = SystemStatus | 'maintenance';
export type ServiceCategory = 'storage' | 'knowledge' | 'automation' | 'media' | 'network' | 'development' | 'cloud' | 'other';
export type ActivityLevel = 'idle' | 'low' | 'medium' | 'high' | 'unknown';

export interface Envelope<T> {
  schemaVersion: string;
  generatedAt: string;
  staleAfterSeconds: number;
  sourceStatus: SourceStatus;
  data: T;
}

export interface NasService {
  id: string;
  label: string;
  category: ServiceCategory;
  status: ServiceStatus;
  availabilityRatio24h: number | null;
  activityLevel: ActivityLevel;
  dependsOn?: string[];
}

export interface NasSnapshotData {
  system: { id: string; label: string; status: SystemStatus; uptimeSeconds: number | null };
  metrics: { cpuUsageRatio: number | null; memoryUsageRatio: number | null; temperatureCelsius: number | null };
  storage: { usedBytes: number | null; totalBytes: number | null; usageRatio: number | null; change24hBytes: number | null };
  backup: { lastCompletedAt: string | null; lastResult: 'success' | 'partial' | 'failed' | 'unknown' };
  services: NasService[];
}

export interface NasHistoryData {
  range: '24h' | '7d';
  resolutionSeconds: number;
  points: Array<{
    timestamp: string;
    cpuUsageRatioAvg: number | null;
    memoryUsageRatioAvg: number | null;
    temperatureCelsiusAvg: number | null;
    storageUsageRatio: number | null;
    onlineServiceRatio: number | null;
  }>;
}

const categories = new Set<ServiceCategory>(['storage', 'knowledge', 'automation', 'media', 'network', 'development', 'cloud', 'other']);
const systemStatuses = new Set<SystemStatus>(['online', 'degraded', 'offline', 'unknown']);
const serviceStatuses = new Set<ServiceStatus>(['online', 'degraded', 'offline', 'unknown', 'maintenance']);
const activities = new Set<ActivityLevel>(['idle', 'low', 'medium', 'high', 'unknown']);

function invariant(value: unknown, message: string): asserts value {
  if (!value) throw new Error(`Lab schema: ${message}`);
}

function ratio(value: unknown, path: string) {
  invariant(value === null || (typeof value === 'number' && value >= 0 && value <= 1), `${path} must be null or a ratio`);
}

function validateEnvelope(value: unknown): asserts value is Envelope<unknown> {
  invariant(value && typeof value === 'object', 'response must be an object');
  const item = value as Record<string, unknown>;
  invariant(typeof item.schemaVersion === 'string', 'schemaVersion is required');
  invariant(typeof item.generatedAt === 'string' && !Number.isNaN(Date.parse(item.generatedAt)), 'generatedAt must be ISO time');
  invariant(typeof item.staleAfterSeconds === 'number' && item.staleAfterSeconds > 0, 'staleAfterSeconds must be positive');
  invariant(['ok', 'partial', 'unavailable'].includes(String(item.sourceStatus)), 'sourceStatus is invalid');
  invariant('data' in item, 'data is required');
}

export function assertSupportedVersion(schemaVersion: string) {
  const major = Number.parseInt(schemaVersion.split('.')[0] ?? '', 10);
  invariant(major === LAB_API_MAJOR, `unsupported schema major ${schemaVersion}`);
}

export function validateNasSnapshot(value: unknown): asserts value is Envelope<NasSnapshotData> {
  validateEnvelope(value);
  const envelope = value as Envelope<NasSnapshotData>;
  assertSupportedVersion(envelope.schemaVersion);
  const data = envelope.data;
  invariant(data && typeof data === 'object', 'snapshot data is required');
  invariant(systemStatuses.has(data.system.status), 'system.status is invalid');
  ratio(data.metrics.cpuUsageRatio, 'metrics.cpuUsageRatio');
  ratio(data.metrics.memoryUsageRatio, 'metrics.memoryUsageRatio');
  ratio(data.storage.usageRatio, 'storage.usageRatio');
  invariant(Array.isArray(data.services), 'services must be an array');
  const ids = new Set<string>();
  for (const service of data.services) {
    invariant(/^[a-z0-9]+(?:-[a-z0-9]+)*$/.test(service.id), `invalid public service id ${service.id}`);
    invariant(!ids.has(service.id), `duplicate public service id ${service.id}`);
    ids.add(service.id);
    invariant(categories.has(service.category), `invalid category for ${service.id}`);
    invariant(serviceStatuses.has(service.status), `invalid status for ${service.id}`);
    invariant(activities.has(service.activityLevel), `invalid activity for ${service.id}`);
    ratio(service.availabilityRatio24h, `${service.id}.availabilityRatio24h`);
  }
  for (const service of data.services) {
    for (const dependency of service.dependsOn ?? []) invariant(ids.has(dependency), `${service.id} references missing dependency ${dependency}`);
  }
}

export function validateNasHistory(value: unknown): asserts value is Envelope<NasHistoryData> {
  validateEnvelope(value);
  const envelope = value as Envelope<NasHistoryData>;
  assertSupportedVersion(envelope.schemaVersion);
  invariant(['24h', '7d'].includes(envelope.data.range), 'history range is invalid');
  invariant(envelope.data.resolutionSeconds > 0, 'history resolution must be positive');
  invariant(Array.isArray(envelope.data.points), 'history points must be an array');
  let previous = 0;
  for (const point of envelope.data.points) {
    const timestamp = Date.parse(point.timestamp);
    invariant(!Number.isNaN(timestamp) && timestamp > previous, 'history timestamps must be valid and ascending');
    previous = timestamp;
    ratio(point.cpuUsageRatioAvg, 'history.cpuUsageRatioAvg');
    ratio(point.memoryUsageRatioAvg, 'history.memoryUsageRatioAvg');
    ratio(point.storageUsageRatio, 'history.storageUsageRatio');
    ratio(point.onlineServiceRatio, 'history.onlineServiceRatio');
  }
}
