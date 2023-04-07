# Bootstrap-xlwings

Bootstrap-xlwings is a Bootstrap theme made for Office.js add-ins in Excel.

## How to use

In your HTML file, add the following in the `<head>` section (check the Release page for available versions):

```html
<link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/xlwings/bootstrap-excel@5.2.3-1/dist/bootstrap-xlwings.min.css">
```

If you don't want to use a CDN, you can also download the files from the ``dist`` directory and reference `bootstrap-xlwings.min.css` locally.

## Versioning

The number before the dash corresponds to the bootstrap version, and the version after the dash corresponds to the build number of the theme.

## Development

Install Node.js (comes with npm).
From the root of this directory, run:

```sh
npm install
npm start
```

Then open http://localhost:1234 to see the example page. Changes to `bootstrap-xlwings.scss` will be hot-reloaded.

## Production build

To build the production CSS file, run (this requires Python):

```sh
python build.py
```

See also: https://github.com/twbs/examples
