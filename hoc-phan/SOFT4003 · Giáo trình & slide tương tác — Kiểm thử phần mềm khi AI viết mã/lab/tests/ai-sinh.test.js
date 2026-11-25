import { describe, it, expect } from 'vitest';
import { xepLoai } from '../src/grading.js';

// Tệp này do một trợ lý AI sinh ra và được commit mà không review.
// Chương 1: chạy `npm test` — vì sao có ca không đạt? Lỗi nằm ở mã hay ở kiểm thử?
// Chương 7: review toàn bộ tệp, sửa hoặc xóa các ca có vấn đề.

describe('xepLoai (AI sinh)', () => {
  it('trả A cho 8.5', () => expect(xepLoai(8.5)).toBe('A'));
  it('trả B cho 8.4', () => expect(xepLoai(8.4)).toBe('B'));
  it('trả C cho 7.0', () => expect(xepLoai(7.0)).toBe('C'));
  it('xử lý điểm 10', () => { xepLoai(10); });
  it('ném lỗi khi sai kiểu', () => expect(() => xepLoai('9')).toThrow());
});
