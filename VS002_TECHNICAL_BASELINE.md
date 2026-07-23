# VS–002 技術基線

> 狀態：技術來源已確認；項目概念與視覺藝術設計尚未開始。
>
> 適用範圍：`Lab / Visual Systems / VS–002` 的工程設計、實作、測試與交付。
>
> 核心原則：採用 Bruno Simon 2025 Portfolio 的瀏覽器 3D 技術方向，但不複製其作品形式、視覺藝術、內容、地圖、車輛或互動敘事。

## 1. 文檔目的與權限

本文件只回答「VS–002 用什麼技術、如何組織、最低品質要求是什麼」。它不決定項目主題、世界觀、視覺語言、玩法或敘事。

規範優先順序：

1. VS–002 後續獲批的項目設計文檔。
2. 本技術基線。
3. `LAB_SECTIONS.md` 與 `LAB_CONTENT_ENGINEERING.md` 的 Lab 共通原則。
4. 外部參考專案的具體實作。

若外部參考與本地需求衝突，以本文件和本地項目設計為準。Bruno Simon 專案是技術證據與研究來源，不是待移植模板。

## 2. 技術來源

主要來源：

- Bruno Simon Portfolio：<https://bruno-simon.com/>
- 公開原始碼（MIT）：<https://github.com/brunosimon/folio-2025>
- Three.js TSL 規格：<https://github.com/mrdoob/three.js/wiki/Three.js-Shading-Language>
- Rapier：<https://rapier.rs/>

從來源採納的技術方向：

- `three/webgpu` 與 `WebGPURenderer`，同一套場景與 TSL 材質支援 WebGPU／WebGL 後端。
- TSL／Node Material 組織自訂材質、程序動畫、粒子與後處理。
- Rapier 3D 處理剛體、碰撞、感測區與需要物理一致性的互動。
- 輸入、物理、視覺同步、相機、世界系統、音訊與渲染按固定順序更新。
- GLB、DRACO、KTX2 等資產壓縮與 GPU 友善格式。
- Instancing、距離啟停、品質分級、像素比上限與按需載入。

不直接採納：

- Bruno Portfolio 的車輛作品集形式、地圖結構、場景佈局與關卡內容。
- 其低多邊形美術、色彩、材質外觀、鏡頭性格、UI、音樂與音效語言。
- 成就、競速榜、留言、伺服器通訊及彩蛋等產品功能。
- 原始碼中的全域單例、檔案命名或類別切分，不視為必須照抄的架構。

## 3. 已鎖定的技術棧

### 3.1 網站外殼

- 現有 Astro 專案繼續負責路由、頁面 metadata、Lab 導航、靜態說明與非 3D fallback；沉浸式 VS–002 路由可使用獨立 `ImmersiveLabLayout` 隱藏共用 LabHeader，但必須保留可訪問的返回／退出入口。
- VS–002 runtime 只在其專屬路由載入，不進入首頁、Visual Systems 索引或其他 Lab 頁面的共用 bundle。
- 不為 3D runtime 引入 React、Vue 等額外 UI 框架；若後續項目設計證明有必要，必須另寫決策記錄。

### 3.2 圖形層

- 採用 Three.js 的 `three/webgpu` 入口與 `WebGPURenderer`。
- WebGPU 是優先後端，WebGL 是正式 fallback；不得把 WebGPU 支援當作進入項目的必要條件。
- 自訂 GPU 邏輯以 TSL 為預設，不以字串替換或大規模 `onBeforeCompile` 作為主要材質方案。
- 後處理使用 Three.js／TSL render pipeline。效果必須可按品質級別關閉，且不能承擔核心資訊。
- Three.js、Rapier 與相關 loader 的確切版本在開始實作時鎖入 `package-lock.json`，不得長期使用浮動版本驗收。

### 3.3 物理層

- 採用 `@dimforge/rapier3d`，以動態 import 延後載入 WASM 與 runtime。
- 物理世界與視覺場景分離；視覺物件只讀取已完成的物理狀態，不反向直接改寫渲染中的暫態矩陣作為物理真值。
- 預設固定 timestep 為 `1 / 60` 秒，使用 accumulator；限制單幀追趕次數，避免頁籤恢復或長幀造成 simulation spiral。
- 感測區、碰撞層、休眠、剛體類型與物理材質必須集中定義，不散落為不可追蹤的 magic numbers。
- 若最終設計不需要物理互動，可以移除 Rapier；不得為了宣稱技術棧而保留空物理世界。

