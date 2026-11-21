# InvenTree website
This project contains the source for InvenTree's website.
It is built with [Zensical](https://zensical.org) (using the same theme setup as the [InvenTree documentation](https://docs.inventree.org)), hosted on GitHub Pages, with Netlify for preview builds.

[![Netlify Status](https://api.netlify.com/api/v1/badges/f84340d0-bc2f-4f7f-ad4c-877c50b33a27/deploy-status)](https://app.netlify.com/sites/inventree-org-preview/deploys)

## Adding a plugin to the list

Any maintainer of a plugin can add their plugin to the list. The plugin will be listed on the website, we might provide a mechanism to discover plugins from within InvenTree in the future.

To add a plugin the following steps are required:
- Fork the repository
- Create a new branch. We recommend `plugin/<plugin-name>` as the branch name.
- Create a new file in `docs/plugins`. We recommend using the package name as the file name.
- Copy the content from `templates/plugin.md` into the new file.
- Fill out the details. Please make sure to use the correct format for the fields.
- If this is your first contribution to the list, please add yourself to the `publishers` folder.
  - Use your GitHub username as the file name, e.g. `publishers/octocat.yml`.
  - Copy the content from `templates/publisher.yml` into the new file.
  - Fill out the details. Please make sure to use the correct format for the fields.
- Commit your changes and create a pull request. We recommend using the title `[REPO] Add plugin <plugin-name>`.

Please note that the plugin list is moderated as we see fit and we reserve the right to reject plugins that do not meet basic quality standards. We will try to provide feedback in the pull request if that is the case.

As a maintainer of a plugin we count on you to keep the information up to date. If you want to update the information, please create a pull request.
The plugin list is just getting started as a static collection, we might enhance the features in the future. If we need more information or make significant changes to the list, we will ping the maintainers via their GitHub handle - so please keep your main GitHub handle up to date in your publisher file.

## Architecture and development

The site configuration is in `mkdocs.yml` (Zensical reads the mkdocs configuration format). Zensical builds static HTML from the Markdown files in `docs/`, which is then hosted on GitHub Pages.

### Folders and files

Content:
`docs/` contains all pages, rendered as the site structure (e.g. `docs/deploy.md` is served at `/deploy/`)  
`docs/blog/posts` contains blog entries - the file name is `YYYY-MM-DD-<slug>.md`, and `date`, `slug`, `title` and `authors` are set in the front matter  
`docs/news/posts` contains news entries (same format as blog entries)  
`docs/.authors.yml` contains the authors of blog and news entries  
`docs/plugins` contains plugin list entries (plus the index pages for the list)  
`publishers/` contains publishers of plugins  
`data/` contains data that is referenced on pages (`stats.yml` is updated daily by a bot)  
`drafts/` contains unpublished drafts  
`templates/` contains templates for new plugins and publishers  

Theme and generated content:
`overrides/` contains theme template overrides (home page hero, plugin detail page)  
`main.py` provides macros which render the plugin list, tag/category/publisher indexes, stats and team lists. Macros are only rendered on pages that set `render_macros: true` in their front matter  
`scripts/post_build.py` generates `plugins.json` and the legacy `feed.atom` feed URLs after the build  
`docs/stylesheets/extra.css` contains custom styles (shared with the documentation where possible)

Old Jekyll URLs (plugin and publisher pages) are kept working via redirects in `mkdocs.yml`.

### Preview builds

Once a PR is created, a preview build is created on Netlify (configured in `netlify.toml`). The preview build is available at `https://<pr-number>-inventree-org-preview.netlify.app/`. The preview build is automatically updated when the PR is updated.
A bot will comment on the PR with the link to the preview build.

### Common commands for local development

Install the build requirements (Python 3.10+), ideally in a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Run a local server that automatically rebuilds on changes:

```bash
zensical serve
```

Build the site (output in `site/`):

```bash
zensical build --clean
python scripts/post_build.py
```
