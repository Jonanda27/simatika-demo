import os
import re
import glob

dir_path = r"C:\Users\ASUS\Documents\gthub\simatika-demo"
paroki_files = glob.glob(os.path.join(dir_path, "paroki_*.html"))

for filepath in paroki_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    is_active = 'paroki_pengguna.html' in filepath
    active_class = ' active' if is_active else ''
    
    # We match from the broken a tag to </nav>
    # Note: we should handle variations of spacing and active class.
    # The broken block always starts with: [spaces]<a href="paroki_pengguna.html" class="nav-item[ active]?">
    # and ends with </nav>
    
    pattern = r'[ \t]*<a href="paroki_pengguna\.html" class="nav-item(?: active)?">.*?</div>\s*</nav>'
    
    new_menu = f"""      <a href="paroki_pengguna.html" class="nav-item{active_class}">
        <div class="nav-item-icon">
          <i data-lucide="users" style="width: 1.25rem; height: 1.25rem;"></i>
          <span class="nav-text">Manajemen Pengguna</span>
        </div>
      </a>
    </nav>"""
    
    new_content = re.sub(pattern, new_menu, content, flags=re.DOTALL)
    
    if new_content != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Fixed {os.path.basename(filepath)}")
