// EduReg — các hàm nghiệp vụ dùng trong bộ lab SOFT4003.
// Đặc tả: docs/yeu-cau.md (R1–R5). Bản này là bản ĐÚNG; lỗi cài sẵn chỉ nằm trong edureg/index.html.

/** R1: xếp loại điểm học phần thang 10. */
export function xepLoai(diem) {
  if (typeof diem !== 'number' || Number.isNaN(diem)) {
    throw new Error('Điểm không hợp lệ');
  }
  if (diem < 0 || diem > 10) {
    throw new Error('Điểm ngoài thang 0–10');
  }
  if (diem >= 8.5) return 'A';
  if (diem >= 7.0) return 'B';
  if (diem >= 5.5) return 'C';
  if (diem >= 4.0) return 'D';
  return 'F';
}

/** R2: số tín chỉ đăng ký hợp lệ trong một học kỳ. */
export const TC_TOI_THIEU = 10;
export const TC_TOI_DA = 15;
export function kiemTraSoTinChi(tc) {
  if (!Number.isInteger(tc)) return { hopLe: false, loi: 'Số tín chỉ phải là số nguyên' };
  if (tc < TC_TOI_THIEU) return { hopLe: false, loi: 'Tối thiểu 10 tín chỉ' };
  if (tc > TC_TOI_DA) return { hopLe: false, loi: 'Tối đa 15 tín chỉ' };
  return { hopLe: true };
}

/** R3: học phí một học kỳ. tinChi: số tín chỉ học mới; hocLai: số tín chỉ học lại. */
export function tinhHocPhi(tinChi, donGia, chinhSach, hocLai) {
  if (tinChi <= 0) {
    throw new Error('Số tín chỉ phải dương');
  }
  let tong = tinChi * donGia;
  if (hocLai > 0) {
    tong = tong + hocLai * donGia * 1.2;
  }
  if (chinhSach) {
    tong = tong * 0.5;
  }
  if (tong > 30000000) {
    tong = 30000000;
  }
  return Math.round(tong);
}

/** R4: xét học bổng. Trả về 'Xuất sắc' | 'Khá' | 'Không'. */
export function xetHocBong(gpa, renLuyen, coF) {
  if (gpa >= 3.2 && renLuyen >= 80 && !coF) {
    if (gpa >= 3.6 && renLuyen >= 90) return 'Xuất sắc';
    return 'Khá';
  }
  return 'Không';
}

/**
 * GPA thang 4 có trọng số tín chỉ, làm tròn 2 chữ số.
 * Quy đổi: A=4, B=3, C=2, D=1, F=0.
 * BÀI TẬP TDD (Chương 7): viết kiểm thử trước trong tests/gpa.test.js, rồi giao agent hiện thực.
 * @param {{diem:number, tinChi:number}[]} _ketQua
 */
export function tinhGPA(_ketQua) {
  throw new Error('Chưa hiện thực');
}
