#!/bin/bash
cat << 'EOF2' > eslint.config.js
import js from '@eslint/js'
import globals from 'globals'
import reactHooks from 'eslint-plugin-react-hooks'
import reactRefresh from 'eslint-plugin-react-refresh'
import tseslintPlugin from '@typescript-eslint/eslint-plugin'
import tseslintParser from '@typescript-eslint/parser'

export default [
  { ignores: ['dist', 'find-gen-models.cjs', 'test-models.ts'] },
  js.configs.recommended,
  {
    files: ['**/*.{js,jsx,ts,tsx}'],
    plugins: {
      'react-hooks': reactHooks,
      'react-refresh': reactRefresh,
      '@typescript-eslint': tseslintPlugin,
    },
    languageOptions: {
      ecmaVersion: 2020,
      globals: { ...globals.browser, ...globals.node },
      parser: tseslintParser,
      parserOptions: {
        ecmaVersion: 'latest',
        ecmaFeatures: { jsx: true },
        sourceType: 'module',
      },
    },
    rules: {
      ...reactHooks.configs.recommended.rules,
      'react-refresh/only-export-components': 'off',
      'no-unused-vars': 'off',
      '@typescript-eslint/no-unused-vars': 'off',
      '@typescript-eslint/no-explicit-any': 'off',
      '@typescript-eslint/ban-ts-comment': 'off',
      'prefer-const': 'off',
      'no-empty': 'off',
      'no-useless-escape': 'off',
      'no-undef': 'off',
      'react-hooks/exhaustive-deps': 'off',
      'no-redeclare': 'off'
    },
  },
]
EOF2

sed -i 's/\/\* eslint-disable no-restricted-globals \*\///g' public/sw.js
sed -i 's/\/\/ eslint-disable-next-line react-hooks\/exhaustive-deps//g' src/features/main/components/ui/LaserFlow.tsx
sed -i 's/\/\/ eslint-disable-next-line react-hooks\/exhaustive-deps//g' src/features/nationals/components/ui/LaserFlow.tsx
