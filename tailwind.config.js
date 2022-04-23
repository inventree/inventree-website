/*
* A tailwinds config file used to generate atomic utility css classes.
* See: https://tailwindcss.com/docs/configuration/
* Default: https://github.com/tailwindcss/tailwindcss/blob/master/stubs/defaultConfig.stub.js
*
* Run '$ npm run css:dev' to compile changes in this file.
*/
const defaultTheme = require('tailwindcss/defaultTheme')

module.exports = {
    purge: {
        enabled: true,
        content: ['./**/*.html'],
      },
    darkMode: 'media',
    theme: {
        extend: {
            colors: {
              'primary':'#90A8D8',
              'secondary':'#DDBC91',
            },
            screens: {
                'xs': '470px',
                ...defaultTheme.screens
            }
        },
    },
    plugins: [
        require('@tailwindcss/typography'),
    ],
}
