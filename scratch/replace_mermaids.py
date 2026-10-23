import re

files_and_replacements = {
    "11_網頁的Vibe Coding_觀念與工具篇_講義.md": [
        ("![網頁開發模式演進：從純手刻到 Agentic Vibe Coding](img/diagram_11_evolution.png)", 0),
        ("![實作專案四：Agentic Vibe Coding 五週里程碑 (每週 80 分鐘)](img/diagram_11_timeline.png)", 1),
        ("![核心工作流程基石：GitHub Desktop 專案初始化與 Antigravity 串聯](img/diagram_11_setup.png)", 2),
        ("![Antigravity 操作 GitHub 的三種層次](img/diagram_11_git_levels.png)", 3),
    ],
    "11_網頁的Vibe Coding_講義.md": [
        ("![網頁開發模式演進：從純手刻到 Agentic Vibe Coding](img/diagram_11_evolution.png)", 0),
        ("![實作專案四：Agentic Vibe Coding 五週里程碑 (每週 80 分鐘)](img/diagram_11_timeline.png)", 1),
        ("![核心工作流程基石：GitHub Desktop 專案初始化與 Antigravity 串聯](img/diagram_11_setup.png)", 2),
        ("![Antigravity 操作 GitHub 的三種層次](img/diagram_11_git_levels.png)", 3),
    ],
    "12_網頁的Vibe Coding_企劃篇_講義.md": [
        ("![企劃思維模式轉變：從隨便提問到藍圖建構](img/diagram_12_mindset.png)", 0),
        ("![PRD (產品需求文件) 五大核心要件](img/diagram_12_prd_components.png)", 1),
        ("![/grill-me 蘇格拉底式需求訪談循序流程](img/diagram_12_grillme.png)", 2),
    ],
    "13_網頁的Vibe Coding_生成篇_講義.md": [
        ("![Phase 2 生成核心工作流：從藍圖到實體代碼](img/diagram_13_generation_flow.png)", 0),
        ("![Tailwind CSS CDN 實用類別與語意標籤導讀](img/diagram_13_tailwind_classes.png)", 1),
        ("![generate_image 圖片素材生成與自動關聯流程](img/diagram_13_image_gen_flow.png)", 2),
    ],
    "14_網頁的Vibe Coding_完善與部署篇_講義.md": [
        ("![Phase 3 完善與發布兩階段路徑](img/diagram_14_refinement_flow.png)", 0),
        ("![GitHub Pages 部署操作 3 步驟](img/diagram_14_deployment_flow.png)", 1),
        ("![雙向作品集生態系串聯 (Portfolio Interlinking)](img/diagram_14_portfolio_interlinking.png)", 2),
    ]
}

pattern = re.compile(r'```mermaid.*?```', re.DOTALL)

for filename, replacements in files_and_replacements.items():
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    
    matches = list(pattern.finditer(content))
    print(f"File {filename}: found {len(matches)} mermaid block(s)")
    
    # Replace in reverse order so string indices remain valid
    for img_tag, idx in reversed(replacements):
        if idx < len(matches):
            m = matches[idx]
            content = content[:m.start()] + img_tag + content[m.end():]
        else:
            print(f"Warning: match index {idx} not found in {filename}")
            
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)
        
    print(f"Updated {filename} successfully! Mermaid remaining: {content.count('```mermaid')}")
