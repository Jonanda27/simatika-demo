import re
import os

files = [
    'css/style.css',
    'css/layout.css',
    'index.html',
    'login.html',
    'semuadata.html',
    'datakeluarga.html'
]

for file in files:
    if not os.path.exists(file):
        continue
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # regex to find border-radius: <value>; and replace with border-radius: 0;
    # but exclude border-radius: 50% for circles (like the ambient splash or icons if any)
    def replace_radius(match):
        val = match.group(1)
        if '50%' in val:
            return match.group(0) # Keep circles
        return 'border-radius: 0;'
        
    new_content = re.sub(r'border-radius\s*:\s*([^;>]+);', replace_radius, content)
    
    # also replace inline border-radius="0.5rem" or similar
    def replace_inline_radius(match):
        val = match.group(1)
        if '50%' in val:
            return match.group(0)
        return 'border-radius="0"'
    
    # replace javascript btn.style.borderRadius = '0.375rem';
    new_content = re.sub(r"btn\.style\.borderRadius\s*=\s*'[^']+';", "btn.style.borderRadius = '0';", new_content)
    
    # write back
    with open(file, 'w', encoding='utf-8') as f:
        f.write(new_content)
        
print("Updated border-radius to 0 for all components.")
