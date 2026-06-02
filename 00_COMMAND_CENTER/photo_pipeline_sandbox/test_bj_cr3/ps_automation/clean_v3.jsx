#target photoshop
function log(msg) {
    var f = new File('/Users/sniper/AI-Brain-Refinery/00_COMMAND_CENTER/photo_pipeline_sandbox/test_bj_cr3/ps_automation/ps.log');
    f.open('a');
    f.writeln(new Date().toString() + ' :: ' + msg);
    f.close();
}
function go() {
    try {
        log('=== START v3 ===');
        app.displayDialogs = DialogModes.NO;
        // Close any open docs
        while (app.documents.length > 0) {
            app.activeDocument.close(SaveOptions.DONOTSAVECHANGES);
        }
        log('cleared open docs');
        var doc = app.open(File('/Users/sniper/AI-Brain-Refinery/00_COMMAND_CENTER/photo_pipeline_sandbox/test_bj_cr3/ps_automation/work_input.jpg'));
        log('opened ' + doc.width.value + 'x' + doc.height.value);
        // Unlock background layer (Content-Aware Fill needs unlocked)
        var bg = doc.activeLayer;
        log('layer isBg=' + bg.isBackgroundLayer + ' name=' + bg.name);
        if (bg.isBackgroundLayer) {
            bg.isBackgroundLayer = false;
            log('background unlocked · new name=' + doc.activeLayer.name);
        }
        var regions = [
            [4400, 1100, 5600, 2000],
            [4500, 1900, 5500, 3300],
            [4500, 3300, 5300, 3700]
        ];
        for (var i = 0; i < regions.length; i++) {
            var r = regions[i];
            doc.selection.select([[r[0], r[1]], [r[2], r[1]], [r[2], r[3]], [r[0], r[3]]]);
            log('selected region ' + i + ' bounds=' + r.join(','));
            // Content-Aware Fill via stringID (modern API)
            var idFill = stringIDToTypeID('fill');
            var fd = new ActionDescriptor();
            fd.putEnumerated(stringIDToTypeID('using'), stringIDToTypeID('fillContents'), stringIDToTypeID('contentAware'));
            fd.putUnitDouble(stringIDToTypeID('opacity'), stringIDToTypeID('percentUnit'), 100);
            fd.putEnumerated(stringIDToTypeID('mode'), stringIDToTypeID('blendMode'), stringIDToTypeID('normal'));
            executeAction(idFill, fd, DialogModes.NO);
            log('filled region ' + i);
        }
        doc.selection.deselect();
        log('deselected');
        // Flatten before save to ensure clean JPEG
        if (doc.layers.length > 1) {
            doc.flatten();
            log('flattened');
        }
        var jpg = new JPEGSaveOptions();
        jpg.quality = 12;
        jpg.embedColorProfile = true;
        doc.saveAs(File('/Users/sniper/AI-Brain-Refinery/00_COMMAND_CENTER/photo_pipeline_sandbox/test_bj_cr3/07_hero/FINAL_hero_v4_ps_auto.jpg'), jpg, true, Extension.LOWERCASE);
        log('saved');
        doc.close(SaveOptions.DONOTSAVECHANGES);
        log('=== DONE ===');
        return 'OK';
    } catch (e) {
        log('ERROR: ' + e.toString() + ' line=' + (e.line || '?'));
        return 'ERR: ' + e.toString();
    }
}
go();
