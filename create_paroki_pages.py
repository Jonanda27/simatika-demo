import os
import glob
import re

SIDEBAR_HTML = """
  <!-- SIDEBAR PAROKI -->
  <aside class="sidebar" id="appSidebar">
    <div class="sidebar-header">
      <img src="images/logo.png" alt="Logo" class="sidebar-logo-img" onerror="this.src='https://via.placeholder.com/40';">
      <div class="sidebar-brand-text">
        <span style="font-weight: 700; font-size: 1.125rem; color: white; line-height: 1.1;">SIMATIKA</span>
        <span style="font-size: 0.6875rem; color: #94a3b8;">Keuskupan Timika</span>
      </div>
    </div>
    
    <nav class="sidebar-nav">
      <p class="nav-label">MENU PAROKI</p>
      
      <a href="paroki_dashboard.html" class="nav-item __ACTIVE_DASHBOARD__">
        <div class="nav-item-icon">
          <i data-lucide="home" style="width: 1.25rem; height: 1.25rem;"></i>
          <span class="nav-text">Dashboard Paroki</span>
        </div>
      </a>
      
      <div class="nav-item" onclick="toggleSubmenu('induk')">
        <div class="nav-item-icon">
          <i data-lucide="users" style="width: 1.25rem; height: 1.25rem;"></i>
          <span class="nav-text">Database Induk</span>
        </div>
        <i data-lucide="__CHEVRON_INDUK__" class="submenu-chevron" style="width: 1rem; height: 1rem;"></i>
      </div>
      <div class="submenu" id="submenu-induk" style="display: __DISPLAY_INDUK__;">
        <a href="paroki_dataumat.html" class="submenu-item __ACTIVE_DATAUMAT__">
          <div style="width: 0.375rem; height: 0.375rem; border-radius: 50%; background-color: __DOT_DATAUMAT__;" class="sub-dot"></div>
          <span class="nav-text" style="color: __COLOR_DATAUMAT__; font-weight: __WEIGHT_DATAUMAT__;">Data Umat</span>
        </a>
        <a href="paroki_datakeluarga.html" class="submenu-item __ACTIVE_DATAKELUARGA__">
          <div style="width: 0.375rem; height: 0.375rem; border-radius: 50%; background-color: __DOT_DATAKELUARGA__;" class="sub-dot"></div>
          <span class="nav-text" style="color: __COLOR_DATAKELUARGA__; font-weight: __WEIGHT_DATAKELUARGA__;">Data Keluarga</span>
        </a>
        <a href="paroki_pengurus.html" class="submenu-item __ACTIVE_PENGURUS__">
          <div style="width: 0.375rem; height: 0.375rem; border-radius: 50%; background-color: __DOT_PENGURUS__;" class="sub-dot"></div>
          <span class="nav-text" style="color: __COLOR_PENGURUS__; font-weight: __WEIGHT_PENGURUS__;">Pengurus Aktif</span>
        </a>
        <a href="paroki_sakramen.html" class="submenu-item __ACTIVE_SAKRAMEN__">
          <div style="width: 0.375rem; height: 0.375rem; border-radius: 50%; background-color: __DOT_SAKRAMEN__;" class="sub-dot"></div>
          <span class="nav-text" style="color: __COLOR_SAKRAMEN__; font-weight: __WEIGHT_SAKRAMEN__;">Data Sakramen</span>
        </a>
        <a href="paroki_mutasi.html" class="submenu-item __ACTIVE_MUTASI__">
          <div style="width: 0.375rem; height: 0.375rem; border-radius: 50%; background-color: __DOT_MUTASI__;" class="sub-dot"></div>
          <span class="nav-text" style="color: __COLOR_MUTASI__; font-weight: __WEIGHT_MUTASI__;">Mutasi Umat</span>
        </a>
        <a href="paroki_aktivitas.html" class="submenu-item __ACTIVE_AKTIVITAS__">
          <div style="width: 0.375rem; height: 0.375rem; border-radius: 50%; background-color: __DOT_AKTIVITAS__;" class="sub-dot"></div>
          <span class="nav-text" style="color: __COLOR_AKTIVITAS__; font-weight: __WEIGHT_AKTIVITAS__;">Aktivitas Pastoral</span>
        </a>
      </div>
      
      <a href="paroki_peta.html" class="nav-item __ACTIVE_PETA__">
        <div class="nav-item-icon">
          <i data-lucide="map" style="width: 1.25rem; height: 1.25rem;"></i>
          <span class="nav-text">Peta Paroki</span>
        </div>
      </a>
      
      <a href="paroki_verifikasi.html" class="nav-item __ACTIVE_VERIFIKASI__">
        <div class="nav-item-icon">
          <i data-lucide="shield-check" style="width: 1.25rem; height: 1.25rem;"></i>
          <span class="nav-text">Approval Akhir</span>
        </div>
      </a>

      <div class="nav-item" onclick="toggleSubmenu('wilayah')">
        <div class="nav-item-icon">
          <i data-lucide="map-pin" style="width: 1.25rem; height: 1.25rem;"></i>
          <span class="nav-text">Manajemen Wilayah</span>
        </div>
        <i data-lucide="__CHEVRON_WILAYAH__" class="submenu-chevron" style="width: 1rem; height: 1rem;"></i>
      </div>
      <div class="submenu" id="submenu-wilayah" style="display: __DISPLAY_WILAYAH__;">
        <a href="paroki_wilayah_stasi.html" class="submenu-item __ACTIVE_WILAYAH_STASI__">
          <div style="width: 0.375rem; height: 0.375rem; border-radius: 50%; background-color: __DOT_WILAYAH_STASI__;" class="sub-dot"></div>
          <span class="nav-text" style="color: __COLOR_WILAYAH_STASI__; font-weight: __WEIGHT_WILAYAH_STASI__;">Data Stasi</span>
        </a>
        <a href="paroki_wilayah_kbg.html" class="submenu-item __ACTIVE_WILAYAH_KBG__">
          <div style="width: 0.375rem; height: 0.375rem; border-radius: 50%; background-color: __DOT_WILAYAH_KBG__;" class="sub-dot"></div>
          <span class="nav-text" style="color: __COLOR_WILAYAH_KBG__; font-weight: __WEIGHT_WILAYAH_KBG__;">Data KBG</span>
        </a>
      </div>
      
      <div class="nav-item" onclick="toggleSubmenu('laporan')">
        <div class="nav-item-icon">
          <i data-lucide="folder-open" style="width: 1.25rem; height: 1.25rem;"></i>
          <span class="nav-text">Laporan & Arsip</span>
        </div>
        <i data-lucide="__CHEVRON_LAPORAN__" class="submenu-chevron" style="width: 1rem; height: 1rem;"></i>
      </div>
      <div class="submenu" id="submenu-laporan" style="display: __DISPLAY_LAPORAN__;">
        <a href="paroki_laporan.html" class="submenu-item __ACTIVE_LAPORAN__">
          <div style="width: 0.375rem; height: 0.375rem; border-radius: 50%; background-color: __DOT_LAPORAN__;" class="sub-dot"></div>
          <span class="nav-text" style="color: __COLOR_LAPORAN__; font-weight: __WEIGHT_LAPORAN__;">Laporan & Statistik</span>
        </a>
        <a href="paroki_dokumen.html" class="submenu-item __ACTIVE_DOKUMEN__">
          <div style="width: 0.375rem; height: 0.375rem; border-radius: 50%; background-color: __DOT_DOKUMEN__;" class="sub-dot"></div>
          <span class="nav-text" style="color: __COLOR_DOKUMEN__; font-weight: __WEIGHT_DOKUMEN__;">Dokumen & Arsip</span>
        </a>
      </div>

      <div class="nav-item" onclick="toggleSubmenu('sistem')">
        <div class="nav-item-icon">
          <i data-lucide="settings" style="width: 1.25rem; height: 1.25rem;"></i>
          <span class="nav-text">Pengaturan Sistem</span>
        </div>
        <i data-lucide="__CHEVRON_SISTEM__" class="submenu-chevron" style="width: 1rem; height: 1rem;"></i>
      </div>
      <div class="submenu" id="submenu-sistem" style="display: __DISPLAY_SISTEM__;">
        <a href="paroki_pengguna.html" class="submenu-item __ACTIVE_PENGGUNA__">
          <div style="width: 0.375rem; height: 0.375rem; border-radius: 50%; background-color: __DOT_PENGGUNA__;" class="sub-dot"></div>
          <span class="nav-text" style="color: __COLOR_PENGGUNA__; font-weight: __WEIGHT_PENGGUNA__;">Manajemen Pengguna</span>
        </a>
        <a href="paroki_pengaturan.html" class="submenu-item __ACTIVE_PENGATURAN__">
          <div style="width: 0.375rem; height: 0.375rem; border-radius: 50%; background-color: __DOT_PENGATURAN__;" class="sub-dot"></div>
          <span class="nav-text" style="color: __COLOR_PENGATURAN__; font-weight: __WEIGHT_PENGATURAN__;">Pengaturan Paroki</span>
        </a>
      </div>

    </nav>
  </aside>
"""

