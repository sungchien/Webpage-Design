---
name: textbook-writer

description: >
  當使用者要求撰寫、整理、改寫、擴充或潤飾課程講義時，請使用本 Skill。
  本 Skill 的目標不是產生聊天式回答，而是協助建立具有完整章節、
  清楚邏輯、正式書面語及大學教材風格的 Markdown 文件。
  適用於教材撰寫、講義整理、課程設計、教育內容重構、
  Markdown 教材編輯以及教學文件標準化等工作。

version: "1.0"

author: "AI Agent 課程"

tags:
  - 教材
  - Markdown
  - 教學
  - 寫作
  - 課程設計

---

# 教材撰寫 Skill

## Skill 目的

本 Skill 用於協助 AI Agent 將零散筆記、草稿、現有 Markdown 文件或課程資料，整理成具有完整結構的大學教材。

本 Skill 的重點並不是摘要內容，而是重新組織知識，使其成為具有良好教學流程、容易閱讀且適合作為課程教材的文件。

---

# 什麼情況應該使用本 Skill？

當使用者提出下列需求時，應優先使用本 Skill：

- 撰寫教材
- 整理課程講義
- 改寫 Markdown 文件
- 擴充教學內容
- 將筆記整理成教材
- 建立課程模組
- 編寫訓練教材
- 統一教材格式
- 建立教學文件

下列情況通常不需要使用本 Skill：

- 一般聊天
- 簡短問答
- 電子郵件撰寫
- 程式除錯
- 數學計算
- 圖片生成

---

# 工作流程

當 Agent 選擇本 Skill 後，請依照下列流程完成工作。

## 第一步：理解教材需求

先分析使用者希望完成的教材內容，包括：

- 教材主題
- 讀者程度
- 課程目標
- 文件用途
- 預期輸出格式

若資訊不足，可先向使用者詢問。

先請使用者輸入02~16當中的一個數字。
運用@Script(scripts/read_weekly_pdf.py)比對資料夾中檔名為使用者輸入週次的pdf檔案，
如果資料夾中有檔名符合的pdf檔案，將其轉為Markdown檔案，並設計課程內容大綱，
如果沒有符合，依據01_課程介紹.md對本週課堂的規劃設計課程內容大綱。

將設計的課程內容與使用者討論，直到使用者確認無誤。

---

## 第二步：閱讀教材寫作規範

開始撰寫之前，請先閱讀：

@Resource(resources/writing_style.md)

此文件定義教材的：

- 敘事風格
- 標題規則
- 段落安排
- 名詞使用方式
- Markdown 排版原則

除非使用者明確要求，否則所有教材均應遵循此文件。

---

## 第三步：閱讀教材範例

接著閱讀：

@Resource(examples/02_deep_learning.md)

請觀察：

- 章節安排
- 段落長度
- 概念銜接方式
- 程式碼說明方式
- 表格與圖例呈現方式

請學習整體風格，而不是直接複製內容。

---

## 第四步：整理 Markdown

若來源文件為 Markdown，請先執行：

@Script(scripts/clean_markdown.py)

利用 Script 完成：

- Markdown 正規化
- 清除多餘空白
- 修正標題格式
- 統一換行
- 基本排版整理

完成後，再開始教材撰寫。

---

## 第五步：完成教材

依照前述規範，重新整理教材內容。

請特別注意：

- 建立完整章節
- 補充必要說明
- 保持敘事連續
- 使用正式書面語
- 維持教材閱讀體驗

避免：

- 投影片式排版
- 大量條列
- 一句一段
- 聊天式回答
- 社群媒體風格

**特別要求**：每節結束前都提供一個課堂上的小活動，
並且也有一段 ```老師的提醒``` 或 ```老師的真心話```，提醒容易混淆的觀念或實務上容易發生錯誤的地方。


---

# 輸出要求

完成教材時，請確認符合下列要求。

## 教材風格

採用正式書面語，但親切而平實，用簡單明瞭的方式說明，讓非電腦相關科系的大學生能夠理解。

閱讀體驗應接近大學教材

而不是：

- ChatGPT 回答
- PowerPoint
- 部落格文章

---

## 標題層級

使用標準 Markdown：

