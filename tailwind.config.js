module.exports = {
  content: ["./**/*.html"],
  darkMode: 'media',
  theme: {
    extend: {
      colors: {
        'primary':'#90A8D8',
        'secondary':'#DDBC91',
      }
    },
  },
  plugins: [
    require('@tailwindcss/typography'),
  ],
}
