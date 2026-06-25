import os

files = [
    'stasi_pengurus.html',
    'stasi_sakramen.html',
    'stasi_mutasi.html',
    'stasi_aktivitas.html',
    'paroki_pengurus.html',
    'paroki_sakramen.html',
    'paroki_mutasi.html',
    'paroki_aktivitas.html'
]

for file in files:
    if not os.path.exists(file):
        print(f"Skipping {file}, does not exist")
        continue
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # replace the padding and max-width in .content-area
    new_content = content.replace("padding: 1.5rem;", "padding: 2rem;")
    new_content = new_content.replace("max-width: 72rem; /* max-w-6xl */", "max-width: 80rem; /* max-w-7xl */")
    
    if new_content != content:
        with open(file, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated padding and width in {file}")
    else:
        print(f"No changes made to {file}")
