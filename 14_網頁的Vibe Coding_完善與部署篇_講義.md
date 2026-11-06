---
puppeteer:
  displayHeaderFooter: true
  scale: 1.15
  headerTemplate: '<div style="font-size: 11px; margin: 0 auto;">第十四至十五週：實作專案四 — AI 協作：Phase 3 完善品管、部署上線與作品集展評</div>'
  footerTemplate: '<div style="font-size: 11px; margin: 0 auto;">第 <span class="pageNumber"></span> 頁 / 共 <span class="totalPages"></span> 頁</div>'
  margin:
    top: "1.5cm"
    bottom: "1.5cm"
    left: "1.5cm"
    right: "1.5cm"
---

<style>
  /* 全域字型、字級與行距 */
  body {
    font-size: 16pt !important;
    line-height: 1.7 !important;
    font-family: "Microsoft JhengHei", "PingFang TC", "Helvetica Neue", sans-serif;
  }

  /* 階層標題微調 */
  h1 { font-size: 30pt !important; margin-bottom: 0.5em !important; }
  h2 { font-size: 24pt !important; page-break-before: always; }
  h3 { font-size: 20pt !important; }
  h4 { font-size: 18pt !important; }

  /* 表格文字放大與排版優化 */
  table, th, td {
    font-size: 15pt !important;
    line-height: 1.5 !important;
  }

  /* 程式碼區塊 (自動換行防止 PDF 截斷) */
  pre, code {
    font-size: 13pt !important;
    font-family: Consolas, "Courier New", monospace !important;
    white-space: pre-wrap !important;
    word-break: break-all !important;
  }
</style>

---

# 第十四至十五週：實作專案四 — AI 協作：Phase 3 完善品管、部署上線與作品集展評 (Phase 3: Multi-Page Refinement, Deployment & Showcase)

**課程名稱**：網頁設計 (Webpage Design)  
**授課教師**：林頌堅 副教授 (Prof. Sung-Chien Lin)  
**授課單位**：世新大學 資訊傳播學系  
**聯絡方式**：scl@mail.shu.edu.tw  
**核心工具**：Google Antigravity 2.0 Desktop、GitHub Desktop、Vercel、VS Code、Google Chrome / Edge  

---

## 本週學習目標 (Weekly Mission)

恭喜大家！經過前兩週的藍圖規劃與代理人生成，你的專案目錄裡現在已經具備了 4 個互相關聯的 HTML 分頁，以及由 AI 繪製的高質感真實素材。

然而，**AI 產出的多頁原型通常只有 70~75 分**。AI 在處理多頁網站時，常常會在手機端排版偷懶、各頁面的字體行高沒有呼吸感、或者殘留了敷衍的假字。這最後兩週，正是你展現「不可替代之人類審美與工程素養」的關鍵時刻 —— **你將化身全方位「AI 多頁品管師 (QA Inspector)」，排查 4 個分頁的破版瑕疵、精準微調視覺氛圍、正式上線發布至 GitHub Pages、進一步串聯 Vercel 雲端平台以支援現代前端框架，並將其無縫串聯進你的個人履歷作品集中！**

完成本週學習後，你將能夠：
1. **本機伺服器真實環境預覽**：在 Antigravity 終端機啟動本地 HTTP 測試伺服器，避免檔案協定造成字型與跨頁跳轉異常。
2. **多頁面跨裝置 RWD 巡檢**：運用瀏覽器 `F12` 開發者工具，全面檢測 4 個頁面在手機、平板與桌機上的排版表現。
3. **手術式自然語言微調**：下達精準指令，指導 AI 批次調整 4 個頁面的字體、色彩過渡、卡片陰影與消除假字。
4. **一鍵部署至 GitHub Pages**：將多頁倉庫公開發布，獲得全世界都能隨時造訪的專屬網址。
5. **連結 Vercel 支援前端框架**：將 GitHub 儲存庫串聯至 Vercel，自動編譯並運行專案中可能包含的 React、Vue、Vite 或 Next.js 等現代前端框架。
6. **打造雙向作品集生態系**：將新完成的多頁專案與個人的線上履歷雙向超連結，展現實務工程水準。

---

## Ⅰ. 完善與發布核心觀念：成為全方位「AI 多頁品管師」 (Becoming the QA Inspector)

