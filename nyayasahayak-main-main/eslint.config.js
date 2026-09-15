import js from '@eslint/js'
import globals from 'globals'

import reactRefresh from 'eslint-plugin-react-refresh'
export default [
  js.configs.recommended,
  reactRefresh.configs.vite,
  { ignores: ['dist'] },
  {
    files: ['**/*.{js,jsx}'],

    languageOptions: {
      ecmaVersion: 2020,
      globals: globals.browser,
      parserOptions: {
        ecmaVersion: 'latest',
        ecmaFeatures: { jsx: true },
        sourceType: 'module',
      },
    },
    rules: {
      'no-unused-vars': ['error', { varsIgnorePattern: '^[A-Z_]' }],
    },
  },

  {
    files: ['**/*.cjs'],
    languageOptions: {
      globals: {
        ...globals.node,
        fetch: 'readonly',
      },
    },
  },
  {
    files: ['**/*.js', '**/*.jsx'],
    languageOptions: {
      globals: {
        ...globals.serviceworker,
      },
    },
  }
]
