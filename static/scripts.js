function showDemoDialog() {
  document.querySelector('.demo-dialog-container').style.display = 'flex';
  document.querySelector('.demo-dialog-container .content').style.display = 'flex';
  document.querySelector('.demo-dialog-container .content-ok').style.display = 'none';
}

function demoDialogOk() {
    document.querySelector('.demo-dialog-container .content').style.display = 'none';
    document.querySelector('.demo-dialog-container .content-ok').style.display = 'flex';
    window.setTimeout(hideDemoDialog, 2000);
}

function hideDemoDialog() {
    document.querySelector('.demo-dialog-container').style.display = 'none';
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
                        sectionAnchors[i].scrollIntoView();
                    }
                }
            });
        }
    }
});