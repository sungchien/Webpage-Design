import os
import subprocess
from PIL import Image, ImageChops

output_dir = os.path.abspath("img")
os.makedirs(output_dir, exist_ok=True)
user_data_dir = os.path.abspath("scratch/edge_diagram_profile")
os.makedirs(user_data_dir, exist_ok=True)
edge_path = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"

BASE_CSS = """
  * { box-sizing: border-box; }
  body {
    margin: 0;
    padding: 30px;
    background: transparent;
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", "Microsoft JhengHei", "PingFang TC", sans-serif;
    display: inline-block;
  }
  .container {
    background: #ffffff;
    border-radius: 20px;
    padding: 32px 40px;
    box-shadow: 0 10px 40px rgba(15, 23, 42, 0.08), 0 1px 3px rgba(15, 23, 42, 0.05);
    border: 1px solid #e2e8f0;
    display: flex;
    flex-direction: column;
    gap: 24px;
    max-width: 1100px;
  }
  .header {
    display: flex;
    align-items: center;
    gap: 14px;
    border-bottom: 2px solid #f1f5f9;
    padding-bottom: 16px;
  }
  .header-icon {
    width: 40px;
    height: 40px;
    border-radius: 12px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 20px;
    color: white;
  }
  .header-title {
    font-size: 22px;
    font-weight: 800;
    color: #0f172a;
    letter-spacing: -0.02em;
  }
  .header-subtitle {
    font-size: 14px;
    color: #64748b;
    margin-top: 2px;
  }
  .flow-row {
    display: flex;
    align-items: stretch;
    gap: 16px;
  }
  .card {
    flex: 1;
    background: #f8fafc;
    border: 1px solid #e2e8f0;
    border-radius: 16px;
    padding: 20px;
    display: flex;
    flex-direction: column;
    gap: 10px;
    position: relative;
  }
  .card.highlight {
    background: #f0fdf4;
    border-color: #86efac;
    box-shadow: 0 4px 20px rgba(34, 197, 94, 0.12);
  }
  .card.primary {
    background: #eff6ff;
    border-color: #93c5fd;
    box-shadow: 0 4px 20px rgba(59, 130, 246, 0.12);
  }
  .card.purple {
    background: #faf5ff;
    border-color: #d8b4fe;
    box-shadow: 0 4px 20px rgba(168, 85, 247, 0.12);
  }
  .card.amber {
    background: #fffbeb;
    border-color: #fde68a;
    box-shadow: 0 4px 20px rgba(245, 158, 11, 0.12);
  }
  .card.rose {
    background: #fff1f2;
    border-color: #fecdd3;
    box-shadow: 0 4px 20px rgba(244, 63, 94, 0.10);
  }
  .card-tag {
    font-size: 12px;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.05em;
    padding: 4px 10px;
    border-radius: 9999px;
    width: fit-content;
  }
  .card-title {
    font-size: 17px;
    font-weight: 700;
    color: #1e293b;
  }
  .card-desc {
    font-size: 14px;
    color: #475569;
    line-height: 1.6;
  }
  .arrow {
    display: flex;
    align-items: center;
    justify-content: center;
    color: #94a3b8;
    font-size: 24px;
    font-weight: bold;
    padding: 0 4px;
  }
  code {
    background: rgba(15, 23, 42, 0.06);
    padding: 1px 5px;
    border-radius: 4px;
    font-family: Consolas, "Courier New", monospace;
    font-size: 12.5px;
  }
"""

diagrams = {}

