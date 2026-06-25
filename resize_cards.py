import os
import re

dir_path = r"C:\Users\ASUS\Documents\gthub\simatika-demo"
files = ["stasi_dashboard.html", "paroki_dashboard.html"]

for filename in files:
    filepath = os.path.join(dir_path, filename)
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Update .content-area
    # from:
    #     .content-area {
    #       padding: 2rem;
    #       max-width: 72rem; /* max-w-6xl */
    #       margin: 0 auto;
    #       width: 100%;
    #       box-sizing: border-box;
    #       flex: 1;
    #       display: flex;
    #       flex-direction: column;
    #       gap: 2rem;
    #     }
    # to:
    #     .content-area {
    #       padding: 1.5rem 2rem;
    #       width: 100%;
    #       box-sizing: border-box;
    #       flex: 1;
    #       display: flex;
    #       flex-direction: column;
    #       gap: 1.5rem;
    #     }
    
    old_content_area_regex = r"\.content-area\s*\{[^}]+\}"
    new_content_area = """.content-area {
      padding: 1.5rem 2rem;
      width: 100%;
      box-sizing: border-box;
      flex: 1;
      display: flex;
      flex-direction: column;
      gap: 1.5rem;
    }
    
    /* GRIDS */
    .grid-4 { display: grid; grid-template-columns: repeat(1, 1fr); gap: 1rem; margin-bottom: 1rem; }
    @media (min-width: 768px) {
      .grid-4 { grid-template-columns: repeat(2, 1fr); }
    }
    @media (min-width: 1024px) {
      .grid-4 { grid-template-columns: repeat(4, 1fr); }
    }"""
    
    content = re.sub(old_content_area_regex, new_content_area, content)

    # 2. Update KPI Grid
    # from:
    # <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(240px, 1fr)); gap: 1rem;">
    # to:
    # <div class="grid-4">
    
    content = content.replace('<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(240px, 1fr)); gap: 1rem;">', '<div class="grid-4">')

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
        
    print(f"Updated {filename}")
