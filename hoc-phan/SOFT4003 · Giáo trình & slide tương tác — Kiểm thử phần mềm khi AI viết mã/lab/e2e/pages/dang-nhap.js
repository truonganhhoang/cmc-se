// Page Object cho trang đăng nhập EduReg (Chương 8).
export class TrangDangNhap {
  constructor(page) {
    this.page = page;
    this.msv = page.getByLabel('Mã sinh viên');
    this.matKhau = page.getByLabel('Mật khẩu');
    this.nutDangNhap = page.getByRole('button', { name: 'Đăng nhập', exact: true });
    this.thongBaoLoi = page.getByRole('alert');
  }
  async moTrang(query = '') { await this.page.goto('/' + query); }
  async dangNhap(msv, mk) {
    await this.msv.fill(msv);
    await this.matKhau.fill(mk);
    await this.nutDangNhap.click();
  }
}
