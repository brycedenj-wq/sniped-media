#target photoshop
function log(msg) {
    var f = new File('/Users/sniper/AI-Brain-Refinery/00_COMMAND_CENTER/photo_pipeline_sandbox/test_bj_cr3/ps_automation/ps.log');
    f.open('a');
    f.writeln(new Date().toString() + ' :: ' + msg);
    f.close();
}
function tryGenFillAction(actionID, withPrompt) {
    try {
        var idFill = stringIDToTypeID(actionID);
        var desc = new ActionDescriptor();
        if (withPrompt) {
            desc.putString(stringIDToTypeID('prompt'), '');
        }
        executeAction(idFill, desc, DialogModes.NO);
        return true;
    } catch (e) {
        log('  try ' + actionID + ' failed: ' + e.toString().substring(0, 80));
        return false;
    }
}
function go() {
    try {
        log('=== START v5 generative ===');
        app.displayDialogs = DialogModes.NO;
        while (app.documents.length > 0) {
            app.activeDocument.close(SaveOptions.DONOTSAVECHANGES);
        }
        var doc = app.open(File('/Users/sniper/AI-Brain-Refinery/00_COMMAND_CENTER/photo_pipeline_sandbox/test_bj_cr3/ps_automation/work_v5.jpg'));
        log('opened ' + doc.width.value + 'x' + doc.height.value);
        if (doc.activeLayer.isBackgroundLayer) {
            doc.activeLayer.isBackgroundLayer = false;
        }
        // Cover the patch area that needs cleanup (where C-stand was)
        var regions = [
            [4400, 1100, 5700, 3500]
        ];
        var fillSucceeded = false;
        var winningAction = '';
        for (var i = 0; i < regions.length; i++) {
            var r = regions[i];
            doc.selection.select([[r[0], r[1]], [r[2], r[1]], [r[2], r[3]], [r[0], r[3]]]);
            log('selected region ' + i + ' bounds=' + r.join(','));

            var candidates = ['generativeFill', 'genFill', 'fillGenerative', 'aiGenerativeFill', 'fireflyGenerativeFill', 'AdobeGenerativeFill'];
            for (var j = 0; j < candidates.length; j++) {
                if (tryGenFillAction(candidates[j], true)) {
                    fillSucceeded = true;
                    winningAction = candidates[j];
                    log('  succeeded with: ' + candidates[j]);
                    break;
                }
            }
            if (!fillSucceeded) {
                // try without prompt
                for (var k = 0; k < candidates.length; k++) {
                    if (tryGenFillAction(candidates[k], false)) {
                        fillSucceeded = true;
                        winningAction = candidates[k] + ' (no prompt)';
                        log('  succeeded with: ' + candidates[k] + ' (no prompt)');
                        break;
                    }
                }
            }
            if (!fillSucceeded) {
                log('  ALL generative attempts failed; falling back to Content-Aware Fill');
                var idFill = stringIDToTypeID('fill');
                var fd = new ActionDescriptor();
                fd.putEnumerated(stringIDToTypeID('using'), stringIDToTypeID('fillContents'), stringIDToTypeID('contentAware'));
                executeAction(idFill, fd, DialogModes.NO);
                winningAction = 'contentAware (fallback)';
            }
        }
        doc.selection.deselect();
        if (doc.layers.length > 1) {
            doc.flatten();
        }
        var jpg = new JPEGSaveOptions();
        jpg.quality = 12;
        jpg.embedColorProfile = true;
        doc.saveAs(File('/Users/sniper/AI-Brain-Refinery/00_COMMAND_CENTER/photo_pipeline_sandbox/test_bj_cr3/07_hero/FINAL_hero_v5_ps_genfill.jpg'), jpg, true, Extension.LOWERCASE);
        doc.close(SaveOptions.DONOTSAVECHANGES);
        log('=== DONE winningAction=' + winningAction + ' ===');
        return 'OK ' + winningAction;
    } catch (e) {
        log('ERROR: ' + e.toString() + ' line=' + (e.line || '?'));
        return 'ERR: ' + e.toString();
    }
}
go();
