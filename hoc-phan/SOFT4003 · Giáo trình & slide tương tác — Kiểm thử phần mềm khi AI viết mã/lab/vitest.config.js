import { defineConfig } from 'vitest/config';

export default defineConfig({
  test: {
    include: ['tests/**/*.test.js'],
    coverage: {
      provider: 'v8',
      include: ['src/**'],
      reporter: ['text', 'html'],
      // Cổng chất lượng (Chương 6, 9, 10). Ban đầu bộ kiểm thử chưa đạt — đó là bài tập.
      thresholds: { statements: 90, branches: 85 },
    },
  },
});
