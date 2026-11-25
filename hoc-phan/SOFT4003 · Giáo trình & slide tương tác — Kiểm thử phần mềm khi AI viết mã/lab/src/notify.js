import { xetHocBong } from './grading.js';

/**
 * Xét học bổng cho một sinh viên và gửi email nếu đạt.
 * Phụ thuộc được tiêm vào để dễ thay bằng test double (Chương 7).
 * @param {string} msv
 * @param {{ kho: { layKetQua(msv: string): Promise<{gpa:number, renLuyen:number, coF:boolean}> },
 *           email: { gui(msv: string, noiDung: string): void } }} deps
 * @returns {Promise<'Xuất sắc'|'Khá'|'Không'>}
 */
export async function thongBaoHocBong(msv, { kho, email }) {
  const kq = await kho.layKetQua(msv);
  const loai = xetHocBong(kq.gpa, kq.renLuyen, kq.coF);
  if (loai !== 'Không') {
    email.gui(msv, `Chúc mừng bạn đạt học bổng ${loai} học kỳ này.`);
  }
  return loai;
}
