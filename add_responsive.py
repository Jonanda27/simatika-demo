import os

css_path = r"C:\Users\ASUS\Documents\gthub\simatika-demo\css\style.css"

responsive_css = """
/* Responsive Grid & Utility Classes */
.grid { display: grid; }
.grid-cols-1 { grid-template-columns: repeat(1, minmax(0, 1fr)); }
.grid-cols-2 { grid-template-columns: repeat(2, minmax(0, 1fr)); }
.grid-cols-3 { grid-template-columns: repeat(3, minmax(0, 1fr)); }
.grid-cols-4 { grid-template-columns: repeat(4, minmax(0, 1fr)); }

.hidden { display: none !important; }
.block { display: block; }
.inline-block { display: inline-block; }

/* Text Sizing */
.text-xs { font-size: 0.75rem; }
.text-sm { font-size: 0.875rem; }
.text-base { font-size: 1rem; }
.text-lg { font-size: 1.125rem; }
.text-xl { font-size: 1.25rem; }
.text-2xl { font-size: 1.5rem; }
.text-3xl { font-size: 1.875rem; }
.text-4xl { font-size: 2.25rem; }
.text-5xl { font-size: 3rem; }
.text-6xl { font-size: 3.75rem; }
.text-7xl { font-size: 4.5rem; }

/* Desktop Hero adjustments */
.hero-title { font-size: 3rem; line-height: 1.1; font-weight: 800; margin-bottom: 1.5rem; }

/* Responsive Breakpoints */
@media (min-width: 640px) {
  .sm\\:grid-cols-2 { grid-template-columns: repeat(2, minmax(0, 1fr)); }
  .sm\\:flex-row { flex-direction: row; }
  .sm\\:hidden { display: none !important; }
  .sm\\:block { display: block !important; }
  .sm\\:flex { display: flex !important; }
  .sm\\:text-6xl { font-size: 3.75rem; }
  
  .hero-title { font-size: 3.75rem; }
}

@media (min-width: 768px) {
  .md\\:grid-cols-2 { grid-template-columns: repeat(2, minmax(0, 1fr)); }
  .md\\:grid-cols-3 { grid-template-columns: repeat(3, minmax(0, 1fr)); }
  .md\\:grid-cols-4 { grid-template-columns: repeat(4, minmax(0, 1fr)); }
  .md\\:block { display: block !important; }
  .md\\:hidden { display: none !important; }
  .md\\:flex { display: flex !important; }
  .md\\:text-7xl { font-size: 4.5rem; }
  
  .hero-title { font-size: 4.5rem; }
}

@media (min-width: 1024px) {
  .lg\\:grid-cols-2 { grid-template-columns: repeat(2, minmax(0, 1fr)); }
  .lg\\:grid-cols-3 { grid-template-columns: repeat(3, minmax(0, 1fr)); }
  .lg\\:grid-cols-4 { grid-template-columns: repeat(4, minmax(0, 1fr)); }
  .lg\\:block { display: block !important; }
  .lg\\:hidden { display: none !important; }
  .lg\\:flex { display: flex !important; }
}

/* Ensure images scale down */
img {
  max-width: 100%;
  height: auto;
}

/* Adjust padding on small devices */
@media (max-width: 639px) {
  .px-6 { padding-left: 1rem; padding-right: 1rem; }
  .py-12 { padding-top: 2rem; padding-bottom: 2rem; }
  .pt-36 { padding-top: 6rem; }
  .gap-16 { gap: 2rem; }
  .gap-8 { gap: 1.5rem; }
  .text-3xl { font-size: 2rem; }
  .hero-pills-container { display: none; } /* Hide complex hero pills on very small screens to save space */
  .carousel-item { width: 85vw; min-width: 280px; }
  .search-input-wrapper { flex-direction: column; }
  .search-input-wrapper .btn-black { width: 100%; margin-top: 0.5rem; }
}
"""

with open(css_path, 'r', encoding='utf-8') as f:
    content = f.read()

if "/* Responsive Grid & Utility Classes */" not in content:
    with open(css_path, 'a', encoding='utf-8') as f:
        f.write("\n" + responsive_css)
    print("Responsive classes added.")
else:
    print("Responsive classes already exist.")
