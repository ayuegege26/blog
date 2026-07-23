# VS–002 S2 建模語彙實驗

狀態：隔離實驗，接入既有 `/lab/visual-systems/vs002-probe`；不屬於正式 S1.5 資產。

## 實驗目的

只用一座核心塔測試低／中模細節是否符合「冷淡、克制、科技神秘」的方向，再決定是否套用到正式世界。此輪不追求完整建築，也不改動正式地圖。

## 本輪試驗內容

- 八邊形分段塔體與三段高度輪廓；
- 低層／高層外露垂直結構肋；
- 四條克制的冷青色嵌入光帶；
- 三層低段數結構環帶；
- 一個外部橋接／節點平台；
- 保留 probe 的 WASD、上下飛行、靠近／離開與點擊信息邏輯。

## 明確不包含

- 正式世界的完整主環、垂直井或懸浮群；
- 正式材質貼圖與最終 shader；
- 高密度 3A 細節；
- 正式內容字段與 Lab 整合。

## 實驗產物

- Blender：[vs002-s2-core-detail-trial.blend](./public/assets/vs002/experiments/vs002-s2-core-detail-trial.blend)
- GLB：[vs002-s2-core-detail-trial.glb](./public/assets/vs002/experiments/vs002-s2-core-detail-trial.glb)
- 生成腳本：[vs002_s2_detail_trial.py](./scripts/vs002_s2_detail_trial.py)
- 預覽：`http://127.0.0.1:4321/lab/visual-systems/vs002-probe`

## 視覺驗收問題

1. 外露垂直肋是否增加尺度感，還是過於像柵欄？
2. 三層環帶是否建立科技結構節奏，還是過度裝飾？
3. 冷青嵌入光帶是否足夠克制？
4. 塔體輪廓是否接近巨構地標，而不是普通遊戲建築？
5. 此細節密度是否適合網頁端遠／中／近三種觀察距離？

只有語彙通過後，才選擇性回寫正式 S2。
