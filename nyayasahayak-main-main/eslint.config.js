import js from '@eslint/js'
import globals from 'globals'
import reactHooks from 'eslint-plugin-react-hooks'
import reactRefresh from 'eslint-plugin-react-refresh'
import tseslintPlugin from '@typescript-eslint/eslint-plugin'
import tseslintParser from '@typescript-eslint/parser'

export default [
  { ignores: ['dist'] },
  js.configs.recommended,
  {
    files: ['**/*.{js,jsx,cjs,mjs,ts,tsx}'],
    languageOptions: {
      ecmaVersion: 2022,
      globals: {
        ...globals.browser,
        ...globals.node,
        ...globals.serviceworker
      },
    },
    rules: {
      'no-undef': 'off',
      'no-unused-vars': 'off'
    }
  },
  {
    files: ['**/*.{ts,tsx}'],
    plugins: {
      'react-hooks': reactHooks,
      'react-refresh': reactRefresh,
      '@typescript-eslint': tseslintPlugin,
    },
    languageOptions: {
      ecmaVersion: 2020,
      globals: globals.browser,
      parser: tseslintParser,
      parserOptions: {
        ecmaVersion: 'latest',
        ecmaFeatures: { jsx: true },
        sourceType: 'module',
      },
    },
    rules: {
      ...reactHooks.configs.recommended.rules,
      'no-unused-vars': 'off',
      '@typescript-eslint/no-unused-vars': 'off',
      '@typescript-eslint/no-explicit-any': 'off',
      'react-hooks/exhaustive-deps': 'off',
      'no-empty': 'off',
      'no-useless-escape': 'off',
      '@typescript-eslint/ban-ts-comment': 'off',
      'no-undef': 'off',
      'prefer-const': 'off',
      'no-redeclare': 'off'
    },
  },
]