# Map page identifiers to the corresponding variables
# Defaults
defaults = {
    '__ACTIVE_DASHBOARD__': '',
    '__CHEVRON_INDUK__': 'chevron-right', '__DISPLAY_INDUK__': 'none',
    '__ACTIVE_DATAUMAT__': '', '__DOT_DATAUMAT__': '#475569', '__COLOR_DATAUMAT__': 'inherit', '__WEIGHT_DATAUMAT__': '500',
    '__ACTIVE_DATAKELUARGA__': '', '__DOT_DATAKELUARGA__': '#475569', '__COLOR_DATAKELUARGA__': 'inherit', '__WEIGHT_DATAKELUARGA__': '500',
    '__ACTIVE_PENGURUS__': '', '__DOT_PENGURUS__': '#475569', '__COLOR_PENGURUS__': 'inherit', '__WEIGHT_PENGURUS__': '500',
    '__ACTIVE_SAKRAMEN__': '', '__DOT_SAKRAMEN__': '#475569', '__COLOR_SAKRAMEN__': 'inherit', '__WEIGHT_SAKRAMEN__': '500',
    '__ACTIVE_MUTASI__': '', '__DOT_MUTASI__': '#475569', '__COLOR_MUTASI__': 'inherit', '__WEIGHT_MUTASI__': '500',
    '__ACTIVE_AKTIVITAS__': '', '__DOT_AKTIVITAS__': '#475569', '__COLOR_AKTIVITAS__': 'inherit', '__WEIGHT_AKTIVITAS__': '500',
    '__ACTIVE_PETA__': '',
    '__ACTIVE_VERIFIKASI__': '',
    '__CHEVRON_WILAYAH__': 'chevron-right', '__DISPLAY_WILAYAH__': 'none',
    '__ACTIVE_WILAYAH_STASI__': '', '__DOT_WILAYAH_STASI__': '#475569', '__COLOR_WILAYAH_STASI__': 'inherit', '__WEIGHT_WILAYAH_STASI__': '500',
    '__ACTIVE_WILAYAH_KBG__': '', '__DOT_WILAYAH_KBG__': '#475569', '__COLOR_WILAYAH_KBG__': 'inherit', '__WEIGHT_WILAYAH_KBG__': '500',
    '__CHEVRON_LAPORAN__': 'chevron-right', '__DISPLAY_LAPORAN__': 'none',
    '__ACTIVE_LAPORAN__': '', '__DOT_LAPORAN__': '#475569', '__COLOR_LAPORAN__': 'inherit', '__WEIGHT_LAPORAN__': '500',
    '__ACTIVE_DOKUMEN__': '', '__DOT_DOKUMEN__': '#475569', '__COLOR_DOKUMEN__': 'inherit', '__WEIGHT_DOKUMEN__': '500',
    '__CHEVRON_SISTEM__': 'chevron-right', '__DISPLAY_SISTEM__': 'none',
    '__ACTIVE_PENGGUNA__': '', '__DOT_PENGGUNA__': '#475569', '__COLOR_PENGGUNA__': 'inherit', '__WEIGHT_PENGGUNA__': '500',
    '__ACTIVE_PENGATURAN__': '', '__DOT_PENGATURAN__': '#475569', '__COLOR_PENGATURAN__': 'inherit', '__WEIGHT_PENGATURAN__': '500',
}

