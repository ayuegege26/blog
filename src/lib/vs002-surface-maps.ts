import * as THREE from 'three';

export interface VS002SurfaceMaps {
  colorMap: THREE.CanvasTexture;
  roughnessMap: THREE.CanvasTexture;
  dispose: () => void;
}

export const createVS002SurfaceMaps = (): VS002SurfaceMaps => {
  const size = 512;
  const colorCanvas = document.createElement('canvas');
  const roughnessCanvas = document.createElement('canvas');
  colorCanvas.width = colorCanvas.height = size;
  roughnessCanvas.width = roughnessCanvas.height = size;
  const colorContext = colorCanvas.getContext('2d')!;
  const roughnessContext = roughnessCanvas.getContext('2d')!;

  colorContext.fillStyle = '#335661';
  colorContext.fillRect(0, 0, size, size);
  roughnessContext.fillStyle = '#aaaaaa';
  roughnessContext.fillRect(0, 0, size, size);

  const xBreaks = [0, 124, 286, 408, size];
  const yBreaks = [0, 70, 154, 244, 332, 430, size];

  for (let row = 0; row < yBreaks.length - 1; row += 1) {
    for (let column = 0; column < xBreaks.length - 1; column += 1) {
      const left = xBreaks[column];
      const right = xBreaks[column + 1];
      const top = yBreaks[row];
      const bottom = yBreaks[row + 1];
      const variation = ((row * 13 + column * 7) % 5) - 2;

      const colorGradient = colorContext.createLinearGradient(left, top, right, bottom);
      colorGradient.addColorStop(0, `rgb(${49 + variation}, ${82 + variation}, ${94 + variation})`);
      colorGradient.addColorStop(1, `rgb(${53 - variation}, ${87 - variation}, ${99 - variation})`);
      colorContext.fillStyle = colorGradient;
      colorContext.fillRect(left, top, right - left, bottom - top);

      const roughnessStart = 168 + variation * 2;
      const roughnessEnd = 173 - variation * 2;
      const roughnessGradient = roughnessContext.createLinearGradient(left, top, right, bottom);
      roughnessGradient.addColorStop(0, `rgb(${roughnessStart}, ${roughnessStart}, ${roughnessStart})`);
      roughnessGradient.addColorStop(1, `rgb(${roughnessEnd}, ${roughnessEnd}, ${roughnessEnd})`);
      roughnessContext.fillStyle = roughnessGradient;
      roughnessContext.fillRect(left, top, right - left, bottom - top);
    }
  }

  colorContext.lineWidth = 3;
  colorContext.strokeStyle = '#17333c';
  roughnessContext.lineWidth = 3;
  roughnessContext.strokeStyle = '#bcbcbc';
  for (const x of xBreaks.slice(1, -1)) {
    colorContext.beginPath();
    colorContext.moveTo(x, 0);
    colorContext.lineTo(x, size);
    colorContext.stroke();
    roughnessContext.beginPath();
    roughnessContext.moveTo(x, 0);
    roughnessContext.lineTo(x, size);
    roughnessContext.stroke();
  }

  const horizontalSegments = [
    [[0, 286], [408, size]],
    [[124, 408]],
    [[0, 124], [286, size]],
    [[0, 408]],
    [[124, 286], [408, size]],
  ];
  yBreaks.slice(1, -1).forEach((y, index) => {
    horizontalSegments[index].forEach(([start, end]) => {
      colorContext.beginPath();
      colorContext.moveTo(start, y);
      colorContext.lineTo(end, y);
      colorContext.stroke();
      roughnessContext.beginPath();
      roughnessContext.moveTo(start, y);
      roughnessContext.lineTo(end, y);
      roughnessContext.stroke();
    });
  });

  colorContext.fillStyle = '#3aa4a7';
  colorContext.fillRect(38, 226, 74, 4);
  colorContext.fillRect(374, 366, 58, 4);
  colorContext.fillStyle = '#1a343d';
  colorContext.fillRect(47, 239, 29, 6);
  colorContext.fillRect(383, 379, 21, 6);

  const colorMap = new THREE.CanvasTexture(colorCanvas);
  colorMap.name = 'VS002_PANEL_COLOR';
  colorMap.colorSpace = THREE.SRGBColorSpace;
  colorMap.wrapS = colorMap.wrapT = THREE.RepeatWrapping;
  colorMap.repeat.set(1.0, 1.25);
  colorMap.anisotropy = 4;

  const roughnessMap = new THREE.CanvasTexture(roughnessCanvas);
  roughnessMap.name = 'VS002_PANEL_ROUGHNESS';
  roughnessMap.wrapS = roughnessMap.wrapT = THREE.RepeatWrapping;
  roughnessMap.repeat.copy(colorMap.repeat);
  roughnessMap.anisotropy = 4;

  return {
    colorMap,
    roughnessMap,
    dispose: () => {
      colorMap.dispose();
      roughnessMap.dispose();
    },
  };
};

export const createVS002SurfaceMaterial = (
  sourceMaterial: THREE.MeshStandardMaterial,
  maps: VS002SurfaceMaps,
  name: string,
) => {
  const material = sourceMaterial.clone();
  material.name = name;
  material.map = maps.colorMap;
  material.roughnessMap = maps.roughnessMap;
  material.color.set(0xffffff);
  material.metalness = 0.42;
  material.roughness = 0.82;
  material.needsUpdate = true;
  return material;
};