# 1. Updated diagram_12_prd_components.png
diagrams["diagram_12_prd_components.png"] = f"""<!DOCTYPE html><html><head><meta charset="utf-8"><style>{BASE_CSS}
  .comp-grid {{
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 16px;
  }}
</style></head><body>
<div class="container" style="width: 1050px;">
  <div class="header">
    <div class="header-icon" style="background: linear-gradient(135deg, #8b5cf6, #6366f1);">📋</div>
    <div>
      <div class="header-title">PRD (產品需求文件) 五大核心要素與技術護欄</div>
      <div class="header-subtitle">指揮 AI 代理人精準實作多頁式原生網站的唯一真相來源 (Single Source of Truth)</div>
    </div>
  </div>
  <div class="comp-grid">
    <div class="card">
      <div class="card-tag" style="background: #e0e7ff; color: #3730a3;">1. 網站目標 Goal</div>
      <div class="card-title">為誰解決什麼問題</div>
      <div class="card-desc">說明官網設立核心目的，例如傳遞專業信賴感、展示服務項目並引導線上預約初談 (CTA)。</div>
    </div>
    <div class="card">
      <div class="card-tag" style="background: #e0e7ff; color: #3730a3;">2. 目標受眾 Audience</div>
      <div class="card-title">網站是做給誰看的</div>
      <div class="card-desc">界定主要受眾（如：高壓上班族、青年）與次要受眾（家長、社區居民）的瀏覽情境。</div>
    </div>
    <div class="card">
      <div class="card-tag" style="background: #e0e7ff; color: #3730a3;">3. 視覺風格 Vibe</div>
      <div class="card-title">色彩計畫與氛圍調性</div>
      <div class="card-desc">拒絕模糊形容詞！明確指定至少 3 組 HEX 色票代碼（背景、主色、點綴色）與襯線/黑體搭配。</div>
    </div>
    <div class="card primary">
      <div class="card-tag" style="background: #dbeafe; color: #1e40af;">4. 網站地圖 Site Map</div>
      <div class="card-title">4 頁獨立架構與導航</div>
      <div class="card-desc">明確定義 <code>index.html</code> 等 4 個分頁檔名、各頁區塊階層，以及全站共用導覽列 <code>active</code> 規範。</div>
    </div>
    <div class="card rose">
      <div class="card-tag" style="background: #ffe4e6; color: #be123c;">5. 技術護欄 Tech Guardrails</div>
      <div class="card-title">限定原生三劍客・禁框架</div>
      <div class="card-desc">限定 HTML5 語意標籤 ＋ 外部 <code>style.css</code> ＋ 原生 <code>script.js</code>；<strong>嚴禁 Vue / React 等需編譯框架</strong>。</div>
    </div>
    <div class="card highlight">
      <div class="card-tag" style="background: #dcfce7; color: #15803d;">同儕審查 &amp; Planning</div>
      <div class="card-title">消除盲點再動工</div>
      <div class="card-desc">經同儕排雷並啟動 Planning Mode 檢視檔案樹後，才算真正合格的 AI 施工藍圖！</div>
    </div>
  </div>
</div>
</body></html>"""

# 2. Updated diagram_13_generation_flow.png
diagrams["diagram_13_generation_flow.png"] = f"""<!DOCTYPE html><html><head><meta charset="utf-8"><style>{BASE_CSS}</style></head><body>
<div class="container" style="width: 1050px;">
  <div class="header">
    <div class="header-icon" style="background: linear-gradient(135deg, #3b82f6, #1d4ed8);">⚙️</div>
    <div>
      <div class="header-title">Phase 2 生成核心工作流：從藍圖到多頁原生代碼</div>
      <div class="header-subtitle">一鍵批准計畫動工，100% 銜接課內 HTML / CSS / JS 知識的自動化工程</div>
    </div>
  </div>
  <div class="flow-row">
    <div class="card">
      <div class="card-tag" style="background: #e2e8f0; color: #475569;">步驟 1</div>
      <div class="card-title">核對計畫批准動工</div>
      <div class="card-desc">檢查 <code>implementation_plan.md</code> 確認無前端框架混入，點擊 Proceed 建立 4 個 <code>.html</code> 與共用 <code>style.css</code>。</div>
    </div>
    <div class="arrow">➔</div>
    <div class="card primary">
      <div class="card-tag" style="background: #dbeafe; color: #1e40af;">步驟 2</div>
      <div class="card-title">原生代碼品管導讀</div>
      <div class="card-desc">檢視語意化標籤、<code>style.css</code> 的 <code>:root</code> 色票變數與跨頁相對路徑，搭配 Visual Diff 掌握變更。</div>
    </div>
    <div class="arrow">➔</div>
    <div class="card amber">
      <div class="card-tag" style="background: #fef3c7; color: #b45309;">步驟 3</div>
      <div class="card-title">點選 JS 微互動賦能</div>
      <div class="card-desc">從「微互動點餐單」挑選漢堡選單、FAQ 摺疊或分類篩選，以純 DOM 邏輯寫入 <code>script.js</code>。</div>
    </div>
    <div class="arrow">➔</div>
    <div class="card highlight">
      <div class="card-tag" style="background: #dcfce7; color: #15803d;">步驟 4</div>
      <div class="card-title">AI 繪圖與里程碑提交</div>
      <div class="card-desc">呼叫 <code>generate_image</code> 產出 4 頁真實商業配圖，驗證跳轉無誤後於 GitHub Desktop 完成 Commit。</div>
    </div>
  </div>
</div>
</body></html>"""