page_configs = {
    'dashboard': {'__ACTIVE_DASHBOARD__': 'active'},
    'dataumat': {'__CHEVRON_INDUK__': 'chevron-down', '__DISPLAY_INDUK__': 'flex', '__ACTIVE_DATAUMAT__': 'active', '__DOT_DATAUMAT__': 'var(--brown-600)', '__COLOR_DATAUMAT__': 'var(--brown-600)', '__WEIGHT_DATAUMAT__': '700'},
    'datakeluarga': {'__CHEVRON_INDUK__': 'chevron-down', '__DISPLAY_INDUK__': 'flex', '__ACTIVE_DATAKELUARGA__': 'active', '__DOT_DATAKELUARGA__': 'var(--brown-600)', '__COLOR_DATAKELUARGA__': 'var(--brown-600)', '__WEIGHT_DATAKELUARGA__': '700'},
    'pengurus': {'__CHEVRON_INDUK__': 'chevron-down', '__DISPLAY_INDUK__': 'flex', '__ACTIVE_PENGURUS__': 'active', '__DOT_PENGURUS__': 'var(--brown-600)', '__COLOR_PENGURUS__': 'var(--brown-600)', '__WEIGHT_PENGURUS__': '700'},
    'sakramen': {'__CHEVRON_INDUK__': 'chevron-down', '__DISPLAY_INDUK__': 'flex', '__ACTIVE_SAKRAMEN__': 'active', '__DOT_SAKRAMEN__': 'var(--brown-600)', '__COLOR_SAKRAMEN__': 'var(--brown-600)', '__WEIGHT_SAKRAMEN__': '700'},
    'mutasi': {'__CHEVRON_INDUK__': 'chevron-down', '__DISPLAY_INDUK__': 'flex', '__ACTIVE_MUTASI__': 'active', '__DOT_MUTASI__': 'var(--brown-600)', '__COLOR_MUTASI__': 'var(--brown-600)', '__WEIGHT_MUTASI__': '700'},
    'aktivitas': {'__CHEVRON_INDUK__': 'chevron-down', '__DISPLAY_INDUK__': 'flex', '__ACTIVE_AKTIVITAS__': 'active', '__DOT_AKTIVITAS__': 'var(--brown-600)', '__COLOR_AKTIVITAS__': 'var(--brown-600)', '__WEIGHT_AKTIVITAS__': '700'},
    'peta': {'__ACTIVE_PETA__': 'active'},
    'verifikasi': {'__ACTIVE_VERIFIKASI__': 'active'},
    'laporan': {'__CHEVRON_LAPORAN__': 'chevron-down', '__DISPLAY_LAPORAN__': 'flex', '__ACTIVE_LAPORAN__': 'active', '__DOT_LAPORAN__': 'var(--brown-600)', '__COLOR_LAPORAN__': 'var(--brown-600)', '__WEIGHT_LAPORAN__': '700'},
    'dokumen': {'__CHEVRON_LAPORAN__': 'chevron-down', '__DISPLAY_LAPORAN__': 'flex', '__ACTIVE_DOKUMEN__': 'active', '__DOT_DOKUMEN__': 'var(--brown-600)', '__COLOR_DOKUMEN__': 'var(--brown-600)', '__WEIGHT_DOKUMEN__': '700'},
    # Specific Paroki ones
    'wilayah_stasi': {'__CHEVRON_WILAYAH__': 'chevron-down', '__DISPLAY_WILAYAH__': 'flex', '__ACTIVE_WILAYAH_STASI__': 'active', '__DOT_WILAYAH_STASI__': 'var(--brown-600)', '__COLOR_WILAYAH_STASI__': 'var(--brown-600)', '__WEIGHT_WILAYAH_STASI__': '700'},
    'wilayah_kbg': {'__CHEVRON_WILAYAH__': 'chevron-down', '__DISPLAY_WILAYAH__': 'flex', '__ACTIVE_WILAYAH_KBG__': 'active', '__DOT_WILAYAH_KBG__': 'var(--brown-600)', '__COLOR_WILAYAH_KBG__': 'var(--brown-600)', '__WEIGHT_WILAYAH_KBG__': '700'},
    'pengguna': {'__CHEVRON_SISTEM__': 'chevron-down', '__DISPLAY_SISTEM__': 'flex', '__ACTIVE_PENGGUNA__': 'active', '__DOT_PENGGUNA__': 'var(--brown-600)', '__COLOR_PENGGUNA__': 'var(--brown-600)', '__WEIGHT_PENGGUNA__': '700'},
    'pengaturan': {'__CHEVRON_SISTEM__': 'chevron-down', '__DISPLAY_SISTEM__': 'flex', '__ACTIVE_PENGATURAN__': 'active', '__DOT_PENGATURAN__': 'var(--brown-600)', '__COLOR_PENGATURAN__': 'var(--brown-600)', '__WEIGHT_PENGATURAN__': '700'},
}