很多人以為 Vibe Coding 就是「隨便問幾句，AI 寫完就結束」。  
事實上，**真正的專業差距，就體現在這最後 25% 的品管細節中！**

![Phase 3 完善與發布兩階段路徑](img/diagram_14_refinement_flow.png)

### 1. 多頁網站最常出現的四大「AI 偷懶病」：
* 📱 **手機端破版災難**：在桌機看很漂亮的三欄卡片，到了手機螢幕卻被擠成一團，文字甚至衝出卡片邊框。
* 🔗 **導覽列跨頁不一致**：在 `index.html` 導覽列有 4 個按鈕，點進 `about.html` 卻少了一個，或是 active 高亮標記給錯頁面。
* 📝 **Lorem Ipsum 假字未清**：內文還殘留著拉丁文假字、商品價格標成 $000、營業時間寫著「請在此輸入時間」。
* 🌫️ **視覺氛圍缺乏細膩度**：按鈕沒有滑鼠懸停 (hover) 動畫、字體過小擠在一起，缺乏日系設計應有的「呼吸感」。

這兩週，我們將透過嚴格的測試與提示詞精修，一一把這些瑕疵全部消滅！

> 💡 **老師的真心話**  
> 很多同學常常問老師：「AI 寫得那麼快，我們到底還要學什麼？」這最後兩週就是最好的答案！AI 寫出來的只是 70 分的半成品，只有具備美感、同理心與品管意識的人類，才能檢查出文字折行、色調突兀與手機端排版擠壓的瑕疵。你對品質的堅持，才是讓作品脫穎而出的關鍵！

---

## Ⅱ. 實戰任務一：檢閱 Walkthrough 工件與啟動本機測試伺服器 (Walkthrough & Local Server)

### 1. 檢視 `walkthrough.md` 走查工件
在 Phase 2 完成後，Antigravity 2.0 會在右側 **Artifacts 窗格** 交付一份 `walkthrough.md` 工件。  
這份工件列出了專案中已建立的 4 個分頁、樣式表與圖片路徑清單，並提醒你值得留意的測試要點。

### 2. 終端機啟動本地 HTTP 測試伺服器
⚠️ **千萬不要直接雙擊 HTML 檔案用 `file:///` 預覽！**  
使用 `file:///` 協定時，瀏覽器會限制 Google Fonts 字體加載、可能無法讀取相對路徑 JavaScript，也會造成跨頁跳轉路徑的判斷偏差。

請在 Antigravity 對話框中輸入：
```text
請在終端機幫我啟動一個本地 HTTP 測試伺服器，讓我可以即時在瀏覽器中預覽多頁網站的效果。
```
Antigravity 會自動在背景終端機執行 `python -m http.server 8000`（若專案包含前端框架，則會執行 `npm run dev`）。  
接著在 Chrome 或 Edge 瀏覽器網址列輸入：  
👉 **`http://localhost:8000`**（或終端機提示之本地埠號），即可享受最標準的網頁伺服器環境！

> 💡 **老師的真心話**  
> 再次強烈叮嚀：不要用雙擊檔案的 `file:///` 方式預覽！因為很多 Google Fonts、相對跳轉或 JavaScript 行為在沒有伺服器環境下會被瀏覽器安全機制阻擋。花 3 秒鐘讓 Antigravity 在終端機跑本地伺服器，用標準的 `localhost` 預覽，能幫你省下無數莫名其妙的除錯時間。

---

## Ⅲ. 實戰任務二：跨頁 RWD 檢測與自然語言手術式精修 (Multi-Page RWD & Vibe Tuning)

### 1. 按下 `F12` 進入手機模式進行 4 頁大巡檢
在瀏覽器中按下鍵盤 **`F12`**（或右鍵點擊「檢查」），點擊左上角的 **「切換裝置工具列 (Toggle Device Toolbar)」**，將畫面寬度調整為 **iPhone 14 (390px)**：