# 3. New diagram_13_code_anatomy.png
diagrams["diagram_13_code_anatomy.png"] = f"""<!DOCTYPE html><html><head><meta charset="utf-8"><style>{BASE_CSS}
  .anatomy-grid {{
    display: grid;
    grid-template-columns: repeat(5, 1fr);
    gap: 12px;
  }}
</style></head><body>
<div class="container" style="width: 1060px;">
  <div class="header">
    <div class="header-icon" style="background: linear-gradient(135deg, #06b6d4, #0284c7);">🧩</div>
    <div>
      <div class="header-title">原生網頁三劍客代碼導讀：印證第 3～5 週課堂所學</div>
      <div class="header-subtitle">結構 (HTML5) × 視覺 (style.css) × 互動 (script.js) 職責分離，每一行代碼都清晰可讀</div>
    </div>
  </div>
  <div class="anatomy-grid">
    <div class="card">
      <div class="card-tag" style="background: #cffafe; color: #0e7490;">HTML5 結構</div>
      <div class="card-title" style="font-size: 15px;">語意化標籤</div>
      <div class="card-desc" style="font-size: 13px;">
        <code>&lt;header&gt;</code> 頁首<br>
        <code>&lt;nav&gt;</code> 導覽列<br>
        <code>&lt;main&gt;</code> 主內容<br>
        <code>&lt;section&gt;</code> 區塊<br>
        <code>&lt;footer&gt;</code> 頁尾
      </div>
    </div>
    <div class="card">
      <div class="card-tag" style="background: #cffafe; color: #0e7490;">跨頁導航</div>
      <div class="card-title" style="font-size: 15px;">相對路徑與高亮</div>
      <div class="card-desc" style="font-size: 13px;">
        <code>href="about.html"</code><br>
        <code>href="menu.html"</code><br>
        拒絕開頭斜線 <code>/</code><br>
        當前頁加 <code>.active</code>
      </div>
    </div>
    <div class="card primary">
      <div class="card-tag" style="background: #dbeafe; color: #1e40af;">style.css 核心</div>
      <div class="card-title" style="font-size: 15px;">:root 色票變數</div>
      <div class="card-desc" style="font-size: 13px;">
        <code>--bg: #FAF8F5;</code><br>
        <code>--primary: #3E2723;</code><br>
        改一處變數，<br>
        4 個分頁同步換色！
      </div>
    </div>
    <div class="card">
      <div class="card-tag" style="background: #cffafe; color: #0e7490;">響應式排版</div>
      <div class="card-title" style="font-size: 15px;">Flex / Grid RWD</div>
      <div class="card-desc" style="font-size: 13px;">
        <code>display: flex;</code><br>
        <code>display: grid;</code><br>
        <code>@media (max-width: 768px)</code><br>
        手機自動轉單欄
      </div>
    </div>
    <div class="card highlight">
      <div class="card-tag" style="background: #dcfce7; color: #15803d;">script.js 大腦</div>
      <div class="card-title" style="font-size: 15px;">原生 DOM 互動</div>
      <div class="card-desc" style="font-size: 13px;">
        <code>querySelector()</code><br>
        <code>addEventListener()</code><br>
        <code>classList.toggle()</code><br>
        輕量驅動動態體驗
      </div>
    </div>
  </div>
</div>
</body></html>"""

