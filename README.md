# InvenTree website
This project contains the source for InvenTree's website.
It is built on Jekyll and GitHub pages for backend / hosting, tailtwindcss for design and Netlify for preview builds.

[![Netlify Status](https://api.netlify.com/api/v1/badges/f84340d0-bc2f-4f7f-ad4c-877c50b33a27/deploy-status)](https://app.netlify.com/sites/inventree-org-preview/deploys)

## Architecture

The website consists of content, layouts and assets. Jekyll runs and builds out of these files static html files - that are then hosted on GitHub pages. Folders with an underscore prefixed are internal folders for Jekyll, folders without are rendered as subdirectories in the output.

Content:
`_data` contains data that is references on pages  
`_drafts` contains drafts for blog pages and news items  
`_news` contains news entries  
`_posts` contains blog entries  
`_publishers` contains authors/publishers  
`_repo` will contain plugin repo entries  

Layouts:
`_includes` contains partials that can be used in layouts  
`_layouts` contains the page defintions  

Assets:
`assets` contains static assets for the pages

The site configuration is saved in `config.yaml`, required gems in `Gemfile` and npm packages in `package.json`.

The CSS stylesheet uses tailwindcss and is built with postcss on demand. NodeJs is needed for this. The main css file is located in `assets/index.css`. Rebuilds are handled by the workflows automatically.

## Common commands
Install packages for ruby and nodejs.
```
sudo apt-get install rubygems ruby-dev nodejs npm
npm install
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