逐一點擊 4 個分頁進行地毯式檢查：
* [ ] **`index.html`**：Hero 主標題在手機螢幕是否會難看地折成 3 行？按鈕在手機上是否容易點擊？
* [ ] **`about.html`**：左右雙欄的「烘豆師照片」與「品牌故事」，在手機端是否自動切換為上下單欄排版？
* [ ] **`menu.html`**：咖啡菜單的 3 欄卡片，在手機端是否正確轉為垂直單欄排列 (`grid-cols-1`)？價格文字是否清晰可見？
* [ ] **`contact.html`**：嵌入的 Google 地圖是否能自動適應手機寬度 (`w-full`)？聯絡表單的輸入框是否好點選？

### 2. Vibe QA 自然語言精修對照表（指引 AI 具體修改）

請運用你在課堂所學的 HTML/CSS 專業概念，向 Antigravity 下達具體、專業的手術式修改指令：

| 品管面向 | ❌ 錯誤的模糊指令 (Garbage In) | ✅ 專業品管師指令 (Professional Prompt) |
| :--- | :--- | :--- |
| **字體與氣質** | 「字體不好看，改文青一點。」 | 「請在所有 4 個 HTML 的 `<head>` 引入 Google Fonts 的 `Noto Serif TC`（思源宋體），將所有標題套用該字體；並在 `mystyles.css` 將內文行高設為 `line-height: 1.8`、字距設為 `0.05em`，提升日系空靈呼吸感。」 |
| **手機端菜單卡片** | 「手機版菜單壞掉了。」 | 「在 `menu.html` 中，菜單卡片在手機端擠在一起。請修改 Tailwind class，在小於 768px 時顯示為單欄 (`grid-cols-1`)，在 `md:` 平板尺寸以上才顯示為三欄 (`md:grid-cols-3`)，並為每張卡片加上 `shadow-sm hover:shadow-md transition-shadow`。」 |
| **清除假字與假價格** | （放任不管） | 「請全面巡檢 index, about, menu, contact 四個頁面，清除所有 `Lorem Ipsum` 與預設文字！菜單請填寫真實手沖品名（耶加雪菲水洗、藝伎蜜處理）與真實價格（NT$ 180 / NT$ 250）；門市資訊請填寫真實世新大學周邊地址與營業時間。」 |
| **跨頁導航一致性** | 「各頁面的選單長得不太一樣。」 | 「請檢查 4 個 HTML 頁面的頂部 `<nav>`：首頁的 active 標籤應在『首頁』；about.html 的 active 應在『關於我們』；menu.html 在『風味菜單』；contact.html 在『門市資訊』。請確保 4 個檔案的導覽按鈕名稱、字級與連結路徑完全一致！」 |

> 💡 **老師的真心話**  
> 當你按下 `F12` 切換到手機尺寸時，請把自己當成第一次走進店裡的手機訪客。按鈕夠大好按嗎？字體讀起來舒適嗎？在指揮 AI 修改時，千萬不要講「弄好看一點」這種模糊的話，直接給它 Tailwind 類別（例如 `line-height: 1.8`、`grid-cols-1 md:grid-cols-3`），AI 就能像外科手術一樣精準修復！

---

## Ⅳ. 實戰任務三：部署多頁專案至 GitHub Pages 公開發布 (Deployment)

經過精細打磨，你的網站現在已經達到 100 分水準！現在，我們要先將專案推送至 GitHub 並啟用 GitHub Pages 發布！

![GitHub Pages 部署操作 3 步驟](img/diagram_14_deployment_flow.png)

### 部署操作 3 步驟：

#### 步驟 1：在 GitHub Desktop 提交並發布 (Commit & Publish)
1. 打開 **GitHub Desktop**。
2. 檢查 Changes 列表，在左下角 Summary 輸入：  
   `完成多頁網頁 RWD 品管修復與文案潤飾，準備部署`
3. 點擊 **`Commit to main`**。
4. 點擊主畫面上方的 **`Publish repository`** 按鈕。
5. 🚨 **極度關鍵步驟**：**取消勾選「Keep this code private」！**  
   （GitHub Pages 免費版只支援公開儲存庫，若未取消勾選將無法啟用網頁發布功能）。

#### 步驟 2：在 GitHub 網頁啟動 GitHub Pages
1. 點擊 GitHub Desktop 頂部選單的 **`Repository > View on GitHub`**，在瀏覽器打開你的線上專案。
2. 點擊上方的 **`Settings`**（設定頁籤）。
3. 在左側側邊欄點擊 **`Pages`**。
4. 在 **Build and deployment** 區塊：
   * **Source**：選擇 `Deploy from a branch`
   * **Branch**：選擇 `main`，資料夾保持 `/(root)`
   * 點擊右側的 **`Save`** 按鈕！

