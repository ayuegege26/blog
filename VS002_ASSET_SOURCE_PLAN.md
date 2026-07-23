# VS–002 數字資產來源與缺口盤點

> 狀態：資產來源方向已初步採納；尚未下載第三方模型、購買資產或搭建場景。
>
> 工具鏈：Blender 5.2.0 LTS。
>
> 美術錨點：冷色、克制、低／中模硬表面科技建築；避免 3A 寫實成本，也避免玩具城鎮、肉鴿地牢與高飽和卡通語言。

> 補充採購規則：現有來源視為開工基線；後續不再預防性搜尋或囤積素材包。只有在具體 blockout、場景製作或效能驗證中出現可描述且無法由既有模組合理解決的缺件時，才針對該缺件補充來源。

## 1. 盤點前提

本盤點依據已確認的 VS–002 初步互動方向：

- 主操控體是半實體粒子／能量體，不需要角色、車輛或坐騎模型。
- `WASD` 在水平面移動，`Left Shift` 上升，`Left Ctrl` 下降。
- 世界需要利用高度軸，不能只是一層平面場景。
- 場景互動只使用靠近觸發與點擊觸發。
- 觸發後可有動態材質、結構展開、燈光、粒子、聲音和鏡頭回饋，但不需要可搬運、可破壞或互相碰撞的大量動態道具。

這些條件顯著降低了角色、骨骼動畫、車輛、武器和物理道具的資產需求；主要成本集中在建築輪廓、垂直結構、場景地標與統一材質。

## 2. 已採納來源

### 2.1 OZEA A-005 Modular Tiles

- 來源：<https://ozea-studio.itch.io/low-poly-sci-fi-modular-tiles-pack-a-005>
- 狀態：**已採納，可作免費樣本與基礎網格零件。**
- 成本：免費／自定價格。
- 授權：允許商業與非商業使用；不得轉售或重新分發原始檔。
- 格式：`.blend`、FBX、OBJ + MTL。
- 內容：5 個 1×1m／2×2m 牆面與地板模組。
- 優勢：無貼圖、材質顏色工作流、比例清楚、可直接檢查 Blender source 和 GLB 輸出。
- 限制：只足以做材質、比例和導出驗證，不能獨立支撐完整場景。

### 2.2 OZEA Sci‑Fi Series A

- 系列入口：<https://ozea-studio.itch.io/>
- 完整 Series A：<https://ozea-studio.itch.io/sci-fi-series-a-complete-bundle/purchase>
- 狀態：**採納為主結構來源家族；尚未批准購買任何包。**
- 當前價格參考：Series A bundle 約 USD 14.99；價格以實際購買頁為準。
- 主要用途：走廊、平台、陽台、坡道、支撐、樓梯、窗牆和多層空間。
- 主要候選：
  - A-001+：20 個核心結構模組，含平台、坡道、護欄與支撐。
  - A-003：12 個玻璃／格柵地面、樓梯與窗牆模組。
  - A-005：5 個免費基礎 tile，已採納。
- 格式：各單包明確提供 `.blend`、FBX、OBJ + MTL。
- 優勢：與審美錨點一致，同一作者、同一比例、無貼圖材質工作流，適合轉為統一 TSL 材質。
- 限制：以室內和設施結構為主，缺少足以定義世界身份的完整外部建築與大型地標。

### 2.3 Quaternius Modular Sci‑Fi Megakit

- 來源：<https://quaternius.com/packs/modularscifimegakit.html>
- 狀態：**採納為結構擴展幾何池；不作美術錨點。**
- 授權：CC0。
- 格式：FBX、OBJ、glTF；付費 source tier 提供完整 `.blend` 與更多內容。
- 內容：277 個 grid-based 模組；免費標準版提供其中約 60–70%。
- 主要用途：立柱、門、牆、平台、房間、通道和少量中性科技 props。
- 優勢：模組數量大、Web 可用格式完整、結構風格偏差仍在可接受範圍內。
- 限制：原始材質和某些造型比目標風格更遊戲化；必須選件、重材質，不能整包照搬。

