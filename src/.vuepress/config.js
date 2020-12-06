const moment = require('moment');
const { description } = require('../../package');

module.exports = {
  /**
   * Ref：https://v1.vuepress.vuejs.org/config/#title
   */
  title: 'PyBase',
  /**
   * Ref：https://v1.vuepress.vuejs.org/config/#description
   */
  description: description,
  /**
   * Extra tags to be injected to the page HTML `<head>`
   *
   * ref：https://v1.vuepress.vuejs.org/config/#head
   */
  head: [
    ['link', { name: 'icon', href: 'https://vuepress.vuejs.org/hero.png' }],
    ['meta', { name: 'theme-color', content: '#429aff' }],
    ['meta', { name: 'apple-mobile-web-app-capable', content: 'yes' }],
    ['meta', { name: 'apple-mobile-web-app-status-bar-style', content: 'black' }]
  ],

  /**
   * Theme configuration, here is the default theme configuration for VuePress.
   *
   * ref：https://v1.vuepress.vuejs.org/theme/default-theme-config.html
   */
  themeConfig: {
    repo: 'https://github.com/PyBase/PyBase',
    repoLabel: 'Contribute with us!',
    editLinks: true,
    docsDir: 'src',
    docsBranch: 'netlify',
    editLinkText: 'Help us improve the docs!',
    searchPlaceholder: 'Search the docs ...',
    lastUpdated: 'Last Updated',
    smoothScroll: true,
    displayAllHeaders: true,
    nav: [
      {
        text: 'Guide',
        link: '/guide/',
      },
      {
        text: 'Docs',
        link: '/docs/',
      },
      {
        text: 'Changelog',
        link: '/changelog/',
      },
    ],
    sidebar: {
      '/guide/': [
        {
          title: 'Guide',
          collapsable: true,
          children: [
            '',
            'installation',
            'integrations',
          ]
        }
      ],
      '/docs/': [
        {
          title: 'Docs',
          collapsable: true,
          children: [
            '',
            'v1.0.0',
            'v0.5.0',
            'v0.4.1',
          ]
        }
      ],
      '/changelog/': [
        {
          title: 'Changelog',
        }
      ]
    },
  },

  /**
   * Apply plugins，ref：https://v1.vuepress.vuejs.org/zh/plugin/
   */
  plugins: [
    '@vuepress/plugin-back-to-top',
    [
      '@vuepress/last-updated',
      {
        transformer: (timestamp, lang) => {
          const moment = require('moment')
          moment.locale(lang)
          return moment(timestamp).fromNow()
        }
      }
    ]
  ],

  /**
   * Markdown configuration
   */
  markdown: {
    lineNumbers: true,
    pageSuffix: "",
    extractHeaders: [ 'h1', 'h2', 'h3', 'h4' ],
    // options for markdown-it-toc
    toc: { includeLevel: [1, 2, 3, 4] },
    extendMarkdown: md => {
      md.set({ breaks: true })
      md.use(require('markdown-it-custom-header-link'))
      md.use(require('markdown-it-tags'))
    }
  }
}
