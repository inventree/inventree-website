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
                'primary': '#DDBC91',
                'secondary': '#90A8D8',
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