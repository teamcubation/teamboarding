import re

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
    if old not in content:
        raise Exception(f'Text "{old}" not found in {INDEX_BASE}')
    content = content.replace(old, new)

def replace_text_regex(old, new):
    global content
    content = re.sub(old, new, content)

# general fixes
add_to_head('<title>Teamboarding - Revolutionize your Technical Onboarding Process</title>')
add_to_head("""<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:ital,opsz,wght@0,14..32,100..900;1,14..32,100..900&display=swap" rel="stylesheet">""")
add_to_head('<meta name="description" content="Simplify and enhance your onboarding experience, ensuring every new team member is set up for success from day one.">')
replace_text('<div class="frame-58">', '<div class="frame-58" style="width: 545px;">')
replace_text('<input class="input-2" placeholder="Fullname" type="text" />', '<input class="input-2" placeholder="Fullname" name="fullname" style="color: #000;" type="text" />')
replace_text('<div class="input-4"><div class="text-wrapper-58">Company</div></div>', '<input class="input-2" placeholder="Company" name="company" style="color: #000;" type="text">')
replace_text('<input class="input-5" placeholder="Company Email" type="email" />', '<input class="input-5" placeholder="Company Email" name="email" style="color: #000;" type="email" />')
replace_text('<div class="link-2">', '<div class="link-2" style="padding: 12px 24px; cursor: pointer;">')
replace_text('<img class="laptop-table-looks-2" src="img/laptop-table-looks-pretty-darkness-1-1.png" />', '<img class="laptop-table-looks-2" src="img/laptop-table-looks-pretty-darkness-1-1.png" style="width: 100%;" />')
replace_text('<div class="title-with-emoji">', '<div class="title-with-emoji" style="width: auto;">')
replace_text('<span class="text-wrapper-4">&nbsp;</span>', '')
replace_text('<img class="img" src="img/frame-276-2.png" />', '')
replace_text('<div class="chips-4">', '<div class="chips-4" style="padding: 3px 6.25px;">')
replace_text('<div class="chips-5">', '<div class="chips-5" style="padding: 3px 6.25px;">')

# add floating buttons
add_to_head('<link rel="stylesheet" href="floating-buttons-style.css" />')
add_to_body("""
    <div class="floating-buttons" style="display: none;">
      <div class="frame-wrapper">
        <div class="div">
          <a class="link" href="#Start"><div class="text-wrapper">Start for free</div></a>
          <div class="text-wrapper-2">or</div>
          <a class="div-wrapper" onclick="showDemoDialog()"><div class="text-wrapper-3">Get a demo</div></a>
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

# add favicon
add_to_head("""<link rel="icon" href="static/favicon.ico">""")

# links
replace_text_regex(r'<div class="header-header-nav">(.*?)</div>', '<a class="header-header-nav" href="#\\1">\\1</a>')
replace_text_regex(r'<div class="header-header-nav-2">(.*?)</div>', '<a class="header-header-nav-2" href="#\\1">\\1</a>')
replace_text_regex(r'<div class="header-header-nav-3">(.*?)</div>', '<a class="header-header-nav-3" href="#\\1">\\1</a>')
replace_text_regex(r'<div class="header-header-nav-4">(.*?)</div>', '<a class="header-header-nav-4" href="#\\1">\\1</a>')
replace_text('<div class="frame-8">', '<div class="frame-8"><a name="About"></a>')
replace_text('<div class="section">', '<div class="section"><a name="Customers"></a>')
replace_text('<div class="frame-19">', '<a name="Features"></a><div class="frame-19">')
replace_text('<div class="overlap-group-3">', '<div class="overlap-group-3"><a name="Integrations"></a>')
replace_text('<div class="frame-67">', '<div class="frame-67"><a name="Benefits"></a>')
replace_text('<div class="text-wrapper">Sign in</div>', '<a style="line-height: 10px;" class="text-wrapper" href="https://app.teamcubation.com/login" target="_blank">Sign in</a>')
replace_text('<div class="text-wrapper">Talk to Sales</div>', '<a style="line-height: 10px;" class="text-wrapper" href="https://calendly.com/natalia-perez-tq/teamboarding-talk-to-sales" target="_blank">Talk to Sales</a>')
replace_text('<div class="section-2"', '<a name="Start"></a><div class="section-2"')
replace_text('<div class="link"><div class="text-wrapper-3">Start for free</div></div>', '<a class="link" href="#Start"><div class="text-wrapper-3">Start for free</div></a>')
replace_text('<span class="text-wrapper-5">Get a demo</span>', '<a class="text-wrapper-5" style="cursor: pointer;" onclick="showDemoDialog()">Get a demo</a>')
replace_text("""<p class="privacy-policy-terms">
              Privacy Policy&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Terms &amp; Conditions
            </p>""",
             """<p class="privacy-policy-terms">
              <a href="https://teamcubation.com/privacy-policy.html" target="_blank" style="color: var(--tokens-text-secondary);">Privacy Policy</a>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <a href="https://teamcubation.com/terms.html" target="_blank" style="color: var(--tokens-text-secondary);">Terms &amp; Conditions</a>
            </p>""")

# demo dialog
add_to_head('<link rel="stylesheet" href="demo-dialog-style.css" />')
add_to_head('<script src="static/scripts.js"></script>')
add_to_body("""<div class="demo-dialog-container" style="display: none;">
      <div class="overlay" onclick="hideDemoDialog()"></div>
      <div class="demo-dialog">
        <img class="demo-dialog-image" src="img/shot-two-smart-business-women-working-together-with-computer-digital-tablet-while-talking-office%201.png" />
        <div class="content">
          <div class="title">
            <div class="text-wrapper">Get a Demo</div>
            <p class="div">The demo includes a test user with dummy data so you can navigate and try out Teamboarding.</p>
          </div>
          <div class="div-2">
            <div class="form">
              <div class="div-2">
                <div class="input">
                  <label class="label" for="demo-name">FULL NAME</label>
                  <input class="input-2" placeholder="Enter your full name" type="text" id="demo-name" name="demo-name" />
                </div>
                <div class="input">
                  <label class="label" for="demo-email">COMPANY EMAIL</label>
                  <input class="input-2" placeholder="Enter your company email" type="email" id="demo-email" name="demo-email" />
                </div>
              </div>
            </div>
            <div class="frame">
              <a class="link" onclick="demoDialogOk()"><div class="text-wrapper-2">Let’s go</div></a>
              <p class="p">By filling out this form and clicking submit, you acknowledge our privacy policy.</p>
            </div>
          </div>
        </div>
        <div class="content-ok" style="display: none;">
          <div class="title">
            <img class="icon" src="img/icon-ok.png" />
            <div class="text-wrapper">Request received</div>
            <p class="thank-you-for-your">
              Thank you for your interest! We&#39;ve received your request and will send you an email soon with all the
              information you need to get started. We&#39;ll be in touch shortly, so keep an eye on your inbox!
            </p>
          </div>
        </div>
      </div>
    </div>
""")

with open(INDEX_OUT, 'w') as f:
    f.write(content)
