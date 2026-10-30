# Kerb starter kit

The asset pack for **Kerb from Scratch**, the ReactBD course that builds Kerb, a ride, food and package
delivery app, in React Native with Expo, one file at a time.

These are the few things the course doesn't type: the icon fonts, the app icon and splash images, and the small
scripts that build the icon font.

## What's inside

```
assets/
  fonts/     KerbSymbols, KerbSymbolsFill, KerbSymbolsLight, KerbSymbolsBold: the app's icon font
  images/    the app icon, the splash icon, Android's adaptive icon layers and the web favicon
scripts/
  icons/     the scripts that build the icon font and its list of icon names
```

## Where this fits in the course

| In Video 1A | What happens |
| --- | --- |
| 7:51 | Lesson 1, "An empty folder", begins |
| 9:47 | What's in this kit, and why it isn't typed |
| 12:31 | Copy the kit into the new app |
| 51:49 | Lesson 3 writes the icon names with `scripts/icons/gen-glyphs.js` |

## How to use it

Follow lesson 1, "An empty folder". Once you've created the app and run `npm run reset-project`:

1. Copy this kit's `assets` folder over your `mobile/assets` folder, replacing the template's images.
2. Copy this kit's `scripts` folder into your `mobile` folder.
3. Delete the template's `mobile/assets/expo.icon` folder: the app icon comes from this kit.

Your `mobile` folder then looks like this:

```
mobile/
  assets/
    fonts/
    images/
  scripts/
    icons/
  ...
```

In lesson 3, `node scripts/icons/gen-glyphs.js` writes the list of icon names the app uses.

## The course

- YouTube: [ReactBD](https://www.youtube.com/@reactjsbd)
- Full source code of the finished app: [Buy Me a Coffee](https://buymeacoffee.com/reactbd)
- Website: [reactbd.com](https://reactbd.com)

## Licences

- The icon fonts are subsets of Google's Material Symbols Rounded, under the Apache License 2.0
  (`assets/fonts/LICENSE-Material-Symbols.txt`).
- The Kerb app icon and splash images are part of the course. Use them while you follow along; make your own for an
  app you publish.
