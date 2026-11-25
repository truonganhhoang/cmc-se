import { test, expect } from 'vitest';
import { xepLoai, tinhHocPhi } from '../src/grading.js';

// Bộ kiểm thử ban đầu: cố ý còn yếu. Chương 6–8 sẽ đo và cải thiện nó.

test('điểm giỏi', () => {
  expect(xepLoai(9)).toBe('A');
});

test('điểm khá', () => {
  expect(xepLoai(7.5)).toBe('B');
});

test('điểm kém', () => {
  xepLoai(2); // không có expect: luôn "đạt"
});

test('học lại, chính sách, số tín chỉ lớn', () => {
  // 40 TC + 10 TC học lại, đơn giá 1.000.000, diện chính sách
  expect(tinhHocPhi(40, 1000000, true, 10)).toBe(26000000);
});

test('tín chỉ âm báo lỗi', () => {
  expect(() => tinhHocPhi(-1, 1000000, false, 0)).toThrow();
});