#### 步驟 3：取得專屬線上網址並驗證
等待 1~3 分鐘重新整理該設定頁，上方會出現醒目的綠色提示訊息：  
**"Your site is live at https://<你的GitHub帳號>.github.io/<專案名稱>/"**

點擊該網址，拿出你的真實手機掃描或點擊測試，確認 4 個分頁是否都能在公網上順暢切換瀏覽！

> 💡 **老師的真心話**  
> 發布到 GitHub Pages 後，如果點進其他頁面跳出 404，請第一時間檢查檔名的大小寫！Windows 電腦不分大小寫，但 GitHub 的 Linux 伺服器分得清清楚楚。檔名 `menu.html` 若在按鈕寫成 `Menu.html` 就會直接死掉。務必親手在手機上把 4 個頁面都點過一遍，才算真正驗收完成！

---

## Ⅴ. 實戰任務四：進階雲端部署 — 連結 Vercel 支援現代前端框架 (Deploying with Vercel)

將網頁部署到 `github.io` 之後，為什麼我們還需要進一步學習連結 **Vercel**？

### 1. 為什麼前端框架在 GitHub Pages 上常常「水土不服」？
在 Vibe Coding 的過程中，當你向 AI 提出更豐富的互動需求（例如：動態購物車、商品篩選器、流暢頁面轉場或模組化元件）時，AI 代理人往往不只有寫純靜態 HTML，而是會自動引入現代前端框架與建置工具（如 **React**、**Vue**、**Next.js**、**Vite** 或 **Tailwind CLI**，專案目錄中會出現 `package.json`、`src/`、`.jsx`、`.tsx` 或 `.vue` 等檔案）。

這類包含前端框架的專案若直接放在 GitHub Pages，會遇到三大技術瓶頸：
1. **無法直接運行未編譯的框架原始碼**：GitHub Pages 預設只是純靜態檔案伺服器，瀏覽器看不懂尚未打包編譯（Build）的 `.jsx` 或 `.vue` 語法，打開網址只會看到**一片空白**或報錯。
2. **子目錄路徑錯亂 (`/專案名稱/`)**：GitHub Pages 的網址結構帶有 `/專案名稱/` 子路徑，常導致前端框架打包後的預設根路徑資源（如 `/assets/...`）全部破圖或載入失敗。
3. **前端路由 (SPA Routing) 重新整理即 404**：使用 React Router 或 Vue Router 的單頁應用程式，在切換頁面後一旦按下瀏覽器重新整理，GitHub Pages 就會直接跳出 `404 Not Found`。

👉 **最佳解決方案：將 GitHub 儲存庫連結至 Vercel！**  
**Vercel** 是全球前端開發者最推崇的現代雲端部署平台。它能直接讀取你的 GitHub 專案，**自動偵測前端框架並在雲端完成編譯打包 (`npm run build`)**，同時提供獨立的根網域（`https://專案名稱.vercel.app`），無論是純靜態 HTML 或複雜的前端框架都能完美運行！

---

### 2. GitHub 連結 Vercel 部署操作 4 步驟

#### 步驟 1：使用 GitHub 帳號一鍵註冊並登入 Vercel
1. 在瀏覽器前往 Vercel 官方網站：**`https://vercel.com`**，點擊右上角的 **`Sign Up`**（若已有帳號請點 **`Log In`**）。
2. 在方案類型選擇 **`Hobby`**（個人與教育免費方案），輸入你的姓名。
3. 點擊 **`Continue with GitHub`**，並在 GitHub 授權畫面點擊同意，完成帳號連動。

#### 步驟 2：從 GitHub 匯入你的專案儲存庫 (Import Git Repository)
1. 進入 Vercel 控制台（Dashboard）主畫面後，點擊右上角的 **`Add New...`** 按鈕，選擇 **`Project`**。
2. 在左側 **Import Git Repository** 清單中，找到你剛才推送到 GitHub 的專案名稱。
   * 💡 *小撇步*：如果清單中沒看到你的專案，請點擊下方的 **`Adjust GitHub App Permissions`**，在彈出的 GitHub 權限設定頁中選擇 **`All repositories`**（或勾選該專案儲存庫），點擊 **`Save`** 後返回即可看到。
