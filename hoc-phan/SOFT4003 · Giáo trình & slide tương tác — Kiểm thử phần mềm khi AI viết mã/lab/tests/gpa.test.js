import { test, expect } from 'vitest';
import { tinhGPA } from '../src/grading.js';

// BÀI TẬP TDD (Chương 7):
// 1. Viết các ca kiểm thử cho tinhGPA từ đặc tả trong src/grading.js (bỏ .todo).
// 2. Giao trợ lý AI / agent viết mã cho tinhGPA. Quy tắc: agent KHÔNG được sửa tệp này.
// 3. Review diff, ghi vào NHAT-KY-AI.md.

test.todo('một học phần điểm A, 3 TC → GPA 4.00');
test.todo('trọng số theo tín chỉ: A (3 TC) và C (1 TC) → 3.50');
test.todo('danh sách rỗng → ném lỗi hoặc trả 0? (hỏi lại đặc tả!)');

// Gợi ý cấu trúc:
// test('…', () => { expect(tinhGPA([{ diem: 9, tinChi: 3 }])).toBe(4); });
void tinhGPA;
