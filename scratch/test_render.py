import os
import subprocess
from PIL import Image

test_html = """<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<style>
  body {
    margin: 0;
    padding: 30px;
    background: transparent;
    font-family: 'Microsoft JhengHei', 'PingFang TC', sans-serif;
    display: inline-block;
  }
  .card {
    background: white;
    padding: 24px 36px;
    border-radius: 16px;
    box-shadow: 0 8px 30px rgba(0,0,0,0.08);
    border: 1px solid #e2e8f0;
    display: flex;
    gap: 20px;
    align-items: center;
  }
  .badge {
    background: linear-gradient(135deg, #3b82f6, #1d4ed8);
    color: white;
    padding: 10px 20px;
    border-radius: 10px;
    font-weight: bold;
    font-size: 20px;
    box-shadow: 0 4px 12px rgba(59,130,246,0.3);
  }
  .title {
    font-size: 22px;
    color: #1e293b;
    font-weight: bold;
  }
</style>
</head>
<body>
  <div class="card">
    <div class="badge">測試節點</div>
    <div class="title">Headless Edge 渲染高畫質圖表測試成功！</div>
  </div>
</body>
</html>"""

html_path = os.path.abspath("test_render.html")
png_path = os.path.abspath("test_render.png")

with open(html_path, "w", encoding="utf-8") as f:
    f.write(test_html)

edge_path = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
cmd = [
    edge_path,
    "--headless",
    "--disable-gpu",
    "--hide-scrollbars",
    "--force-device-scale-factor=2",
    f"--screenshot={png_path}",
    "--window-size=1200,400",
    html_path
]
subprocess.run(cmd, check=True)

# Auto-crop with PIL
im = Image.open(png_path)
bg = Image.new(im.mode, im.size, im.getpixel((0, 0)))
diff = ImageChops.difference(im, bg) if 'ImageChops' in globals() else None
print("Rendered PNG size:", os.path.getsize(png_path), "Image dimensions:", im.size)
