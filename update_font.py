import os
import re
import glob

dir_path = r"C:\Users\ASUS\Documents\gthub\simatika-demo"

# CSS files
css_files = glob.glob(os.path.join(dir_path, "css", "*.css"))
html_files = glob.glob(os.path.join(dir_path, "*.html"))

files_to_process = css_files + html_files

for filepath in files_to_process:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 1. Replace google fonts URL
    new_content = re.sub(r'family=Inter:wght@400;500;600;700;800&display=swap', r'family=Roboto:wght@400;500;700;900&display=swap', content)
    
    # 2. Replace 'Inter' with 'Roboto'
    new_content = new_content.replace("'Inter'", "'Roboto'")
    new_content = new_content.replace('"Inter"', '"Roboto"')
    new_content = new_content.replace('Inter,', 'Roboto,')
    
    if new_content != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated {os.path.basename(filepath)}")
