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
<link href="https://fonts.googleapis.com/css2?family=Inter:ital,opsz,wght@0,14..32,100..900;1,14..32,100..900&display=swap" rel="stylesheet">
<link href="https://fonts.cdnfonts.com/css/satoshi?styles=135002,135000" rel="stylesheet">""")
add_to_head('<meta name="description" content="Simplify and enhance your onboarding experience, ensuring every new team member is set up for success from day one.">')
add_to_head('<meta name="viewport" content="width=device-width, initial-scale=1">')
add_to_head("""<!-- Hotjar Tracking Code for Landing teambaording -->
<script>
    (function(h,o,t,j,a,r){
        h.hj=h.hj||function(){(h.hj.q=h.hj.q||[]).push(arguments)};
        h._hjSettings={hjid:5153745,hjsv:6};
        a=o.getElementsByTagName('head')[0];
        r=o.createElement('script');r.async=1;
        r.src=t+h._hjSettings.hjid+j+h._hjSettings.hjsv;
        a.appendChild(r);
    })(window,document,'https://static.hotjar.com/c/hotjar-','.js?sv=');
</script>""")
add_to_head("""<!-- Mixpanel -->
<script type="text/javascript">
  (function (f, b) { if (!b.__SV) { var e, g, i, h; window.mixpanel = b; b._i = []; b.init = function (e, f, c) { function g(a, d) { var b = d.split("."); 2 == b.length && ((a = a[b[0]]), (d = b[1])); a[d] = function () { a.push([d].concat(Array.prototype.slice.call(arguments, 0))); }; } var a = b; "undefined" !== typeof c ? (a = b[c] = []) : (c = "mixpanel"); a.people = a.people || []; a.toString = function (a) { var d = "mixpanel"; "mixpanel" !== c && (d += "." + c); a || (d += " (stub)"); return d; }; a.people.toString = function () { return a.toString(1) + ".people (stub)"; }; i = "disable time_event track track_pageview track_links track_forms track_with_groups add_group set_group remove_group register register_once alias unregister identify name_tag set_config reset opt_in_tracking opt_out_tracking has_opted_in_tracking has_opted_out_tracking clear_opt_in_out_tracking start_batch_senders people.set people.set_once people.unset people.increment people.append people.union people.track_charge people.clear_charges people.delete_user people.remove".split( " "); for (h = 0; h < i.length; h++) g(a, i[h]); var j = "set set_once union unset remove delete".split(" "); a.get_group = function () { function b(c) { d[c] = function () { call2_args = arguments; call2 = [c].concat(Array.prototype.slice.call(call2_args, 0)); a.push([e, call2]); }; } for ( var d = {}, e = ["get_group"].concat( Array.prototype.slice.call(arguments, 0)), c = 0; c < j.length; c++) b(j[c]); return d; }; b._i.push([e, f, c]); }; b.__SV = 1.2; e = f.createElement("script"); e.type = "text/javascript"; e.async = !0; e.src = "undefined" !== typeof MIXPANEL_CUSTOM_LIB_URL ? MIXPANEL_CUSTOM_LIB_URL : "file:" === f.location.protocol && "//cdn.mxpnl.com/libs/mixpanel-2-latest.min.js".match(/^\/\//) ? "https://cdn.mxpnl.com/libs/mixpanel-2-latest.min.js" : "//cdn.mxpnl.com/libs/mixpanel-2-latest.min.js"; g = f.getElementsByTagName("script")[0]; g.parentNode.insertBefore(e, g); } })(document, window.mixpanel || []);
</script>""")
add_to_head("""<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id=AW-16722831487">
</script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());

  gtag('config', 'AW-16722831487');
</script>""")
add_to_head("""<script>function initApollo(){var n=Math.random().toString(36).substring(7),o=document.createElement("script");
o.src="https://assets.apollo.io/micro/website-tracker/tracker.iife.js?nocache="+n,o.async=!0,o.defer=!0,
o.onload=function(){window.trackingFunctions.onLoad({appId:"669817d6d1af0c01b288be3b"})},
document.head.appendChild(o)}initApollo();</script>""")
add_to_head("""<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-ZKJ6GFFR5L"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());

  gtag('config', 'G-ZKJ6GFFR5L');
</script>""")
add_to_head("""<script type="text/javascript">
    (function(c,l,a,r,i,t,y){
        c[a]=c[a]||function(){(c[a].q=c[a].q||[]).push(arguments)};
        t=l.createElement(r);t.async=1;t.src="https://www.clarity.ms/tag/"+i;
        y=l.getElementsByTagName(r)[0];y.parentNode.insertBefore(t,y);
    })(window, document, "clarity", "script", "obxut7ej7c");
</script>""")
add_to_head("""<script>
function gtag_report_conversion(url) {
  var callback = function () {
    if (typeof(url) != 'undefined') {
      window.location = url;
    }
  };
  gtag('event', 'conversion', {
      'send_to': 'AW-16722831487/UX4mCN6-ytgZEP_QiKY-',
      'event_callback': callback
  });
  return false;
}
</script>""")
replace_text('<body>', '<body style="overflow-x: hidden;">')
replace_text('<div class="frame-184">', '<div class="frame-184" style="width: 545px;">')
replace_text('<input class="input-2" placeholder="Fullname" type="text" />', '<input class="input-2" placeholder="Fullname" name="fullname" style="color: #000;" type="text" />')
replace_text('<div class="input-4"><div class="text-wrapper-57">Company</div></div>', '<input class="input-2" placeholder="Company" name="company" style="color: #000;" type="text">')
replace_text('<input class="input-5" placeholder="Company Email" type="email" />', '<input class="input-5" placeholder="Company Email" name="email" style="color: #000;" type="email" />')
replace_text('<div class="link-3">', '<div class="link-3 req-trial-button" style="padding: 12px 24px; cursor: pointer;">')
replace_text('<div class="link-2">', '<div class="link-2 req-trial-button" style="padding: 12px 24px; cursor: pointer;">')
replace_text('<img class="laptop-table-looks-6" src="img/laptop-table-looks-pretty-darkness-1-5.png" />', '<img class="laptop-table-looks-6" src="img/laptop-table-looks-pretty-darkness-1-5.png" style="width: 100%;" />')
replace_text('<img class="laptop-table-looks-4" src="img/laptop-table-looks-pretty-darkness-1-3.png" />', '<img class="laptop-table-looks-4" src="img/laptop-table-looks-pretty-darkness-1-3.png" style="width: 100%;" />')
replace_text('<img class="laptop-table-looks-2" src="img/laptop-table-looks-pretty-darkness-1-1.png" />', '<img class="laptop-table-looks-2" src="img/laptop-table-looks-pretty-darkness-1-1.png" style="width: 100%; height: 100%;" />')
replace_text('<div class="title-with-emoji">', '<div class="title-with-emoji" style="width: auto;">')
replace_text('<div class="title-with-emoji-2">', '<div class="title-with-emoji-2" style="width: auto;">')
replace_text('<div class="title-with-emoji-3">', '<div class="title-with-emoji-3" style="width: auto;">')
replace_text('<span class="text-wrapper-4">&nbsp;</span>', '')
replace_text('<img class="img-5" src="img/frame-276-20.png" />', '')
replace_text('<img class="img-5" src="img/frame-276-11.png" />', '')
replace_text('<img class="img-5" src="img/frame-276-10.png" />', '')
replace_text('<img class="img-5" src="img/frame-276.png" />', '')
replace_text('<img class="img-5" src="img/frame-276-2.png" />', '')
replace_text('<div class="chips-17">', '<div class="chips-17" style="padding: 5px 6.25px 2px;">')
replace_text('<div class="chips-18">', '<div class="chips-18" style="padding: 5px 6.25px 3px;">')
replace_text('<div class="chips-3">', '<div class="chips-3" style="padding: 4px 3.7px 1px;">')
replace_text('<div class="chips-4">', '<div class="chips-4" style="padding: 4px 3.7px 1px;">')
replace_text('<div class="chips-11">', '<div class="chips-11" style="padding: 4px 8.07px;">')
replace_text('<div class="chips-12">', '<div class="chips-12" style="padding: 4px 8.07px;">')
replace_text('<div class="container-wrapper-3">', '<div class="container-wrapper-3" style="width: 300px;">')
replace_text('<div class="container-wrapper-2">', '<div class="container-wrapper-2" style="width: 190px;">')
replace_text('<div class="container-wrapper">', '<div class="container-wrapper" style="width: 90px;">')

# add floating buttons
add_to_head('<link rel="stylesheet" href="floating-buttons-style.css" />')
add_to_body("""
    <div class="floating-buttons" style="display: none;">
      <div class="frame-wrapper">
        <div class="div">
          <a class="link floating" href="#Start"><div class="text-wrapper">Start for free</div></a>
          <div class="text-wrapper-2">or</div>
          <a class="div-wrapper demo-button floating" onclick="showDemoDialog()"><div class="text-wrapper-3">Get a demo</div></a>
        </div>
      </div>
    </div>
""")

# add favicon
add_to_head("""<link rel="icon" href="static/favicon.ico">""")

# links
replace_text_regex(r'<div class="header-header-nav-2">(.*?)</div>', '<a class="header-header-nav-2" href="#\\1">\\1</a>')
replace_text_regex(r'<div class="header-header-nav-3">(.*?)</div>', '<a class="header-header-nav-3" href="#\\1">\\1</a>')
replace_text_regex(r'<div class="header-header-nav-4">(.*?)</div>', '<a class="header-header-nav-4" href="#\\1">\\1</a>')
replace_text_regex(r'<div class="header-header-nav-5">(.*?)</div>', '<a class="header-header-nav-5" href="#\\1">\\1</a>')
replace_text_regex(r'<div class="header-header-nav-6">(.*?)</div>', '<a class="header-header-nav-6" href="#\\1">\\1</a>')
replace_text('<div class="frame-77">', '<div class="frame-77"><a name="About"></a>')
replace_text('<div class="div-rounded-xl-wrapper">', '<a name="About"></a><div class="div-rounded-xl-wrapper">')
replace_text('<div class="section-7">', '<div class="section-7"><a name="Customers"></a>')
replace_text('<div class="section-4">', '<div class="section-4"><a name="Customers"></a>')
replace_text('<div class="section">', '<div class="section-4"><a name="Customers"></a>')
replace_text('<div class="frame-145">', '<a name="Features"></a><div class="frame-145">')
replace_text('<div class="frame-89">', '<a name="Features"></a><div class="frame-89">')
replace_text('<div class="frame-17">', '<a name="Features"></a><div class="frame-17">')
replace_text('<div class="overlap-group-9">', '<div class="overlap-group-9"><a name="Integrations"></a>')
replace_text('<div class="frame-56">', '<div class="frame-56" style="padding: 40px 10px;"><a name="Integrations"></a>')
replace_text('<div class="frame-194">', '<div class="frame-194"><a name="Benefits"></a>')
replace_text('<div class="frame-125">', '<div class="frame-125"><a name="Benefits"></a>')
replace_text('<div class="frame-63">', '<div class="frame-63"><a name="Benefits"></a>')
replace_text('<div class="header-header-nav"><div class="text-wrapper">Sign in</div></div>', '<a class="header-header-nav" href="https://app.teamcubation.com/login" target="_blank"><div style="line-height: 10px;" class="text-wrapper">Sign in</div></a>')
replace_text('<div class="header-header-nav"><div class="text-wrapper">Talk to Sales</div></div>', '<a class="header-header-nav" href="https://calendly.com/natalia-perez-tq/teamboarding-talk-to-sales" target="_blank"><div style="line-height: 10px;" class="text-wrapper">Talk to Sales</div></a>')
replace_text('<div class="section-5"', '<a name="Start"></a><div class="section-5"')
replace_text('<div class="section-8"', '<a name="Start"></a><div class="section-8"')
replace_text('<div class="section-2"', '<a name="Start"></a><div class="section-2"')
replace_text('<div class="link"><div class="text-wrapper-3">Start for free</div></div>', '<a class="link non-floating" href="#Start"><div class="text-wrapper-3">Start for free</div></a>')
replace_text('<span class="text-wrapper-5">Get a demo</span>', '<a class="text-wrapper-5 demo-button non-floating" style="cursor: pointer;" onclick="showDemoDialog()">Get a demo</a>')
replace_text("""<p class="privacy-policy-terms-2">
              Privacy Policy&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Terms &amp; Conditions
            </p>""",
             """<p class="privacy-policy-terms-2">
              <a href="https://teamcubation.com/privacy-policy.html" target="_blank" style="color: var(--tokens-text-secondary);">Privacy Policy</a>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <a href="https://teamcubation.com/terms.html" target="_blank" style="color: var(--tokens-text-secondary);">Terms &amp; Conditions</a>
            </p>""")
replace_text("""<p class="privacy-policy-terms">
              Privacy Policy&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Terms &amp; Conditions
            </p>""",
             """<p class="privacy-policy-terms">
              <a href="https://teamcubation.com/privacy-policy.html" target="_blank" style="color: var(--tokens-text-secondary);">Privacy Policy</a>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <a href="https://teamcubation.com/terms.html" target="_blank" style="color: var(--tokens-text-secondary);">Terms &amp; Conditions</a>
            </p>""")

# demo dialog
add_to_head('<link rel="stylesheet" href="demo-dialog-style.css" />')
add_to_head('<script src="static/texts.js?v=5"></script>')
add_to_head('<script src="static/scripts.js?v=5"></script>')
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
              <a class="link" onclick="demoDialogOk()"><div class="text-wrapper-2" id="demo-button">Let’s go</div></a>
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
