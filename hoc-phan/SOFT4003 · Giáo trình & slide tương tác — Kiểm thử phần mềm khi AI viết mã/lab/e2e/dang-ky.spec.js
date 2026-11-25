import { test, expect } from '@playwright/test';
import { TrangDangNhap } from './pages/dang-nhap.js';

test('đăng nhập sai mật khẩu hiển thị lỗi', async ({ page }) => {
  const dn = new TrangDangNhap(page);
  await dn.moTrang();
  await dn.dangNhap('BIT230001', 'sai-mat-khau');
  await expect(dn.thongBaoLoi).toHaveText('Mã sinh viên hoặc mật khẩu không đúng');
});

test('đăng ký 12 tín chỉ hiển thị học phí', async ({ page }) => {
  const dn = new TrangDangNhap(page);
  await dn.moTrang();
  await dn.dangNhap('BIT230001', '123456');
  await expect(page.getByRole('heading', { name: 'Xin chào, Nguyễn Văn A' })).toBeVisible();
  await page.getByRole('link', { name: 'Đăng ký học phần' }).click();
  for (const hp of ['SOFT4003', 'SOFT3001', 'INFO2005', 'MATH1001']) {
    await page.getByRole('row', { name: new RegExp(hp) }).getByRole('checkbox').check();
  }
  await expect(page.getByTestId('tong-tc')).toHaveText('12');
  await expect(page.getByTestId('hoc-phi')).toHaveText('6.000.000 đ');
});

// Bài tập Chương 8: thêm ca cho học phí có tín chỉ học lại (R3), giới hạn 10–15 TC (R2),
// trạng thái phiếu (R5). Chạy cả với bản có lỗi (mặc định) và bản đúng (moTrang('?bugs=0')).
