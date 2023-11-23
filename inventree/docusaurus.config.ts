import {themes as prismThemes} from 'prism-react-renderer';
import type {Config} from '@docusaurus/types';
import type * as Preset from '@docusaurus/preset-classic';

const config: Config = {
  title: 'InvenTree',
  tagline: 'Intuitive Inventory Management',
  favicon: 'img/favicon.ico',

  // Set the production url of your site here
  url: 'https://your-docusaurus-site.example.com',
  // Set the /<baseUrl>/ pathname under which your site is served
  // For GitHub pages deployment, it is often '/<projectName>/'
  baseUrl: '/',

  // GitHub pages deployment config.
  // If you aren't using GitHub pages, you don't need these.
  organizationName: 'InvenTree', // Usually your GitHub org/user name.
  projectName: 'inventree-website', // Usually your repo name.

  onBrokenLinks: 'throw',
  onBrokenMarkdownLinks: 'warn',

  // Even if you don't use internationalization, you can use this field to set
  // useful metadata like html lang. For example, if your site is Chinese, you
  // may want to replace "en" with "zh-Hans".
  i18n: {
    defaultLocale: 'en',
    locales: ['en'],
  },

  presets: [
    [
      'classic',
      {
        docs: {
          sidebarPath: './sidebars.ts',
        },
        blog: {
          showReadingTime: true,
        },
        theme: {
          customCss: './src/css/custom.css',
        },
      } satisfies Preset.Options,
    ],
  ],

  themeConfig: {
    // Replace with your project's social card
    image: 'img/docusaurus-social-card.jpg',
    navbar: {
      title: 'InvenTree',
      logo: {
        alt: 'InvenTree Logo',
        src: 'img/inventree.png',
      },
      items: [
        {
          to: '/deploy',
          label: 'Deploy',
          position: 'left',
        },
        {
          href: 'https://docs.inventree.org/',
          label: 'Docs',
          position: 'left',
        },
        {to: '/blog', label: 'Blog', position: 'left'},
        {to: '/demo', label: 'Demo', position: 'right'},
      ],
    },
    footer: {
      style: 'dark',
      links: [
        {
          title: 'InvenTree',
          items: [
            {
              label: 'Documentation',
              href: 'https://docs.inventree.org/',
            },
            {
              label: 'Source Code',
              href: 'https://github.com/inventree/inventree',
            },
            {
              label: 'Blog',
              to: '/blog',
            },
          ],
        },
        {
          title: 'Ecosystem',
          items: [
            {
              label: 'Plugins',
              to: '/plugins',
            },
            {
              label: 'API',
              to: '/api',
            },
            {
              label: 'Mobile App',
              to: '/app',
            }
          ]
        },
        {
          title: 'About',
          items: [
            {
              label: 'Contribute',
              to: '/contribute',
            },
            {
              label: 'Support',
              to: '/support'
            }
          ],
        },
        {
          title: 'Community',
          items: [
            {
              label: 'GitHub',
              href: 'https://github.com/inventree/inventree/discussions',
            },
            {
              label: 'Reddit',
              href: 'https://www.reddit.com/r/InvenTree/',
            },
            {
              label: 'Twitter',
              href: 'https://twitter.com/inventreedb',
            },
          ],
        },
      ],
      copyright: `Copyright © ${new Date().getFullYear()} InvenTree. Built with Docusaurus.`,
    },
    prism: {
      theme: prismThemes.github,
      darkTheme: prismThemes.dracula,
    },
  } satisfies Preset.ThemeConfig,

  plugins: [
    [
      '@docusaurus/plugin-sitemap',
      {
        changefreq: 'weekly',
        priority: 0.5,
        ignorePatterns: ['/tags/**'],
        filename: 'sitemap.xml',
      },
    ],
  ]
};

export default config;
