import js from '@eslint/js';
import globals from 'globals';

export default [
  js.configs.recommended,
  {
    files: ['src/**/*.js'],
    languageOptions: { ecmaVersion: 2023, sourceType: 'module', globals: { ...globals.node } },
    rules: {
      'no-cond-assign': 'error',   // if (a = b)
      'no-unused-vars': ['error', { argsIgnorePattern: '^_' }],
      eqeqeq: 'error',             // bắt buộc === thay vì ==
      complexity: ['warn', 10],    // độ phức tạp chu trình quá cao
    },
  },
];
