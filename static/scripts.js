let TB_MODE = 'onboarding';
let TB_SOURCE = 'direct';
const API_URL = 'https://api.prod.tq.teamcubation.com';

const getVarText = (elementId) => document.getElementById(elementId).value;

function initMode() {
    // get source from url
    if (window.location.search.indexOf('s=e') > -1) {
        TB_SOURCE = 'email';
    } else if (window.location.search.indexOf('s=a') > -1) {
        TB_SOURCE = 'ads';
    } else if (window.location.search.indexOf('fbclid') > -1) {
        TB_SOURCE = 'facebook/instagram';
    }

    // get mode from localStorage
    if (localStorage.getItem('tb_mode') && window.location.search.indexOf('override') === -1) {
        TB_MODE = localStorage.getItem('tb_mode');
    } else {
        if (window.location.search.indexOf('m=t') > -1) {
            TB_MODE = 'tracking';
        } else if (window.location.search.indexOf('m=p') > -1) {
            TB_MODE = 'performance';
        }
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

    trackEvent('Page View');

    const startButtons = document.querySelectorAll('.link.non-floating[href="#Start"]');
    for (let i = 0; i < startButtons.length; i++) {
        startButtons[i].addEventListener('click', function() {
            trackEvent('Start for free Button Clicked', {'type': 'top'});
        });
    }

    document.querySelector('.link.floating[href="#Start"]').addEventListener('click', function() {
        trackEvent('Start for free Button Clicked', {'type': 'floating'});
    });

    const demoButtons = document.querySelectorAll('.demo-button.non-floating');
    for (let i = 0; i < demoButtons.length; i++) {
        demoButtons[i].addEventListener('click', function() {
            trackEvent('New View Demo Button Clicked', {'type': 'top'});
        });
    }

    document.querySelector('.demo-button.floating').addEventListener('click', function() {
        trackEvent('New View Demo Button Clicked', {'type': 'floating'});
    });

    const loginButtons = document.querySelectorAll('a[href="https://app.teamcubation.com/login"]');
    for (let i = 0; i < loginButtons.length; i++) {
        loginButtons[i].addEventListener('click', function() {
            trackEvent('Sign in Button Clicked');
        });
    }

    const talkToSalesButtons = document.querySelectorAll('a[href="https://calendly.com/natalia-perez-tq/teamboarding-talk-to-sales"]');
    for (let i = 0; i < talkToSalesButtons.length; i++) {
        talkToSalesButtons[i].addEventListener('click', function() {
            trackEvent('Talk to Sales Button Clicked');
        });
    }
}

function trackEvent(eventName, eventProps) {
    if (!eventProps) {
        eventProps = {};
    }
    eventProps.source = TB_SOURCE;
    eventProps.mode = TB_MODE;
    eventProps.url = window.location.href;
    eventName = 'Teamboarding Landing - ' + eventName;
    if (typeof mixpanel !== 'undefined') {
        mixpanel.track(eventName, eventProps);
    }
}

function buildSource() {
    return 'Teamboarding Landing (mode: ' + TB_MODE + ', source: ' + TB_SOURCE + ', url: ' + window.location.href + ')';
}

function validateEmail(email) {
    return /^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$/.test(email);
}

function trackDemoOpened() {
    trackEvent('New View Demo Button Clicked');
}

function createUUID4() {
    return ([1e7]+-1e3+-4e3+-8e3+-1e11).replace(/[018]/g, c =>
        (c ^ crypto.getRandomValues(new Uint8Array(1))[0] & 15 >> c / 4).toString(16)
    );
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
    mixpanel.init("76b651d87641a235bf95859fdd1fbba7", {
        debug: true,
        track_pageview: true,
        persistence: "localStorage",
        loaded: function(mixpanel) {
            const existingUUID = localStorage.getItem('MP_UUID');
            if (existingUUID) {
                mixpanel.identify(existingUUID);
            } else {
                mixpanel.identify(createUUID4());
                localStorage.setItem('MP_UUID', mixpanel.get_distinct_id());
            }
            const demo_links = document.querySelectorAll(`[href="https://demo.teamcubation.com/login"]`);
            for (let i = 0; i < demo_links.length; i++) {
                demo_links[i].href = demo_links[i].href + '?mid=' + mixpanel.get_distinct_id();
            }

            window.mixpanel = mixpanel;

            initMode();
        }
    });

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
        const varTextSending = getVarText('var-text-sending');
        button.addEventListener('click', function() {
            if (button.innerText !== varTextSending) {
                const form = button.closest('.form-2');
                const full_name = form.querySelector('input[name="fullname"]').value;
                const company = form.querySelector('input[name="company"]').value;
                const email = form.querySelector('input[name="email"]').value;
                if (full_name && company && email) {
                    if (!validateEmail(email)) {
                        alert(getVarText('var-text-invalid-email'));
                        return;
                    }
                    if (!CompanyEmailValidator.isCompanyEmail(email)) {
                        alert(getVarText('var-text-company-email'));
                        return;
                    }
                    button.innerHTML = '<div class="text-wrapper-58">' + varTextSending + '</div>';
                    trackEvent('Request Trial Button Clicked');
                    if (typeof gtag_report_conversion !== 'undefined') {
                        gtag_report_conversion();
                    }
                    fetch(API_URL + '/obi-trial', {
                        method: 'POST',
                        headers: {
                            'Content-Type': 'application/json',
                        },
                        body: JSON.stringify({
                          "company": company,
                          "name": full_name,
                          "email": email,
                          "source": buildSource()
                        })
                    })
                    .then(response => {
                        button.innerHTML = '<div class="text-wrapper-58">' + getVarText('var-text-request-trial') + '</div>';
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
                    alert(getVarText('var-text-missing-fields'));
                }
            }
        });
    });

    document.querySelector('.top-actions-bar .lang-button').addEventListener('click', function(e) {
        e.target.classList.toggle('active');
        document.querySelector('.top-actions-bar .lang-switch-menu').classList.toggle('active');
    });

    // hide the menu when clicking outside of it
    document.addEventListener('click', function(e) {
        if (!e.target.matches('.lang-switch-menu') && !e.target.matches('.lang-button')) {
            document.querySelector('.top-actions-bar .lang-button').classList.remove('active');
            document.querySelector('.top-actions-bar .lang-switch-menu').classList.remove('active');
        }
    });
});