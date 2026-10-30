import sys, json
from fontTools.ttLib import TTFont
from fontTools.varLib import instancer
from fontTools import subset
src, glyphs_json, outdir = sys.argv[1:]
cps = sorted(set(json.load(open(glyphs_json)).values()))
variants = [("KerbSymbols", 0, 400), ("KerbSymbolsFill", 1, 400), ("KerbSymbolsLight", 0, 300), ("KerbSymbolsBold", 0, 700)]
for name, fill, wght in variants:
    f = TTFont(src)
    inst = instancer.instantiateVariableFont(f, {"FILL": fill, "wght": wght, "GRAD": 0, "opsz": 24})
    opts = subset.Options(); opts.layout_features = []; opts.name_IDs = ['*']; opts.notdef_outline = True; opts.glyph_names = False
    sub = subset.Subsetter(opts); sub.populate(unicodes=cps); sub.subset(inst)
    nt = inst['name']
    for rec in list(nt.names):
        if rec.nameID in (1, 4, 16): nt.setName(name, rec.nameID, rec.platformID, rec.platEncID, rec.langID)
        elif rec.nameID == 6: nt.setName(name, 6, rec.platformID, rec.platEncID, rec.langID)
        elif rec.nameID in (2, 17): nt.setName("Regular", rec.nameID, rec.platformID, rec.platEncID, rec.langID)
    inst.save(f"{outdir}/{name}.ttf")
    print(name, "ok")
