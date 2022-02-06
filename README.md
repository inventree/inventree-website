# InvenTree home website
This project contains the source for the new InvenTree website.
It is built on Jekyll and GitHub pages for backend / hosting and tailtwindcss for frontend.

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