```text
# 第一層標題

## 第二層標題

### 第三層標題
```

請勿跳階使用標題。

---

## 段落原則

每一個段落應完整說明一個概念。

段落之間應具有自然轉承。

避免：

- 一句一段
- 過多留白
- 只有一兩行文字
- 大量碎片化條列
- 單一自然段或 `>` 引言區塊字數過於龐大（超過約 150～200 字時，應依語意轉折適度分段；若在 `>` 區塊內分段，段落間空行必須保留 `>` 符號）

---

## 專有名詞

重要術語第一次出現時，請同時提供中英文名稱。

例如：

> Context Engineering（上下文工程）

之後即可直接使用中文。

---

## 程式碼

若教材包含程式碼：

- 程式碼前先說明目的。
- 程式碼後說明重要內容。
- 不要只貼程式碼而沒有解釋。
- 長篇程式碼、範本或提示詞區塊超過約 35～40 行時，應依功能或章節切分為多個子區塊（例如 `Part 1`、`Part 2`），避免單一 `<pre>` 橫跨多頁並在匯出 PDF 時被截斷。
- 提示詞或文字區塊中的長條列項目（超過約 120～150 字）應改為結構化縮排子項目；純敘事句中切勿隨意插入手動硬換行（`\n`），以免折出只有 2～3 字的孤立短尾行。

---

## 表格

表格用於整理資訊。

不要用表格取代完整說明。

表格前後均應搭配完整文字。

---

## KaTeX 數學公式與 VS Code Preview 排版規範

若教材包含 KaTeX 數學公式與 VS Code 閱讀排版：

1. **粗體字標記前留空白 (`**`)**：在冒號（`：`）、全形標點（`，。】)`）或中文漢字後使用 `**粗體**` 時，`**` 開頭前方**必須帶有半形空白**（例如 `： **粗體**`），否則 VS Code Preview 解析器無法辨識為粗體語法。
2. **加色區塊 (`>`) 換行連續性**：引言/提示區塊 `>` 的多行內文之間若有空行，該空行**必須帶有 `>` 符號**（即單獨一行的 `>`），否則 VS Code Preview 會將其撕裂為多個獨立的分散框線。
3. **表格內部不得有空白行**：Markdown 表格行與行之間**絕不能有空行**，否則 VS Code Preview 會中斷表格渲染。
4. **純文字美金符號轉譯 (`\$50`)**：內文中的金額（如 `\$50` 元、`\$800` 元）必須轉譯，防止 VS Code 將同一段落中的多個美金符號誤判為 KaTeX 數學公式開頭與結尾。
5. **反斜線轉譯保護**：當使用 Python 寫入或產出 Markdown 檔案時，公式中的反斜線（`\text`, `\frac`, `\beta`, `\right`, `\left`, `\times`, `\approx`, `\rightarrow`）必須採用原始字串 `r"..."` 或雙重轉譯。
6. **完成後強制清理**：每次產出或編輯講義 Markdown 檔後，**必須強制執行** `@Script(scripts/clean_markdown.py)` 自動校正並修復所有 VS Code 排版、KaTeX 語法與 Markdown 格式！

---

## VS Code Preview 匯出 PDF 防截斷排版與樣式規範

當講義透過 VS Code Markdown Preview Enhanced (MPE) 搭配 Puppeteer 匯出 PDF（預設 `scale: 1.15`、邊距 `1.5cm`、內文 `16pt`、程式碼 `13pt`）時，MPE 內建主題（如 `github-light.css`、`prism_theme`）的預設樣式容易導致文字右緣切截、跨頁漏行或表格欄寬崩塌。撰寫與編輯講義時，必須同時遵循下列 **內容結構原則** 與 **CSS 覆寫規範**：

### 一、長段落與程式／提示詞區塊防截斷撰寫原則

