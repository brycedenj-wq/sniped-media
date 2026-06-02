#target photoshop

function cleanDistractions() {
    try {
        app.displayDialogs = DialogModes.NO;

        var inputPath = "/Users/sniper/AI-Brain-Refinery/00_COMMAND_CENTER/photo_pipeline_sandbox/test_bj_cr3/ps_automation/work_input.jpg";
        var outputPath = "/Users/sniper/AI-Brain-Refinery/00_COMMAND_CENTER/photo_pipeline_sandbox/test_bj_cr3/07_hero/FINAL_hero_v4_ps_auto.jpg";

        // Open file
        var doc = app.open(File(inputPath));

        // Distraction regions (rectangular, image-pixel coordinates in 6022x4014)
        // Strategy: clean the right-edge C-stand / softbox / light kit in three slices
        // to give Content-Aware Fill smaller, more digestible regions.
        var regions = [
            // [x1, y1, x2, y2]
            [4400, 1100, 5600, 2000],   // upper · softbox / modifier
            [4500, 1900, 5500, 3300],   // main · vertical pole
            [4500, 3300, 5300, 3700]    // lower · spreader / feet
        ];

        for (var i = 0; i < regions.length; i++) {
            var r = regions[i];
            var sel = [
                [r[0], r[1]],
                [r[2], r[1]],
                [r[2], r[3]],
                [r[0], r[3]]
            ];
            doc.selection.select(sel, SelectionType.REPLACE, 4, false);

            // Content-Aware Fill via ActionManager
            var idFill = charIDToTypeID("Fl  ");
            var fillDesc = new ActionDescriptor();
            fillDesc.putEnumerated(charIDToTypeID("Usng"), charIDToTypeID("FlCn"), charIDToTypeID("CntA"));
            fillDesc.putUnitDouble(charIDToTypeID("Opct"), charIDToTypeID("#Prc"), 100.0);
            fillDesc.putEnumerated(charIDToTypeID("Md  "), charIDToTypeID("BlnM"), charIDToTypeID("Nrml"));
            executeAction(idFill, fillDesc, DialogModes.NO);
        }

        doc.selection.deselect();

        // Save as JPEG quality 12 (visually lossless)
        var jpgOpts = new JPEGSaveOptions();
        jpgOpts.quality = 12;
        jpgOpts.embedColorProfile = true;
        jpgOpts.formatOptions = FormatOptions.STANDARDBASELINE;
        doc.saveAs(File(outputPath), jpgOpts, true, Extension.LOWERCASE);
        doc.close(SaveOptions.DONOTSAVECHANGES);

        return "OK: saved " + outputPath;
    } catch (e) {
        return "ERROR: " + e.toString() + " · line " + (e.line || "?");
    }
}
cleanDistractions();
