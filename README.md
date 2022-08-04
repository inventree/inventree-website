# InvenTree home website
This project contains the source for the new InvenTree website.
It is built on Jekyll and GitHub pages for backend / hosting and tailtwindcss for frontend.

## File structure

State as of ###.
``` bash

```

## Common commands
Install packages
```
sudo apt-get install rubygems ruby-dev
sudo gem install bundler
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