1. **切分過長 Code Block（上限約 35～40 行）**：當程式範例、文件範本（如 `PRD.md`、`implementation_plan.md`）或長篇提示詞超過約 **35～40 行** 時，**禁止放入同一個超長區塊**，應依邏輯拆分為數個子區塊（例如 `範本 Part 1`、`Part 2`、`Part 3`），並於前後補充引導文字，避免瀏覽器處理多頁 `<pre>` 分頁時發生大片留白或漏行。
2. **避免單行過長與任意手動硬換行**：在預設版面下，程式碼區塊每視覺行約僅能容納 **31～33 個全形中文字**。超過約 120～150 字的單行條列應拆成具縮排階層的子項目；但 **不可在純敘事句中間隨意插入手動 `\n` 折行**（若人工換行處略大於 33 字，PDF 會先自動折行一次、遇 `\n` 再強制換行，產生只有 2～3 字的孤立短尾行），應交由 CSS `pre-wrap` 自動折行。
3. **高字數段落與引言框適度分段**：一般段落或 `> 💡 **老師的真心話**` 等 `blockquote` 區塊若單段超過約 **150～200 字**，應依語意轉折拆分為 **2～3 個自然段**。若於 `>` 區塊內分段，段落之間的空行 **必須保留單獨一行的** `>` 符號。
4. **表格儲存格精簡控制**：表格儲存格內避免放置超長連續不換行字串或過長段落，使 `table-layout: auto` 能依內容分配合理欄寬。

### 二、檔首 CSS 防截斷覆寫重點

因 MPE 內建規則具較高選擇器權重（如 `html body pre`、`pre[class*="language-"]`、`@media print { html body pre { page-break-inside: avoid } }`），僅撰寫簡短的 `pre, code` 無法生效，必須於講義檔首 `<style>` 落實下列規則：

1. **程式碼區塊與行內代碼分離覆寫**：對 `html body pre`、`html body pre[class*="language-"]`、`html body .highlight pre`、`html body pre > code`、`html body code[class*="language-"]`（並於 `@media print` 內重複宣告）設定 `white-space: pre-wrap !important`、`overflow-wrap: break-word !important`、`word-break: break-word !important`、`overflow: visible !important`，並以 `page-break-inside: auto !important; break-inside: auto !important;` 允許長程式碼自然跨頁。行內代碼 `html body code` 則獨立維持 `white-space: normal !important`，避免與 `pre` 互相干擾。
2. **表格寬度與斷字保護**：對 `html body table` 覆寫 MPE 預設的 `overflow: auto` 與 `word-break: keep-all`，強制設定 `display: table !important; width: 100% !important; max-width: 100% !important; table-layout: auto !important; overflow: visible !important;`，並對 `table, th, td` 使用 `word-break: normal !important; overflow-wrap: break-word !important;`（ **嚴禁對表格儲存格使用** `overflow-wrap: anywhere`，以免 Chromium 將窄欄壓縮至單字元寬度而拆斷英文單字）；同時對 `tr` 加入 `page-break-inside: avoid; break-inside: avoid;`。
3. **段落、清單與引文區塊容許跨頁與斷行**：對 `p, li, blockquote` 設定 `overflow-wrap: break-word !important; max-width: 100% !important;`，並讓 `blockquote` 設定 `overflow: visible !important; page-break-inside: auto !important; break-inside: auto !important;`。
4. **隱藏 `h2` 換頁前的孤立分隔線**：講義已設定 `h2 { page-break-before: always; break-before: page; }`，為防止前一頁恰好寫滿時 `---` 單獨掉到新頁形成空白線頁，必須於 `@media print` 內加入 `html body hr:has(+ h2) { display: none !important; }`。

### 三、講義檔首標準範本（YAML Frontmatter + `<style>`）

新建或重整講義 Markdown 時，請直接於檔首套用下列標準設定（將 `headerTemplate` 的週次與單元名稱替換為當週內容）：

