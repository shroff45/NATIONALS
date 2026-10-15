import js from '@eslint/js'
import globals from 'globals'


export default [
  { ignores: ['dist'] },
  { files: ['*/*.cjs', '*.cjs'], languageOptions: { globals: globals.node } },
  js.configs.recommended,
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
]