### 2.4 核心地標輪廓種子

- 方向：參考柳京飯店／荒坂塔式「權力巨構」的壓迫輪廓。
- 固定語彙：極端垂直比例、三角楔形或三翼量體、明確的頂部冠體、少量巨大切口，以及能從遠距離讀出的單一主輪廓。
- [BlenderKit Sci Fi Pyramid](https://www.blenderkit.com/asset-gallery-detail/ea170c62-c925-4276-9c84-38db3912198e/)：**採納為免費 blockout／比例種子**；3.7 MiB、254 faces，適合拆解、拉伸和重組，不足以原樣成為正式地標。
- [Sketchfab Ryugyong Hotel](https://sketchfab.com/3d-models/ryugyong-hotel-7f0d241e4ee54d0b8dd1389dca278296)：**僅作尺寸、斜面比例與視角研究**；免費 Standard License，但約 173.4k triangles，不進入 runtime，也不以減面後的原樓作成品。
- 製作邊界：先以 pyramid seed 加 primitive 建立自有 silhouette，再從 Series A／Megakit 嵌入平台、空橋、結構肋和冠體；地標身份來自重組後的體量與本項目材質，而非 stock model 本身。
- 當前最小化 probe 中的錐形建築只是 **blockout**：使用程序 primitive、未做正式拓撲、UV 或表層皮膚，不能作為正式建模精度的判定。
- 正式 hero landmark 的目標是 **正常低／中模建模精度＋無貼圖為預設**：輪廓、斜面、冠體、結構肋和平台連接需要乾淨拓撲與可控 bevel；材質先由 Three.js／TSL 程序材質和發光規則完成，只有在幾何無法合理表達時才增加小尺寸、可壓縮的貼圖。
- 正式模型不是 3A 高精度資產，也不是未整理的 primitive 堆疊；進入 runtime 前仍需清理命名、法線、碰撞 proxy、LOD 和 GLB 輸出。

## 3. 已排除或受限來源

| 來源 | 狀態 | 原因 |
| --- | --- | --- |
| KayKit Space Base Bits | 排除 | 玩具城鎮／模擬經營感過強，與冷淡科技神秘風格不符。 |
| Quaternius Ultimate Modular Ruins | 排除 | 奇幻肉鴿／地牢語言過強，不能靠換色解決。 |
| OZEA Ultimate Library | 排除整庫購買 | 風格可作錨點，但整庫價格超出目前合理範圍；改採 Series A 與必要單包。 |
| Kenney Space／Station | 暫不採納 | 物件類型可能有用，但風格接近已排除的 KayKit；只有中性單件經匹配測試後才可例外使用。 |
| Blendkit／BlenderKit 多作者模型 | 僅候選 | 可補單件，但拓撲、比例、授權和風格不一致，不可作主來源。 |
| 3A／寫實 PBR 科幻城市包 | 排除 | 貼圖、材質、面數和下載成本不適合瀏覽器，也偏離目標風格。 |

### 3.1 本輪新增候選的判定

| 來源 | 判定 | 使用邊界 |
| --- | --- | --- |
| [Epic Sci‑Fi Buildings and Environment](https://www.fab.com/listings/cfad311d-6c86-402f-bd4a-d84175c4e472) | **保留為外部體量候選，未採購** | 28 個模型、總計約 380k polygons；單塔約 500–20k、base 約 7k–50k，並有 `.blend`／GLB／glTF。幾何規模可控，但原 4K PBR 與細節傾向比目標更寫實；只有價格合理且實模檢查通過才取其塔、base 和大型輪廓，材質全部重做。 |
| [FuritayBR Sci‑Fi Low Poly Modular Buildings](https://furitaybr.itch.io/sci-fi-low-poly-buildings) | **免費試驗候選，不升格主來源** | 自定價格、6.5 MB，含牆、窗、門、柱、地面與頂板；授權允許修改及商業使用。可補基礎外殼，但沒有證據顯示能補塔冠、垂直井或大型輪廓，且與 Series A 功能重疊。 |
| [loafbrr sci fi like asset pack](https://loafbrr.itch.io/sci-fi-like-asset-pack) | **暫不採納** | 免費且有 `.blend`／glTF／FBX，但下載約 752 MB；公開頁未提供足夠清楚的授權與模組清單，不能因免費就納入正式來源。 |
| PopNerd Sci‑Fi City Kitbash | **排除 runtime 使用** | USD 1+、10 棟建築，但作者明示用於 concept art，存在重疊幾何且不適合 game engine／animation。 |
| Kevin Jick Sci Fi Kitbash Vol. 1 | **排除** | USD 32、85+ assets，但作者明示不是 game-ready；需要重做 topology、UV 和 texture，與網頁端目標不匹配。 |
| BlenderKit Si‑Fi Tower | **不採納** | 免費但約 216k faces；單件重量已高於我們對 hero building 的合理預算，且沒有提供比自有 pyramid kitbash 更強的必要輪廓。 |

## 4. 當前覆蓋度

### 4.1 已基本覆蓋

| 資產類別 | 覆蓋度 | 說明 |
| --- | --- | --- |
| 基礎地面／牆面 | 高 | A-005 可驗證；Series A 與 Megakit 可完成正式組合。 |
| 樓梯／坡道／護欄 | 高 | A-001+、A-003 和 Megakit 已有候選。 |
| 走廊／房間／平台 | 高 | 兩個模組家族均能提供。 |
| 門框／門體／窗牆 | 中高 | 幾何已有候選；觸發動畫由 runtime 實現。 |
| 一般立柱／支撐 | 中高 | Megakit 數量充足，需篩選符合風格的輪廓。 |
| 小型控制台／中性科技 props | 中 | Megakit 能覆蓋一部分；缺件再查 OZEA 單包。 |
| 主操控體 | 完整 | 使用 TSL／粒子程序生成，不需要外部角色模型。 |
| 互動提示與觸發回饋 | 完整 | 使用 TSL、DOM、燈光和 transform animation，不依賴模型包。 |
| 簡化碰撞體／觸發區 | 完整 | 以 primitive 或自製 proxy 生成，不購買碰撞模型。 |

### 4.2 明確缺口

| 缺口 | 大小 | 需求方向 | 建議解法 |
| --- | --- | --- | --- |
| 垂直巨構連接件 | 中偏小 | 升降井、塔身段、懸橋、吊掛平台、環形通道、底部支撐 | Series A／Megakit 現有直線模組配合 Blender Array、Curve、Mirror 和 primitive 可覆蓋大部分；目前沒有必要另買專用包。若 blockout 證明環形／斜向接頭不足，再補一個小包。 |
| 外部建築體量 | 中 | 不只是室內牆片，而是從遠處可識別的塔、核心艙、觀測站和垂直聚落 | 先以 primitive＋既有模組建立輪廓；Epic Sci‑Fi 只保留為條件式候選，不直接購買完整城市場景。 |
| Hero landmarks | 數量小、重要性大 | 約 3–5 個承擔世界身份與導航的標誌結構；主地標採柳京／荒坂式垂直權力巨構語彙 | Sci Fi Pyramid 作 blockout seed，深度重組為原創地標；Ryugyong 模型只作比例研究。其餘地標從同一形體語法衍生，不直接使用通用 stock building。 |
| 科技表面細節 | 小至中 | 通風、管線、天線、感測器、能源節點、維修接口 | 優先查 OZEA USD 0–5 單包；其次才從 Blendkit 找中性單件。 |
| 發光標識／圖形系統 | 中 | 冷色引導線、符號、區域識別、點擊／靠近回饋 | 不找模型；自行設計 atlas、decal 與 TSL emissive 規則。 |
| 統一冷色材質 | 大，但不是建模缺口 | 冷灰基底、藍綠發光、低飽和層次、霧與局部暖色 | 完全由本項目建立 TSL 材質與燈光，不沿用資產包美術。 |
| 場景背景／邊界 | 中，取決於項目概念 | 虛空、雲霧、抽象城市深層、封閉巨構或遠景層 | 項目設計後決定使用程序背景、低模遠景或額外環境資產。 |

## 5. 缺口判斷

若只計算普通結構零件，現有來源可以覆蓋約 **70–80%** 的需要；目前不缺另一個大型通用素材庫。

真正缺少的不是更多牆、門和箱子，而是：

1. 能把高度軸變成空間體驗的垂直巨構語彙；零件大致足夠，缺的是組合規則與 blockout 驗證。
2. 3–5 個不帶素材包既視感的 hero landmarks；主地標已有免費輪廓種子，但仍需原創重組。
3. 將不同幾何統一成冷淡科技神秘風格的材質、燈光、霧和圖形系統。

因此，後續資產投入應集中在「高辨識度、少數量」部分，而不是繼續購買數百個通用 props。模型數量缺口屬中小；藝術整合和場景設計缺口屬大。

## 6. 建議取得順序

本階段不執行下載或購買。進入資產驗證階段後按以下順序：

1. 下載免費 OZEA A-005。
2. 在 Blender 5.2 LTS 檢查比例、origin、材質 slot、拓撲、法線、命名和 GLB 導出。
3. 做一個只含牆／地板／平台的離線材質試片，不接網站、不做場景。
4. 審美和導出通過後，再決定購買 Series A bundle，或只購買 A-001+／A-003。
5. 下載 Quaternius Megakit 免費標準版，只建立「可用／需改造／排除」清單。
6. 經 BlenderKit 取得免費 Sci Fi Pyramid，僅建立主地標 blockout；同時以 Ryugyong 模型／公開視圖核對高度、斜面和冠體比例，不導入 runtime。
7. 以既有模組完成一組升降井、直塔段、空橋、懸台和環形平台測試；只有其中某類失敗，才搜索該類的專用小包。
8. 完成項目空間設計後，再根據明確缺件購買 OZEA 單包或評估 Epic Sci‑Fi；禁止預防性囤積整庫。

任何新增素材必須同時記錄：在哪個具體工作階段發現、缺少哪一類幾何、既有資產為何不能合理改造、預計使用數量、runtime 成本與授權。未能回答這六項的候選不得進入採購或正式資產清單。

## 7. Blender 工具鏈

本機已確認：

```text
C:\Program Files\Blender Foundation\Blender 5.2\blender.exe
Blender 5.2.0 LTS
```

規則：

- VS–002 的 DCC 基準固定為 Blender 5.2 LTS。
- `.blend` 是可編輯來源，不直接進入 Web runtime。
- runtime 輸出使用 GLB／glTF，後續再進行 DRACO／KTX2 等壓縮。
- 第三方 `.blend` 首次打開後先另存本地工作副本，不覆蓋下載原檔。
- 若資產以舊版 Blender 保存，先測試材質、modifier 和 glTF 導出，再升級保存。
- 進入正式資產階段時建立 `asset-manifest`，記錄 URL、作者、授權、取得日期、版本、修改和輸出檔。

## 8. 下一個決策門

核心空間與操作基線已移入 `VS002_PROJECT_DESIGN.md`；在開始下載和搭建前，仍需把其中的信息架構和 blockout 參數落成可驗收草案，至少確定：

- 單一環圍巨構、少量垂直井城／懸浮建築群的具體 blockout。
- 玩家飛行高度、相機視距、導航層和隱形邊界。
- 3–5 個 hero landmarks 各自對應的 NAS／工具／博客內容。
- 靠近光效、點擊信息和離開復原的內容字段與視覺表現。
- 全部外部空間中，平台、外露通道和半開放結構的比例。

這些答案會把目前「中等大小」的外部建築缺口收斂成可購買、可 kitbash 或必須自製的確切清單。
