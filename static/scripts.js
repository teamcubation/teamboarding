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
