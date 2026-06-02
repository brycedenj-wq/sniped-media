#target photoshop
function log(msg) {
    var f = new File('/Users/sniper/AI-Brain-Refinery/00_COMMAND_CENTER/photo_pipeline_sandbox/test_bj_cr3/ps_automation/ps.log');
    f.open('a');
    f.writeln(new Date().toString() + ' :: ' + msg);
    f.close();
}
function go() {
    try {
        log('=== START basic test ===');
        app.displayDialogs = DialogModes.NO;
        log('dialogs off');
        var doc = app.open(File('/Users/sniper/AI-Brain-Refinery/00_COMMAND_CENTER/photo_pipeline_sandbox/test_bj_cr3/ps_automation/work_input.jpg'));
        log('opened: w=' + doc.width + ' h=' + doc.height + ' mode=' + doc.mode);
        var w = doc.width.value;
        var h = doc.height.value;
        log('numeric w=' + w + ' h=' + h);
        var jpg = new JPEGSaveOptions();
        jpg.quality = 12;
        jpg.embedColorProfile = true;
        doc.saveAs(File('/Users/sniper/AI-Brain-Refinery/00_COMMAND_CENTER/photo_pipeline_sandbox/test_bj_cr3/ps_automation/test_basic.jpg'), jpg, true, Extension.LOWERCASE);
        log('saved');
        doc.close(SaveOptions.DONOTSAVECHANGES);
        log('closed');
        return 'OK_BASIC';
    } catch (e) {
        log('ERROR: ' + e.toString() + ' line=' + (e.line || '?'));
        return 'ERROR: ' + e.toString();
    }
}
go();