### 3.4 音訊層

- 需要空間音訊或多聲道管理時採用 Howler.js；簡單提示音可使用更小的原生方案。
- 音訊必須在使用者手勢後啟動，預設提供靜音控制，並保存合理的本地偏好。
- 聲音是體驗層，不得成為理解核心內容的唯一方式。

### 3.5 引擎與套件來源

Astro 不是 VS–002 的 3D 引擎；它只負責現有網站的路由、頁面外殼與 Vite bundle。VS–002 的 3D renderer／runtime 是 Three.js，並在其上按需接入 TSL、Rapier 和 Howler。

VS–002 不使用 Unity、Unreal、PlayCanvas 或另一個完整場景引擎作為執行基礎，理由是：

- 作品必須直接整合現有 Astro Lab，並維持路由級按需載入，而不是把整個頁面包進另一個引擎 runtime。
- 我們需要直接控制 WebGPU／WebGL fallback、TSL shader graph、資產載入、互動狀態機與生命周期，不需要完整引擎附帶的場景編輯器、遊戲循環或專案格式。
- 瀏覽器輸出只需要可部署的 ESM／WebGL／WebGPU 資源，避免引入引擎 runtime、轉出格式與部署層的額外重量。
- 這是技術邊界，不是禁止未來使用 Blender、Geometry Nodes 或外部 DCC；它們可以用於資產製作，但不成為瀏覽器執行引擎。

因此，本項目採用「Astro 網站外殼 + Three.js 圖形 runtime + 專案級互動／物理模組」的分層，而不是「Astro 取代 3D 引擎」。以下是確定的官方來源：

