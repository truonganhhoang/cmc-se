import { test, expect } from 'vitest';
import { taoKhoTrongBoNho, taoDichVuDangKy } from '../src/dangky.js';

// Kiểm thử tích hợp thành phần: dịch vụ đăng ký + tính học phí + kho giả (fake).
test('đăng ký 12 TC tạo phiếu Nháp có học phí đúng', async () => {
  const db = taoKhoTrongBoNho();
  const dv = taoDichVuDangKy({ db, donGia: 500000 });
  const phieu = await dv.dangKy('BIT230001', ['SOFT4003', 'SOFT3001', 'INFO2005', 'MATH1001']);
  expect(phieu.trangThai).toBe('Nháp');
  expect(phieu.tongTC).toBe(12);
  expect(phieu.hocPhi).toBe(6000000);
});

test('dưới 10 TC bị từ chối', async () => {
  const dv = taoDichVuDangKy({ db: taoKhoTrongBoNho(), donGia: 500000 });
  await expect(dv.dangKy('BIT230001', ['SOFT4003', 'SOFT3001', 'INFO2005'])).rejects.toThrow('Tối thiểu 10');
});
