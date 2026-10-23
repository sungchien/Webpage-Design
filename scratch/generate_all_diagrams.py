import os
import subprocess
import time
from PIL import Image

output_dir = os.path.abspath("img")
os.makedirs(output_dir, exist_ok=True)
user_data_dir = os.path.abspath("scratch/edge_diagram_profile")
os.makedirs(user_data_dir, exist_ok=True)
edge_path = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"

diagrams = {}

# Common CSS Template
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
    transition: all 0.2s;
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
  .card-list {
    margin: 0;
    padding-left: 18px;
    font-size: 13.5px;
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
"""

# 1. vibe_dev_evolution
diagrams["diagram_11_evolution.png"] = f"""<!DOCTYPE html><html><head><meta charset="utf-8"><style>{BASE_CSS}</style></head><body>
<div class="container" style="width: 1020px;">
  <div class="header">
    <div class="header-icon" style="background: linear-gradient(135deg, #6366f1, #3b82f6);">🚀</div>
    <div>
      <div class="header-title">網頁開發模式演進：從純手刻到 Agentic Vibe Coding</div>
      <div class="header-subtitle">軟體工程三部曲：由「逐行碼農」進化為「AI 產品總監」</div>
    </div>
  </div>
  <div class="flow-row">
    <div class="card">
      <div class="card-tag" style="background: #e2e8f0; color: #475569;">2022 以前</div>
      <div class="card-title">傳統手刻開發時代</div>
      <div class="card-desc"><strong>80% 寫代碼 / 20% 規劃</strong></div>
      <ul class="card-list">
        <li>一磚一瓦純手寫 HTML / CSS</li>
        <li>手動調整響應式 RWD 與除錯</li>
        <li>容易陷入重複勞動與語法細節</li>
      </ul>
    </div>
    <div class="arrow">➔</div>
    <div class="card">
      <div class="card-tag" style="background: #e0e7ff; color: #4338ca;">2023 - 2024</div>
      <div class="card-title">對話式 AI 時代</div>
      <div class="card-desc"><strong>ChatGPT / Gemini 網頁聊天</strong></div>
      <ul class="card-list">
        <li>在聊天視窗複製貼上數百行代碼</li>
        <li>容易遭遇版本錯亂與標籤閉合失誤</li>
        <li>充斥失效的佔位假圖與假字</li>
      </ul>
    </div>
    <div class="arrow">➔</div>
    <div class="card highlight">
      <div class="card-tag" style="background: #dcfce7; color: #15803d;">2025+ 現今</div>
      <div class="card-title">Agentic Vibe Coding</div>
      <div class="card-desc"><strong>60% 規劃 / 10% 指揮 / 30% 品管</strong></div>
      <ul class="card-list">
        <li>以 <strong>PRD.md</strong> 為唯一真相藍圖</li>
        <li>Antigravity 2.0 直接讀寫本地工作區</li>
        <li>內建 <code>generate_image</code> 產出專屬素材</li>
        <li>審查 Visual Diff 掌控每一行代碼</li>
      </ul>
    </div>
  </div>
</div>
</body></html>"""

# 2. vibe_5week_timeline
diagrams["diagram_11_timeline.png"] = f"""<!DOCTYPE html><html><head><meta charset="utf-8"><style>{BASE_CSS}
  .timeline-grid {{
    display: grid;
    grid-template-columns: repeat(5, 1fr);
    gap: 14px;
  }}
  .timeline-card {{
    background: #f8fafc;
    border: 1px solid #e2e8f0;
    border-radius: 16px;
    padding: 18px 16px;
    display: flex;
    flex-direction: column;
    gap: 8px;
    position: relative;
  }}
  .timeline-week {{
    font-size: 12px;
    font-weight: 800;
    color: white;
    padding: 4px 10px;
    border-radius: 9999px;
    width: fit-content;
  }}
</style></head><body>
<div class="container" style="width: 1060px;">
  <div class="header">
    <div class="header-icon" style="background: linear-gradient(135deg, #0ea5e9, #2563eb);">📅</div>
    <div>
      <div class="header-title">實作專案四：Agentic Vibe Coding 五週里程碑 (每週 80 分鐘)</div>
      <div class="header-subtitle">第 11 至 15 週循序漸進的現代化開發工作流程</div>
    </div>
  </div>
  <div class="timeline-grid">
    <div class="timeline-card" style="border-top: 4px solid #3b82f6;">
      <div class="timeline-week" style="background: #3b82f6;">第 11 週</div>
      <div class="card-title" style="font-size: 15px;">工具與環境上手</div>
      <div class="card-desc" style="font-size: 13px;">
        • Vibe Coding 觀念重塑<br>
        • GitHub Desktop 建倉庫<br>
        • Antigravity 掛載工作區<br>
        • 零複製貼上破冰實作
      </div>
    </div>
    <div class="timeline-card" style="border-top: 4px solid #8b5cf6;">
      <div class="timeline-week" style="background: #8b5cf6;">第 12 週</div>
      <div class="card-title" style="font-size: 15px;">Phase 1 企劃藍圖</div>
      <div class="card-desc" style="font-size: 13px;">
        • <code>/grill-me</code> 需求訪談<br>
        • 手繪草圖/網址多模態輸入<br>
        • 輸出本機 <code>PRD.md</code><br>
        • 同儕互評與架構工件
      </div>
    </div>
    <div class="timeline-card" style="border-top: 4px solid #ec4899;">
      <div class="timeline-week" style="background: #ec4899;">第 13 週</div>
      <div class="card-title" style="font-size: 15px;">Phase 2 生成與素材</div>
      <div class="card-desc" style="font-size: 13px;">
        • Proceed 批准動工<br>
        • Tailwind CSS CDN 佈局<br>
        • <code>generate_image</code> 畫真實圖<br>
        • 導讀 Visual Diff 審查
      </div>
    </div>
    <div class="timeline-card" style="border-top: 4px solid #f59e0b;">
      <div class="timeline-week" style="background: #f59e0b;">第 14 週</div>
      <div class="card-title" style="font-size: 15px;">Phase 3 品管與微調</div>
      <div class="card-desc" style="font-size: 13px;">
        • 檢閱 walkthrough 工件<br>
        • 啟動本機伺服器預覽<br>
        • 手機端 RWD 破版排查<br>
        • Vibe QA 自然語言微調
      </div>
    </div>
    <div class="timeline-card" style="border-top: 4px solid #10b981;">
      <div class="timeline-week" style="background: #10b981;">第 15 週</div>
      <div class="card-title" style="font-size: 15px;">發布與作品展評</div>
      <div class="card-desc" style="font-size: 13px;">
        • GitHub Pages 發布上線<br>
        • 雙向串聯個人履歷<br>
        • 線上 Showcase 互評<br>
        • 提煉產品總監思維
      </div>
    </div>
  </div>
</div>
</body></html>"""

# 3. github_desktop_antigravity_flow
diagrams["diagram_11_setup.png"] = f"""<!DOCTYPE html><html><head><meta charset="utf-8"><style>{BASE_CSS}</style></head><body>
<div class="container" style="width: 1020px;">
  <div class="header">
    <div class="header-icon" style="background: linear-gradient(135deg, #64748b, #1e293b);">🛠️</div>
    <div>
      <div class="header-title">核心工作流程基石：GitHub Desktop 專案初始化與 Antigravity 串聯</div>
      <div class="header-subtitle">雙重視覺安全網：AI 負責編程，GUI 負責審查與同步</div>
    </div>
  </div>
  <div class="flow-row">
    <div class="card primary">
      <div class="card-tag" style="background: #dbeafe; color: #1e40af;">步驟 1</div>
      <div class="card-title">GitHub Desktop 建立倉庫</div>
      <div class="card-desc">
        • 點擊 <code>File > New repository</code><br>
        • 取名例如 <code>coffee-shop</code><br>
        • 自動完成 <code>git init</code> 與目錄隔離
      </div>
    </div>
    <div class="arrow">➔</div>
    <div class="card purple">
      <div class="card-tag" style="background: #f3e8ff; color: #6b21a8;">步驟 2</div>
      <div class="card-title">Antigravity 2.0 掛載專案</div>
      <div class="card-desc">
        • 點擊 <code>Projects > Open Project</code><br>
        • 選擇剛建立的倉庫資料夾<br>
        • Agent 獲得全工作區檔案感知與讀寫權限
      </div>
    </div>
    <div class="arrow">➔</div>
    <div class="card highlight">
      <div class="card-tag" style="background: #dcfce7; color: #15803d;">步驟 3</div>
      <div class="card-title">雙螢幕即時同步工作流</div>
      <div class="card-desc">
        • <strong>Antigravity</strong>：自動建立與修訂代碼<br>
        • <strong>GitHub Desktop</strong>：Changes 列表即時亮起綠色變更！
      </div>
    </div>
  </div>
</div>
</body></html>"""

# 4. antigravity_github_levels
diagrams["diagram_11_git_levels.png"] = f"""<!DOCTYPE html><html><head><meta charset="utf-8"><style>{BASE_CSS}</style></head><body>
<div class="container" style="width: 1020px;">
  <div class="header">
    <div class="header-icon" style="background: linear-gradient(135deg, #10b981, #047857);">⚡</div>
    <div>
      <div class="header-title">Antigravity 操作 GitHub 的三種層次</div>
      <div class="header-subtitle">結合本地終端執行力與 MCP 雲端協調生態系</div>
    </div>
  </div>
  <div class="flow-row">
    <div class="card highlight">
      <div class="card-tag" style="background: #dcfce7; color: #15803d;">層次 1 ⭐ 最推薦</div>
      <div class="card-title">內建終端機標準 Git 指令</div>
      <div class="card-desc">
        <strong>免任何額外 Token 設定</strong><br>
        口語指令：「幫我 commit 並推送到 GitHub！」<br>
        自動執行：<code>git add .</code> ➔ <code>git commit</code> ➔ <code>git push</code>
      </div>
    </div>
    <div class="card primary">
      <div class="card-tag" style="background: #dbeafe; color: #1e40af;">層次 2</div>
      <div class="card-title">GitHub CLI (gh 命令列工具)</div>
      <div class="card-desc">
        <strong>命令列進階管理</strong><br>
        終端直接執行：<br>
        • <code>gh repo create</code> 建立遠端倉庫<br>
        • <code>gh pr create</code> 發布 Pull Request
      </div>
    </div>
    <div class="card purple">
      <div class="card-tag" style="background: #f3e8ff; color: #6b21a8;">層次 3</div>
      <div class="card-title">官方 GitHub MCP Server</div>
      <div class="card-desc">
        <strong>@modelcontextprotocol/server-github</strong><br>
        走 GitHub REST/GraphQL API：<br>
        • Agent 直接建立倉庫與讀寫檔案<br>
        • 免開瀏覽器管理 Issue 與分支
      </div>
    </div>
  </div>
</div>
</body></html>"""

# 5. vibe_mindset_shift
diagrams["diagram_12_mindset.png"] = f"""<!DOCTYPE html><html><head><meta charset="utf-8"><style>{BASE_CSS}</style></head><body>
<div class="container" style="width: 980px;">
  <div class="header">
    <div class="header-icon" style="background: linear-gradient(135deg, #f59e0b, #d97706);">💡</div>
    <div>
      <div class="header-title">企劃思維模式轉變：從隨便提問到藍圖建構</div>
      <div class="header-subtitle">成為專案的產品經理 (Product Manager)，掌控 Single Source of Truth</div>
    </div>
  </div>
  <div class="flow-row">
    <div class="card" style="background: #fef2f2; border-color: #fca5a5;">
      <div class="card-tag" style="background: #fee2e2; color: #b91c1c;">❌ 傳統迷思 (Garbage In)</div>
      <div class="card-title">直接叫 AI 寫代碼</div>
      <div class="card-desc">
        「幫我做一個很潮的咖啡廳網站。」<br>
        <strong>後果：</strong><br>
        • AI 只能憑空瞎猜通靈<br>
        • 產出毫無靈魂的千篇一律公版<br>
        • 充斥假字假圖與錯誤邏輯
      </div>
    </div>
    <div class="arrow">VS</div>
    <div class="card highlight">
      <div class="card-tag" style="background: #dcfce7; color: #15803d;">✅ 專業做法 (Single Source of Truth)</div>
      <div class="card-title">先完成 PRD.md 需求藍圖</div>
      <div class="card-desc">
        「確立目標、受眾、侘寂風格色調、三欄菜單與地圖。」<br>
        <strong>成果：</strong><br>
        • 建立專案唯一真相來源<br>
        • AI 分毫不差地精確執行實作<br>
        • 產出具備商業質感的量身作品
      </div>
    </div>
  </div>
</div>
</body></html>"""

# 6. prd_5_components
diagrams["diagram_12_prd_components.png"] = f"""<!DOCTYPE html><html><head><meta charset="utf-8"><style>{BASE_CSS}
  .comp-grid {{
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 16px;
  }}
</style></head><body>
<div class="container" style="width: 1040px;">
  <div class="header">
    <div class="header-icon" style="background: linear-gradient(135deg, #8b5cf6, #6366f1);">📋</div>
    <div>
      <div class="header-title">PRD (產品需求文件) 五大核心要件</div>
      <div class="header-subtitle">指揮 AI 代理人實作的最關鍵藍圖架構</div>
    </div>
  </div>
  <div class="comp-grid">
    <div class="card">
      <div class="card-tag" style="background: #e0e7ff; color: #3730a3;">1. 網站目標 Goal</div>
      <div class="card-title">為誰解決什麼問題</div>
      <div class="card-desc">說明官網設立目的，例如讓客人線上看菜單、了解自烘豆理念與來店路線 (CTA)。</div>
    </div>
    <div class="card">
      <div class="card-tag" style="background: #e0e7ff; color: #3730a3;">2. 目標受眾 Audience</div>
      <div class="card-title">網站是做給誰看的</div>
      <div class="card-desc">界定核心讀者（如：用筆電的上班族、大學生）與次要讀者（社區鄰居）。</div>
    </div>
    <div class="card">
      <div class="card-tag" style="background: #e0e7ff; color: #3730a3;">3. 視覺調性 Vibe</div>
      <div class="card-title">Vibe Coding 的靈魂</div>
      <div class="card-desc">日系侘寂風、黑金專業商務風、暗黑霓虹；定義色彩 HEX 代碼與字體風格。</div>
    </div>
    <div class="card">
      <div class="card-tag" style="background: #e0e7ff; color: #3730a3;">4. 功能區塊 Features</div>
      <div class="card-title">單頁式由上至下佈局</div>
      <div class="card-desc">Navbar 導覽列 ➔ Hero 主視覺 ➔ About Us ➔ Menu 菜單 ➔ Contact & Map ➔ Footer。</div>
    </div>
    <div class="card">
      <div class="card-tag" style="background: #e0e7ff; color: #3730a3;">5. 技術要求 Tech Specs</div>
      <div class="card-title">前端工程規範</div>
      <div class="card-desc">單頁式 (SPA)、Tailwind CSS CDN、Mobile-First 響應式 (RWD)、HTML5 語意標籤。</div>
    </div>
    <div class="card highlight">
      <div class="card-tag" style="background: #dcfce7; color: #15803d;">同儕互評審查</div>
      <div class="card-title">消除模糊盲點</div>
      <div class="card-desc">經同桌同學挑出 3 個抽象形容詞並修訂後，才算真正合格的 AI 提示藍圖！</div>
    </div>
  </div>
</div>
</body></html>"""

# 7. grill_me_workflow
diagrams["diagram_12_grillme.png"] = f"""<!DOCTYPE html><html><head><meta charset="utf-8"><style>{BASE_CSS}</style></head><body>
<div class="container" style="width: 1000px;">
  <div class="header">
    <div class="header-icon" style="background: linear-gradient(135deg, #ec4899, #be185d);">🎤</div>
    <div>
      <div class="header-title">`/grill-me` 蘇格拉底式需求訪談循序流程</div>
      <div class="header-subtitle">化被動為主動：AI 擔任嚴格產品總監，為你補齊設計盲點</div>
    </div>
  </div>
  <div class="flow-row">
    <div class="card primary">
      <div class="card-tag" style="background: #dbeafe; color: #1e40af;">步驟 1：啟動訪談</div>
      <div class="card-title">學生下達指令</div>
      <div class="card-desc">
        輸入 <code>/grill-me</code><br>
        「我想做老王咖啡形象官網，請透過深度提問幫我理清思路並產出 PRD。」
      </div>
    </div>
    <div class="arrow">➔</div>
    <div class="card purple">
      <div class="card-tag" style="background: #f3e8ff; color: #6b21a8;">步驟 2：深度發問</div>
      <div class="card-title">AI 連續追問痛點</div>
      <div class="card-desc">
        • TA 是上班族還是學生？<br>
        • 最自豪的招牌是什麼？<br>
        • 想要哪 3 種主要色調？<br>
        • 顧客最關鍵的 CTA 是什麼？
      </div>
    </div>
    <div class="arrow">➔</div>
    <div class="card highlight">
      <div class="card-tag" style="background: #dcfce7; color: #15803d;">步驟 3：一鍵固化</div>
      <div class="card-title">寫入 PRD.md 檔案</div>
      <div class="card-desc">
        「請根據訪談紀錄整理成標準 PRD 並建立檔案！」<br>
        Agent 直接呼叫工具，在專案根目錄產生 <code>PRD.md</code>！
      </div>
    </div>
  </div>
</div>
</body></html>"""

# 8. vibe_generation_flow
diagrams["diagram_13_generation_flow.png"] = f"""<!DOCTYPE html><html><head><meta charset="utf-8"><style>{BASE_CSS}</style></head><body>
<div class="container" style="width: 1020px;">
  <div class="header">
    <div class="header-icon" style="background: linear-gradient(135deg, #3b82f6, #1d4ed8);">⚙️</div>
    <div>
      <div class="header-title">Phase 2 生成核心工作流：從藍圖到實體代碼</div>
      <div class="header-subtitle">一鍵批准計畫動工，零複製貼上的代理人自動化工程</div>
    </div>
  </div>
  <div class="flow-row">
    <div class="card">
      <div class="card-tag" style="background: #e2e8f0; color: #475569;">步驟 1</div>
      <div class="card-title">審核實作計畫</div>
      <div class="card-desc">在 Artifact 窗格核對 <code>implementation_plan.md</code> 的色票與 Mermaid 區塊圖。</div>
    </div>
    <div class="arrow">➔</div>
    <div class="card primary">
      <div class="card-tag" style="background: #dbeafe; color: #1e40af;">步驟 2</div>
      <div class="card-title">點擊 Proceed 動工</div>
      <div class="card-desc">Antigravity 自動建立 <code>index.html</code>、<code>mystyles.css</code> 與 <code>img/</code> 資料夾。</div>
    </div>
    <div class="arrow">➔</div>
    <div class="card purple">
      <div class="card-tag" style="background: #f3e8ff; color: #6b21a8;">步驟 3</div>
      <div class="card-title">AI 繪圖注入素材</div>
      <div class="card-desc">調用 <code>generate_image</code> 生成 Hero Banner 與商品卡片圖，取代佔位假圖。</div>
    </div>
    <div class="arrow">➔</div>
    <div class="card highlight">
      <div class="card-tag" style="background: #dcfce7; color: #15803d;">步驟 4</div>
      <div class="card-title">審查 Visual Diff</div>
      <div class="card-desc">觀察綠色新增與語意標籤，切換至 GitHub Desktop 進行第一階段 Commit。</div>
    </div>
  </div>
</div>
</body></html>"""

# 9. tailwind_classes_overview
diagrams["diagram_13_tailwind_classes.png"] = f"""<!DOCTYPE html><html><head><meta charset="utf-8"><style>{BASE_CSS}
  .tailwind-grid {{
    display: grid;
    grid-template-columns: repeat(5, 1fr);
    gap: 12px;
  }}
</style></head><body>
<div class="container" style="width: 1050px;">
  <div class="header">
    <div class="header-icon" style="background: linear-gradient(135deg, #06b6d4, #0284c7);">🎨</div>
    <div>
      <div class="header-title">Tailwind CSS CDN 實用類別與語意標籤導讀</div>
      <div class="header-subtitle">現代前端 utility-first 快速佈局與響應式核心類別</div>
    </div>
  </div>
  <div class="tailwind-grid">
    <div class="card">
      <div class="card-tag" style="background: #cffafe; color: #0e7490;">排版佈局</div>
      <div class="card-title" style="font-size: 15px;">Flexbox</div>
      <div class="card-desc" style="font-size: 13px;">
        <code>flex</code><br>
        <code>justify-between</code><br>
        <code>items-center</code><br>
        <code>space-x-6</code>
      </div>
    </div>
    <div class="card">
      <div class="card-tag" style="background: #cffafe; color: #0e7490;">網格系統</div>
      <div class="card-title" style="font-size: 15px;">Grid & RWD</div>
      <div class="card-desc" style="font-size: 13px;">
        <code>grid</code><br>
        <code>grid-cols-1</code><br>
        <code>md:grid-cols-3</code><br>
        <code>gap-6</code>
      </div>
    </div>
    <div class="card">
      <div class="card-tag" style="background: #cffafe; color: #0e7490;">間距尺寸</div>
      <div class="card-title" style="font-size: 15px;">Spacing</div>
      <div class="card-desc" style="font-size: 13px;">
        <code>p-6</code> (內距)<br>
        <code>py-16</code> (垂直內距)<br>
        <code>mt-8</code> (上外距)<br>
        <code>max-w-6xl</code>
      </div>
    </div>
    <div class="card">
      <div class="card-tag" style="background: #cffafe; color: #0e7490;">外觀樣式</div>
      <div class="card-title" style="font-size: 15px;">Style</div>
      <div class="card-desc" style="font-size: 13px;">
        <code>bg-amber-50</code><br>
        <code>text-stone-800</code><br>
        <code>rounded-2xl</code><br>
        <code>shadow-md</code>
      </div>
    </div>
    <div class="card highlight">
      <div class="card-tag" style="background: #dcfce7; color: #15803d;">互動回饋</div>
      <div class="card-title" style="font-size: 15px;">Hover 動效</div>
      <div class="card-desc" style="font-size: 13px;">
        <code>hover:scale-105</code><br>
        <code>hover:shadow-xl</code><br>
        <code>transition-all</code><br>
        <code>duration-300</code>
      </div>
    </div>
  </div>
</div>
</body></html>"""

# 10. generate_image_flow
diagrams["diagram_13_image_gen_flow.png"] = f"""<!DOCTYPE html><html><head><meta charset="utf-8"><style>{BASE_CSS}</style></head><body>
<div class="container" style="width: 1020px;">
  <div class="header">
    <div class="header-icon" style="background: linear-gradient(135deg, #f43f5e, #be123c);">🖼️</div>
    <div>
      <div class="header-title">`generate_image` 圖片素材生成與自動關聯流程</div>
      <div class="header-subtitle">告別灰色 placeholder 假圖，為網站注入靈魂的商業質感</div>
    </div>
  </div>
  <div class="flow-row">
    <div class="card primary">
      <div class="card-tag" style="background: #dbeafe; color: #1e40af;">要素 1：畫面描述</div>
      <div class="card-title">精確 Prompt 提示詞</div>
      <div class="card-desc">
        主體 + 光影 + 風格調性<br>
        例：日系手沖咖啡吧台、晨光散景、黃銅手沖壺、深烘焙咖啡豆。
      </div>
    </div>
    <div class="arrow">➔</div>
    <div class="card amber">
      <div class="card-tag" style="background: #fef3c7; color: #b45309;">要素 2：比例與路徑</div>
      <div class="card-title">指定尺寸與儲存</div>
      <div class="card-desc">
        • Banner 設 <code>16:9</code><br>
        • 卡片/頭像設 <code>1:1</code><br>
        • 自動儲存為 <code>img/hero.jpg</code>
      </div>
    </div>
    <div class="arrow">➔</div>
    <div class="card highlight">
      <div class="card-tag" style="background: #dcfce7; color: #15803d;">要素 3：自動關聯</div>
      <div class="card-title">寫入 index.html</div>
      <div class="card-desc">
        Antigravity 自動檢查 HTML，將 <code>&lt;img src="img/hero.jpg"&gt;</code> 替換到位！
      </div>
    </div>
  </div>
</div>
</body></html>"""

# 11. vibe_refinement_flow
diagrams["diagram_14_refinement_flow.png"] = f"""<!DOCTYPE html><html><head><meta charset="utf-8"><style>{BASE_CSS}</style></head><body>
<div class="container" style="width: 1020px;">
  <div class="header">
    <div class="header-icon" style="background: linear-gradient(135deg, #10b981, #059669);">🏆</div>
    <div>
      <div class="header-title">Phase 3 完善與發布兩階段路徑</div>
      <div class="header-subtitle">從 70 分工程師原型，打磨到 100 分商業交付官網</div>
    </div>
  </div>
  <div class="flow-row">
    <div class="card">
      <div class="card-tag" style="background: #e2e8f0; color: #475569;">起點</div>
      <div class="card-title">70 分 AI 初版原型</div>
      <div class="card-desc">
        • 版型骨架完整<br>
        • 手機端排版可能擠壓<br>
        • 仍有部分假字與細節生硬
      </div>
    </div>
    <div class="arrow">➔</div>
    <div class="card primary">
      <div class="card-tag" style="background: #dbeafe; color: #1e40af;">第 14 週品管微調</div>
      <div class="card-title">成為 AI 品管師 (QA)</div>
      <div class="card-desc">
        • 終端啟動本機預覽伺服器<br>
        • F12 跨裝置手機 RWD 排查<br>
        • 思源宋體導入與行高微調<br>
        • 消除所有假字，換上真文案
      </div>
    </div>
    <div class="arrow">➔</div>
    <div class="card highlight">
      <div class="card-tag" style="background: #dcfce7; color: #15803d;">第 15 週發布展評</div>
      <div class="card-title">正式發布全世界</div>
      <div class="card-desc">
        • GitHub Pages 部署上線<br>
        • 雙向串聯個人作品集<br>
        • 線上 Showcase 互評發表<br>
        • 100 分個人數位代表作
      </div>
    </div>
  </div>
</div>
</body></html>"""

# 12. github_pages_deployment
diagrams["diagram_14_deployment_flow.png"] = f"""<!DOCTYPE html><html><head><meta charset="utf-8"><style>{BASE_CSS}</style></head><body>
<div class="container" style="width: 1020px;">
  <div class="header">
    <div class="header-icon" style="background: linear-gradient(135deg, #2563eb, #1d4ed8);">🌐</div>
    <div>
      <div class="header-title">GitHub Pages 部署操作 3 步驟</div>
      <div class="header-subtitle">將本機專案上傳至雲端，免費取得個人專屬公開網址</div>
    </div>
  </div>
  <div class="flow-row">
    <div class="card primary">
      <div class="card-tag" style="background: #dbeafe; color: #1e40af;">步驟 1</div>
      <div class="card-title">Commit & Publish</div>
      <div class="card-desc">
        • GitHub Desktop 點擊 <strong>Commit to main</strong><br>
        • 點擊 <strong>Publish repository</strong><br>
        • <strong>!! 重要 !! 取消勾選 Keep this code private</strong>
      </div>
    </div>
    <div class="arrow">➔</div>
    <div class="card purple">
      <div class="card-tag" style="background: #f3e8ff; color: #6b21a8;">步驟 2</div>
      <div class="card-title">開啟 Pages 功能</div>
      <div class="card-desc">
        • 前往 GitHub 倉庫 <code>Settings > Pages</code><br>
        • Source 選擇 <strong>Deploy from a branch</strong><br>
        • Branch 選擇 <strong>main</strong>，資料夾選 <strong>/(root)</strong> 儲存
      </div>
    </div>
    <div class="arrow">➔</div>
    <div class="card highlight">
      <div class="card-tag" style="background: #dcfce7; color: #15803d;">步驟 3</div>
      <div class="card-title">取得專屬網址</div>
      <div class="card-desc">
        等待 1~3 分鐘即時發布完成！<br>
        網址格式：<br>
        <code>https://帳號.github.io/專案名稱/</code>
      </div>
    </div>
  </div>
</div>
</body></html>"""

# 13. portfolio_interlinking
diagrams["diagram_14_portfolio_interlinking.png"] = f"""<!DOCTYPE html><html><head><meta charset="utf-8"><style>{BASE_CSS}</style></head><body>
<div class="container" style="width: 980px;">
  <div class="header">
    <div class="header-icon" style="background: linear-gradient(135deg, #8b5cf6, #7c3aed);">🔗</div>
    <div>
      <div class="header-title">雙向作品集生態系串聯 (Portfolio Interlinking)</div>
      <div class="header-subtitle">建立多專案互聯網絡，展現全方位數位創作能力</div>
    </div>
  </div>
  <div class="flow-row">
    <div class="card primary">
      <div class="card-tag" style="background: #dbeafe; color: #1e40af;">網站 A：個人履歷首頁</div>
      <div class="card-title"><code>your-username.github.io</code></div>
      <div class="card-desc">
        <strong>任務一：加入專案卡片</strong><br>
        在履歷的「作品集區塊」中，新增前往新官網的精美卡片連結：<br>
        <code>👉 前往瀏覽老王咖啡官網</code>
      </div>
    </div>
    <div class="arrow" style="font-size: 32px;">⇄</div>
    <div class="card highlight">
      <div class="card-tag" style="background: #dcfce7; color: #15803d;">網站 B：新 AI 形象專案</div>
      <div class="card-title"><code>.../my-vibe-cafe/</code></div>
      <div class="card-desc">
        <strong>任務二：頁尾連回履歷</strong><br>
        在官網頁尾 <code>&lt;footer&gt;</code> 加上作者品牌署名：<br>
        <code>Designed by &lt;a href="履歷網址"&gt;你的名字&lt;/a&gt;</code>
      </div>
    </div>
  </div>
</div>
</body></html>"""

print(f"Total diagrams to render: {len(diagrams)}")

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
        "--window-size=1200,600",
        file_url
    ]
    subprocess.run(cmd, check=True)
    
    # Auto-crop with PIL
    im = Image.open(out_png)
    # Convert white background to transparent or crop
    bg = Image.new(im.mode, im.size, im.getpixel((0, 0)))
    from PIL import ImageChops
    diff = ImageChops.difference(im, bg)
    bbox = diff.getbbox()
    if bbox:
        # Add a comfortable 15px padding
        pad = 20
        w, h = im.size
        crop_box = (max(0, bbox[0]-pad), max(0, bbox[1]-pad), min(w, bbox[2]+pad), min(h, bbox[3]+pad))
        im_cropped = im.crop(crop_box)
        im_cropped.save(out_png)
    
    print(f"Rendered: {filename} -> Size: {os.path.getsize(out_png)} bytes, Dimensions: {Image.open(out_png).size}")

print("All diagrams generated successfully!")
