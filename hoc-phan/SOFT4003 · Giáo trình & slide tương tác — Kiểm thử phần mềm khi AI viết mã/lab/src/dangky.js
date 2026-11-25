import { kiemTraSoTinChi, tinhHocPhi } from './grading.js';

export const DANH_MUC = {
  SOFT4003: { ten: 'Kiểm thử phần mềm', tc: 3 },
  SOFT3001: { ten: 'Kiến trúc phần mềm', tc: 3 },
  INFO2005: { ten: 'Công nghệ phần mềm', tc: 3 },
  MATH1001: { ten: 'Toán rời rạc', tc: 3 },
  MATH1002: { ten: 'Xác suất thống kê', tc: 3 },
  SOFT3010: { ten: 'Phát triển ứng dụng web', tc: 4 },
  ENGL2001: { ten: 'Tiếng Anh 2', tc: 2 },
  PHYS1001: { ten: 'Vật lý đại cương', tc: 2 },
  PE1001: { ten: 'Giáo dục thể chất', tc: 1 },
};

/** Fake: kho dữ liệu trong bộ nhớ (dùng cho kiểm thử tích hợp). */
export function taoKhoTrongBoNho() {
  const phieu = new Map();
  return {
    async luuPhieu(p) { phieu.set(p.msv, { ...p }); return p; },
    async layPhieu(msv) { return phieu.get(msv) ?? null; },
    async hocLaiCua(_msv) { return []; },
    async laChinhSach(_msv) { return false; },
  };
}

/** Dịch vụ đăng ký học phần: kiểm tra R2, tính học phí R3, tạo phiếu Nháp (R5). */
export function taoDichVuDangKy({ db, donGia }) {
  return {
    async dangKy(msv, maHocPhan) {
      const hocLai = new Set(await db.hocLaiCua(msv));
      let tcMoi = 0, tcLai = 0;
      for (const ma of maHocPhan) {
        const hp = DANH_MUC[ma];
        if (!hp) throw new Error(`Không có học phần ${ma}`);
        if (hocLai.has(ma)) tcLai += hp.tc; else tcMoi += hp.tc;
      }
      const kt = kiemTraSoTinChi(tcMoi + tcLai);
      if (!kt.hopLe) throw new Error(kt.loi);
      const hocPhi = tinhHocPhi(tcMoi, donGia, await db.laChinhSach(msv), tcLai);
      return db.luuPhieu({ msv, maHocPhan, tongTC: tcMoi + tcLai, hocPhi, trangThai: 'Nháp' });
    },
  };
}
