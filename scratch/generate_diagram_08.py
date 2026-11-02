import os
import subprocess
from PIL import Image, ImageChops

output_dir = os.path.abspath("img")
os.makedirs(output_dir, exist_ok=True)
user_data_dir = os.path.abspath("scratch/edge_diagram_profile")
os.makedirs(user_data_dir, exist_ok=True)
edge_path = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"

filename = "diagram_08_github_update_flow.png"

html_content = """<!DOCTYPE html>
<html lang="zh-Hant">
<head>
<meta charset="utf-8">
<style>
  * { box-sizing: border-box; }
  html, body {
    margin: 0;
    padding: 0;
    background: #ffffff;
  }
  body {
    padding: 28px;
    font-family: "Microsoft JhengHei", "PingFang TC", -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
    display: inline-block;
  }
  .container {
    width: 940px;
    background: #ffffff;
    border-radius: 20px;
    padding: 28px 36px 30px;
    box-shadow: 0 10px 36px rgba(15, 23, 42, 0.08), 0 1px 3px rgba(15, 23, 42, 0.05);
    border: 1.5px solid #e2e8f0;
    display: flex;
    flex-direction: column;
    gap: 18px;
  }
  .header {
    display: flex;
    align-items: center;
    gap: 16px;
    border-bottom: 2px solid #f1f5f9;
    padding-bottom: 16px;
  }
  .header-icon {
    width: 46px;
    height: 46px;
    border-radius: 13px;
    background: linear-gradient(135deg, #2563eb, #4f46e5);
    display: flex;
    align-items: center;
    justify-content: center;
    color: #ffffff;
    flex-shrink: 0;
    box-shadow: 0 4px 12px rgba(37, 99, 235, 0.25);
  }
  .header-title {
    font-size: 22px;
    font-weight: 800;
    color: #0f172a;
    letter-spacing: -0.01em;
  }
  .header-subtitle {
    font-size: 14.5px;
    color: #64748b;
    margin-top: 3px;
    font-weight: 500;
  }
  .steps-list {
    display: flex;
    flex-direction: column;
    align-items: stretch;
    gap: 0;
  }
  .step-card {
    display: flex;
    align-items: center;
    gap: 18px;
    padding: 15px 20px;
    border-radius: 14px;
    border: 1.5px solid #e2e8f0;
    background: #f8fafc;
  }
  .step-card.s1 {
    background: #f8fafc;
    border-color: #cbd5e1;
  }
  .step-card.s2 {
    background: #eff6ff;
    border-color: #93c5fd;
  }
  .step-card.s3 {
    background: #faf5ff;
    border-color: #d8b4fe;
  }
  .step-card.s4 {
    background: #eef2ff;
    border-color: #a5b4fc;
  }
  .step-card.s5 {
    background: #f0fdf4;
    border-color: #86efac;
    box-shadow: 0 4px 16px rgba(34, 197, 94, 0.10);
  }
  .step-badge {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    min-width: 78px;
    padding: 8px 12px;
    border-radius: 11px;
    font-weight: 800;
    font-size: 14px;
    letter-spacing: 0.03em;
    flex-shrink: 0;
  }
  .s1 .step-badge { background: #e2e8f0; color: #334155; }
  .s2 .step-badge { background: #dbeafe; color: #1d4ed8; }
  .s3 .step-badge { background: #f3e8ff; color: #7e22ce; }
  .s4 .step-badge { background: #e0e7ff; color: #4338ca; }
  .s5 .step-badge { background: #dcfce7; color: #15803d; }

  .step-content {
    flex: 1;
    display: flex;
    flex-direction: column;
    gap: 4px;
  }
  .step-title {
    font-size: 18px;
    font-weight: 800;
    color: #0f172a;
    line-height: 1.3;
  }
  .step-desc {
    font-size: 15px;
    color: #334155;
    line-height: 1.5;
  }
  code {
    font-family: Consolas, "Courier New", monospace;
    font-size: 14px;
    font-weight: 700;
    background: rgba(15, 23, 42, 0.07);
    color: #0f172a;
    padding: 2px 7px;
    border-radius: 6px;
  }
  .btn-pill {
    display: inline-block;
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", "Microsoft JhengHei", sans-serif;
    font-size: 13.5px;
    font-weight: 700;
    padding: 2px 9px;
    border-radius: 6px;
    background: #1d4ed8;
    color: #ffffff;
  }
  .btn-pill.purple {
    background: #7e22ce;
  }
  .btn-pill.indigo {
    background: #4338ca;
  }
  .stage-tag {
    font-size: 12.5px;
    font-weight: 700;
    padding: 5px 12px;
    border-radius: 9999px;
    white-space: nowrap;
    flex-shrink: 0;
  }
  .s1 .stage-tag { background: #ffffff; color: #475569; border: 1px solid #cbd5e1; }
  .s2 .stage-tag { background: #ffffff; color: #1d4ed8; border: 1px solid #bfdbfe; }
  .s3 .stage-tag { background: #ffffff; color: #7e22ce; border: 1px solid #e9d5ff; }
  .s4 .stage-tag { background: #ffffff; color: #4338ca; border: 1px solid #c7d2fe; }
  .s5 .stage-tag { background: #16a34a; color: #ffffff; border: 1px solid #16a34a; }

  .arrow-row {
    display: flex;
    justify-content: center;
    align-items: center;
    height: 22px;
    color: #94a3b8;
  }
</style>
</head>
<body>
<div class="container">
  <div class="header">
    <div class="header-icon">
      <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">
        <path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/>
        <polyline points="17 8 12 3 7 8"/>
        <line x1="12" y1="3" x2="12" y2="15"/>
      </svg>
    </div>
    <div>
      <div class="header-title">GitHub Pages 線上履歷日常更新維護標準流程</div>
      <div class="header-subtitle">本地編輯存檔 ➔ 檢視變更差異 ➔ 本地提交 (Commit) ➔ 雲端推送 (Push) ➔ 自動更新上線</div>
    </div>
  </div>

  <div class="steps-list">
    <div class="step-card s1">
      <div class="step-badge">步驟 1</div>
      <div class="step-content">
        <div class="step-title">本地修改檔案</div>
        <div class="step-desc">在 VS Code 中修改 <code>index.html</code> 內容，並按下快捷鍵 <code>Ctrl + S</code> 儲存檔案</div>
      </div>
      <div class="stage-tag">VS Code 編輯</div>
    </div>

    <div class="arrow-row">
      <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#64748b" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round">
        <line x1="12" y1="4" x2="12" y2="20"/><polyline points="18 14 12 20 6 14"/>
      </svg>
    </div>

    <div class="step-card s2">
      <div class="step-badge">步驟 2</div>
      <div class="step-content">
        <div class="step-title">開啟 GitHub Desktop</div>
        <div class="step-desc">軟體會自動偵測專案變更，並於畫面列出修改過的檔案清單與行數差異 (Diff)</div>
      </div>
      <div class="stage-tag">自動偵測差異</div>
    </div>

    <div class="arrow-row">
      <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#64748b" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round">
        <line x1="12" y1="4" x2="12" y2="20"/><polyline points="18 14 12 20 6 14"/>
      </svg>
    </div>

    <div class="step-card s3">
      <div class="step-badge">步驟 3</div>
      <div class="step-content">
        <div class="step-title">輸入 Summary 並 Commit</div>
        <div class="step-desc">於左下角填寫變更說明（如：完成經歷、技能與作品集內容），點擊 <span class="btn-pill purple">Commit to main</span></div>
      </div>
      <div class="stage-tag">建立本地存檔點</div>
    </div>

    <div class="arrow-row">
      <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#64748b" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round">
        <line x1="12" y1="4" x2="12" y2="20"/><polyline points="18 14 12 20 6 14"/>
      </svg>
    </div>

    <div class="step-card s4">
      <div class="step-badge">步驟 4</div>
      <div class="step-content">
        <div class="step-title">點擊 Push origin</div>
        <div class="step-desc">點擊上方選單列 <span class="btn-pill indigo">Push origin</span> 按鈕，將本地最新提交同步推送至 GitHub 雲端伺服器</div>
      </div>
      <div class="stage-tag">推送雲端伺服器</div>
    </div>

    <div class="arrow-row">
      <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#64748b" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round">
        <line x1="12" y1="4" x2="12" y2="20"/><polyline points="18 14 12 20 6 14"/>
      </svg>
    </div>

    <div class="step-card s5">
      <div class="step-badge">步驟 5</div>
      <div class="step-content">
        <div class="step-title">自動更新上線</div>
        <div class="step-desc">等待 1～3 分鐘編譯完成，重新整理線上網址 <code>https://your-username.github.io</code> 即可看到最新完整履歷！</div>
      </div>
      <div class="stage-tag">全球同步上線 ✓</div>
    </div>
  </div>
</div>
</body>
</html>
"""

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
    "--window-size=1200,900",
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

print(f"Rendered {out_png}: {os.path.getsize(out_png)} bytes, size={Image.open(out_png).size}")
