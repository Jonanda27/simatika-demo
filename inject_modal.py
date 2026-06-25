import re

def inject_modal(target_file):
    with open(target_file, 'r', encoding='utf-8') as f:
        content = f.read()

    if "MODAL DETAIL UMAT" in content or "modal-overlay" in content:
        print(f"Modal already exists in {target_file}")
        return

    # Extract components from stasi_dataumat.html
    with open('stasi_dataumat.html', 'r', encoding='utf-8') as f:
        stasi_content = f.read()

    # Extract CSS
    css_match = re.search(r'(/\* Modal Overlay \*/.*?\/\* Table specifics \*/.*?)(?=\s*</style>)', stasi_content, re.DOTALL)
    if not css_match:
        # Fallback if Table specifics comes before or after
        css_match = re.search(r'(/\* Table specifics \*/.*?\/\* Modal Overlay \*/.*?(?:}\s*}|;\s*}))(?=\s*</style>|\s*\w+\s*{)', stasi_content, re.DOTALL)
    
    # Simpler regex since we know lines 31-84 approximately
    css_start = stasi_content.find('/* Table specifics */')
    css_end = stasi_content.find('</style>')
    modal_css = stasi_content[css_start:css_end]

    # Extract HTML
    html_start = stasi_content.find('<!-- MODAL DETAIL UMAT -->')
    html_end = stasi_content.find('<script>', html_start)
    modal_html = stasi_content[html_start:html_end]

    # Extract JS
    js_start = stasi_content.find('// Modal Logic')
    js_end = stasi_content.find('</script>', js_start)
    modal_js = stasi_content[js_start:js_end]

    # Inject into target
    # 1. Inject CSS before </style>
    content = content.replace('</style>', '\n' + modal_css + '\n</style>')

    # 2. Inject HTML before <script> (first main script) or </body>
    content = content.replace('</body>', '\n' + modal_html + '\n</body>')

    # 3. Inject JS before </body> inside a script tag, or append to last script
    # It's safer to just replace </body> with the JS script block then </body>
    js_block = f"""
  <script>
    {modal_js}
  </script>
"""
    content = content.replace('</body>', js_block + '\n</body>')

    # 4. Replace alerts
    # In semuadata.html: onclick="alert('Membuka detail id: ${item.id}')"
    content = re.sub(r'onclick="alert\([^)]+\)"', 'onclick="openDetailModal()"', content)

    with open(target_file, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Updated {target_file}")

inject_modal('semuadata.html')
inject_modal('datakeluarga.html')