| 能力 | 確定來源 | 使用邊界 |
| --- | --- | --- |
| 3D scene／renderer | [Three.js](https://threejs.org/docs/pages/WebGPURenderer.html) | scene graph、camera、geometry、WebGPU／WebGL renderer |
| shader／GPU material | [Three.js TSL](https://github.com/mrdoob/three.js/wiki/Three.js-Shading-Language) | Node Material、uniform、attribute、storage、compute（按需） |
| 3D physics | [Rapier JavaScript bindings](https://rapier.rs/javascript3d/) | rigid body、collider、sensor、collision event（只有設計需要時） |
| audio | [Howler.js](https://howlerjs.com/) | 受控音效、音樂與可選的空間音訊 |
| build／route shell | 現有 Astro + Vite | 路由、載入邊界、fallback、靜態頁面與 bundle |

依賴必須從官方 npm package 或官方 repository 安裝，版本鎖定於 lockfile；不從未驗證 CDN、複製貼上的 minified build 或不明 fork 引入核心 runtime。

## 4. Runtime 架構

VS–002 採用專案級 runtime，不把 3D 狀態放入 Astro 頁面模板。最低模組邊界如下：

```text
VS002 page / Astro shell
└── bootstrap
    ├── capability + quality
    ├── resources
    ├── input
    ├── time / scheduler
    ├── physics (conditional)
    ├── experience / world
    ├── camera
    ├── audio (conditional)
    ├── renderer / post-processing
    └── lifecycle / diagnostics
```

模組透過明確介面或事件交換狀態。禁止用未記錄的建構順序暗中建立依賴；需要先後順序的系統必須在 scheduler 中註冊階段。

### 4.1 互動邏輯基線

互動邏輯採「輸入意圖 → 互動查詢 → 狀態轉移 → 回饋」四層，不讓 pointer click 直接改寫場景物件：

```text
raw input
  ↓
semantic action / intent
  ↓
interaction resolver（距離、視線、優先級、可用條件）
  ↓
command
  ↓
experience state machine
  ├── world / physics mutation
  ├── camera response
  ├── visual feedback
  ├── audio feedback
  └── accessible DOM status
```

通用規則：

- 每個可互動對象具有穩定 `id`、`interaction type`、`enabled`、`priority`、`range` 與 `availability`，不以 mesh 名稱作為產品邏輯識別。
- 每幀最多產生一個主要 focus target；候選按明確排序解決：可用性 → 距離 → 視線／投影命中 → 優先級 → 穩定 tie-breaker。
- `interact` 是語義 action，不限定為 Enter、Click 或觸控 Tap；不同設備映射到同一 intent。
- 互動執行必須產生可記錄的 command 或 domain event，禁止讓 UI 事件直接呼叫任意物件內部方法。
- 具有時間跨度的互動使用有限狀態機：`idle → focused → available → running → completed / cancelled / failed`。每個狀態定義進入、更新、退出與可接受的中斷。
- 互動要可取消、可重置、可重入；若不可重入，必須明確標註鎖定原因並提供恢復路徑。
- 物理互動先建立 command，再在固定 physics step 套用；視覺互動可以在非物理階段更新。
- 回饋至少有視覺或文字路徑；音訊、震動、粒子和 camera response 只能是附加回饋。
- 核心狀態與 URL、localStorage 或 server 的保存邊界必須分開決定；預設不把暫態互動寫入永久狀態。
- reduced-motion、低性能與圖形 fallback 下，互動仍要能被辨識、執行和完成。

VS–002 的場景互動動詞已限制為兩類：**靠近觸發**與**點擊觸發**。不採用駕駛、拖曳、搬運、投擲、破壞或物件彼此動態作用；觸發後只產生由狀態驅動的結構 transform、材質、燈光、粒子、聲音與相機回饋，不把一次性動畫播放當作互動模型。兩類互動都必須映射到上述 resolver、command 和 state machine，不因輸入方式簡單而繞過狀態層。

### 4.2 幀更新順序

```text
0  time + input sampling
1  experience pre-physics commands
2  physical controllers / forces
3  fixed-step physics
4  collision events + dynamic object state
5  physics-to-visual snapshot
6  experience post-physics state
7  camera
8  world visuals / zones / effects
9  spatial audio + UI state
98 render
99 diagnostics
```

要求：

- scheduler 支援具名階段、註冊、解除註冊與完整銷毀。
- `delta` 設上限；動畫時間與物理時間分開管理。
- GPU uniform 使用同一時間來源，避免各效果自行呼叫 `performance.now()`。
- 頁面隱藏、失焦、開啟阻塞式 modal 或離開路由時，按設計暫停或降頻。

## 5. 輸入與相機

- 將鍵盤、滑鼠／pointer、觸控與 gamepad 映射到語義化 actions，不讓世界模組直接監聽原始 DOM 事件。
- action 至少描述 `active`、`justPressed`、`justReleased` 與連續值。
- 輸入模式切換不得重置不相關的項目狀態。
- 必須提供鍵盤可完成的主要操作；觸控版採重新設計的控制方式，不縮小桌面 UI 硬套。
- 相機是獨立系統，負責跟隨、阻尼、限制、視口適配與必要的碰撞／遮擋處理。
- 相機晃動、速度感與景深等效果受 reduced-motion 和品質級別控制。

主操控體已確定為半實體粒子／能量體；桌面鍵盤使用 `WASD` 相對相機水平移動、`Left Shift` 上升、`Left Ctrl` 下降。移動採微弱加減速慣性，上下速度略慢於水平；可穿過細小結構，撞擊主要建築後停止並沿表面滑動，地圖與高度邊界使用隱形限制。這些按鍵仍映射成語義 action，不能由 player object 直接監聽；正式項目的速度、相機距離和視野仍可在 blockout 後微調。

最小 probe 只以桌面鍵盤和 pointer drag／click 驗證上述邏輯；觸控虛擬控制與 gamepad 仍屬正式項目設計範圍，不宣稱已由 probe 覆蓋。

## 6. TSL、材質與 GPU 系統

- 共用節點函數、noise、色彩轉換、reveal、風場等放入可測試的 shader modules。
- TSL 節點名稱描述意圖，不綁定最終藝術風格，例如使用 `surfaceResponse`，避免提前命名為某種美術效果。
- 動態值使用 uniform；幾何固有值使用 attribute；大量重複物件優先使用 instanced attributes。
- GPU compute／storage buffer 只用於數量或互動成本能證明收益的系統，並提供 WebGL 可用的降級路徑或關閉策略。
- 程序效果必須使用可重現 seed；需要隨機的項目狀態不得完全依賴不可重放的 `Math.random()`。
- 所有自訂材質必須記錄透明、深度、陰影、色彩空間與 blend 假設。

## 7. 3D 資產管線

### 7.1 來源與輸出

- DCC 預設使用 Blender，runtime 交付格式為 GLB／glTF。
- 原始 Blender 檔、貼圖來源和匯出檔分層保存；瀏覽器只發佈 runtime 資產。
- 靜態重複物件使用 instancing；不得為每個相同物件生成獨立材質與 geometry。
- 碰撞模型與視覺模型分離，碰撞幾何以簡化、穩定和可預測為優先。

### 7.2 壓縮

- 幾何依實測使用 DRACO；載入器與 decoder 版本必須相容。
- GPU 貼圖優先輸出 KTX2／Basis Universal，並依用途正確標記 sRGB、linear、normal 或單通道資料。
- DOM／UI bitmap 使用 WebP 或 AVIF；SVG 適合的圖形不轉成位圖。
- 建置流程保留未壓縮來源，不覆蓋原始資產。
- 在項目藝術與內容清單完成後，另行制定首屏下載量、總資產量、貼圖尺寸和幾何數量預算。

### 7.3 載入策略

- 首屏只載入進入體驗所需的最小資產，其他區域按距離、階段或使用意圖載入。
- loader 統一處理 cache、進度、錯誤、取消與重試；世界模組不得各自建立不受控 loader。
- 載入失敗時顯示可理解狀態，不能永久停在無說明的進度畫面。

### 7.4 數字資產來源與優先級

VS–002 已採納、排除的具體資產來源與當前缺口，統一記錄於 `VS002_ASSET_SOURCE_PLAN.md`；本節只保留通用來源規則。

資產來源按以下優先級選擇：

1. **原創／程序生成**：項目身份、主要 hero asset、特殊互動物件與不可替代的標誌性元素。
2. **CC0 公共資產**：優先使用 [Poly Haven](https://polyhaven.com/license)、[ambientCG](https://docs.ambientcg.com/license/)、[Kenney](https://www.kenney.nl/assets) 和 [Quaternius](https://quaternius.com/)。仍須保存下載頁和資產版本，方便日後追溯。
3. **購買或訂閱資產**：可使用 [Fab](https://dev.epicgames.com/documentation/fab/licenses-and-pricing-in-fab) 等平台，但每個資產必須確認是 Personal／Professional、CC-BY 或其他適用授權，不能只記錄平台名稱。
4. **委託製作**：只用於核心辨識元素、特殊角色、動畫或現有資產無法合理改造的物件。

每個進入 repository 或 build 的資產都要有 manifest 記錄：`assetId`、原始 URL、作者／發佈者、授權名稱、下載或購買日期、原始檔位置、修改範圍、是否可再分發、runtime 輸出檔與 attribution 要求。禁止把「免費下載」當成授權判斷，也禁止把 CC-BY、CC-BY-NC、Editorial-only 或限制 AI／再分發的資產混用而不標記。

通用資產不能原樣決定整體美術；所有採用的模型必須經過比例、材質、色彩、構圖、命名、碰撞和效能的項目化處理。資產選擇、改造深度和 hero asset 清單由後續 `VS–002 Asset Bible` 定案。

## 8. 效能與品質分級

最低品質級別為 `high`、`low`，可增加 `auto` 作為偵測入口：

| 項目 | High | Low |
| --- | --- | --- |
| 目標更新／渲染 | 60 FPS | 穩定 30 FPS 以上 |
| device pixel ratio | 上限 2 | 上限 1–1.25 |
| 陰影 | 設計需要時開啟 | 降解析度、降數量或關閉 |
| 後處理 | 完整但有預算 | 僅保留必要效果 |
| 粒子／環境物件 | 完整密度 | 降低密度與更新頻率 |
| 物理 | 固定 timestep | 同 timestep，降低非核心物件成本 |

共同要求：

- 不以 user agent 作為唯一品質判斷；裝置偵測只提供初始建議，使用者可手動切換。
- 像素比、陰影貼圖、post-processing pass、instancing、draw calls 與活躍剛體數納入 diagnostics。
- 使用距離啟停、休眠、frustum culling、區域可見性與按需更新，避免所有系統每幀全量工作。
- 不在正常遊玩路徑持續建立 Vector、Matrix、材質、geometry 或臨時陣列。
- 正式驗收前，在桌面高品質、桌面 fallback、主流手機與 reduced-motion 四條路徑記錄實測結果。

## 9. Lifecycle 與資源釋放

離開 VS–002 路由後必須：

- 停止 animation loop、物理步進、計時器與音訊。
- 移除 DOM、pointer、keyboard、gamepad、visibility 和 resize listeners。
- 終止 Worker，取消未完成載入，關閉不再需要的網路連線。
- dispose geometry、material、texture、render target、post-processing 與 renderer 資源。
- 清除 runtime 建立的 DOM、debug panel 與全域引用。

重新進入頁面必須能建立乾淨的新 instance，不依賴上一次殘留狀態。

## 10. 可訪問性與失敗降級

- 頁面在 Canvas 初始化前先提供標題、項目目的、操作說明、返回 Lab 與能力需求。
- WebGPU／WebGL 初始化失敗時保留可使用的 HTML fallback，不顯示空白頁。
- 尊重 `prefers-reduced-motion`；降低或停用相機晃動、連續視差、閃爍與非必要粒子。
- 暫停、重置、品質與音訊控制可由鍵盤存取並有可讀 label。
- 色彩不能成為唯一狀態編碼；必要資訊在 DOM 層提供文字表達。
- 對閃光、快速運動或暈動風險，在開始體驗前提供說明與關閉方法。

## 11. 資料、網路與隱私

- 第一版預設為純客戶端體驗，不要求伺服器才能成立。
- 若項目設計需要網路功能，必須先定義資料來源、失敗模式、保存期限、公開範圍與無網路降級。
- localStorage 只保存必要偏好或明確的本地進度，使用穩定 namespace 並提供重置方式。
- 不讀取不必要的裝置權限、瀏覽器識別資訊或高熵硬體資料。
- debug、性能監測與錯誤輸出不得包含私人資料。

## 12. 原創與授權邊界

以下項目必須由 VS–002 重新設計與製作：

- 項目概念、內容價值、世界觀與互動目標。
- 構圖、空間、色彩、光線、材質外觀與動效節奏。
- 模型、貼圖、圖形、字體組合、UI、聲音與音樂。
- 相機語法、操作手感、回饋、敘事和進程結構。

不得從 Bruno Portfolio 擷取或近似重製其模型、Blender 場景、貼圖、音訊、地圖、文字、品牌元素及高辨識度視覺組合。即使外部程式碼為 MIT，也應優先重寫符合本地架構的模組；若實際複用程式碼，必須保留授權與來源記錄。

## 13. 開始實作前的決策門

技術來源已敲定，但在寫 runtime 前仍必須完成一份 VS–002 項目設計，至少回答：

具體內容以 `VS002_PROJECT_DESIGN.md` 為準；本節只作為實作前檢查清單。

正式版的分階段生產、驗收門、回退和不確定項目實驗流程，以 `VS002_PRODUCTION_PLAN.md` 為準；未通過前一階段 Gate，不得進入下一階段。

1. 這個項目讓訪問者觀察、理解或完成什麼？
2. 核心循環與結束條件是什麼？
3. 空間結構、主要互動物與相機關係是什麼？
4. 原創視覺語言和聲音語言是什麼？
5. 哪些功能確實需要 Rapier、GPU compute、音訊或後處理？
6. 桌面、觸控、鍵盤、reduced-motion 和圖形失敗時各如何使用？
7. 資產清單與性能預算是多少？

未回答的能力不得先以 demo 特效形式悄悄成為正式架構。

## 14. 技術驗收條件

- VS–002 bundle 與重型資產只在其路由載入。
- WebGPU 與 WebGL fallback 均可進入核心體驗。
- 更新順序可追蹤，物理與視覺狀態沒有互相覆寫競態。
- high／low、靜音、暫停、重置與 reduced-motion 路徑可用。
- 資產壓縮、色彩空間、cache 與載入失敗行為經驗證。
- 離頁後沒有持續 animation frame、Worker、音訊或事件監聽。
- 鍵盤與觸控可以完成項目定義的核心操作。
- 性能結果、已知限制、第三方依賴及授權記錄隨交付更新。
- 視覺和內容通過原創性檢查，不以 Bruno Portfolio 的藝術身份作為設計捷徑。
