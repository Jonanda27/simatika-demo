// js/app.js

document.addEventListener('DOMContentLoaded', () => {
  // --- Header Scroll Effect ---
  const header = document.getElementById('main-header');
  window.addEventListener('scroll', () => {
    if (window.scrollY > 50) {
      header.classList.add('scrolled');
    } else {
      header.classList.remove('scrolled');
    }
  });

  // --- Carousel Drag to Scroll ---
  const carousel = document.getElementById('features-carousel');
  let isDown = false;
  let startX;
  let scrollLeft;

  carousel.addEventListener('mousedown', (e) => {
    isDown = true;
    carousel.classList.add('active');
    startX = e.pageX - carousel.offsetLeft;
    scrollLeft = carousel.scrollLeft;
  });
  carousel.addEventListener('mouseleave', () => {
    isDown = false;
    carousel.classList.remove('active');
  });
  carousel.addEventListener('mouseup', () => {
    isDown = false;
    carousel.classList.remove('active');
  });
  carousel.addEventListener('mousemove', (e) => {
    if (!isDown) return;
    e.preventDefault();
    const x = e.pageX - carousel.offsetLeft;
    const walk = (x - startX) * 1.5; // Scroll speed
    carousel.scrollLeft = scrollLeft - walk;
  });

  // --- Search Functionality ---
  const searchForm = document.getElementById('search-form');
  const searchInput = document.getElementById('search-query');
  const searchResults = document.getElementById('search-results');

  searchForm.addEventListener('submit', async (e) => {
    e.preventDefault();
    const query = searchInput.value.trim();
    if (!query) return;

    // Show Loading
    searchResults.innerHTML = `
      <div style="display:flex; flex-direction:column; items-center; justify-content:center; padding:3rem; color:var(--brown-600);">
        <div style="width:3rem; height:3rem; border:4px solid var(--brown-200); border-top-color:var(--brown-600); border-radius:50%; animation:spin 1s linear infinite; margin-bottom:1rem; margin-left:auto; margin-right:auto;"></div>
        <p style="font-weight:700; font-size:1.125rem; text-align:center;">Mencari data ke database pusat...</p>
      </div>
      <style>@keyframes spin { 0% { transform: rotate(0deg); } 100% { transform: rotate(360deg); } }</style>
    `;

    try {
      // Menggunakan data langsung (embedded) untuk mencegah error saat membuka via file://
      const data = [
        {
          "no_kk_paroki": "91010123560001",
          "kode_unik_keluarga": "12356",
          "status_numpang": "Keluarga Utama",
          "status_rumah": "Milik Sendiri",
          "Umats": [
            {
              "nama_lengkap": "Bpk. Budi Santoso",
              "nomor_induk_umat": "UMT-001",
              "jenis_kelamin": "L",
              "status_dalam_keluarga": "Kepala Keluarga"
            },
            {
              "nama_lengkap": "Ibu Siti Aminah",
              "nomor_induk_umat": "UMT-002",
              "jenis_kelamin": "P",
              "status_dalam_keluarga": "Istri"
            },
            {
              "nama_lengkap": "Andi Santoso",
              "nomor_induk_umat": "UMT-003",
              "jenis_kelamin": "L",
              "status_dalam_keluarga": "Anak"
            },
            {
              "nama_lengkap": "Rina Santoso",
              "nomor_induk_umat": "UMT-004",
              "jenis_kelamin": "P",
              "status_dalam_keluarga": "Anak"
            }
          ]
        }
      ];
      
      // Simulate network delay
      setTimeout(() => {
        // Search logic
        const result = data.find(item => 
          item.no_kk_paroki === query || 
          item.kode_unik_keluarga === query || 
          item.Umats.some(u => u.nomor_induk_umat === query)
        );

        if (result) {
          renderResult(result);
        } else {
          renderNotFound(query);
        }
      }, 1000);

    } catch (error) {
      console.error("Error fetching dummy data:", error);
      searchResults.innerHTML = `<p style="color:red;">Terjadi kesalahan saat mengambil data.</p>`;
    }
  });

  function renderNotFound(query) {
    searchResults.innerHTML = `
      <div class="result-card" style="max-width:42rem; background-color:rgba(255, 228, 230, 0.5); padding:2.5rem; text-align:center; border:1px solid #ffe4e6; border-radius:0;">
        <div style="width:4rem; height:4rem; background-color:#ffe4e6; display:flex; align-items:center; justify-content:center; color:#f43f5e; margin:0 auto 1.5rem auto;">
          <i data-lucide="x" style="width:2rem; height:2rem;"></i>
        </div>
        <h3 style="font-size:1.5rem; font-weight:700; color:var(--text-slate-800); margin-bottom:0.75rem;">Data Tidak Ditemukan</h3>
        <p style="color:var(--text-slate-600); font-weight:500; line-height:1.625;">
          Kami tidak menemukan data dengan Nomor/Kode <span style="font-weight:700; color:var(--text-slate-800);">"${query}"</span>. 
          Jika Anda merasa ini keliru, segera hubungi Ketua KBG Anda untuk melakukan pendataan ulang atau sinkronisasi.
        </p>
      </div>
    `;
    lucide.createIcons();
  }

  function renderResult(result) {
    const umatsHtml = result.Umats.map(umat => `
      <div style="display:flex; align-items:center; justify-content:space-between; padding:1.25rem; border:1px solid #e2e8f0; background:white; transition:all 0.3s;" class="umat-card">
        <div style="display:flex; align-items:center; gap:1rem;">
          <div style="width:3rem; height:3rem; background-color:#f8fafc; display:flex; align-items:center; justify-content:center; color:var(--text-slate-400);">
            <i data-lucide="user-circle-2" style="width:1.75rem; height:1.75rem;"></i>
          </div>
          <div>
            <p style="font-weight:700; color:var(--text-slate-800); font-size:1.125rem; margin-bottom:0.125rem;">${umat.nama_lengkap}</p>
            <div style="font-size:0.6875rem; font-family:monospace; font-weight:500; color:var(--brown-600); background:var(--brown-50); padding:0.125rem 0.5rem; display:inline-block; margin-bottom:0.375rem; border:1px solid var(--brown-100);">
              Kode Umat: ${umat.nomor_induk_umat || '-'}
            </div>
            <div style="display:flex; align-items:center; gap:0.5rem;">
              <span style="font-size:0.75rem; font-weight:600; color:var(--text-slate-500); text-transform:uppercase;">
                ${umat.jenis_kelamin === 'L' ? 'Laki-laki' : 'Perempuan'}
              </span>
              <span style="width:4px; height:4px; background-color:#cbd5e1;"></span>
              <span style="font-size:0.75rem; font-weight:700; color:var(--brown-600); text-transform:uppercase; background:var(--brown-50); padding:0.125rem 0.5rem;">
                ${umat.status_dalam_keluarga || "-"}
              </span>
            </div>
          </div>
        </div>
      </div>
    `).join('');

    searchResults.innerHTML = `
      <div class="result-card">
        <!-- Header -->
        <div class="result-header">
          <div style="position:absolute; right:0; top:0; width:16rem; height:16rem; background:rgba(255,255,255,0.05); border-radius:50%; filter:blur(24px); transform:translate(50%, -50%);"></div>
          <div style="position:relative; z-index:10;">
            <div style="display:flex; align-items:center; gap:0.5rem; margin-bottom:0.5rem;">
              <div style="background-color:#22c55e; color:white; font-size:0.625rem; font-weight:700; padding:0.25rem 0.5rem; text-transform:uppercase; letter-spacing:0.05em; display:flex; align-items:center; gap:0.25rem;">
                <i data-lucide="check-circle-2" style="width:0.75rem; height:0.75rem;"></i> Terverifikasi
              </div>
            </div>
            <h3 style="font-size:1.875rem; font-weight:800; color:white; margin-bottom:0.25rem;">Keluarga Terdaftar</h3>
            <p style="color:#cbd5e1; font-weight:500; font-family:monospace; font-size:1.125rem; opacity:0.8;">
              No. KK: ${result.no_kk_paroki || '-'}
            </p>
            <p style="color:#94a3b8; font-weight:500; font-family:monospace; font-size:0.875rem; margin-top:0.25rem;">
              Kode Keluarga: ${result.kode_unik_keluarga || '-'}
            </p>
          </div>
          <div style="width:4rem; height:4rem; background:rgba(255,255,255,0.1); backdrop-filter:blur(10px); border:1px solid rgba(255,255,255,0.2); display:flex; align-items:center; justify-content:center; position:relative; z-index:10;">
            <i data-lucide="shield-check" style="width:2rem; height:2rem; color:white;"></i>
          </div>
        </div>

        <!-- Details -->
        <div style="padding:2rem 2.5rem;">
          <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(200px, 1fr)); gap:1.5rem; margin-bottom:2.5rem;">
            <div style="background:#f8fafc; padding:1.25rem; border:1px solid #f1f5f9; display:flex; align-items:center; gap:1rem;">
              <div style="width:3rem; height:3rem; background:white; box-shadow:var(--shadow-sm); display:flex; align-items:center; justify-content:center; color:var(--brown-600); flex-shrink:0;">
                <i data-lucide="map-pin"></i>
              </div>
              <div>
                <p style="font-size:0.75rem; font-weight:700; color:var(--text-slate-400); text-transform:uppercase; margin-bottom:0.125rem;">Status Tempat Tinggal</p>
                <p style="color:var(--text-slate-800); font-weight:700; font-size:1.125rem;">${result.status_numpang || "Keluarga Utama"}</p>
              </div>
            </div>
            <div style="background:#f8fafc; padding:1.25rem; border:1px solid #f1f5f9; display:flex; align-items:center; gap:1rem;">
              <div style="width:3rem; height:3rem; background:white; box-shadow:var(--shadow-sm); display:flex; align-items:center; justify-content:center; color:var(--brown-600); flex-shrink:0;">
                <i data-lucide="map-pin"></i>
              </div>
              <div>
                <p style="font-size:0.75rem; font-weight:700; color:var(--text-slate-400); text-transform:uppercase; margin-bottom:0.125rem;">Status Kepemilikan Rumah</p>
                <p style="color:var(--text-slate-800); font-weight:700; font-size:1.125rem;">${result.status_rumah || "Milik Sendiri"}</p>
              </div>
            </div>
          </div>

          <!-- Umats -->
          <div>
            <div style="display:flex; align-items:center; justify-content:space-between; margin-bottom:1.5rem; padding-bottom:1rem; border-bottom:1px solid #f1f5f9;">
              <h4 style="font-size:1.25rem; font-weight:700; color:var(--text-slate-800); display:flex; align-items:center; gap:0.5rem;">
                <i data-lucide="users" style="width:1.5rem; height:1.5rem; color:var(--text-slate-400);"></i>
                Daftar Anggota Keluarga
              </h4>
              <span style="background:var(--brown-100); color:var(--brown-800); font-size:0.875rem; font-weight:700; padding:0.375rem 1rem;">
                ${result.Umats.length} Orang
              </span>
            </div>

            <style>
              .members-grid { display: grid; grid-template-columns: 1fr; gap: 1rem; }
              @media (min-width: 768px) { .members-grid { grid-template-columns: repeat(2, 1fr); } }
            </style>
            <div class="members-grid">
              ${umatsHtml}
            </div>

            <div style="margin-top:2rem; padding-top:1.5rem; border-top:1px solid #f1f5f9; display:flex; justify-content:flex-end;">
              <button class="btn btn-black" style="box-shadow:var(--shadow-md);" onclick="window.location.href='keluargadetail.html'">
                Lihat Detail Lengkap
                <i data-lucide="arrow-right" style="width:1.25rem; height:1.25rem; margin-left:0.5rem;"></i>
              </button>
            </div>
          </div>
        </div>
      </div>
    `;
    lucide.createIcons();
    
    // Add hover effects for dynamically created cards
    document.querySelectorAll('.umat-card').forEach(card => {
      card.addEventListener('mouseenter', () => {
        card.style.borderColor = 'var(--brown-400)';
        card.style.boxShadow = 'var(--shadow-md)';
        card.querySelector('.lucide-user-circle-2').style.color = 'var(--brown-600)';
        card.firstElementChild.firstElementChild.style.backgroundColor = 'var(--brown-50)';
      });
      card.addEventListener('mouseleave', () => {
        card.style.borderColor = '#e2e8f0';
        card.style.boxShadow = 'none';
        card.querySelector('.lucide-user-circle-2').style.color = 'var(--text-slate-400)';
        card.firstElementChild.firstElementChild.style.backgroundColor = '#f8fafc';
      });
    });
  }
});