```markdown
---
puppeteer:
  displayHeaderFooter: true
  scale: 1.15
  headerTemplate: '<div style="font-size: 11px; margin: 0 auto;">第 X 週：課程單元名稱</div>'
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
    overflow-wrap: break-word !important;
    word-wrap: break-word !important;
  }

  /* 階層標題微調 */
  h1 { font-size: 30pt !important; margin-bottom: 0.5em !important; }
  h2 { font-size: 24pt !important; page-break-before: always; break-before: page; }
  h3 { font-size: 20pt !important; }
  h4 { font-size: 18pt !important; }

  /* 長段落、清單與引文避免溢出或跨頁截斷 */
  html body p,
  html body li,
  html body blockquote {
    overflow-wrap: break-word !important;
    word-wrap: break-word !important;
    max-width: 100% !important;
  }

  html body blockquote {
    overflow: visible !important;
    page-break-inside: auto !important;
    break-inside: auto !important;
    padding: 8px 15px !important;
  }

  /* 表格文字放大與排版優化（覆寫 MPE 預設 keep-all 與 overflow: auto，避免寬度溢出截斷） */
  html body table {
    display: table !important;
    width: 100% !important;
    max-width: 100% !important;
    table-layout: auto !important;
    overflow: visible !important;
    word-break: normal !important;
    overflow-wrap: break-word !important;
    box-sizing: border-box !important;
  }

  html body table,
  html body th,
  html body td {
    font-size: 15pt !important;
    line-height: 1.5 !important;
    white-space: normal !important;
    word-break: normal !important;
    overflow-wrap: break-word !important;
  }

  html body tr {
    page-break-inside: avoid;
    break-inside: avoid;
  }

  /* 行內代碼與程式碼區塊分離設定（pre > code 置後以維持更高權重，防止 MPE 覆寫造成 PDF 截斷） */
  html body code {
    font-size: 13pt !important;
    font-family: Consolas, "Courier New", monospace !important;
    white-space: normal !important;
    word-wrap: break-word !important;
    overflow-wrap: break-word !important;
    word-break: break-word !important;
  }

  html body pre,
  html body pre[class*="language-"],
  html body .highlight pre,
  html body pre > code,
  html body code[class*="language-"] {
    font-size: 13pt !important;
    font-family: Consolas, "Courier New", monospace !important;
    white-space: pre-wrap !important;
    word-wrap: break-word !important;
    overflow-wrap: break-word !important;
    word-break: break-word !important;
  }

  html body pre,
  html body pre[class*="language-"],
  html body .highlight pre {
    overflow: visible !important;
    overflow-x: visible !important;
    page-break-inside: auto !important;
    break-inside: auto !important;
    max-width: 100% !important;
    box-sizing: border-box !important;
  }

  /* Mermaid 流程圖節點字體放大 */
  .mermaid text {
    font-size: 14px !important;
  }

  @media print {
    html body pre,
    html body pre[class*="language-"],
    html body .highlight pre,
    html body pre > code,
    html body code[class*="language-"] {
      white-space: pre-wrap !important;
      overflow-wrap: break-word !important;
      word-break: break-word !important;
      overflow: visible !important;
      page-break-inside: auto !important;
      break-inside: auto !important;
    }

    html body code {
      white-space: normal !important;
      overflow-wrap: break-word !important;
      word-break: break-word !important;
    }

    html body blockquote {
      overflow: visible !important;
      page-break-inside: auto !important;
      break-inside: auto !important;
    }

    html body table {
      display: table !important;
      overflow: visible !important;
      word-break: normal !important;
    }

    /* h2 已強制換頁，隱藏緊鄰 h2 前的分隔線，避免產生只有一條線的空白頁 */
    html body hr:has(+ h2) {
      display: none !important;
    }
  }
</style>
```

---

# 完成前檢查

送出教材之前，請再次確認：

- 是否符合教材寫作風格。
- 是否具有完整章節。
- 是否維護自然敘事。
- 是否遵循教材寫作規範。
- 是否參考教材範例。
- 是否已將超過 35～40 行的程式碼／範本區塊與高字數段落／`>` 引言框（約 150～200 字以上）適度切分，並確認無過長單行或不當手動換行。
- 檔首是否已完整納入 VS Code Preview 匯出 PDF 防截斷 `<style>` 規範（含 `pre-wrap`、`page-break-inside: auto`、`table` 寬度修正與 `hr:has(+ h2)` 規則）。
- 是否完成 Markdown 與 KaTeX 自動整理 (`clean_markdown.py`)。
- 是否沒有聊天式語氣。
- 是否適合作為正式教材。
- 每節結束前是否有課堂小活動以及```老師的提醒```。

---

# 最終輸出

請輸出完整 Markdown 文件，並確保已執行 `clean_markdown.py` 校正格式。

除非使用者另有要求，不需加入任何額外說明。