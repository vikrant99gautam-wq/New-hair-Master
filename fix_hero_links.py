import re, glob

def process_file(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

    # First, a blanket replace for any `#why-choose-us` references
    content = content.replace('href="#why-choose-us"', 'href="why-choose-us.html"')
    content = content.replace("href='#why-choose-us'", 'href="why-choose-us.html"')

    # Regex to capture the whole <a> tag, its attributes, and its inner text.
    # Group 1: <a ... up to href
    # Group 2: the current href value (e.g. #)
    # Group 3: ... the rest of the opening tag >
    # Group 4: the inner html
    # Group 5: </a>
    pattern = re.compile(r'(<a\s+[^>]*?href=")([^"]*)("[^>]*>)(.*?)(</a>)', re.IGNORECASE | re.DOTALL)

    def replacer(match):
        prefix = match.group(1)
        current_href = match.group(2)
        mid = match.group(3)
        inner_text = match.group(4)
        end = match.group(5)
        
        inner_upper = inner_text.upper()
        
        new_href = current_href
        
        if "BOOK" in inner_upper or "APPOINTMENT" in inner_upper:
            new_href = "contact.html"
        elif "WHY CHOOSE" in inner_upper:
            new_href = "why-choose-us.html"
            
        return prefix + new_href + mid + inner_text + end

    new_content = pattern.sub(replacer, content)

    if new_content != content:
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated links in {filename}")

for f in glob.glob('*.html'):
    process_file(f)
