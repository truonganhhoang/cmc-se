# Hướng dẫn cho trợ lý AI và agent trong dự án EduReg (SOFT4003)

Tệp này là prompt hệ thống của dự án (Claude Code đọc CLAUDE.md; có thể chép sang
`.github/copilot-instructions.md` cho Copilot).

## Bối cảnh
- Đặc tả: `docs/yeu-cau.md` (R1–R7). Chỉ dùng thông tin trong đặc tả; nếu thiếu, hỏi lại, không đoán.
- Mã nghiệp vụ: `src/`. Kiểm thử đơn vị, tích hợp: `tests/` (Vitest). E2E: `e2e/` (Playwright).
- Ứng dụng mô phỏng: `edureg/index.html` (mặc định có lỗi cài sẵn; `?bugs=0` là bản đúng).

## Quy tắc bắt buộc
1. KHÔNG sửa, xóa, `.skip` kiểm thử trong `tests/` hoặc `e2e/` để làm kiểm thử xanh, trừ khi người dùng yêu cầu rõ.
2. KHÔNG thay đổi giá trị mong đợi trong khẳng định. Nếu nghi kiểm thử sai, giải thích và dừng lại.
3. Kết quả mong đợi luôn lấy từ `docs/yeu-cau.md`, không suy ra từ mã hiện tại.
4. Locator Playwright: ưu tiên getByRole, getByLabel, getByText, getByTestId; không dùng chờ cứng (`waitForTimeout`).
5. Không dùng dữ liệu cá nhân thật. Không thêm phụ thuộc mới khi chưa được đồng ý.
6. Sau mỗi thay đổi: chạy `npm test` và `npm run lint`, báo kết quả.
