/* eslint-env node */
module.exports = {
  root: true,
  extends: [
    'plugin:vue/vue3-recommended',
    'prettier'
  ],
  parserOptions: {
    ecmaVersion: 'latest'
  },
  rules: {
    'prefer-promise-reject-errors': 'off',
    'semi': [2, 'never'],
    'quotes': [2, 'single', { avoidEscape: true }],
    'object-curly-spacing': ['error', 'always'],
    'vue/no-irregular-whitespace': ['error', {
      'skipStrings': true,
      'skipComments': false,
      'skipRegExps': false,
      'skipTemplates': false,
      'skipHTMLAttributeValues': false,
      'skipHTMLTextContents': false
    }],
    'vue/match-component-file-name': ['error', {
      'extensions': ['vue'],
      'shouldMatchCase': false
    }],
    'vue/component-name-in-template-casing': ['error', 'kebab-case', {
      'registeredComponentsOnly': true
    }],
    'comma-dangle': ['error', {
      arrays: 'never',
      objects: 'never',
      imports: 'never',
      exports: 'never',
      functions: 'never'
    }],
    'no-debugger': process.env.NODE_ENV === 'production' ? 'error' : 'off',
    'no-console': process.env.NODE_ENV === 'production' ? 'warn' : 'off',
    'arrow-parens': ['error', 'as-needed'],
    'no-plusplus': 'off',
    'import/extensions': 'off',
    'import/prefer-default-export': 'off',
    'no-unused-expressions': 'error',
    'no-param-reassign': 'off',
    'prefer-destructuring': ['error', {
          'array': true,
          'object': true
        }, {
          'enforceForRenamedProperties': false
        }
      ],
    'no-bitwise': ['error', { allow: ['~'] }],
    'no-unused-vars': ['error', { argsIgnorePattern: '^_' }],
    'lines-between-class-members': ['error', 'always', { exceptAfterSingleLine: true }]
  }
}
