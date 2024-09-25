INDEX_BASE = 'index-base.html'
INDEX_OUT = 'index.html'

with open(INDEX_BASE, 'r') as f:
    content = f.read()

def add_to_head(s):
    global content
    content = content.replace('</head>', f'{s}\n</head>')

def add_to_body(s):
    global content
    content = content.replace('</body>', f'{s}\n</body>')

def replace_text(old, new):
    global content
    content = content.replace(old, new)

# general fixes
add_to_head('<title>Teamboarding - Revolutionize your Technical Onboarding Process</title>')
add_to_head("""<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:ital,opsz,wght@0,14..32,100..900;1,14..32,100..900&display=swap" rel="stylesheet">""")
add_to_head('<meta name="description" content="Simplify and enhance your onboarding experience, ensuring every new team member is set up for success from day one.">')
replace_text('<div class="text-wrapper">', '<div class="text-wrapper" style="line-height: 10px;">')
replace_text('<div class="frame-62">', '<div class="frame-62" style="width: 545px;">')
replace_text('<input class="input-2" placeholder="Fullname" type="text" />', '<input class="input-2" placeholder="Fullname" name="fullname" style="color: #000;" type="text" />')
replace_text('<div class="input-4"><div class="text-wrapper-59">Company</div></div>', '<input class="input-2" placeholder="Company" name="company" style="color: #000;" type="text">')
replace_text('<input class="input-5" placeholder="Company Email" type="email" />', '<input class="input-5" placeholder="Company Email" name="email" style="color: #000;" type="email" />')
replace_text('<div class="link-2">', '<div class="link-2" style="padding: 12px 24px; cursor: pointer;">')
replace_text('<img class="laptop-table-looks-2" src="img/laptop-table-looks-pretty-darkness-1-1.png" />', '<img class="laptop-table-looks-2" src="img/laptop-table-looks-pretty-darkness-1-1.png" style="width: 100%;" />')

# add floating buttons
add_to_head('<link rel="stylesheet" href="floating-buttons-style.css" />')
add_to_body("""
    <div class="floating-buttons" style="display: none;">
      <div class="frame-wrapper">
        <div class="div">
          <a class="link"><div class="text-wrapper">Start for free</div></a>
          <div class="text-wrapper-2">or</div>
          <a class="div-wrapper"><div class="text-wrapper-3">Get a demo</div></a>
        </div>
      </div>
    </div>
    <script type="text/javascript">
      const floatingButtons = document.querySelector('.floating-buttons');
      window.onscroll = function() {
        if (window.pageYOffset > 600) {
          floatingButtons.style.display = 'inline-flex';
        } else {
          floatingButtons.style.display = 'none';
        }
      };
    </script>
""")


with open(INDEX_OUT, 'w') as f:
    f.write(content)