3. 點擊該專案右側的 **`Import`** 按鈕。

#### 步驟 3：檢視前端框架自動偵測設定並一鍵部署 (Configure & Deploy)
1. 進入 **Configure Project** 頁面，Vercel 會自動掃描你的專案結構：
   * **Framework Preset（框架預設集）**：
     * **含有前端框架的專案**：若專案內含 `package.json`（如 Vite、React、Next.js、Vue），Vercel 會自動辨識並顯示對應的框架圖示，且自動填妥 Build Command（如 `npm run build`）與 Output Directory（如 `dist` 或 `.next`），**完全不需手動修改**！
     * **純靜態 HTML 專案**：此處會自動顯示為 **`Other`**，同樣保持預設即可直接部署。
   * **Root Directory（專案根目錄）**：保持預設的 `./` 即可（除非你的前端框架檔案與 `package.json` 被放在子資料夾中，才需點擊 `Edit` 指定該子資料夾）。
2. 直接點擊最下方的 **`Deploy`** 按鈕！

#### 步驟 4：雲端自動編譯與取得 `.vercel.app` 專屬網址
1. 點擊後，畫面會進入 **Building（雲端建置中）** 狀態，Vercel 會自動幫你安裝相依套件 (`npm install`) 並編譯前端框架（約需 30 秒至 1 分鐘）。
2. 當畫面灑下慶祝彩帶並顯示 **「Congratulations!」** 時，代表你的網站已經成功上線！
3. 點擊 **`Continue to Dashboard`** 進入專案主控台，在 **Domains** 區塊即可取得你的專屬網址：  
   👉 **`https://<專案名稱>.vercel.app`**

---

### 3. GitHub Pages 與 Vercel 特性比較與 AI 協作除錯

| 比較項目 | GitHub Pages (`github.io`) | Vercel (`vercel.app`) |
| :--- | :--- | :--- |
| **適用專案類型** | 純靜態網頁（純 HTML / CSS / 傳統 JS） | **通吃！** 純靜態網頁 ＋ **所有現代前端框架 (React / Vue / Vite / Next.js)** |
| **雲端自動編譯** | 預設無（需手動打包或另寫 GitHub Actions） | **全自動偵測**並執行 `npm install` 與 `npm run build` |
| **網址結構** | `https://帳號.github.io/專案名稱/`（子目錄） | `https://專案名稱.vercel.app/`（**獨立根網域，不破圖**） |
| **儲存庫權限要求** | 免費版強制要求 **Public（公開）** | **Public 與 Private（私有）皆可免費部署** |
| **自動同步更新** | GitHub Desktop `Push` 後自動更新 | GitHub Desktop `Push` 後**自動重新編譯並更新** |

* 🔧 **遇到 Vercel 編譯失敗 (`Build Failed`) 時的 Vibe 急救法**：  
  若 AI 寫的前端框架專案在 Vercel 建置時出現紅字錯誤，請直接複製 Vercel 畫面上的 **Build Logs（錯誤日誌）**，貼回 Antigravity 對話框：
  ```text
  我將這個專案連結到 Vercel 部署時出現以下 Build Error，請幫我檢查 package.json 或程式碼並直接修復錯誤：
  [在此貼上 Vercel 的紅字錯誤訊息]
  ```
  等 AI 修復後，再到 GitHub Desktop 點擊 **`Commit to main`** 與 **`Push origin`**，Vercel 就會自動重新編譯並順利上線！

> 💡 **老師的真心話**  
> 為什麼老師在教完 `github.io` 之後，一定要帶大家連結 Vercel？因為在 Vibe Coding 時代，AI 隨時都可能為了幫你實現超酷的動態介面而動用 React、Vite 或 Next.js 等現代前端框架。很多同學把含有前端框架的網頁推上 GitHub Pages 後發現一片空白，還以為自己把網站做壞了！學會「GitHub + Vercel」這套業界標準的黃金組合後，不管 AI 用什麼前端框架寫網頁，你都能在 1 分鐘內讓它在雲端自動編譯上線。而且往後只要在 GitHub Desktop 按下 Push，兩邊的網站都會自動同步更新，這就是真正的現代雲端工程實力！

