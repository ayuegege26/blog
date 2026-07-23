import * as THREE from 'three';

type Point3 = readonly [number, number, number];
type Point2 = readonly [number, number];

export type VS002ProximityShape =
  | {
      kind: 'sphere';
      center: Point3;
      radius: number;
    }
  | {
      kind: 'vertical-cylinder';
      center: Point2;
      radius: number;
      minY: number;
      maxY: number;
    }
  | {
      kind: 'annulus';
      center: Point2;
      radius: number;
      halfWidth: number;
      y: number;
      halfHeight: number;
    }
  | {
      kind: 'segment';
      start: Point3;
      end: Point3;
      radius: number;
    };

export interface VS002ProximityNodeConfig {
  id: string;
  label: string;
  profile: 'core' | 'ring' | 'well' | 'bridge' | 'floating' | 'probe';
  priority: number;
  enterDistance: number;
  exitDistance: number;
  anchor: Point3;
  shape: VS002ProximityShape;
}

export interface VS002ProximityNodeState {
  config: VS002ProximityNodeConfig;
  active: boolean;
  activation: number;
  distance: number;
  transition: 'enter' | 'exit' | null;
}

export interface VS002ProximitySnapshot {
  states: readonly VS002ProximityNodeState[];
  focus: VS002ProximityNodeState | null;
}

const pointA = new THREE.Vector3();
const pointB = new THREE.Vector3();
const segmentDirection = new THREE.Vector3();
const pointOffset = new THREE.Vector3();

const distanceToShape = (position: THREE.Vector3, shape: VS002ProximityShape) => {
  if (shape.kind === 'sphere') {
    pointA.fromArray(shape.center);
    return Math.max(0, position.distanceTo(pointA) - shape.radius);
  }

  if (shape.kind === 'vertical-cylinder') {
    const horizontal = Math.max(
      0,
      Math.hypot(position.x - shape.center[0], position.z - shape.center[1]) - shape.radius,
    );
    const vertical = position.y < shape.minY
      ? shape.minY - position.y
      : position.y > shape.maxY
        ? position.y - shape.maxY
        : 0;
    return Math.hypot(horizontal, vertical);
  }

  if (shape.kind === 'annulus') {
    const radial = Math.hypot(position.x - shape.center[0], position.z - shape.center[1]);
    const horizontal = Math.max(0, Math.abs(radial - shape.radius) - shape.halfWidth);
    const vertical = Math.max(0, Math.abs(position.y - shape.y) - shape.halfHeight);
    return Math.hypot(horizontal, vertical);
  }

  pointA.fromArray(shape.start);
  pointB.fromArray(shape.end);
  segmentDirection.subVectors(pointB, pointA);
  pointOffset.subVectors(position, pointA);
  const lengthSquared = segmentDirection.lengthSq();
  const t = lengthSquared > 0
    ? THREE.MathUtils.clamp(pointOffset.dot(segmentDirection) / lengthSquared, 0, 1)
    : 0;
  pointA.addScaledVector(segmentDirection, t);
  return Math.max(0, position.distanceTo(pointA) - shape.radius);
};

export class VS002ProximityRegistry {
  private readonly states: VS002ProximityNodeState[];

  constructor(configs: readonly VS002ProximityNodeConfig[]) {
    this.states = configs.map((config) => ({
      config,
      active: false,
      activation: 0,
      distance: Number.POSITIVE_INFINITY,
      transition: null,
    }));
  }

  update(position: THREE.Vector3, delta: number): VS002ProximitySnapshot {
    for (const state of this.states) {
      state.distance = distanceToShape(position, state.config.shape);
      const wasActive = state.active;
      const threshold = wasActive ? state.config.exitDistance : state.config.enterDistance;
      state.active = state.distance <= threshold;
      state.transition = state.active === wasActive ? null : state.active ? 'enter' : 'exit';
      state.activation = THREE.MathUtils.damp(
        state.activation,
        state.active ? 1 : 0,
        state.active ? 5.2 : 3.8,
        delta,
      );
    }

    const focus = this.states
      .filter((state) => state.active)
      .sort((left, right) => (
        right.config.priority - left.config.priority
        || left.distance - right.distance
      ))[0] ?? null;

    return { states: this.states, focus };
  }
}

export const VS002_PROBE_PROXIMITY_NODES: readonly VS002ProximityNodeConfig[] = [
  {
    id: 'probe-core',
    label: 'NAS CORE',
    profile: 'probe',
    priority: 100,
    enterDistance: 12.5,
    exitDistance: 15.5,
    anchor: [0, 31.4, 14.25],
    shape: {
      kind: 'sphere',
      center: [0, 31.4, 14.25],
      radius: 0,
    },
  },
];

