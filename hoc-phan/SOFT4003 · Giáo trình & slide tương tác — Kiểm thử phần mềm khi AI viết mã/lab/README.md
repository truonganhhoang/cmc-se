# Bộ lab SOFT4003 — EduReg

Bộ lab dùng xuyên suốt 10 chương của học phần Kiểm thử phần mềm (Trường Đại học CMC).
EduReg là cổng đăng ký học phần **mô phỏng**, dữ liệu hư cấu.

## Cần có
- Node.js 22 trở lên, VS Code, Git.
- Tùy chọn: GitHub Copilot hoặc Claude Code (theo chính sách AI của học phần).

## Cài đặt
```bash
npm install
npx playwright install chromium   # cho kiểm thử E2E (Chương 8)
```

## Lệnh
| Lệnh | Việc | Chương |
|---|---|---|
| `npm test` | Chạy kiểm thử đơn vị, tích hợp (Vitest) | 1, 7 |
| `npm run coverage` | Đo bao phủ, kiểm tra ngưỡng (90% câu lệnh, 85% nhánh) | 6 |
| `npm run lint` | Phân tích tĩnh (ESLint) | 4 |
| `npm run app` | Chạy EduReg tại http://localhost:5173 | 1, 6, 8 |
| `npm run e2e` | Chạy kiểm thử E2E (Playwright) | 8 |
| `npm run mutate` | Kiểm thử đột biến (StrykerJS) — cần mọi kiểm thử đang xanh | 8 |

EduReg cũng mở trực tiếp được bằng trình duyệt: `edureg/index.html`.
Tài khoản: `BIT230001 / 123456`, `BIT230002 / 654321`.
Mặc định EduReg **có lỗi cài sẵn** để luyện tập; thêm `?bugs=0` vào địa chỉ để chạy bản đúng.

## Cấu trúc
```
docs/yeu-cau.md        Đặc tả R1–R7 (cố ý còn chỗ mơ hồ — Chương 4)
src/grading.js         xepLoai, kiemTraSoTinChi, tinhHocPhi, xetHocBong, tinhGPA (TDD)
src/dangky.js          Dịch vụ đăng ký + kho giả (kiểm thử tích hợp)
src/notify.js          Thông báo học bổng (test double)
tests/                 Kiểm thử Vitest (bộ ban đầu cố ý yếu; ai-sinh.test.js có ca sai)
e2e/                   Kiểm thử Playwright + Page Object
edureg/index.html      Ứng dụng mô phỏng
.github/workflows/     CI: lint → đơn vị + bao phủ → E2E → đột biến
CLAUDE.md              Quy tắc cho trợ lý AI, agent
NHAT-KY-AI.md          Mẫu nhật ký sử dụng AI (bắt buộc nộp)
```

## Lưu ý
- Lần đầu `npm test` sẽ có **một ca không đạt** (`tests/ai-sinh.test.js`). Đó là câu hỏi của Lab 1.
- `npm run coverage` ban đầu **không đạt ngưỡng**. Đó là bài tập Lab 6.
- `npm run mutate` cần mọi kiểm thử đang xanh; điểm ban đầu thấp. Đó là bài tập Lab 8.
