import os
import re
import glob

dir_path = r"C:\Users\ASUS\Documents\gthub\simatika-demo"
paroki_files = glob.glob(os.path.join(dir_path, "paroki_*.html"))

pattern = r'<div class="nav-item[^>]*onclick="toggleSubmenu\(\'sistem\'\)".*?</div>\s*<div class="submenu" id="submenu-sistem".*?</div>'

for filepath in paroki_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    is_active = 'paroki_pengguna.html' in filepath
    active_class = ' active' if is_active else ''
    
    new_menu = f"""      <a href="paroki_pengguna.html" class="nav-item{active_class}">
        <div class="nav-item-icon">
          <i data-lucide="users" style="width: 1.25rem; height: 1.25rem;"></i>
          <span class="nav-text">Manajemen Pengguna</span>
        </div>
      </a>"""
      
    new_content = re.sub(pattern, new_menu, content, flags=re.DOTALL)
    
    if new_content != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated {os.path.basename(filepath)}")
