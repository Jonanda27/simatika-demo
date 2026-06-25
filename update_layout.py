import os
import re

files_info = {
    'dashboard.html': {'title': 'Dashboard KBG', 'active': 'dashboard'},
    'pendataan.html': {'title': 'Form Pendataan', 'active': 'pendataan'},
    'datadraft.html': {'title': 'Data Draft', 'active': 'draft'},
    'semuadata.html': {'title': 'Semua Data', 'active': 'semuadata'},
    'datakeluarga.html': {'title': 'Data Keluarga', 'active': 'datakeluarga'},
    'pengurusaktif.html': {'title': 'Pengurus Aktif', 'active': 'pengurus'},
    'pengajuanpengurus.html': {'title': 'Pengajuan Pengurus', 'active': 'pengajuan'}
}

sidebar_template = """  <!-- SIDEBAR -->
  <aside class="sidebar" id="appSidebar">
    <div class="sidebar-header">
      <img src="images/logo.png" alt="Logo" class="sidebar-logo-img" onerror="this.src='https://via.placeholder.com/40';">
      <div class="sidebar-brand-text">
        <span style="font-weight: 700; font-size: 1.125rem; color: white; line-height: 1.1;">SIMATIKA</span>
        <span style="font-size: 0.6875rem; color: #94a3b8;">Keuskupan Timika</span>
      </div>
    </div>
    
    <nav class="sidebar-nav">
      <p class="nav-label">MENU KBG</p>
      
      <a href="dashboard.html" class="nav-item {DASHBOARD_ACTIVE}">
        <div class="nav-item-icon">
          <i data-lucide="home" style="width: 1.25rem; height: 1.25rem;"></i>
          <span class="nav-text">Dashboard KBG</span>
        </div>
      </a>
      
      <div class="nav-item {SENSUS_ACTIVE}" onclick="toggleSubmenu('sensus')">
        <div class="nav-item-icon">
          <i data-lucide="clipboard-list" style="width: 1.25rem; height: 1.25rem;"></i>
          <span class="nav-text">Sensus Umat</span>
        </div>
        <i data-lucide="chevron-down" class="submenu-chevron" style="width: 1rem; height: 1rem; {CHEVRON_DIR}"></i>
      </div>
      <div class="submenu" id="submenu-sensus" style="display: {SENSUS_DISPLAY};">
        <a href="pendataan.html" class="submenu-item {PENDATAAN_ACTIVE}">
          <div style="width: 0.375rem; height: 0.375rem; border-radius: 50%; background-color: #475569;" class="sub-dot"></div>
          <span class="nav-text">Form Pendataan</span>
        </a>
        <a href="datadraft.html" class="submenu-item {DRAFT_ACTIVE}">
          <div style="width: 0.375rem; height: 0.375rem; border-radius: 50%; background-color: #475569;" class="sub-dot"></div>
          <span class="nav-text">Data Draft</span>
        </a>
      </div>
      
      <a href="semuadata.html" class="nav-item {SEMUADATA_ACTIVE}">
        <div class="nav-item-icon">
          <i data-lucide="folder-open" style="width: 1.25rem; height: 1.25rem;"></i>
          <span class="nav-text">Semua Data</span>
        </div>
      </a>
      
      <a href="datakeluarga.html" class="nav-item {DATAKELUARGA_ACTIVE}">
        <div class="nav-item-icon">
          <i data-lucide="user-plus" style="width: 1.25rem; height: 1.25rem;"></i>
          <span class="nav-text">Data Keluarga</span>
        </div>
      </a>
      
      <a href="petaumat.html" class="nav-item {PETA_ACTIVE}">
        <div class="nav-item-icon">
          <i data-lucide="map" style="width: 1.25rem; height: 1.25rem;"></i>
          <span class="nav-text">Peta Umat</span>
        </div>
      </a>
      
      <a href="pengurusaktif.html" class="nav-item {PENGURUS_ACTIVE}">
        <div class="nav-item-icon">
          <i data-lucide="users" style="width: 1.25rem; height: 1.25rem;"></i>
          <span class="nav-text">Pengurus Aktif</span>
        </div>
      </a>
      
      <a href="pengajuanpengurus.html" class="nav-item {PENGAJUAN_ACTIVE}">
        <div class="nav-item-icon">
          <i data-lucide="shield-check" style="width: 1.25rem; height: 1.25rem;"></i>
          <span class="nav-text">Pengajuan Pengurus</span>
        </div>
      </a>
    </nav>
    <div class="sidebar-footer">
      <div class="circle-badge">N</div>
    </div>
  </aside>"""