def create_sidebar(page_id):
    s = SIDEBAR_HTML
    config = defaults.copy()
    if page_id in page_configs:
        config.update(page_configs[page_id])
    for k, v in config.items():
        s = s.replace(k, v)
    return s

stasi_files = glob.glob('c:/Users/ASUS/Documents/gthub/simatika-demo/stasi_*.html')

for filepath in stasi_files:
    filename = os.path.basename(filepath)
    page_id = filename.replace('stasi_', '').replace('.html', '')
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Replace sidebar
    sidebar_match = re.search(r'<!-- SIDEBAR -->.*?<!-- MAIN CONTENT -->', content, re.DOTALL)
    if sidebar_match:
        new_sidebar = create_sidebar(page_id) + '\n  <!-- MAIN CONTENT -->'
        content = content.replace(sidebar_match.group(0), new_sidebar)
    
    # Topbar tweaks
    content = content.replace('stasi_paulus', 'admin_paroki')
    content = content.replace('Admin Stasi', 'Admin Paroki')
    content = content.replace('>SP<', '>AP<')
    content = content.replace('stasi_dashboard.html', 'paroki_dashboard.html')
    
    # Title tweak
    content = re.sub(r'<title>(.*?)</title>', lambda m: f'<title>{m.group(1).replace("Stasi", "Paroki")}</title>', content)
    # Peta Title tweak
    content = content.replace('Peta Stasi', 'Peta Paroki')
    content = content.replace('Verifikasi Stasi', 'Approval Paroki')
    
    out_path = os.path.join(os.path.dirname(filepath), f'paroki_{page_id}.html')
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Created {out_path}")