export const VS002_FORMAL_PROXIMITY_NODES: readonly VS002ProximityNodeConfig[] = [
  {
    id: 'core',
    label: 'CORE TOWER',
    profile: 'core',
    priority: 100,
    enterDistance: 6.05,
    exitDistance: 9.9,
    anchor: [0, 30, 0],
    shape: {
      kind: 'vertical-cylinder',
      center: [0, 0],
      radius: 14,
      minY: 1,
      maxY: 60,
    },
  },
  {
    id: 'upper-ring',
    label: 'UPPER RING',
    profile: 'ring',
    priority: 90,
    enterDistance: 4.4,
    exitDistance: 7.7,
    anchor: [0, 29.5, 34],
    shape: {
      kind: 'annulus',
      center: [0, 0],
      radius: 34,
      halfWidth: 3,
      y: 29.5,
      halfHeight: 3.2,
    },
  },
  {
    id: 'upper-ring-east',
    label: 'UPPER RING / EAST',
    profile: 'ring',
    priority: 89,
    enterDistance: 4.4,
    exitDistance: 7.7,
    anchor: [35.8, 32, 0],
    shape: {
      kind: 'sphere',
      center: [35.8, 32, 0],
      radius: 0,
    },
  },
  {
    id: 'upper-ring-north',
    label: 'UPPER RING / NORTH',
    profile: 'ring',
    priority: 89,
    enterDistance: 4.4,
    exitDistance: 7.7,
    anchor: [0, 32, 35.8],
    shape: {
      kind: 'sphere',
      center: [0, 32, 35.8],
      radius: 0,
    },
  },
  {
    id: 'upper-ring-west',
    label: 'UPPER RING / WEST',
    profile: 'ring',
    priority: 89,
    enterDistance: 4.4,
    exitDistance: 7.7,
    anchor: [-35.8, 32, 0],
    shape: {
      kind: 'sphere',
      center: [-35.8, 32, 0],
      radius: 0,
    },
  },
  {
    id: 'upper-ring-south',
    label: 'UPPER RING / SOUTH',
    profile: 'ring',
    priority: 89,
    enterDistance: 4.4,
    exitDistance: 7.7,
    anchor: [0, 32, -35.8],
    shape: {
      kind: 'sphere',
      center: [0, 32, -35.8],
      radius: 0,
    },
  },
  {
    id: 'main-ring',
    label: 'MAIN RING',
    profile: 'ring',
    priority: 86,
    enterDistance: 4.95,
    exitDistance: 8.25,
    anchor: [0, 16, 42],
    shape: {
      kind: 'annulus',
      center: [0, 0],
      radius: 42,
      halfWidth: 5,
      y: 16,
      halfHeight: 4.8,
    },
  },
  {
    id: 'well-a',
    label: 'VERTICAL WELL A',
    profile: 'well',
    priority: 80,
    enterDistance: 5.5,
    exitDistance: 8.8,
    anchor: [-42, 20, 42],
    shape: {
      kind: 'vertical-cylinder',
      center: [-42, 42],
      radius: 6,
      minY: 1,
      maxY: 36,
    },
  },
  {
    id: 'well-b',
    label: 'VERTICAL WELL B',
    profile: 'well',
    priority: 80,
    enterDistance: 5.5,
    exitDistance: 8.8,
    anchor: [42, 20, -42],
    shape: {
      kind: 'vertical-cylinder',
      center: [42, -42],
      radius: 5.5,
      minY: 1,
      maxY: 35,
    },
  },
  {
    id: 'floating-group',
    label: 'FLOATING GROUP',
    profile: 'floating',
    priority: 76,
    enterDistance: 6.6,
    exitDistance: 11,
    anchor: [50, 40, 48],
    shape: {
      kind: 'sphere',
      center: [50, 40, 48],
      radius: 12,
    },
  },
  {
    id: 'bridge-a',
    label: 'BRIDGE A',
    profile: 'bridge',
    priority: 70,
    enterDistance: 4.4,
    exitDistance: 7.7,
    anchor: [-36, 28, 36],
    shape: {
      kind: 'segment',
      start: [-29.7, 24, 29.7],
      end: [-42, 31, 42],
      radius: 3,
    },
  },
  {
    id: 'bridge-b',
    label: 'BRIDGE B',
    profile: 'bridge',
    priority: 70,
    enterDistance: 4.4,
    exitDistance: 7.7,
    anchor: [40, 34, 39],
    shape: {
      kind: 'segment',
      start: [29.7, 30, 29.7],
      end: [50, 38, 48],
      radius: 3,
    },
  },
  {
    id: 'bridge-c',
    label: 'BRIDGE C',
    profile: 'bridge',
    priority: 70,
    enterDistance: 4.4,
    exitDistance: 7.7,
    anchor: [36, 25, -36],
    shape: {
      kind: 'segment',
      start: [29.7, 22, -29.7],
      end: [42, 28, -42],
      radius: 3,
    },
  },
];
