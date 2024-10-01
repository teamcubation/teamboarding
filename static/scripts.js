let TB_MODE = 'onboarding';
const API_URL = 'https://api.prod.tq.teamcubation.com';

function initMode() {
    // get mode from localStorage
    if (localStorage.getItem('tb_mode') && window.location.search.indexOf('override') === -1) {
        TB_MODE = localStorage.getItem('tb_mode');
    } else {
        if (window.location.search.indexOf('m=t') > -1) {
            TB_MODE = 'tracking';
        } else if (window.location.search.indexOf('m=p') > -1) {
            TB_MODE = 'performance';
        }
        // remove mode from url
        window.history.replaceState({}, '', window.location.pathname.replace(/\/m\/t|\/m\/p/, ''));
        // save mode in local storage
        localStorage.setItem('tb_mode', TB_MODE);
    }

    // replace the texts in the page
    for (const [text, replacements] of Object.entries(TEXTS)) {
        if (TB_MODE in replacements) {
            const elems = document.evaluate(`//*[contains(text(), "${text}")]`, document, null, XPathResult.ORDERED_NODE_SNAPSHOT_TYPE, null);
            for (let i = 0; i < elems.snapshotLength; i++) {
                const elem = elems.snapshotItem(i);
                elem.textContent = replacements[TB_MODE];
            }
        }
    }
}

function validateEmail(email) {
    return /^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$/.test(email);
}

function showDemoDialog() {
  document.querySelector('.demo-dialog-container').style.display = 'flex';
  document.querySelector('.demo-dialog-container .content').style.display = 'flex';
  document.querySelector('.demo-dialog-container .content-ok').style.display = 'none';
  window.setTimeout(function() {
    document.querySelector('.demo-dialog').style.opacity = '1';
  }, 10);
}

function demoDialogOk() {
    const demo_name = document.querySelector('#demo-name').value;
    const demo_email = document.querySelector('#demo-email').value;
    const demo_button = document.querySelector('#demo-button');
    if (demo_button.innerText !== 'Please wait...') {
        if (demo_name && demo_email) {
            if (!validateEmail(demo_email)) {
                alert('Please enter a valid email');
                return;
            }
            demo_button.innerText = 'Please wait...';
            fetch(API_URL + '/request-demo', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                  "name": demo_name,
                  "email": demo_email,
                  "source": "Teamboarding Landing - " + TB_MODE
                })
            })
            .then(response => {
                demo_button.innerText = 'Let’s go';
                document.querySelector('.demo-dialog-container .content').style.display = 'none';
                document.querySelector('.demo-dialog-container .content-ok').style.display = 'flex';
                document.querySelector('#demo-name').value = '';
                document.querySelector('#demo-email').value = '';
                window.setTimeout(hideDemoDialog, 3000);
            });
        } else {
            alert('Please fill all the fields');
        }
    }
}

function hideDemoDialog() {
    document.querySelector('.demo-dialog-container').style.display = 'none';
    document.querySelector('.demo-dialog').style.opacity = '0';
}

function getScrollXY() {
    var scrOfX = 0, scrOfY = 0;
    if( typeof( window.pageYOffset ) == 'number' ) {
        //Netscape compliant
        scrOfY = window.pageYOffset;
        scrOfX = window.pageXOffset;
    } else if( document.body && ( document.body.scrollLeft || document.body.scrollTop ) ) {
        //DOM compliant
        scrOfY = document.body.scrollTop;
        scrOfX = document.body.scrollLeft;
    } else if( document.documentElement && ( document.documentElement.scrollLeft || document.documentElement.scrollTop ) ) {
        //IE6 standards compliant mode
        scrOfY = document.documentElement.scrollTop;
        scrOfX = document.documentElement.scrollLeft;
    }
    return [ scrOfX, scrOfY ];
}

function getDocHeight() {
    var D = document;
    return Math.max(
        D.body.scrollHeight, D.documentElement.scrollHeight,
        D.body.offsetHeight, D.documentElement.offsetHeight,
        D.body.clientHeight, D.documentElement.clientHeight
    );
}

function atBottomMinus(n) {
    return getDocHeight() - getScrollXY()[1] - window.innerHeight <= n;
}

document.addEventListener('DOMContentLoaded', function() {
    initMode();

    const floatingButtons = document.querySelector('.floating-buttons');
    window.onscroll = function() {
        if (window.pageYOffset > 600 && (document.body.scrollWidth >= 1440 || !atBottomMinus(400))) {
            floatingButtons.style.display = 'inline-flex';
        } else {
            floatingButtons.style.display = 'none';
        }
    };

    for (const section of ['Start', 'About', 'Customers', 'Features', 'Integrations', 'Benefits']) {
        const allSectionButtons = document.querySelectorAll(`[href="#${section}"]`)
        for (let i = 0; i < allSectionButtons.length; i++) {
            allSectionButtons[i].addEventListener('click', function() {
                const sectionAnchors = document.querySelectorAll(`a[name="${section}"]`);
                for (let i = 0; i < sectionAnchors.length; i++) {
                    if (sectionAnchors[i].offsetParent) {
                        sectionAnchors[i].scrollIntoView({behavior: 'smooth'});
                    }
                }
            });
        }
    }

    document.querySelectorAll('.req-trial-button').forEach(function(button) {
        button.addEventListener('click', function() {
            if (button.innerText !== 'Sending...') {
                const form = button.closest('.form-2');
                const full_name = form.querySelector('input[name="fullname"]').value;
                const company = form.querySelector('input[name="company"]').value;
                const email = form.querySelector('input[name="email"]').value;
                if (full_name && company && email) {
                    if (!validateEmail(email)) {
                        alert('Please enter a valid email');
                        return;
                    }
                    button.innerHTML = '<div class="text-wrapper-58">Sending...</div>';
                    fetch(API_URL + '/obi-trial', {
                        method: 'POST',
                        headers: {
                            'Content-Type': 'application/json',
                        },
                        body: JSON.stringify({
                          "company": company,
                          "name": full_name,
                          "email": email,
                          "source": "Teamboarding Landing - " + TB_MODE
                        })
                    })
                    .then(response => {
                        button.innerHTML = '<div class="text-wrapper-58">Request Trial</div>';
                        form.querySelector('input[name="fullname"]').value = '';
                        form.querySelector('input[name="company"]').value = '';
                        form.querySelector('input[name="email"]').value = '';
                        const trial_request_container = form.closest('.trial-request-container');
                        const trial_request_form = trial_request_container.querySelector('.trial-request-form');
                        const trial_ok_msg =  trial_request_container.querySelector('.trial-ok-msg');
                        trial_request_form.style.display = 'none';
                        trial_ok_msg.style.display = 'flex';
                        window.setTimeout(function() {
                            trial_ok_msg.style.display = 'none';
                            trial_request_form.style.display = 'flex';
                        }, 5000);
                    });
                } else {
                    alert('Please fill all the fields');
                }
            }
        });
    });
});