---

## Ⅵ. 實戰任務五：打造雙向作品集生態系 (Portfolio Interlinking)

一個成熟的資訊傳播人，懂得將所有獨立專案相互串聯，形成個人的「數位資產網絡」！

![雙向作品集生態系串聯 (Portfolio Interlinking)](img/diagram_14_portfolio_interlinking.png)

### 動作 1：在「個人線上履歷」新增老王咖啡展示卡片
1. 在 GitHub Desktop 左上角切換儲存庫至你的個人履歷倉庫（`你的帳號.github.io`）。
2. 用 VS Code 打開履歷的 `index.html`，找到「作品集 (Projects/Portfolio)」區塊。
3. 加入一組精美的專案展示卡片 HTML（可同時放上 `github.io` 或支援前端框架的 `vercel.app` 網址）：

```html
<!-- 作品集新增項目 -->
<div class="border rounded-xl p-6 bg-white shadow-sm hover:shadow-md transition">
  <span class="text-xs font-semibold px-2.5 py-0.5 rounded bg-amber-100 text-amber-800">AI 代理人協同開發</span>
  <h3 class="text-xl font-bold mt-2 text-stone-800">老王手沖咖啡 多頁形象官網</h3>
  <p class="text-stone-600 text-sm mt-2 leading-relaxed">
    運用 PRD 需求規範與 Vibe Coding 流程，與 Google Antigravity 2.0 代理人協同實作之 4 頁式日系形象官網。具備客製 AI 影像素材、全站跨頁無縫導航與完整手機端 RWD 適配，並透過 GitHub 與 Vercel 完成雲端部署。
  </p>
  <div class="mt-4 flex space-x-4 text-sm">
    <a href="https://專案名稱.vercel.app" target="_blank" class="text-amber-700 font-bold hover:underline">
      👉 線上造訪網站 (Vercel)
    </a>
    <a href="https://你的帳號.github.io/專案名稱/index.html" target="_blank" class="text-stone-600 font-semibold hover:underline">
      🔗 GitHub Pages 備份站
    </a>
  </div>
</div>
```
4. 在 GitHub Desktop 中進行 Commit 並點擊 **Push origin** 推送上線！

### 動作 2：在「老王咖啡」頁尾加入導回「個人履歷」的設計師簽名
1. 在 GitHub Desktop 切換回你的老王咖啡倉庫。
2. 指揮 Antigravity 或手動打開 4 個頁面的 `<footer>` 區塊，加入設計師品牌署名：

```html
<p class="text-center text-stone-500 text-xs mt-4">
  Designed & Developed with AI Agent by 
  <a href="https://你的帳號.github.io/" class="underline hover:text-[#556B2F] font-bold" target="_blank">
    你的姓名
  </a> 
  | 世新資傳 2026
</p>
```
3. Commit 並 Push！至此，你的個人履歷與多頁專案達成了完美的雙向互通！

> 💡 **老師的真心話**  
> 「雙向串聯」是專業設計師非常重視的細節。面試官看你的履歷時，能一鍵點進你的老王咖啡專案；在老王咖啡專案頁尾，又能看到你作為設計師的署名並點回你的履歷。這種環環相扣的專業度，會讓你的作品集瞬間從學生作業升格為商業級專案！

---

## Ⅶ. 專案終極自我檢核清單 (Final Project Checklist)

在將線上網址提交至數位教學平台前，請逐一打勾確認：

* [ ] **4 個分頁完整運作**：`index.html`、`about.html`、`menu.html`、`contact.html`（或框架路由頁面）皆能透過導航列互相順暢切換。
* [ ] **無死連結與 404 錯誤**：所有跨頁連結均使用正確相對路徑或路由，無多餘的斜線 `/` 或大小寫拼寫錯誤。
* [ ] **真實內容滿載**：全站無任何 `Lorem Ipsum` 假字、無 `$000` 假價格，皆為符合主題的真實文案。
* [ ] **專屬素材到位**：全站無任何未替換的灰色 placeholder 假圖，皆為 `generate_image` 繪製或專屬實拍照。
* [ ] **跨裝置 RWD 完美適配**：在 iPhone 手機模式下，導覽列、卡片網格與嵌入地圖皆能自適應單欄流暢顯示。
* [ ] **GitHub Pages 順暢上線**：已將專案公開推送至 GitHub 並啟用 `github.io` 網址。
* [ ] **Vercel 雲端連結與框架支援**：已將 GitHub 儲存庫匯入 Vercel 並取得 `.vercel.app` 網址，確保專案中可能包含的前端框架完成雲端編譯並正常顯示。
* [ ] **雙向串聯大功告成**：個人履歷網站有本專案的展示卡片，本專案頁尾有導回個人履歷的設計師超連結。

