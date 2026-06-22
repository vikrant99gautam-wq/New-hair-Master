import re, glob

pattern = re.compile(r'<div class="([^"]*)">\s*New hair Master\s*</div>', re.IGNORECASE)

for f in glob.glob('*.html'):
    try:
        content = open(f, encoding='utf-8').read()
        
        def repl(m):
            cls = m.group(1)
            # Add a slight hover effect if desired, or just use the same class
            return f'<a href="index.html" class="{cls} hover:opacity-80 transition-opacity cursor-pointer">New hair Master</a>'
            
        new_content, count = pattern.subn(repl, content)
        
        if count > 0:
            open(f, 'w', encoding='utf-8').write(new_content)
            print(f"Updated {count} logo(s) in {f}")
        else:
            print(f"No logo found in {f}")
            
    except Exception as e:
        print(f"Error on {f}: {e}")
