import re, glob

for f in glob.glob('*.html'):
    try:
        content = open(f, encoding='utf-8').read()
        new_content = re.sub(r'href="tel:[^"]+"', 'href="tel:+918818980001"', content)
        if new_content != content:
            open(f, 'w', encoding='utf-8').write(new_content)
            print(f"Updated phone number in {f}")
    except Exception as e:
        print(f"Error: {e}")
