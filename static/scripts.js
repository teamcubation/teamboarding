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

document.addEventListener('DOMContentLoaded', function() {
    const floatingButtons = document.querySelector('.floating-buttons');
    window.onscroll = function() {
        if (window.pageYOffset > 600 && (document.body.scrollWidth >= 1440 || window.pageYOffset + document.body.clientHeight < document.body.scrollHeight - 50)) {
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