topbar_template = """    <header class="topbar">
      <div style="display: flex; align-items: center; gap: 1rem;">
        <button class="btn-hamburger" onclick="toggleSidebarLayout()">
          <i data-lucide="menu" style="width: 1.5rem; height: 1.5rem; color: #475569;"></i>
        </button>
        <h1 class="topbar-title">{PAGE_TITLE}</h1>
      </div>
      <div style="display: flex; align-items: center; gap: 1.25rem;">
        
        <div class="notification-wrapper">
          <i data-lucide="bell" style="width: 1.25rem; height: 1.25rem; color: #475569;"></i>
          <span class="notification-badge">5</span>
        </div>
        
        <div style="display: flex; align-items: center; gap: 0.75rem; padding-left: 1.25rem; border-left: 1px solid #e2e8f0;">
          <div style="text-align: right;">
            <p style="font-weight: 700; font-size: 0.875rem; margin: 0; color: #1e293b;">kbg_paulus</p>
            <p style="font-size: 0.75rem; color: #64748b; margin: 0;">Ketua KBG</p>
          </div>
          <div style="width: 2.5rem; height: 2.5rem; background-color: #6d4b40; color: white; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-weight: 700;">
            KP
          </div>
        </div>
        
        <a href="index.html" class="btn-logout" title="Keluar">
          <i data-lucide="log-out" style="width: 1.25rem; height: 1.25rem; color: #334155;"></i>
        </a>
      </div>
    </header>"""

js_addition = """
    function toggleSidebarLayout() {
      const sidebar = document.getElementById('appSidebar');
      const main = document.querySelector('.main-content');
      sidebar.classList.toggle('collapsed');
      main.classList.toggle('expanded');
    }
"""

def process_file(filename, info):
    filepath = os.path.join(r"C:\Users\ASUS\Documents\gthub\simatika-demo", filename)
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Add <link rel="stylesheet" href="css/layout.css"> to <head> if not exists
    if 'css/layout.css' not in content:
        content = content.replace('</head>', '  <link rel="stylesheet" href="css/layout.css">\n</head>')

    # Prepare Sidebar format variables
    format_vars = {
        'DASHBOARD_ACTIVE': '',
        'SENSUS_ACTIVE': '',
        'CHEVRON_DIR': 'transform: rotate(0deg);',
        'SENSUS_DISPLAY': 'none',
        'PENDATAAN_ACTIVE': '',
        'DRAFT_ACTIVE': '',
        'SEMUADATA_ACTIVE': '',
        'DATAKELUARGA_ACTIVE': '',
        'PETA_ACTIVE': '',
        'PENGURUS_ACTIVE': '',
        'PENGAJUAN_ACTIVE': '',
        'PAGE_TITLE': info['title']
    }
    
    active = info['active']
    if active == 'dashboard': format_vars['DASHBOARD_ACTIVE'] = 'active'
    elif active == 'pendataan':
        format_vars['PENDATAAN_ACTIVE'] = 'active'
        format_vars['SENSUS_DISPLAY'] = 'flex'
        format_vars['CHEVRON_DIR'] = 'transform: rotate(180deg);'
    elif active == 'draft':
        format_vars['DRAFT_ACTIVE'] = 'active'
        format_vars['SENSUS_DISPLAY'] = 'flex'
        format_vars['CHEVRON_DIR'] = 'transform: rotate(180deg);'
    elif active == 'semuadata': format_vars['SEMUADATA_ACTIVE'] = 'active'
    elif active == 'datakeluarga': format_vars['DATAKELUARGA_ACTIVE'] = 'active'
    elif active == 'pengurus': format_vars['PENGURUS_ACTIVE'] = 'active'
    elif active == 'pengajuan': format_vars['PENGAJUAN_ACTIVE'] = 'active'

    new_sidebar = sidebar_template.format(**format_vars)
    new_topbar = topbar_template.format(**format_vars)

    # Replace sidebar: <aside class="sidebar">...</aside>
    # Note: Using regex with DOTALL
    content = re.sub(r'<!-- SIDEBAR -->\s*<aside class="sidebar".*?</aside>', new_sidebar, content, flags=re.DOTALL)
    if '<!-- SIDEBAR -->' not in content: # Fallback if no comment
        content = re.sub(r'<aside class="sidebar".*?</aside>', new_sidebar, content, flags=re.DOTALL)
        
    # Replace topbar
    # Try finding <!-- TOPBAR --> or just <header class="topbar">
    content = re.sub(r'<header class="topbar">.*?</header>', new_topbar, content, flags=re.DOTALL)
    
    # Remove old inline CSS to prevent conflicts
    # Removing .sidebar, .topbar, etc. from <style> blocks
    # Instead of complex regex, the styles in layout.css and inline <style> might conflict.
    # It's better to remove all CSS starting with .sidebar { ... } to .main-content { ... }
    # Let's just remove the specific blocks that we know conflict:
    content = re.sub(r'\.sidebar\s*\{.*?\}(?=\s*\.)', '', content, flags=re.DOTALL)
    content = re.sub(r'\.sidebar-header\s*\{.*?\}(?=\s*\.)', '', content, flags=re.DOTALL)
    content = re.sub(r'\.sidebar-nav\s*\{.*?\}(?=\s*\.)', '', content, flags=re.DOTALL)
    content = re.sub(r'\.topbar\s*\{.*?\}(?=\s*\.)', '', content, flags=re.DOTALL)
    content = re.sub(r'\.main-content\s*\{.*?\}(?=\s*\.)', '', content, flags=re.DOTALL)

    # Inject toggleSidebarLayout function
    if 'function toggleSidebarLayout' not in content:
        content = content.replace('</script>', js_addition + '\n  </script>')

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Updated {filename}")

for filename, info in files_info.items():
    process_file(filename, info)

print("All files updated successfully.")
