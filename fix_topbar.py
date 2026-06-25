import re
import os

stasi_files = [
    'stasi_pengurus.html',
    'stasi_sakramen.html',
    'stasi_mutasi.html',
    'stasi_aktivitas.html'
]

paroki_files = [
    'paroki_pengurus.html',
    'paroki_sakramen.html',
    'paroki_mutasi.html',
    'paroki_aktivitas.html'
]

stasi_topbar_new = """      <div style="display: flex; align-items: center; gap: 1.25rem;">
        
        <div class="notification-wrapper">
          <i data-lucide="bell" style="width: 1.25rem; height: 1.25rem; color: #475569;"></i>
          <span class="notification-badge">2</span>
        </div>
        
        <div style="display: flex; align-items: center; gap: 0.75rem; padding-left: 1.25rem; border-left: 1px solid #e2e8f0;">
          <div style="text-align: right;">
            <p style="font-weight: 700; font-size: 0.875rem; margin: 0; color: #1e293b;">stasi_paulus</p>
            <p style="font-size: 0.75rem; color: #64748b; margin: 0;">Admin Stasi</p>
          </div>
          <div style="width: 2.5rem; height: 2.5rem; background-color: #6d4b40; color: white; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-weight: 700;">
            SP
          </div>
        </div>
        
        <a href="index.html" class="btn-logout" title="Keluar">
          <i data-lucide="log-out" style="width: 1.25rem; height: 1.25rem; color: #334155;"></i>
        </a>
      </div>"""

paroki_topbar_new = """      <div style="display: flex; align-items: center; gap: 1.25rem;">
        
        <div class="notification-wrapper">
          <i data-lucide="bell" style="width: 1.25rem; height: 1.25rem; color: #475569;"></i>
          <span class="notification-badge">2</span>
        </div>
        
        <div style="display: flex; align-items: center; gap: 0.75rem; padding-left: 1.25rem; border-left: 1px solid #e2e8f0;">
          <div style="text-align: right;">
            <p style="font-weight: 700; font-size: 0.875rem; margin: 0; color: #1e293b;">admin_paroki</p>
            <p style="font-size: 0.75rem; color: #64748b; margin: 0;">Admin Paroki</p>
          </div>
          <div style="width: 2.5rem; height: 2.5rem; background-color: #6d4b40; color: white; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-weight: 700;">
            AP
          </div>
        </div>
        
        <a href="index.html" class="btn-logout" title="Keluar">
          <i data-lucide="log-out" style="width: 1.25rem; height: 1.25rem; color: #334155;"></i>
        </a>
      </div>"""

def replace_topbar(files, new_topbar):
    for file in files:
        if not os.path.exists(file):
            continue
        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # We find the start of the right side of the topbar
        # <div style="display: flex; align-items: center; gap: 1.25rem;">
        # ...
        # </header>
        pattern = r'<div style="display: flex; align-items: center; gap: 1\.25rem;">.*?</div>\s*</header>'
        replacement = new_topbar + "\n    </header>"
        
        new_content = re.sub(pattern, replacement, content, flags=re.DOTALL)
        
        with open(file, 'w', encoding='utf-8') as f:
            f.write(new_content)
            print(f"Updated topbar in {file}")

replace_topbar(stasi_files, stasi_topbar_new)
replace_topbar(paroki_files, paroki_topbar_new)
