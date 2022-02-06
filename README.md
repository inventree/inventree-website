# InvenTree home website
This project contains the source for the new InvenTree website.
It is built on Jekyll and GitHub pages for backend / hosting and tailtwindcss for frontend.

## file structure

State as of f154fc0.
``` bash
├── assets
│   ├── index.css
│   └── logo.png
├── _data
│   ├── ctas
│   │   ├── end.yml
│   │   └── learn.yml
│   ├── functions
│   │   ├── extras.yml
│   │   └── general.yml
│   ├── general
│   │   ├── footer.yml
│   │   └── stats.yml
│   ├── for_business.yml
│   ├── for_edu.yml
│   └── for_maker.yml
├── _includes
│   ├── cta.html
│   ├── features.html
│   ├── footer.html
│   ├── functions.html
│   ├── header.html
│   ├── head.html
│   ├── hero.html
│   ├── learn_more.html
│   ├── link.html
│   ├── stats.html
│   ├── team.html
│   └── testimonials.html
├── _layouts
│   ├── branche.html
│   ├── default.html
│   └── post.html
├── 404.md
├── business.md
├── _config.yml
├── education.md
├── functions.md
├── Gemfile
├── Gemfile.lock
├── index.md
├── LICENSE
├── maker.md
├── package.json
├── package-lock.json
├── postcss.config.js
├── README.md
└── tailwind.config.js
```

## common commands
Install packages
```
bundle install
```

Build site locally
```
bundle exec jekyll build
```

Run debug server
```
bundle exec jekyll serve --incremental
```

Regenerate file structure
```
tree -I '_site|.git|.jekyll-cache|node_modules' --dirsfirst
```
