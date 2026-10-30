# Icon font (Material Symbols Rounded)

The app renders icons from static, subset instances of Google's **Material Symbols Rounded**
variable font (Apache 2.0):

| File | Axes |
| --- | --- |
| `assets/fonts/KerbSymbols.ttf` | FILL 0, wght 400 |
| `assets/fonts/KerbSymbolsFill.ttf` | FILL 1, wght 400 |
| `assets/fonts/KerbSymbolsLight.ttf` | FILL 0, wght 300 |
| `assets/fonts/KerbSymbolsBold.ttf` | FILL 0, wght 700 |

Only the glyphs listed in `glyphs.json` are included (≈100 KB per file). `IconName` in
`src/components/ui/icon-glyphs.ts` is generated from the same list, so TypeScript rejects
icons that aren't bundled.

## Adding icons

1. Download the variable font and codepoints into a scratch folder:
   - `https://raw.githubusercontent.com/google/material-design-icons/master/variablefont/MaterialSymbolsRounded%5BFILL%2CGRAD%2Copsz%2Cwght%5D.ttf`
   - `https://raw.githubusercontent.com/google/material-design-icons/master/variablefont/MaterialSymbolsRounded%5BFILL%2CGRAD%2Copsz%2Cwght%5D.codepoints`
2. Add names to the `extra` list in `collect.py`.
3. `pip install fonttools` (in a virtualenv), then:
   ```bash
   python collect.py rounded.codepoints glyphs.json ../../../design/kerb-ride-app-design/project/*.html
   python build.py rounded.ttf glyphs.json ../../assets/fonts
   node gen-glyphs.js
   ```