# 4. New diagram_13_js_menu.png
diagrams["diagram_13_js_menu.png"] = f"""<!DOCTYPE html><html><head><meta charset="utf-8"><style>{BASE_CSS}
  .menu-grid {{
    display: grid;
    grid-template-columns: repeat(5, 1fr);
    gap: 12px;
  }}
</style></head><body>
<div class="container" style="width: 1060px;">
  <div class="header">
    <div class="header-icon" style="background: linear-gradient(135deg, #f59e0b, #d97706);">⚡</div>
    <div>
      <div class="header-title">原生 JavaScript 微互動點餐單（免框架賦能 5 選 1～2）</div>
      <div class="header-subtitle">不必引入複雜 Vue / React，用幾十行純 DOM 語法就能打造媲美商業官網的靈動體驗</div>
    </div>
  </div>
  <div class="menu-grid">
    <div class="card primary">
      <div class="card-tag" style="background: #dbeafe; color: #1e40af;">必備保底 ★</div>
      <div class="card-title" style="font-size: 15px;">📱 漢堡選單開合</div>
      <div class="card-desc" style="font-size: 13px;">
        手機版點擊 <code>☰</code> 圖示時，透過 <code>classList.toggle</code> 平滑展開或收合導覽列。
      </div>
    </div>
    <div class="card">
      <div class="card-tag" style="background: #fef3c7; color: #b45309;">推薦選配 A</div>
      <div class="card-title" style="font-size: 15px;">💬 FAQ 摺疊手風琴</div>
      <div class="card-desc" style="font-size: 13px;">
        適合服務／入社頁：點擊常見問題標題才動態展開解答，保持版面清爽俐落。
      </div>
    </div>
    <div class="card">
      <div class="card-tag" style="background: #fef3c7; color: #b45309;">推薦選配 B</div>
      <div class="card-title" style="font-size: 15px;">☕ 分類即時篩選器</div>
      <div class="card-desc" style="font-size: 13px;">
        適合菜單／作品頁：點擊「手沖／義式／甜點」標籤，免換頁即時篩選顯示對應卡片。
      </div>
    </div>
    <div class="card">
      <div class="card-tag" style="background: #fef3c7; color: #b45309;">推薦選配 C</div>
      <div class="card-title" style="font-size: 15px;">🌙 日夜間氛圍切換</div>
      <div class="card-desc" style="font-size: 13px;">
        點擊切換深淺色主題變數，搭配 <code>localStorage</code> 跨頁記住訪客的閱讀偏好。
      </div>
    </div>
    <div class="card highlight">
      <div class="card-tag" style="background: #dcfce7; color: #15803d;">推薦選配 D</div>
      <div class="card-title" style="font-size: 15px;">✉️ 表單驗證與回饋</div>
      <div class="card-desc" style="font-size: 13px;">
        適合聯絡預約頁：檢查必填欄位並攔截預設重整，彈出溫暖的預約成功確認訊息。
      </div>
    </div>
  </div>
</div>
</body></html>"""

for filename, html_content in diagrams.items():
    temp_html = os.path.abspath(f"scratch/temp_{filename}.html")
    out_png = os.path.join(output_dir, filename)
    with open(temp_html, "w", encoding="utf-8") as f:
        f.write(html_content)

    file_url = "file:///" + temp_html.replace("\\", "/")
    cmd = [
        edge_path,
        "--headless=new",
        "--disable-gpu",
        "--hide-scrollbars",
        "--force-device-scale-factor=2",
        f"--user-data-dir={user_data_dir}",
        f"--screenshot={out_png}",
        "--window-size=1250,700",
        file_url,
    ]
    subprocess.run(cmd, check=True)

    im = Image.open(out_png)
    bg = Image.new(im.mode, im.size, im.getpixel((0, 0)))
    diff = ImageChops.difference(im, bg)
    bbox = diff.getbbox()
    if bbox:
        pad = 20
        w, h = im.size
        crop_box = (
            max(0, bbox[0] - pad),
            max(0, bbox[1] - pad),
            min(w, bbox[2] + pad),
            min(h, bbox[3] + pad),
        )
        im_cropped = im.crop(crop_box)
        im_cropped.save(out_png)

    print(f"Rendered: {filename} -> Dimensions: {Image.open(out_png).size}")
