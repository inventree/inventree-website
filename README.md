# InvenTree website
This project contains the source for InvenTree's website.
It is built on Jekyll and GitHub pages for backend / hosting, tailtwindcss for design and Netlify for preview builds.

[![Netlify Status](https://api.netlify.com/api/v1/badges/f84340d0-bc2f-4f7f-ad4c-877c50b33a27/deploy-status)](https://app.netlify.com/sites/inventree-org-preview/deploys)

## Adding a plugin to the repository

Any maintainer of a plugin can add their plugin to the repository. The plugin will be listed on the website, we might provide a mechanism to discover plugins from within InvenTree in the future.

To add a plugin the following steps are required:
- Fork the repository
- Create a new branch. We recommend `plugin/<plugin-name>` as the branch name.
- Create a new file in `_repo`. We recommend using the package name as the file name.
- Copy the content from `_repo/template.md` into the new file.
- Fill out the details. Please make sure to use the correct format for the fields.
- If this is your first contribution to the repository, please add yourself to the `_publishers` folder.
  - Use your GitHub username as the file name.
  - Copy the content from `_publishers/_template.md` into the new file.
  - Fill out the details. Please make sure to use the correct format for the fields.
- Commit your changes and create a pull request. We recommend using the title `[REPO] Add plugin <plugin-name>`.

Please note that the plugin repository is moderated as we see fit and we reserve the right to reject plugins that do not meet basic quality standards. We will try to provide feedback in the pull request if that is the case.

As a maintainer of a plugin we count on you to keep the information up to date. If you want to update the information, please create a pull request.
The plugin repository is just getting started as a static collection, we might enhance the features in the future. If we need more information or make significant changes to the repository, we will ping the maintainers via their GitHub handle - so please keep your main GitHub handle up to date in your publisher file.

## Architecture

The website consists of content, layouts and assets. Jekyll runs and builds out of these files static html files - that are then hosted on GitHub pages. Folders with an underscore prefixed are internal folders for Jekyll, folders without are rendered as subdirectories in the output.

Content:
`_data` contains data that is references on pages  
`_drafts` contains drafts for blog pages and news items  
`_news` contains news entries  
`_posts` contains blog entries  
`_publishers` contains authors/publishers of blog entries, news items and plugins  
`_repo` contains plugin repo entries  

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
