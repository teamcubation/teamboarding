INDEX_BASE = 'index-base.html'
INDEX_OUT = 'index.html'

def read_base():
    with open(INDEX_BASE, 'r') as f:
        content = f.read()
    return content

def write_out(content):
    with open(INDEX_OUT, 'w') as f:
        f.write(content)

def add_to_head(content, s):
    return content.replace('</head>', f'{s}\n</head>')

def replace_text(content, old, new):
    return content.replace(old, new)

content = read_base()

content = add_to_head(content, '<title>Teamboarding - Revolutionize your Technical Onboarding Process</title>')
content = add_to_head(content, """<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:ital,opsz,wght@0,14..32,100..900;1,14..32,100..900&display=swap" rel="stylesheet">""")
content = replace_text(content, '<div class="text-wrapper">', '<div class="text-wrapper" style="line-height: 10px;">')
content = replace_text(content, '<div class="frame-62">', '<div class="frame-62" style="width: 545px;">')
content = replace_text(content, '<input class="input-2" placeholder="Fullname" type="text" />', '<input class="input-2" placeholder="Fullname" name="fullname" style="color: #000;" type="text" />')
content = replace_text(content, '<div class="input-4"><div class="text-wrapper-59">Company</div></div>', '<input class="input-2" placeholder="Company" name="company" style="color: #000;" type="text">')
content = replace_text(content, '<input class="input-5" placeholder="Company Email" type="email" />', '<input class="input-5" placeholder="Company Email" name="email" style="color: #000;" type="email" />')
content = replace_text(content, '<div class="link-2">', '<div class="link-2" style="padding: 12px 24px; cursor: pointer;">')

write_out(content)