> 💡 **老師的真心話**  
> 這份終極檢核清單，就是你專業水準的試金石。確認全站沒有任何 Lorem Ipsum 假字、沒有破圖、跨頁導航與前端框架完全暢通。當所有項目都打勾時，你就可以自信滿滿地將網址繳交上去了！

---

## Ⅷ. 踩坑急救包 (Troubleshooting)

* **Q1：GitHub Pages 網址打開後顯示 404 Not Found？**  
  👉 **解答**：
    1. 檢查倉庫是否設為 **Public（公開）**。如果剛才建立時勾了 Private，請至 Settings 頁面最下方的 Danger Zone 改為 Public。
    2. 檢查 GitHub Desktop 是否有未 Push 的代碼。務必點擊 **Push origin** 將本地代碼推上雲端。
    3. 首頁檔名必須嚴格為小寫的 `index.html`（不能寫成 `Index.html` 或 `home.html`）。
* **Q2：首頁能正常打開，但點進「風味菜單」卻出現 404？**  
  👉 **解答**：這是 Linux 伺服器對**大小寫極度敏感**造成的！請檢查你的檔案名稱是否為 `menu.html`，而你的按鈕連結是否寫成了 `href="Menu.html"`。在 Windows 本機測試時大小寫不分，但放到雲端伺服器上就會直接失效！
* **Q3：圖片在本地預覽正常，發布到 GitHub Pages 後卻變成破圖？**  
  👉 **解答**：檢查 HTML 裡的圖片路徑！不能寫絕對路徑 `src="/img/hero.jpg"`（開頭帶斜線），因為 GitHub Pages 的網址包含了子目錄 `/專案名稱/`。請改為相對路徑 `src="img/hero.jpg"`，或是改用 **Vercel** 部署（享有獨立根網域，不會受子目錄影響）！
* **Q4：我的網頁在本機預覽很正常，但因為包含了前端框架（如 React / Vite / Vue），推上 GitHub Pages 後打開卻是一片空白？**  
  👉 **解答**：因為 GitHub Pages 只能直接讀取純靜態 HTML，無法直接運行未經打包編譯的 `.jsx` / `.vue` 原始碼與 `package.json` 套件。請立即按照「**Ⅴ. 實戰任務四**」的步驟，將你的 GitHub 儲存庫連結至 **Vercel**，讓 Vercel 自動執行 `npm run build` 編譯並產生 `.vercel.app` 網址，你的前端框架就能完美復活！
* **Q5：在 Vercel 匯入專案時找不到我的 GitHub 儲存庫，或單頁應用 (SPA) 在 Vercel 重新整理內頁時出現 404 怎麼辦？**  
  👉 **解答**：
    1. **找不到專案**：點擊 Vercel 匯入清單下方的 `Adjust GitHub App Permissions`，在 GitHub 授權設定中選擇 `All repositories` 並按下 Save。
    2. **SPA 內頁重新整理 404**：若你的專案使用了 React Router 或 Vue Router，請對 Antigravity 下令：「`請幫我在專案根目錄新增 vercel.json，設定將所有路由 rewrite 導向至 /index.html`」，接著在 GitHub Desktop Commit 並 Push 即可解決！

---

> 💡 **老師的真心話**  
> 恭喜大家完整走過這趟劃時代的 Vibe Coding 之旅！  
> 回想五週前，大家可能還在為如何寫出第一個標籤而苦惱；而今天，你們已經能獨立規劃 PRD、指揮 AI 代理人實作、嚴格把關多頁面 RWD 品管，並同時掌握 GitHub Pages 與 Vercel 兩大雲端部署利器，完成全球發布與作品集串聯。這套思維與實戰能力，將會是你們在 AI 時代最核心、最無可取代的競爭力。恭喜大家順利通關！
