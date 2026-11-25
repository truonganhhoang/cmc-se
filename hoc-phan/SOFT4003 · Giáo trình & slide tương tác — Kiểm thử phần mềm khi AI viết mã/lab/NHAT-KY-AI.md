# Nhật ký sử dụng AI — SOFT4003

Mỗi lần dùng AI cho bài lab, thêm một dòng. Nhật ký là một phần điểm (Chương 1, 10).

| Ngày | Lab | Mức (M1–M5) | Công cụ, mô hình | Mục đích | Prompt (tóm tắt hoặc liên kết) | Đầu ra dùng được? | Kiểm chứng thế nào | Số liệu (precision, recall, tỷ lệ chạy…) | Đề xuất bị từ chối và vì sao |
|---|---|---|---|---|---|---|---|---|---|
| 2027-09-08 | Lab 1 | M2 | (ví dụ) Claude | Hỏi khác biệt lỗi, khiếm khuyết, hỏng hóc | “Giải thích … theo ISTQB CTFL v4.0” | Một phần | Đối chiếu giáo trình mục 1.3 | — | AI gọi “bug” là “failure” — sai thuật ngữ |

## Quy tắc
- Không đưa dữ liệu cá nhân thật, mật khẩu, khóa API vào công cụ AI.
- Kết quả mong đợi của ca kiểm thử phải có căn cứ từ đặc tả, không lấy từ AI.
- Agent không được sửa tệp trong `tests/` và `e2e/` trừ khi được yêu cầu rõ (xem CLAUDE.md).