# Now generate specific paroki pages (wilayah_stasi, wilayah_kbg, pengguna, pengaturan)
# I will just use paroki_dashboard.html as a template for them and change the content area slightly.
dashboard_path = 'c:/Users/ASUS/Documents/gthub/simatika-demo/paroki_dashboard.html'
with open(dashboard_path, 'r', encoding='utf-8') as f:
    dash_content = f.read()

def create_specific_page(page_id, title, subtitle):
    # Fix sidebar
    sidebar_match = re.search(r'<!-- SIDEBAR PAROKI -->.*?<!-- MAIN CONTENT -->', dash_content, re.DOTALL)
    if sidebar_match:
        new_sidebar = create_sidebar(page_id) + '\n  <!-- MAIN CONTENT -->'
        content = dash_content.replace(sidebar_match.group(0), new_sidebar)
    else:
        content = dash_content
        
    # Replace main content area
    content_area_match = re.search(r'<div class="content-area">.*?</main>', content, re.DOTALL)
    if content_area_match:
        new_content_area = f"""<div class="content-area">
      <div style="display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 1rem; margin-bottom: 1rem;">
        <div>
          <h2 style="font-size: 1.5rem; font-weight: 700; color: #0f172a; margin: 0; letter-spacing: -0.025em;">{title}</h2>
          <p style="font-size: 0.875rem; color: #64748b; margin: 0.25rem 0 0 0; font-weight: 500;">{subtitle}</p>
        </div>
      </div>
      
      <div style="background: white; border: 1px solid #e2e8f0; padding: 3rem; text-align: center; color: #64748b; font-weight: 500;">
        <i data-lucide="settings" style="width: 3rem; height: 3rem; color: #cbd5e1; margin-bottom: 1rem;"></i>
        <p>Halaman ini merupakan halaman khusus role Admin Paroki.</p>
        <p style="font-size: 0.875rem; margin-top: 0.5rem;">[Tampilan Dummy]</p>
      </div>
    </div>
  </main>"""
        content = content.replace(content_area_match.group(0), new_content_area)
    
    # Topbar Title
    content = re.sub(r'<h1 class="topbar-title">.*?</h1>', f'<h1 class="topbar-title">{title}</h1>', content)
    content = re.sub(r'<title>.*?</title>', f'<title>{title} - SIMATIKA</title>', content)
    
    out_path = os.path.join(os.path.dirname(dashboard_path), f'paroki_{page_id}.html')
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Created {out_path}")

create_specific_page('wilayah_stasi', 'Manajemen Data Stasi', 'Kelola semua stasi yang ada di bawah paroki')
create_specific_page('wilayah_kbg', 'Manajemen Data KBG', 'Kelola semua KBG di seluruh stasi')
create_specific_page('pengguna', 'Manajemen Pengguna', 'Kelola akun Admin Stasi, Admin Paroki, dan KBG')
create_specific_page('pengaturan', 'Pengaturan Paroki', 'Konfigurasi profil dan pengaturan sistem paroki')
