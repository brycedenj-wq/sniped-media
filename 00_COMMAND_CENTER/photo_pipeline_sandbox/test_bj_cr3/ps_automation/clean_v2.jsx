#target photoshop
function log(msg) {
    var f = new File('/Users/sniper/AI-Brain-Refinery/00_COMMAND_CENTER/photo_pipeline_sandbox/test_bj_cr3/ps_automation/ps.log');
    f.open('a');
    f.writeln(new Date().toString() + ' :: ' + msg);
    f.close();
}
function go() {
    try {
        log('START');
        app.displayDialogs = DialogModes.NO;
        var doc = app.open(File('/Users/sniper/AI-Brain-Refinery/00_COMMAND_CENTER/photo_pipeline_sandbox/test_bj_cr3/ps_automation/work_input.jpg'));
        log('opened ' + doc.width.value + 'x' + doc.height.value);
        var regions = [
            [4400, 1100, 5600, 2000],
            [4500, 1900, 5500, 3300],
            [4500, 3300, 5300, 3700]
        ];
        for (var i = 0; i < regions.length; i++) {
            var r = regions[i];
            doc.selection.select([[r[0], r[1]], [r[2], r[1]], [r[2], r[3]], [r[0], r[3]]]);
            log('selected region ' + i);
            var idFill = charIDToTypeID('Fl  ');
            var fd = new ActionDescriptor();
            fd.putEnumerated(charIDToTypeID('Usng'), charIDToTypeID('FlCn'), charIDToTypeID('CntA'));
            executeAction(idFill, fd, DialogModes.NO);
            log('filled region ' + i);
        }
        doc.selection.deselect();
        log('deselected');
        var jpg = new JPEGSaveOptions();
        jpg.quality = 12;
        jpg.embedColorProfile = true;
        doc.saveAs(File('/Users/sniper/AI-Brain-Refinery/00_COMMAND_CENTER/photo_pipeline_sandbox/test_bj_cr3/07_hero/FINAL_hero_v4_ps_auto.jpg'), jpg, true, Extension.LOWERCASE);
        log('saved');
        doc.close(SaveOptions.DONOTSAVECHANGES);
        log('closed · DONE');
        return 'OK';
    } catch (e) {
        log('ERROR: ' + e.toString() + ' line=' + (e.line || '?') + ' number=' + (e.number || '?'));
        return 'ERR: ' + e.toString();
    }
}
go();
