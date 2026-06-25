import os

html_content = """<!DOCTYPE html>
<html lang="id">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Detail Keluarga - SIMATIKA</title>
  <link rel="stylesheet" href="css/style.css">
  <script src="https://unpkg.com/lucide@latest"></script>
  <style>
    body {
      background-color: #f8fafc;
      font-family: var(--font-sans);
      margin: 0;
      padding-bottom: 6rem;
    }
  </style>
</head>
<body>

  <!-- HEADER NAV -->
  <nav style="background-color: white; border-bottom: 1px solid #e2e8f0; position: sticky; top: 0; z-index: 50; box-shadow: var(--shadow-sm);">
    <div style="max-width: 72rem; margin: 0 auto; padding: 0 1.5rem; height: 5rem; display: flex; align-items: center; justify-content: space-between;">
      <div style="display: flex; align-items: center; gap: 1rem;">
        <button onclick="window.history.back()" style="background: transparent; border: none; cursor: pointer; padding: 0.5rem; border-radius: 0.375rem; transition: background 0.2s;" onmouseover="this.style.backgroundColor='#f1f5f9'" onmouseout="this.style.backgroundColor='transparent'">
          <i data-lucide="arrow-left" style="width: 1.5rem; height: 1.5rem; color: #475569;"></i>
        </button>
        <div style="display: flex; align-items: center; gap: 0.75rem; border-left: 1px solid #e2e8f0; padding-left: 1rem;">
          <img src="images/logo.png" alt="Logo" style="width: 2rem; height: 2rem; object-fit: contain;" onerror="this.src='https://via.placeholder.com/40';">
          <span style="font-weight: 800; color: #1e293b; letter-spacing: -0.025em;">SIMATIKA</span>
        </div>
      </div>
    </div>
  </nav>

  <main style="max-width: 72rem; margin: 2rem auto 0; padding: 0 1.5rem;">
    
    <!-- HERO SECTION DETAIL -->
    <div style="background: white; border-radius: 0; box-shadow: var(--shadow-sm); border: 1px solid #e2e8f0; overflow: hidden; margin-bottom: 2rem;">
      <div style="height: 16rem; background-color: #0f172a; position: relative;">
        <div style="position: absolute; inset: 0; background: linear-gradient(to top right, #3f2b20, #0f172a);"></div>
        <div style="position: absolute; inset: 0; background: linear-gradient(to top, #0f172a, transparent, transparent);"></div>
        
        <div style="position: absolute; bottom: 2rem; left: 2rem; right: 2rem; color: white;">
          <div style="display: flex; align-items: center; gap: 0.5rem; margin-bottom: 0.5rem;">
            <span style="background-color: rgba(34, 197, 94, 0.2); color: #4ade80; border: 1px solid rgba(34, 197, 94, 0.3); font-size: 0.75rem; font-weight: 700; padding: 0.25rem 0.75rem; text-transform: uppercase; letter-spacing: 0.05em; display: inline-flex; align-items: center; gap: 0.25rem; backdrop-filter: blur(4px);">
              <i data-lucide="check-circle-2" style="width: 0.75rem; height: 0.75rem;"></i> Data Aktif
            </span>
          </div>
          <h1 style="font-size: 2.25rem; font-weight: 800; letter-spacing: -0.025em; margin: 0 0 0.25rem 0;">
            Data Lengkap Keluarga
          </h1>
          <p style="color: #cbd5e1; font-family: monospace; font-size: 1.125rem; opacity: 0.9; margin: 0; display: flex; align-items: center; gap: 0.5rem;">
            <i data-lucide="shield-check" style="width: 1.25rem; height: 1.25rem;"></i> No. KK: 91010123560001
          </p>
          <p style="color: #94a3b8; font-family: monospace; font-size: 0.875rem; margin: 0.25rem 0 0 0;">
            Kode Keluarga: 12356
          </p>
        </div>
      </div>

      <div style="padding: 2rem; display: grid; grid-template-columns: 2fr 1fr; gap: 2rem;">
        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 1.5rem;">
          <div>
            <p style="font-size: 0.875rem; font-weight: 700; color: #94a3b8; text-transform: uppercase; letter-spacing: 0.025em; margin: 0 0 0.25rem 0;">Status Kepemilikan</p>
            <div style="display: flex; align-items: center; gap: 0.5rem; font-size: 1.125rem; font-weight: 700; color: #1e293b;">
              <i data-lucide="home" style="width: 1.25rem; height: 1.25rem; color: var(--brown-600);"></i> Milik Sendiri
            </div>
          </div>
          <div>
            <p style="font-size: 0.875rem; font-weight: 700; color: #94a3b8; text-transform: uppercase; letter-spacing: 0.025em; margin: 0 0 0.25rem 0;">Status Menumpang</p>
            <div style="display: flex; align-items: center; gap: 0.5rem; font-size: 1.125rem; font-weight: 700; color: #1e293b;">
              <i data-lucide="users" style="width: 1.25rem; height: 1.25rem; color: var(--brown-600);"></i> Keluarga Utama
            </div>
          </div>
          <div style="grid-column: span 2; padding-top: 1rem; border-top: 1px solid #f1f5f9;">
            <p style="font-size: 0.875rem; font-weight: 700; color: #94a3b8; text-transform: uppercase; letter-spacing: 0.025em; margin: 0 0 0.75rem 0;">Fasilitas Properti</p>
            <div style="display: flex; flex-wrap: wrap; gap: 0.75rem;">
              <span style="background-color: #eff6ff; color: #1d4ed8; border: 1px solid #bfdbfe; padding: 0.5rem 1rem; font-size: 0.875rem; font-weight: 700; display: inline-flex; align-items: center; gap: 0.5rem;">
                <i data-lucide="bath" style="width: 1rem; height: 1rem;"></i> Kamar Mandi
              </span>
              <span style="background-color: #eff6ff; color: #1d4ed8; border: 1px solid #bfdbfe; padding: 0.5rem 1rem; font-size: 0.875rem; font-weight: 700; display: inline-flex; align-items: center; gap: 0.5rem;">
                <i data-lucide="droplets" style="width: 1rem; height: 1rem;"></i> Toilet / WC
              </span>
              <span style="background-color: #f8fafc; color: #94a3b8; border: 1px solid #e2e8f0; padding: 0.5rem 1rem; font-size: 0.875rem; font-weight: 700; display: inline-flex; align-items: center; gap: 0.5rem;">
                <i data-lucide="droplets" style="width: 1rem; height: 1rem;"></i> Tempat Cuci
              </span>
            </div>
          </div>
        </div>

        <div style="background-color: #f8fafc; padding: 1.5rem; border: 1px solid #f1f5f9; text-align: center; display: flex; flex-direction: column; justify-content: center;">
          <h3 style="font-size: 3rem; font-weight: 800; color: var(--brown-600); margin: 0 0 0.5rem 0;">4</h3>
          <p style="color: #475569; font-weight: 700; text-transform: uppercase; letter-spacing: 0.1em; font-size: 0.75rem; margin: 0;">Total Anggota</p>
        </div>
      </div>
    </div>

    <!-- MAP & MEMBERS GRID -->
    <div style="display: grid; grid-template-columns: 2fr 1fr; gap: 2rem;">
      
      <!-- MEMBERS LIST -->
      <div style="display: flex; flex-direction: column; gap: 1.5rem;">
        <h2 style="font-size: 1.5rem; font-weight: 800; color: #1e293b; display: flex; align-items: center; gap: 0.75rem; margin: 0;">
          <i data-lucide="users" style="width: 1.5rem; height: 1.5rem; color: var(--brown-600);"></i> Profil Anggota Keluarga
        </h2>

        <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 1rem;">
          
          <!-- Umat 1 -->
          <div style="background: white; padding: 1.5rem; border: 1px solid #e2e8f0; box-shadow: var(--shadow-sm); transition: all 0.2s;" onmouseover="this.style.borderColor='var(--brown-300)'; this.style.boxShadow='var(--shadow-md)'" onmouseout="this.style.borderColor='#e2e8f0'; this.style.boxShadow='var(--shadow-sm)'">
            <div style="display: flex; align-items: flex-start; gap: 1rem; margin-bottom: 1rem;">
              <div style="width: 3rem; height: 3rem; background-color: var(--brown-50); color: var(--brown-600); display: flex; align-items: center; justify-content: center; flex-shrink: 0;">
                <i data-lucide="user-circle-2" style="width: 1.75rem; height: 1.75rem;"></i>
              </div>
              <div>
                <h3 style="font-weight: 700; color: #1e293b; font-size: 1.125rem; margin: 0 0 0.25rem 0; line-height: 1.2;">Bpk. Budi Santoso</h3>
                <div style="display: flex; align-items: center; gap: 0.5rem; margin-bottom: 0.5rem;">
                  <span style="background-color: #f1f5f9; color: #475569; font-size: 0.625rem; font-weight: 700; padding: 0.125rem 0.5rem; text-transform: uppercase; letter-spacing: 0.05em;">Kepala Keluarga</span>
                  <span style="font-size: 0.625rem; font-family: monospace; font-weight: 500; color: var(--brown-700); background-color: var(--brown-50); padding: 0.125rem 0.5rem; border: 1px solid var(--brown-100);">UMT-001</span>
                </div>
              </div>
            </div>
            <div style="display: flex; flex-direction: column; gap: 0.75rem; padding-top: 1rem; border-top: 1px solid #f1f5f9;">
              <div style="display: flex; align-items: center; gap: 0.75rem; font-size: 0.875rem; color: #475569;">
                <i data-lucide="briefcase" style="width: 1rem; height: 1rem; color: #94a3b8; flex-shrink: 0;"></i> <span>PNS</span>
              </div>
              <div style="display: flex; align-items: center; gap: 0.75rem; font-size: 0.875rem; color: #475569;">
                <i data-lucide="graduation-cap" style="width: 1rem; height: 1rem; color: #94a3b8; flex-shrink: 0;"></i> <span>S1 Sarjana</span>
              </div>
              <div style="display: flex; align-items: center; gap: 0.75rem; font-size: 0.875rem; color: #475569;">
                <i data-lucide="activity" style="width: 1rem; height: 1rem; color: #94a3b8; flex-shrink: 0;"></i> <span>Kesehatan: <span style="font-weight: 500; color: #1e293b;">Sehat</span></span>
              </div>
            </div>
          </div>

          <!-- Umat 2 -->
          <div style="background: white; padding: 1.5rem; border: 1px solid #e2e8f0; box-shadow: var(--shadow-sm); transition: all 0.2s;" onmouseover="this.style.borderColor='var(--brown-300)'; this.style.boxShadow='var(--shadow-md)'" onmouseout="this.style.borderColor='#e2e8f0'; this.style.boxShadow='var(--shadow-sm)'">
            <div style="display: flex; align-items: flex-start; gap: 1rem; margin-bottom: 1rem;">
              <div style="width: 3rem; height: 3rem; background-color: var(--brown-50); color: var(--brown-600); display: flex; align-items: center; justify-content: center; flex-shrink: 0;">
                <i data-lucide="user-circle-2" style="width: 1.75rem; height: 1.75rem;"></i>
              </div>
              <div>
                <h3 style="font-weight: 700; color: #1e293b; font-size: 1.125rem; margin: 0 0 0.25rem 0; line-height: 1.2;">Ibu Siti Aminah</h3>
                <div style="display: flex; align-items: center; gap: 0.5rem; margin-bottom: 0.5rem;">
                  <span style="background-color: #f1f5f9; color: #475569; font-size: 0.625rem; font-weight: 700; padding: 0.125rem 0.5rem; text-transform: uppercase; letter-spacing: 0.05em;">Istri</span>
                  <span style="font-size: 0.625rem; font-family: monospace; font-weight: 500; color: var(--brown-700); background-color: var(--brown-50); padding: 0.125rem 0.5rem; border: 1px solid var(--brown-100);">UMT-002</span>
                </div>
              </div>
            </div>
            <div style="display: flex; flex-direction: column; gap: 0.75rem; padding-top: 1rem; border-top: 1px solid #f1f5f9;">
              <div style="display: flex; align-items: center; gap: 0.75rem; font-size: 0.875rem; color: #475569;">
                <i data-lucide="briefcase" style="width: 1rem; height: 1rem; color: #94a3b8; flex-shrink: 0;"></i> <span>Ibu Rumah Tangga</span>
              </div>
              <div style="display: flex; align-items: center; gap: 0.75rem; font-size: 0.875rem; color: #475569;">
                <i data-lucide="graduation-cap" style="width: 1rem; height: 1rem; color: #94a3b8; flex-shrink: 0;"></i> <span>SMA/SMK</span>
              </div>
              <div style="display: flex; align-items: center; gap: 0.75rem; font-size: 0.875rem; color: #475569;">
                <i data-lucide="activity" style="width: 1rem; height: 1rem; color: #94a3b8; flex-shrink: 0;"></i> <span>Kesehatan: <span style="font-weight: 500; color: #1e293b;">Sehat</span></span>
              </div>
            </div>
          </div>

          <!-- Umat 3 -->
          <div style="background: white; padding: 1.5rem; border: 1px solid #e2e8f0; box-shadow: var(--shadow-sm); transition: all 0.2s;" onmouseover="this.style.borderColor='var(--brown-300)'; this.style.boxShadow='var(--shadow-md)'" onmouseout="this.style.borderColor='#e2e8f0'; this.style.boxShadow='var(--shadow-sm)'">
            <div style="display: flex; align-items: flex-start; gap: 1rem; margin-bottom: 1rem;">
              <div style="width: 3rem; height: 3rem; background-color: var(--brown-50); color: var(--brown-600); display: flex; align-items: center; justify-content: center; flex-shrink: 0;">
                <i data-lucide="user-circle-2" style="width: 1.75rem; height: 1.75rem;"></i>
              </div>
              <div>
                <h3 style="font-weight: 700; color: #1e293b; font-size: 1.125rem; margin: 0 0 0.25rem 0; line-height: 1.2;">Andi Santoso</h3>
                <div style="display: flex; align-items: center; gap: 0.5rem; margin-bottom: 0.5rem;">
                  <span style="background-color: #f1f5f9; color: #475569; font-size: 0.625rem; font-weight: 700; padding: 0.125rem 0.5rem; text-transform: uppercase; letter-spacing: 0.05em;">Anak</span>
                  <span style="font-size: 0.625rem; font-family: monospace; font-weight: 500; color: var(--brown-700); background-color: var(--brown-50); padding: 0.125rem 0.5rem; border: 1px solid var(--brown-100);">UMT-003</span>
                </div>
              </div>
            </div>
            <div style="display: flex; flex-direction: column; gap: 0.75rem; padding-top: 1rem; border-top: 1px solid #f1f5f9;">
              <div style="display: flex; align-items: center; gap: 0.75rem; font-size: 0.875rem; color: #475569;">
                <i data-lucide="briefcase" style="width: 1rem; height: 1rem; color: #94a3b8; flex-shrink: 0;"></i> <span>Mahasiswa</span>
              </div>
              <div style="display: flex; align-items: center; gap: 0.75rem; font-size: 0.875rem; color: #475569;">
                <i data-lucide="graduation-cap" style="width: 1rem; height: 1rem; color: #94a3b8; flex-shrink: 0;"></i> <span>SMA/SMK</span>
              </div>
              <div style="display: flex; align-items: center; gap: 0.75rem; font-size: 0.875rem; color: #475569;">
                <i data-lucide="activity" style="width: 1rem; height: 1rem; color: #94a3b8; flex-shrink: 0;"></i> <span>Kesehatan: <span style="font-weight: 500; color: #1e293b;">Sehat</span></span>
              </div>
            </div>
          </div>

          <!-- Umat 4 -->
          <div style="background: white; padding: 1.5rem; border: 1px solid #e2e8f0; box-shadow: var(--shadow-sm); transition: all 0.2s;" onmouseover="this.style.borderColor='var(--brown-300)'; this.style.boxShadow='var(--shadow-md)'" onmouseout="this.style.borderColor='#e2e8f0'; this.style.boxShadow='var(--shadow-sm)'">
            <div style="display: flex; align-items: flex-start; gap: 1rem; margin-bottom: 1rem;">
              <div style="width: 3rem; height: 3rem; background-color: var(--brown-50); color: var(--brown-600); display: flex; align-items: center; justify-content: center; flex-shrink: 0;">
                <i data-lucide="user-circle-2" style="width: 1.75rem; height: 1.75rem;"></i>
              </div>
              <div>
                <h3 style="font-weight: 700; color: #1e293b; font-size: 1.125rem; margin: 0 0 0.25rem 0; line-height: 1.2;">Rina Santoso</h3>
                <div style="display: flex; align-items: center; gap: 0.5rem; margin-bottom: 0.5rem;">
                  <span style="background-color: #f1f5f9; color: #475569; font-size: 0.625rem; font-weight: 700; padding: 0.125rem 0.5rem; text-transform: uppercase; letter-spacing: 0.05em;">Anak</span>
                  <span style="font-size: 0.625rem; font-family: monospace; font-weight: 500; color: var(--brown-700); background-color: var(--brown-50); padding: 0.125rem 0.5rem; border: 1px solid var(--brown-100);">UMT-004</span>
                </div>
              </div>
            </div>
            <div style="display: flex; flex-direction: column; gap: 0.75rem; padding-top: 1rem; border-top: 1px solid #f1f5f9;">
              <div style="display: flex; align-items: center; gap: 0.75rem; font-size: 0.875rem; color: #475569;">
                <i data-lucide="briefcase" style="width: 1rem; height: 1rem; color: #94a3b8; flex-shrink: 0;"></i> <span>Pelajar</span>
              </div>
              <div style="display: flex; align-items: center; gap: 0.75rem; font-size: 0.875rem; color: #475569;">
                <i data-lucide="graduation-cap" style="width: 1rem; height: 1rem; color: #94a3b8; flex-shrink: 0;"></i> <span>SD</span>
              </div>
              <div style="display: flex; align-items: center; gap: 0.75rem; font-size: 0.875rem; color: #475569;">
                <i data-lucide="activity" style="width: 1rem; height: 1rem; color: #94a3b8; flex-shrink: 0;"></i> <span>Kesehatan: <span style="font-weight: 500; color: #1e293b;">Sehat</span></span>
              </div>
            </div>
          </div>

        </div>
      </div>

      <!-- GPS LOCATION MAP -->
      <div style="display: flex; flex-direction: column; gap: 1.5rem;">
        <h2 style="font-size: 1.5rem; font-weight: 800; color: #1e293b; display: flex; align-items: center; gap: 0.75rem; margin: 0;">
          <i data-lucide="map-pin" style="width: 1.5rem; height: 1.5rem; color: var(--brown-600);"></i> Titik Lokasi GPS
        </h2>
        
        <div style="background: white; box-shadow: var(--shadow-sm); border: 1px solid #e2e8f0; height: 400px; display: flex; flex-direction: column; overflow: hidden;">
          <div style="flex: 1; display: flex; flex-direction: column; items-center; justify-content: center; padding: 2rem; text-align: center; background-color: #f8fafc; position: relative;">
            <div style="position: absolute; inset: 0; background-image: radial-gradient(#cbd5e1 1px, transparent 1px); background-size: 20px 20px; opacity: 0.5;"></div>
            <i data-lucide="map-pin" style="width: 3rem; height: 3rem; color: var(--brown-500); margin: 0 auto 0.75rem; position: relative; z-index: 10;"></i>
            <h4 style="font-weight: 700; color: #334155; margin: 0 0 0.25rem 0; position: relative; z-index: 10;">Lokasi Ditemukan</h4>
            <p style="font-size: 0.875rem; color: #64748b; margin: 0; position: relative; z-index: 10;">Lokasi keluarga telah dipetakan oleh KBG.</p>
          </div>
          <div style="padding: 1rem; background: white; border-top: 1px solid #f1f5f9; display: flex; items-center; justify-content: space-between;">
            <div style="font-size: 0.75rem; font-family: monospace; color: #64748b;">
              -4.549210, 136.883921
            </div>
            <a href="#" style="font-size: 0.75rem; font-weight: 700; color: #2563eb; text-decoration: none; transition: color 0.2s;" onmouseover="this.style.color='#1e40af'" onmouseout="this.style.color='#2563eb'">
              Buka di Google Maps &rarr;
            </a>
          </div>
        </div>
      </div>

    </div>
  </main>

  <script>
    lucide.createIcons();
  </script>
</body>
</html>
"""

with open(r"C:\Users\ASUS\Documents\gthub\simatika-demo\keluargadetail.html", 'w', encoding='utf-8') as f:
    f.write(html_content)
    
print("Created keluargadetail.html")
