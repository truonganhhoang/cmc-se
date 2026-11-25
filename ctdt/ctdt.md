# CTĐT Kỹ thuật phần mềm AI-native – Trường Đại học CMC (v2027.3 (đề xuất))

> Bản đề xuất chỉnh sửa lớn chương trình đào tạo để Khoa, Hội đồng Khoa học & Đào tạo xem xét. Mã học phần mới, số tín chỉ và phân bổ học kỳ là dự kiến, chờ thẩm định và phê duyệt theo quy định. Cập nhật 23/11/2026.

- Thời gian: 3 năm, 9 học kỳ, mỗi học kỳ 10 tuần; tổng 123 tín chỉ (chưa gồm GDTC, GDQP-AN).
- Mỗi học kỳ có một học phần Studio làm ra một sản phẩm; tốt nghiệp với hồ sơ 9 sản phẩm.
- Hai cổng năng lực không AI cuối năm 1 và năm 2; thang mức dùng AI M1–M5 cho từng bài đánh giá.

## Nguyên tắc

- **Ship từ học kỳ 1:** Mỗi học kỳ 10 tuần kết thúc bằng Demo Day: sinh viên trình diễn một sản phẩm chạy thật. Sau 9 học kỳ, mỗi sinh viên có hồ sơ 9 sản phẩm.
- **AI là đồng nghiệp, kỹ sư là người chịu trách nhiệm:** AI có mặt ở mọi học phần chuyên môn với mức sử dụng được quy định cho từng bài đánh giá. Người ký tên vào sản phẩm luôn là sinh viên.
- **Nền tảng tinh gọn, không lùi:** Bớt giờ giảng lý thuyết cho những phần AI làm tốt hoặc sẽ sớm lỗi thời, dồn thời gian cho thực hành và phán đoán kỹ thuật. Phần cốt lõi vẫn thi không AI: hai cổng năng lực cuối năm 1 và năm 2 bảo đảm sinh viên tự đọc, tự viết, tự sửa và tự đánh giá được code, thiết kế do AI đưa ra.
- **Đặc tả trước, code sau:** Kỹ năng viết yêu cầu và đặc tả đủ rõ cho cả người lẫn AI agent được dạy riêng và chấm điểm từ năm 2.
- **Doanh nghiệp vào lớp học:** Từ học kỳ 6, đề bài Studio đến từ các công ty thuộc Tập đoàn Công nghệ CMC; học kỳ 8 là thực tập OJT.
- **Chương trình có changelog và học phần mở:** CTĐT được quản lý như phần mềm: có số phiên bản, ghi chép thay đổi, rà soát công nghệ mỗi năm. Hai học phần mở (Chủ đề hiện đại; Nghiên cứu và đổi mới) có chuẩn đầu ra cố định nhưng nội dung đổi hằng năm, đưa công nghệ mới vào lớp ngay mà không phải sửa chương trình.

## Mục tiêu (PO)

- **PO1:** Có nền tảng vững về khoa học máy tính và kỹ thuật phần mềm để hiểu, đánh giá và sửa được phần mềm, kể cả phần mềm do AI sinh ra.
- **PO2:** Xây dựng, kiểm chứng, triển khai và vận hành sản phẩm phần mềm có chất lượng, làm việc hiệu quả cùng trợ lý và tác tử AI.
- **PO3:** Thiết kế và tích hợp tính năng AI vào sản phẩm một cách an toàn, đo lường được và có trách nhiệm.
- **PO4:** Làm việc nhóm, giao tiếp chuyên nghiệp, sử dụng được tiếng Anh trong công việc kỹ thuật, làm việc với khách hàng và doanh nghiệp.
- **PO5:** Tuân thủ pháp luật và đạo đức nghề nghiệp; tự học, thích ứng với công nghệ thay đổi nhanh; có tư duy sản phẩm và khởi nghiệp.

## Chuẩn đầu ra (PLO)

- **PLO1** (Kiến thức): Vận dụng kiến thức toán, khoa học máy tính và kỹ thuật phần mềm để phân tích và giải quyết bài toán phần mềm.
  - PI1.1: Chọn và cài đặt đúng cấu trúc dữ liệu, giải thuật cho bài toán có ràng buộc hiệu năng, trong bài thi không dùng AI.
  - PI1.2: Giải thích và sửa được lỗi trong mã nguồn của người khác hoặc do AI sinh ra.
- **PLO2** (Kỹ năng): Thu thập, phân tích và đặc tả yêu cầu rõ ràng, kiểm chứng được cho cả con người và AI agent.
  - PI2.1: Viết câu chuyện người dùng, tiêu chí chấp nhận và đặc tả kỹ thuật đạt rubric đặc tả của Khoa.
  - PI2.2: Đặc tả được một tính năng đủ để AI agent cài đặt và vượt qua bộ kiểm thử chấp nhận cho trước.
- **PLO3** (Kỹ năng): Thiết kế kiến trúc, dữ liệu, API và giao diện cho hệ thống phần mềm có quy mô.
  - PI3.1: Lập và bảo vệ bản thiết kế kiến trúc có ghi chép quyết định (ADR) cho một sản phẩm nhiều thành phần.
  - PI3.2: Thiết kế cơ sở dữ liệu và API đáp ứng yêu cầu chức năng và phi chức năng đã đặc tả.
- **PLO4** (Kỹ năng): Lập trình thành thạo và làm việc hiệu quả cùng trợ lý lập trình AI, AI agent theo quy trình có kiểm soát.
  - PI4.1: Hoàn thành bài thực hành lập trình trong thời gian quy định cả khi có và không có AI.
  - PI4.2: Điều phối AI agent hoàn thành một tác vụ nhiều bước, có nhật ký, đánh giá và từ chối được đề xuất sai.
- **PLO5** (Kỹ năng): Kiểm chứng chất lượng phần mềm bằng kiểm thử tự động, review, phân tích bảo mật và đo lường.
  - PI5.1: Xây bộ kiểm thử tự động đạt ngưỡng bao phủ và phát hiện được lỗi gieo sẵn (mutation).
  - PI5.2: Phát hiện và khắc phục lỗ hổng bảo mật phổ biến trong mã do người và AI viết.
- **PLO6** (Kỹ năng): Triển khai và vận hành phần mềm trên đám mây với CI/CD, giám sát và quản lý sự cố.
  - PI6.1: Thiết lập pipeline CI/CD triển khai tự động một sản phẩm lên môi trường đám mây.
  - PI6.2: Đặt chỉ số, cảnh báo và xử lý một sự cố giả lập theo quy trình.
- **PLO7** (Năng lực AI): Xây dựng, đánh giá và quản trị tính năng AI trong sản phẩm phần mềm.
  - PI7.1: Tích hợp mô hình ngôn ngữ (RAG hoặc agent) vào sản phẩm và đánh giá bằng bộ đánh giá (eval) có chỉ số.
  - PI7.2: Lập hồ sơ rủi ro AI của sản phẩm: dữ liệu, an toàn, chi phí, tuân thủ Luật Trí tuệ nhân tạo.
- **PLO8** (Kỹ năng): Làm việc nhóm theo Agile, giao tiếp kỹ thuật, đọc hiểu và viết tài liệu kỹ thuật tiếng Anh, làm việc với khách hàng.
  - PI8.1: Hoàn thành vai trò trong nhóm qua các sprint, được đánh giá chéo và theo dữ liệu kho mã.
  - PI8.2: Viết tài liệu dự án bằng tiếng Anh (README, mô tả pull request, tệp ngữ cảnh cho AI agent) đạt rubric; trình bày sản phẩm rõ ràng trước khách hàng và hội đồng.
- **PLO9** (Tự chủ và trách nhiệm): Tuân thủ pháp luật, đạo đức nghề nghiệp và liêm chính học thuật khi sử dụng công nghệ và AI.
  - PI9.1: Khai báo đầy đủ, trung thực việc dùng AI theo quy tắc ứng xử của Trường trong mọi sản phẩm học thuật.
  - PI9.2: Phân tích được vấn đề pháp lý, đạo đức (dữ liệu cá nhân, sở hữu trí tuệ, AI) của một sản phẩm cụ thể.
- **PLO10** (Năng lực số và học tập suốt đời): Tự học, thích ứng công nghệ mới, có tư duy sản phẩm và đổi mới sáng tạo.
  - PI10.1: Tự học và áp dụng một công nghệ chưa được dạy để hoàn thành sản phẩm, có báo cáo phản tư.
  - PI10.2: Xây hồ sơ năng lực số gồm các sản phẩm, minh chứng đóng góp và kế hoạch phát triển nghề nghiệp.

## Khung năng lực AI

- **B1 Hiểu và dùng an toàn** (Năm 1): Biết AI làm được gì, sai ở đâu; đặt câu hỏi tốt; kiểm chứng câu trả lời; không đưa dữ liệu nhạy cảm vào công cụ công cộng.
- **B2 Cộng tác** (Năm 1–2): Lập trình cặp với AI, nhờ AI sinh test, review, giải thích; luôn hiểu và giải thích được mã mình nộp.
- **B3 Điều phối** (Năm 2): Viết đặc tả và ngữ cảnh cho AI agent, chia việc nhiều bước, đặt rào chắn (test, review, quyền hạn), đo chất lượng đầu ra.
- **B4 Xây dựng** (Năm 3): Xây tính năng AI trong sản phẩm: RAG, agent dùng công cụ; thiết kế bộ đánh giá (eval) và giám sát.
- **B5 Quản trị** (Năm 3): Đánh giá rủi ro, bảo mật, chi phí và tuân thủ pháp luật của hệ thống AI; ra quyết định khi nào không dùng AI.

## Thang mức dùng AI trong đánh giá

- **M1 Không AI:** Làm độc lập trong phòng thi có kiểm soát. Dùng cho bài thi nền tảng và vấn đáp.
- **M2 AI hỗ trợ học:** Được hỏi AI để hiểu bài, lên ý tưởng; không nộp nội dung do AI tạo.
- **M3 AI cộng tác có nhật ký:** AI được viết một phần sản phẩm; bắt buộc nhật ký AI và giải thích được mọi phần.
- **M4 AI toàn phần có kiểm chứng:** Được dùng AI agent tự do; chấm cả kết quả lẫn quy trình kiểm chứng, review, kiểm thử.
- **M5 Xây dựng AI:** Đối tượng đánh giá là chính hệ thống AI sinh viên xây và đánh giá.

## Kế hoạch 9 học kỳ

### Học kỳ 1 (14 TC)
Sản phẩm: Trang portfolio cá nhân và một ứng dụng web nhỏ chạy trên Internet.
- SOFT1001 Nhập môn Kỹ thuật phần mềm AI-native – 3 TC
- PROG2005 Cơ sở lập trình (Python, có trợ lý AI) – 4 TC
- MATH2005 Toán rời rạc và logic cho lập trình – 2 TC
- SOFT1101 Studio 1: Sản phẩm số đầu tiên – 2 TC
- POLI1001 Triết học Mác – Lênin – 3 TC

### Học kỳ 2 (13 TC)
Sản phẩm: Ứng dụng quản lý dữ liệu nhỏ, ví dụ sổ điểm cá nhân hoặc thư viện sách của câu lạc bộ.
- INFO2002 Cấu trúc dữ liệu và giải thuật – 3 TC
- INFO2007 Cơ sở dữ liệu – 3 TC
- PROG2101 Phát triển web full-stack – 3 TC
- SOFT1102 Studio 2: Ứng dụng dữ liệu – 2 TC
- POLI1002 Kinh tế chính trị Mác – Lênin – 2 TC

### Học kỳ 3 (14 TC)
Sản phẩm: Ứng dụng web có đăng nhập và cơ sở dữ liệu, có bạn bè trong lớp dùng thật.
- PROG2006 Lập trình hướng đối tượng và mã sạch – 3 TC
- MATH2101 Toán cho AI: Đại số tuyến tính và Xác suất thống kê – 3 TC
- ENGL2002 Tiếng Anh kỹ thuật cho kỹ sư phần mềm – 2 TC
- SOFT3003 Thiết kế trải nghiệm người dùng – 2 TC
- SOFT1103 Studio 3: Sản phẩm có người dùng – 2 TC
- POLI1003 Chủ nghĩa xã hội khoa học – 2 TC

### Học kỳ 4 (15 TC)
Sản phẩm: Bản đầu tiên của ứng dụng di động làm theo nhóm, viết từ đặc tả.
- SOFT2001 Kỹ nghệ yêu cầu và đặc tả cho người và AI agent – 3 TC
- SOFT2002 Kiến trúc phần mềm: ra quyết định cùng AI – 3 TC
- PROG3002 Phát triển ứng dụng di động – 3 TC
- SOFT2003 Hệ thống máy tính và mạng cho kỹ sư phần mềm – 2 TC
- SOFT1201 Studio 4: Ứng dụng di động nhóm – 2 TC
- LAW1001 Pháp luật đại cương – 2 TC

### Học kỳ 5 (13 TC)
Sản phẩm: Sản phẩm nhóm cho người dùng trong trường, có kiểm thử tự động và triển khai tự động lên cloud.
- INFO2011 Công nghệ phần mềm: sản phẩm và Agile – 2 TC
- SOFT4003 Kiểm thử và đảm bảo chất lượng phần mềm với AI – 3 TC
- INFO3008 DevOps, CI/CD và điện toán đám mây – 3 TC
- SOFT2004 Kỹ nghệ phần mềm với AI agent – 3 TC
- SOFT1202 Studio 5: Sản phẩm cho cộng đồng trường – 2 TC

### Học kỳ 6 (14 TC)
Sản phẩm: Sản phẩm giải bài toán thật của một công ty thuộc Tập đoàn Công nghệ CMC, kèm báo cáo bảo mật.
- SOFT3001 Học máy ứng dụng cho kỹ sư phần mềm – 3 TC
- SOFT3002 Bảo mật ứng dụng và an toàn mã do AI sinh – 3 TC
- SOFT3007 Chủ đề hiện đại trong Kỹ thuật phần mềm – 3 TC
- SOFT2101 Studio 6: Dự án doanh nghiệp – 3 TC
- POLI1004 Lịch sử Đảng Cộng sản Việt Nam – 2 TC

### Học kỳ 7 (13 TC)
Sản phẩm: Một tính năng AI (trợ lý, tìm kiếm thông minh hoặc agent) tích hợp vào sản phẩm, kèm báo cáo đánh giá độ tin cậy.
- SOFT3004 Phát triển ứng dụng mô hình ngôn ngữ lớn – 3 TC
- SOFT3005 Hệ thống phân tán, dữ liệu và vận hành – 3 TC
- INFO3001 Pháp lý, đạo đức nghề nghiệp và AI có trách nhiệm – 2 TC
- SOFT3008 Nghiên cứu và đổi mới trong Kỹ thuật phần mềm – 3 TC
- SOFT2102 Studio 7: Tính năng AI có đánh giá – 2 TC

### Học kỳ 8 (13 TC)
- SOFT3901 Thực tập OJT tại doanh nghiệp – 6 TC
- TRACK-1 Học phần chuyên sâu 1 – 3 TC
- SOFT3006 Đổi mới sáng tạo và khởi nghiệp sản phẩm số – 2 TC
- POLI1005 Tư tưởng Hồ Chí Minh – 2 TC

### Học kỳ 9 (14 TC)
- TRACK-2 Học phần chuyên sâu 2 – 3 TC
- ELEC-1 Học phần tự chọn liên ngành – 3 TC
- SOFT3902 Đồ án tốt nghiệp – 8 TC

## Đề cương rút gọn

### SOFT1001 Nhập môn Kỹ thuật phần mềm AI-native (3 TC, HK1)
Nhập môn ngành theo hướng làm sản phẩm: phần mềm được làm ra thế nào, vai trò của kỹ sư phần mềm khi có AI, cách học hiệu quả với AI, máy tính và mạng ở mức đủ dùng, đạo đức và an toàn khi dùng AI. Sinh viên xây và đưa trang portfolio cá nhân lên Internet ngay trong 3 tuần đầu.

- CLO1: Mô tả vòng đời phần mềm và vai trò của người, trợ lý AI, AI agent trong một đội phần mềm. (→ PLO10)
- CLO2: Dùng dòng lệnh, Git, trình soạn thảo và trợ lý AI để làm và đưa một trang web lên Internet. (→ PLO4)
- CLO3: Áp dụng quy tắc dùng AI an toàn, trung thực và khai báo được việc dùng AI. (→ PLO9)

Giáo trình chính: MIT Missing Semester of Your CS Education, bản 2026 (học liệu mở); Tài liệu Quy tắc ứng xử về AI của Khoa (theo Thông tư 49/2026)
Tham khảo: Addy Osmani, Beyond Vibe Coding: From Coder to AI-Era Developer, O'Reilly, 2025 – chương 1–3; Leo Porter, Daniel Zingaro, Learn AI-Assisted Python Programming, 2nd ed., Manning, 2024 – chương 1; SWEBOK Guide V4.0 – chương giới thiệu
Khóa học tham chiếu: CS50x 2026 và trợ giảng AI CS50 Duck (Harvard University · edX · 2026); The Missing Semester of Your CS Education (bản 2026) (MIT CSAIL · 2026); 15-113 Effective Coding with AI (Carnegie Mellon University · 2025); Generative AI for Software Development (3 khóa) (DeepLearning.AI · Coursera · 2024–2025)

Kế hoạch 10 tuần:
1. Ngành Kỹ thuật phần mềm, nghề kỹ sư phần mềm thời AI; cách học trong chương trình AI-native; quy tắc ứng xử về AI.
2. Dòng lệnh, tệp, Git và GitHub; môi trường phát triển trên cloud có trợ lý AI (theo Missing Semester 2026).
3. Web hoạt động thế nào: HTTP, HTML, CSS; xây và đưa portfolio cá nhân lên Internet.
4. AI tạo sinh và mô hình ngôn ngữ: làm được gì, sai thế nào; luyện hỏi AI như hỏi gia sư (mô hình CS50 Duck) và kiểm chứng câu trả lời.
5. Thuật toán và lưu đồ; từ bài toán đến chương trình; dùng AI để giải thích, không để làm hộ.
6. Vòng đời phần mềm và các vai trò: yêu cầu, thiết kế, lập trình, kiểm thử, vận hành; ai làm gì khi có AI agent.
7. Mạng máy tính và Internet ở mức kỹ sư phần mềm cần: DNS, máy chủ, dịch vụ đám mây.
8. Dữ liệu, quyền riêng tư và bảo mật cơ bản; Luật Trí tuệ nhân tạo và liêm chính học thuật.
9. Làm việc nhóm, giao tiếp kỹ thuật, ghi nhật ký AI và phản tư.
10. Trình bày portfolio và kế hoạch học tập cá nhân; kiểm tra cuối kỳ.

Đánh giá: Tự học trên Trợ giảng AI 5% (M2); Bài thực hành 20% (M3); Giữa kỳ: sản phẩm/bài tập lớn 25% (M4); Cuối kỳ: sản phẩm + vấn đáp cá nhân 50% (M4 + M1)

### PROG2005 Cơ sở lập trình (Python, có trợ lý AI) (4 TC, HK1)
Tư duy lập trình và Python: biến, kiểu dữ liệu, rẽ nhánh, vòng lặp, hàm, cấu trúc dữ liệu có sẵn, xử lý tệp và ngoại lệ, kiểm thử đơn vị đầu tiên. Trợ lý AI được dùng như gia sư trong giờ thực hành; các bài thi đo năng lực lập trình độc lập, không dùng AI.

- CLO1: Viết chương trình Python giải bài toán nhỏ, đúng và dễ đọc, không cần AI. (→ PLO1, PLO4)
- CLO2: Đọc hiểu, tìm và sửa lỗi trong chương trình của người khác hoặc do AI sinh. (→ PLO4)
- CLO3: Viết kiểm thử đơn vị cho hàm do mình viết hoặc do AI sinh. (→ PLO5)

Giáo trình chính: Leo Porter, Daniel Zingaro, Learn AI-Assisted Python Programming, 2nd ed., Manning, 2024
Tham khảo: Tony Gaddis, Starting Out with Python, Pearson; CS50's Introduction to Programming with Python (bài giảng mở)
Khóa học tham chiếu: CS50x 2026 và trợ giảng AI CS50 Duck (Harvard University · edX · 2026); Learn AI-Assisted Python Programming – cách dạy của UC San Diego (UC San Diego · Manning 2024)

Kế hoạch 10 tuần:
1. Giới thiệu Python, môi trường, biến, kiểu dữ liệu, nhập xuất; quy tắc dùng trợ lý AI trong học phần.
2. Biểu thức, rẽ nhánh; đọc lỗi và gỡ lỗi; nhờ AI giải thích thông báo lỗi.
3. Vòng lặp; mẫu bài toán đếm, tổng, tìm kiếm.
4. Hàm, tham số, phạm vi biến; phân rã bài toán thành hàm nhỏ; viết kiểm thử trước khi nhờ AI sinh mã (theo Porter & Zingaro).
5. Chuỗi, danh sách, bộ; xử lý văn bản.
6. Từ điển, tập hợp; bài toán dữ liệu nhỏ. Giữa kỳ: thi thực hành trên máy không AI.
7. Tệp, ngoại lệ; đọc và ghi dữ liệu CSV/JSON.
8. Lập trình hướng đối tượng mở đầu trong Python; module và thư viện.
9. Đọc mã do AI sinh: tìm lỗi cài cắm, ca biên bị bỏ sót; viết thêm kiểm thử để chứng minh lỗi.
10. Ôn tập, dự án nhỏ; thi cuối kỳ không AI.

Đánh giá: Tự học trên Trợ giảng AI 10% (M2); Thực hành hằng tuần 20% (M3); Giữa kỳ: thi thực hành trên máy 20% (M1); Cuối kỳ: thi tự luận/thực hành 50% (M1)

### MATH2005 Toán rời rạc và logic cho lập trình (2 TC, HK1)
Tinh gọn từ 3 xuống 2 tín chỉ, giữ phần kỹ sư phần mềm dùng hằng ngày: logic (để đặc tả và kiểm thử), tập hợp, quan hệ, đếm, đồ thị và cây; mọi chủ đề học qua bài cài đặt Python. Bớt phần chứng minh hình thức và hệ đếm, đại số Bool chuyển thành tự học có Trợ giảng AI.

- CLO1: Dùng logic, tập hợp, quan hệ để mô hình hóa và đặc tả bài toán tin học. (→ PLO1)
- CLO2: Giải bài toán đếm và đồ thị cơ bản, cài đặt được bằng Python. (→ PLO1)

Giáo trình chính: Kenneth Rosen, Discrete Mathematics and Its Applications, 8th ed., McGraw-Hill
Tham khảo: Lehman, Leighton, Meyer, Mathematics for Computer Science (MIT, bản mở)
Khóa học tham chiếu: 6.042J Mathematics for Computer Science (MIT OpenCourseWare); CS50x 2026 và trợ giảng AI CS50 Duck (Harvard University · edX · 2026)

Kế hoạch 10 tuần:
1. Logic mệnh đề; điều kiện trong chương trình và đặc tả.
2. Logic vị từ; tiền điều kiện, hậu điều kiện, bất biến.
3. Tập hợp, quan hệ, hàm; ánh xạ sang kiểu dữ liệu Python.
4. Phương pháp đếm; đếm số ca kiểm thử.
5. Đệ quy và quy nạp qua bài lập trình; giữa kỳ.
6. Đồ thị: khái niệm, biểu diễn bằng Python.
7. Duyệt đồ thị; đường đi.
8. Cây; cây quyết định.
9. Ứng dụng: phụ thuộc gói, lập lịch, mạng xã hội.
10. Ôn tập; thi cuối kỳ.

Đánh giá: Tự học trên Trợ giảng AI 10% (M2); Thực hành hằng tuần 20% (M3); Giữa kỳ: thi thực hành trên máy 20% (M1); Cuối kỳ: thi tự luận/thực hành 50% (M1)

### SOFT1101 Studio 1: Sản phẩm số đầu tiên (2 TC, HK1)
Học phần dự án xuyên suốt của học kỳ 1. Sinh viên làm cá nhân, tập quy trình làm ra một sản phẩm nhỏ hoàn chỉnh và tập dùng AI như gia sư.

- CLO1: Lập kế hoạch một sản phẩm số nhỏ cho chính mình, có mục tiêu rõ. (→ PLO10)
- CLO2: Xây sản phẩm chạy trên Internet, dùng AI ở mức được phép và có nhật ký. (→ PLO4)
- CLO3: Giải thích được mọi phần mã của mình khi không có AI. (→ PLO4)

Giáo trình chính: Ryan Singer, Shape Up (Basecamp, bản đọc trực tuyến miễn phí); Hướng dẫn Studio và rubric của Khoa
Tham khảo: Addy Osmani, Beyond Vibe Coding: From Coder to AI-Era Developer, O'Reilly, 2025
Khóa học tham chiếu: 15-113 Effective Coding with AI (Carnegie Mellon University · 2025); CSCI 1970 Agentic Studio (Brown University · 2026)

Kế hoạch 10 tuần:
1. Khởi động: chọn bài toán, phỏng vấn người dùng, viết đặc tả và tiêu chí chấp nhận cho trang portfolio cá nhân và một ứng dụng web nhỏ chạy trên internet.
2. Thiết kế: phác thảo giao diện, dữ liệu, kiến trúc; chia việc; thiết lập kho mã, CI và quy ước dùng AI.
3. Sprint 1: lát cắt chức năng đầu tiên chạy được từ đầu đến cuối; trang portfolio đưa lên mạng ngay tuần 3.
4. Sprint 1 (tiếp): kiểm thử, review chéo; Sprint review 1 với giảng viên.
5. Sprint 2: mở rộng chức năng chính; thêm một ứng dụng nhỏ như sổ tay học tập hoặc trò chơi đố vui.
6. Sprint 2 (tiếp): đo chất lượng, sửa lỗi; Sprint review 2, đối chiếu nhật ký AI.
7. Sprint 3: hoàn thiện; hoàn thiện giao diện và nội dung.
8. Sprint 3 (tiếp): thử nghiệm với người dùng thật, thu phản hồi; Sprint review 3.
9. Làm cứng sản phẩm: kiểm thử hồi quy, rà soát bảo mật, tài liệu, chuẩn bị trình diễn.
10. Demo Day: trình diễn trước hội đồng; vấn đáp cá nhân giải thích code; phản tư.

Đánh giá: Sprint review (3 lần) 30% (M4); Nhật ký AI và phản tư 10% (M3); Demo Day tuần 10 40% (M4); Vấn đáp cá nhân: giải thích code 20% (M1)

### INFO2002 Cấu trúc dữ liệu và giải thuật (3 TC, HK2)
Kiểu dữ liệu trừu tượng, danh sách, ngăn xếp, hàng đợi, bảng băm, cây, đồ thị; sắp xếp, tìm kiếm; chia để trị, quy hoạch động; phân tích độ phức tạp. Đây là học phần nền tảng giữ thi không AI để bảo đảm năng lực tự giải bài toán; AI được dùng để luyện tập và so sánh lời giải. v2027.3 chuyển 10 tiết lý thuyết sang thực hành cài đặt, đo hiệu năng.

- CLO1: Chọn và cài đặt cấu trúc dữ liệu phù hợp theo yêu cầu hiệu năng. (→ PLO1)
- CLO2: Phân tích độ phức tạp, so sánh và cải tiến lời giải, kể cả lời giải do AI đưa ra. (→ PLO1)
- CLO3: Giải bài toán thuật toán trong thời gian giới hạn không dùng AI. (→ PLO1)

Giáo trình chính: Goodrich, Tamassia, Goldwasser, Data Structures and Algorithms in Python, Wiley
Tham khảo: Aditya Bhargava, Grokking Algorithms, 2nd ed., Manning, 2024; Cormen và cộng sự, Introduction to Algorithms, 4th ed., MIT Press
Khóa học tham chiếu: Algorithms, Part I & II (Princeton University · Coursera); 6.006 Introduction to Algorithms (MIT OpenCourseWare); CS50x 2026 và trợ giảng AI CS50 Duck (Harvard University · edX · 2026)

Kế hoạch 10 tuần:
1. Giới thiệu, phân tích độ phức tạp; luật dùng AI để luyện tập.
2. Mảng, danh sách liên kết, ngăn xếp, hàng đợi.
3. Bảng băm; sắp xếp cơ bản.
4. Sắp xếp nâng cao, tìm kiếm nhị phân; đo thời gian chạy thực nghiệm, so sánh với lời giải AI đề xuất và giải thích chênh lệch.
5. Cây, cây nhị phân tìm kiếm.
6. Cây cân bằng, heap; giữa kỳ thi thực hành không AI.
7. Đồ thị: biểu diễn, duyệt.
8. Đường đi ngắn nhất, cây khung.
9. Chia để trị, quy hoạch động.
10. Ôn tập; thi cuối kỳ không AI.

Đánh giá: Tự học trên Trợ giảng AI 10% (M2); Thực hành hằng tuần 20% (M3); Giữa kỳ: thi thực hành trên máy 20% (M1); Cuối kỳ: thi tự luận/thực hành 50% (M1)

### INFO2007 Cơ sở dữ liệu (3 TC, HK2)
Mô hình quan hệ, SQL, mô hình E-R, chuẩn hóa, giao tác, chỉ mục; thực hành trên PostgreSQL. Bổ sung: dùng AI sinh và rà soát truy vấn, nhận diện truy vấn sai hoặc không an toàn; giới thiệu cơ sở dữ liệu vector cho ứng dụng AI.

- CLO1: Thiết kế lược đồ cơ sở dữ liệu quan hệ chuẩn hóa từ yêu cầu. (→ PLO3)
- CLO2: Viết và tối ưu truy vấn SQL; phát hiện truy vấn sai, không an toàn do AI sinh. (→ PLO1)
- CLO3: Tích hợp cơ sở dữ liệu vào một ứng dụng, kể cả tìm kiếm vector cơ bản. (→ PLO3)

Giáo trình chính: Silberschatz, Korth, Sudarshan, Database System Concepts, 7th ed., McGraw-Hill
Tham khảo: Martin Kleppmann, Chris Riccomini, Designing Data-Intensive Applications, 2nd ed., O'Reilly, 2026 – chương 3–4; Tài liệu PostgreSQL và pgvector
Khóa học tham chiếu: 15-445/645 Database Systems (Carnegie Mellon University); Generative AI for Software Development (3 khóa) (DeepLearning.AI · Coursera · 2024–2025)

Kế hoạch 10 tuần:
1. Giới thiệu hệ cơ sở dữ liệu; PostgreSQL.
2. Mô hình quan hệ, đại số quan hệ.
3. SQL: truy vấn cơ bản.
4. SQL nâng cao: kết nối, gộp nhóm, truy vấn con; AI chuyển câu hỏi thành SQL, sinh viên kiểm chứng bằng bộ dữ liệu có đáp án.
5. Mô hình E-R; từ yêu cầu đến lược đồ.
6. Chuẩn hóa; giữa kỳ.
7. Giao tác, khóa, chỉ mục và hiệu năng.
8. Bảo mật dữ liệu, SQL injection, phân quyền.
9. NoSQL và cơ sở dữ liệu vector (pgvector) cho ứng dụng AI; kiểm định dữ liệu thử do AI sinh.
10. Ôn tập; thi cuối kỳ.

Đánh giá: Tự học trên Trợ giảng AI 10% (M2); Thực hành hằng tuần 20% (M3); Giữa kỳ: thi thực hành trên máy 20% (M1); Cuối kỳ: thi tự luận/thực hành 50% (M1)

### PROG2101 Phát triển web full-stack (3 TC, HK2)
JavaScript/TypeScript, giao diện web theo thành phần, API REST, xác thực người dùng, kết nối cơ sở dữ liệu, triển khai lên cloud. Lập trình cặp với AI có nhật ký; mỗi sinh viên phải giải thích được toàn bộ mã của mình.

- CLO1: Xây ứng dụng web có giao diện, API, đăng nhập và cơ sở dữ liệu. (→ PLO4)
- CLO2: Dùng trợ lý AI có kiểm soát: nhật ký, kiểm thử, giải thích được mã. (→ PLO4)
- CLO3: Triển khai ứng dụng web lên môi trường đám mây. (→ PLO6)

Giáo trình chính: Full Stack Open, University of Helsinki (học liệu mở); MDN Web Docs
Tham khảo: Addy Osmani, Beyond Vibe Coding: From Coder to AI-Era Developer, O'Reilly, 2025 – chương 7 (quy trình web với AI); CS50W bài giảng mở
Khóa học tham chiếu: Full Stack Open (University of Helsinki); CS50's Web Programming with Python and JavaScript (Harvard University · edX); Generative AI for Software Development (3 khóa) (DeepLearning.AI · Coursera · 2024–2025)

Kế hoạch 10 tuần:
1. JavaScript hiện đại và TypeScript; công cụ phát triển.
2. DOM, sự kiện, gọi API.
3. Khung giao diện theo thành phần (React hoặc tương đương).
4. Quản lý trạng thái, định tuyến, biểu mẫu.
5. Máy chủ Node.js, API REST.
6. Kết nối cơ sở dữ liệu; dựng khung dự án bằng AI rồi review từng tệp; giữa kỳ: nộp ứng dụng có CRUD.
7. Xác thực, phân quyền, bảo mật web cơ bản.
8. Kiểm thử thành phần và API; AI sinh kiểm thử, sinh viên đo độ bao phủ và bổ sung ca biên.
9. Triển khai lên cloud; tên miền, HTTPS.
10. Trình diễn ứng dụng, vấn đáp.

Đánh giá: Tự học trên Trợ giảng AI 5% (M2); Bài thực hành 20% (M3); Giữa kỳ: sản phẩm/bài tập lớn 25% (M4); Cuối kỳ: sản phẩm + vấn đáp cá nhân 50% (M4 + M1)

### SOFT1102 Studio 2: Ứng dụng dữ liệu (2 TC, HK2)
Học phần dự án xuyên suốt của học kỳ 2. Sinh viên làm theo cặp, kết hợp kiến thức cơ sở dữ liệu và lập trình, dùng AI sinh dữ liệu thử.

- CLO1: Thiết kế dữ liệu cho một ứng dụng nhỏ từ nhu cầu người dùng. (→ PLO3)
- CLO2: Xây ứng dụng dữ liệu có kiểm thử, dùng AI sinh dữ liệu thử có kiểm định. (→ PLO4)
- CLO3: Giải thích được truy vấn và mã của mình khi không có AI. (→ PLO4)

Giáo trình chính: Ryan Singer, Shape Up (Basecamp, bản đọc trực tuyến miễn phí); Hướng dẫn Studio và rubric của Khoa
Tham khảo: Addy Osmani, Beyond Vibe Coding: From Coder to AI-Era Developer, O'Reilly, 2025
Khóa học tham chiếu: CSCI 1970 Agentic Studio (Brown University · 2026)

Kế hoạch 10 tuần:
1. Khởi động: chọn bài toán, phỏng vấn người dùng, viết đặc tả và tiêu chí chấp nhận cho ứng dụng quản lý dữ liệu nhỏ, ví dụ sổ điểm cá nhân hoặc thư viện sách của câu lạc bộ.
2. Thiết kế: phác thảo giao diện, dữ liệu, kiến trúc; chia việc; thiết lập kho mã, CI và quy ước dùng AI.
3. Sprint 1: lát cắt chức năng đầu tiên chạy được từ đầu đến cuối; thiết kế cơ sở dữ liệu và các thao tác cơ bản.
4. Sprint 1 (tiếp): kiểm thử, review chéo; Sprint review 1 với giảng viên.
5. Sprint 2: mở rộng chức năng chính; tìm kiếm, thống kê, xuất dữ liệu.
6. Sprint 2 (tiếp): đo chất lượng, sửa lỗi; Sprint review 2, đối chiếu nhật ký AI.
7. Sprint 3: hoàn thiện; kiểm thử và xử lý dữ liệu lỗi.
8. Sprint 3 (tiếp): thử nghiệm với người dùng thật, thu phản hồi; Sprint review 3.
9. Làm cứng sản phẩm: kiểm thử hồi quy, rà soát bảo mật, tài liệu, chuẩn bị trình diễn.
10. Demo Day: trình diễn trước hội đồng; vấn đáp cá nhân giải thích code; phản tư.

Đánh giá: Sprint review (3 lần) 30% (M4); Nhật ký AI và phản tư 10% (M3); Demo Day tuần 10 40% (M4); Vấn đáp cá nhân: giải thích code 20% (M1)

### PROG2006 Lập trình hướng đối tượng và mã sạch (3 TC, HK3)
Đóng gói, kế thừa, đa hình, trừu tượng; mẫu thiết kế; tái cấu trúc và mã sạch; kiểm thử đơn vị. Cập nhật: thực hành tái cấu trúc mã do AI sinh, đánh giá thiết kế đề xuất bởi AI theo nguyên lý SOLID.

- CLO1: Thiết kế lớp và quan hệ giữa các lớp theo nguyên lý hướng đối tượng. (→ PLO3)
- CLO2: Áp dụng mẫu thiết kế và tái cấu trúc mã, kể cả mã do AI sinh. (→ PLO4)
- CLO3: Viết kiểm thử đơn vị cho chương trình hướng đối tượng. (→ PLO1)

Giáo trình chính: Martin Fowler, Refactoring, 2nd ed., Addison-Wesley; Eric Freeman, Elisabeth Robson, Head First Design Patterns, 2nd ed., O'Reilly
Tham khảo: C. Thomas Wu, An Introduction to Object-Oriented Programming with Java, McGraw-Hill; Robert Martin, Clean Code
Khóa học tham chiếu: Generative AI for Software Development (3 khóa) (DeepLearning.AI · Coursera · 2024–2025); 17-313 Foundations of Software Engineering (bài AI for SE, Vibe coding) (Carnegie Mellon University · 2025–2026)

Kế hoạch 10 tuần:
1. Lập trình trên ngôn ngữ hướng đối tượng (Java hoặc TypeScript); đóng gói.
2. Kế thừa.
3. Đa hình.
4. Trừu tượng, giao diện; nguyên lý SOLID.
5. Kiểu dữ liệu nâng cao, generic, collection; giữa kỳ.
6. Mẫu thiết kế khởi tạo và cấu trúc.
7. Mẫu thiết kế hành vi.
8. Mã sạch và tái cấu trúc theo danh mục ‘mùi mã’ của Fowler: thực hành trên mã do AI sinh, đo độ phức tạp trước/sau.
9. Kiểm thử đơn vị, mock.
10. Dự án nhỏ; thi cuối kỳ.

Đánh giá: Tự học trên Trợ giảng AI 10% (M2); Thực hành hằng tuần 20% (M3); Giữa kỳ: thi thực hành trên máy 20% (M1); Cuối kỳ: thi tự luận/thực hành 50% (M1)

### MATH2101 Toán cho AI: Đại số tuyến tính và Xác suất thống kê (3 TC, HK3)
Vectơ, ma trận, phép biến đổi tuyến tính, độ tương đồng; xác suất, phân phối, kỳ vọng, suy luận thống kê, kiểm định; ứng dụng trong học máy, tìm kiếm ngữ nghĩa và đánh giá A/B. Mọi chủ đề đều có bài thực hành Python.

- CLO1: Vận dụng đại số tuyến tính để biểu diễn và xử lý dữ liệu, nhúng (embedding). (→ PLO1, PLO7)
- CLO2: Vận dụng xác suất thống kê để đánh giá mô hình và thử nghiệm sản phẩm. (→ PLO1)

Giáo trình chính: Deisenroth, Faisal, Ong, Mathematics for Machine Learning, Cambridge University Press (bản mở)
Tham khảo: Gilbert Strang, Introduction to Linear Algebra
Khóa học tham chiếu: Mathematics for Machine Learning and Data Science (DeepLearning.AI · Coursera); Machine Learning Specialization (Andrew Ng) (DeepLearning.AI & Stanford Online · Coursera)

Kế hoạch 10 tuần:
1. Vectơ, độ dài, tích vô hướng; độ tương đồng cosine.
2. Ma trận, phép nhân, hệ phương trình.
3. Biến đổi tuyến tính; trị riêng ở mức ứng dụng.
4. Nhúng văn bản bằng mô hình có sẵn, tìm kiếm ngữ nghĩa với Python; trực quan hóa không gian nhúng.
5. Xác suất, biến cố, xác suất có điều kiện; giữa kỳ.
6. Biến ngẫu nhiên, phân phối.
7. Thống kê mô tả, ước lượng.
8. Kiểm định giả thuyết, thử nghiệm A/B.
9. Chỉ số đánh giá mô hình: độ chính xác, độ nhạy, F1; áp dụng cho tác vụ phân loại dùng LLM.
10. Ôn tập; thi cuối kỳ.

Đánh giá: Tự học trên Trợ giảng AI 10% (M2); Thực hành hằng tuần 20% (M3); Giữa kỳ: thi thực hành trên máy 20% (M1); Cuối kỳ: thi tự luận/thực hành 50% (M1)

### ENGL2002 Tiếng Anh kỹ thuật cho kỹ sư phần mềm (2 TC, HK3)
Gộp Tiếng Anh chuyên ngành 1 (3 TC) và Giao tiếp kỹ thuật bằng tiếng Anh (2 TC) thành một học phần 2 tín chỉ, tập trung vào việc kỹ sư phần mềm thật sự làm bằng tiếng Anh: đọc tài liệu, đặc tả, mã nguồn; viết README, issue, mô tả pull request, tệp ngữ cảnh cho AI agent. Dùng AI dịch, tóm tắt và sửa văn có kiểm chứng; luyện thuyết trình kỹ thuật ngắn. Chuẩn đầu ra ngoại ngữ chung theo quy định của Trường.

- CLO1: Đọc hiểu tài liệu kỹ thuật tiếng Anh, có dùng AI hỗ trợ và kiểm chứng được. (→ PLO8)
- CLO2: Viết tài liệu dự án ngắn bằng tiếng Anh cho người và cho AI agent. (→ PLO8)

Giáo trình chính: Google Technical Writing One & Two (miễn phí)
Tham khảo: Tài liệu tiếng Anh kỹ thuật của Khoa; Tài liệu Demo Day của Khoa
Khóa học tham chiếu: Technical Writing One & Two (Google for Developers · miễn phí); The Missing Semester of Your CS Education (bản 2026) (MIT CSAIL · 2026)

Kế hoạch 10 tuần:
1. Đọc tài liệu kỹ thuật: cấu trúc, từ vựng cốt lõi; dùng AI dịch và tóm tắt, kiểm chứng với bản gốc.
2. Đọc tài liệu API và thông báo lỗi; tìm câu trả lời trong tài liệu chính thức.
3. Viết README.
4. Viết issue và báo lỗi tái hiện được.
5. Mô tả pull request, nhận xét review; giữa kỳ.
6. Viết đặc tả ngắn và tệp hướng dẫn dự án cho AI agent bằng tiếng Anh.
7. Viết tài liệu thiết kế ngắn; AI góp ý độ rõ, sinh viên tự quyết định sửa.
8. Email và tin nhắn công việc với khách hàng, đồng nghiệp nước ngoài.
9. Thuyết trình kỹ thuật 3 phút.
10. Bài cuối kỳ: hồ sơ tài liệu tiếng Anh của Studio 3.

Đánh giá: Tự học trên Trợ giảng AI 5% (M2); Bài thực hành 20% (M3); Giữa kỳ: sản phẩm/bài tập lớn 25% (M4); Cuối kỳ: sản phẩm + vấn đáp cá nhân 50% (M4 + M1)

### SOFT3003 Thiết kế trải nghiệm người dùng (2 TC, HK3)
Nghiên cứu người dùng, thiết kế tương tác, nguyên mẫu, kiểm tra khả dụng, khả năng tiếp cận; thiết kế trải nghiệm cho tính năng AI (độ tin cậy, giải thích, sửa lỗi của AI). v2027.3 chuyển từ học kỳ 6 lên học kỳ 3 để đi cùng Studio 3 (sản phẩm có người dùng thật).

- CLO1: Thiết kế và kiểm tra khả dụng một giao diện. (→ PLO3)
- CLO2: Thiết kế trải nghiệm phù hợp cho tính năng AI từ nhu cầu người dùng. (→ PLO2, PLO3)

Giáo trình chính: Google UX Design Professional Certificate (học liệu Coursera); Don Norman, The Design of Everyday Things, bản cập nhật
Tham khảo: Google PAIR, People + AI Guidebook; Microsoft, Guidelines for Human-AI Interaction (HAX)
Khóa học tham chiếu: Google UX Design Professional Certificate (đã tích hợp AI) (Google · Coursera); People + AI Guidebook (Google PAIR); HAX Toolkit – Guidelines for Human-AI Interaction (Microsoft Research)

Kế hoạch 10 tuần:
1. Trải nghiệm người dùng là gì.
2. Nghiên cứu người dùng.
3. Kiến trúc thông tin, luồng.
4. Nguyên mẫu nhanh; AI tạo phương án giao diện, sinh viên phản biện theo nghiên cứu người dùng.
5. Kiểm tra khả dụng; giữa kỳ.
6. Khả năng tiếp cận.
7. Thiết kế cho tính năng AI: kỳ vọng, sai sót, quyền kiểm soát; kiểm tra bằng 18 nguyên tắc HAX.
8. Hệ thống thiết kế.
9. Đo trải nghiệm.
10. Bảo vệ thiết kế.

Đánh giá: Tự học trên Trợ giảng AI 5% (M2); Bài thực hành 20% (M3); Giữa kỳ: sản phẩm/bài tập lớn 25% (M4); Cuối kỳ: sản phẩm + vấn đáp cá nhân 50% (M4 + M1)

### SOFT1103 Studio 3: Sản phẩm có người dùng (2 TC, HK3)
Học phần dự án xuyên suốt của học kỳ 3. Sinh viên làm nhóm 2–3 người, đưa sản phẩm đến tay người dùng thật đầu tiên. Kết thúc học kỳ là Cổng năng lực 1.

- CLO1: Viết câu chuyện người dùng và tiêu chí chấp nhận cho sản phẩm có người dùng thật. (→ PLO2)
- CLO2: Xây và cải tiến sản phẩm theo phản hồi người dùng, có kiểm thử và nhật ký AI. (→ PLO4)
- CLO3: Làm việc nhóm 2–3 người, trình diễn và trả lời chất vấn. (→ PLO8)

Giáo trình chính: Ryan Singer, Shape Up (Basecamp, bản đọc trực tuyến miễn phí); Hướng dẫn Studio và rubric của Khoa
Tham khảo: Addy Osmani, Beyond Vibe Coding: From Coder to AI-Era Developer, O'Reilly, 2025
Khóa học tham chiếu: CSCI 1970 Agentic Studio (Brown University · 2026); Stanford CS146S The Modern Software Developer (Stanford University · 2025–2026)

Kế hoạch 10 tuần:
1. Khởi động: chọn bài toán, phỏng vấn người dùng, viết đặc tả và tiêu chí chấp nhận cho ứng dụng web có đăng nhập và cơ sở dữ liệu, có bạn bè trong lớp dùng thật.
2. Thiết kế: phác thảo giao diện, dữ liệu, kiến trúc; chia việc; thiết lập kho mã, CI và quy ước dùng AI.
3. Sprint 1: lát cắt chức năng đầu tiên chạy được từ đầu đến cuối; đăng nhập và dữ liệu người dùng.
4. Sprint 1 (tiếp): kiểm thử, review chéo; Sprint review 1 với giảng viên.
5. Sprint 2: mở rộng chức năng chính; tính năng chính theo phản hồi người dùng.
6. Sprint 2 (tiếp): đo chất lượng, sửa lỗi; Sprint review 2, đối chiếu nhật ký AI.
7. Sprint 3: hoàn thiện; đo số người dùng và sửa lỗi họ báo.
8. Sprint 3 (tiếp): thử nghiệm với người dùng thật, thu phản hồi; Sprint review 3.
9. Làm cứng sản phẩm: kiểm thử hồi quy, rà soát bảo mật, tài liệu, chuẩn bị trình diễn.
10. Demo Day: trình diễn trước hội đồng; vấn đáp cá nhân giải thích code; phản tư.

Đánh giá: Sprint review (3 lần) 30% (M4); Nhật ký AI và phản tư 10% (M3); Demo Day tuần 10 40% (M4); Vấn đáp cá nhân: giải thích code 20% (M1)

### SOFT2001 Kỹ nghệ yêu cầu và đặc tả cho người và AI agent (3 TC, HK4)
Thu thập và phân tích yêu cầu, câu chuyện người dùng, tiêu chí chấp nhận, đặc tả kỹ thuật, truy vết yêu cầu. Trọng tâm mới: viết đặc tả đủ rõ để AI agent cài đặt đúng, phát triển hướng đặc tả (spec-driven) và kiểm thử chấp nhận tự động.

- CLO1: Thu thập và phân tích yêu cầu từ người dùng thật. (→ PLO2)
- CLO2: Viết đặc tả kiểm chứng được cho người và AI agent. (→ PLO2, PLO4)
- CLO3: Đánh giá mức độ đúng của phần mềm do AI cài đặt so với đặc tả. (→ PLO2)

Giáo trình chính: Karl Wiegers, Candase Hokanson, Software Requirements Essentials, Addison-Wesley, 2023; GitHub Spec Kit – tài liệu Spec-Driven Development (mở)
Tham khảo: Wiegers, Beatty, Software Requirements, 3rd ed.; Addy Osmani, Beyond Vibe Coding: From Coder to AI-Era Developer, O'Reilly, 2025 – chương 2 (prompt là mã nguồn)
Khóa học tham chiếu: GitHub Spec Kit – Spec-Driven Development (GitHub · 2025–2026); Stanford CS146S The Modern Software Developer (Stanford University · 2025–2026); Claude Code: Software Engineering with Generative AI Agents (Vanderbilt University · Coursera · 2025)

Kế hoạch 10 tuần:
1. Vai trò của yêu cầu; vì sao đặc tả quan trọng hơn khi có AI.
2. Phỏng vấn, quan sát, chân dung người dùng; AI hỗ trợ tóm tắt phỏng vấn.
3. Câu chuyện người dùng, tiêu chí chấp nhận.
4. Yêu cầu phi chức năng: hiệu năng, bảo mật, khả dụng.
5. Mô hình hóa: use case, luồng, trạng thái.
6. Đặc tả kỹ thuật và hợp đồng API; giữa kỳ.
7. Phát triển hướng đặc tả với GitHub Spec Kit: constitution → specify → plan → tasks → implement; kiểm thử chấp nhận tự động.
8. Ngữ cảnh cho AI: tệp hướng dẫn dự án, ví dụ, ràng buộc; đo sai lệch giữa đặc tả và kết quả agent.
9. Truy vết và quản lý thay đổi yêu cầu.
10. Bảo vệ bộ đặc tả và kết quả cài đặt bằng AI.

Đánh giá: Tự học trên Trợ giảng AI 5% (M2); Bài thực hành 20% (M3); Giữa kỳ: sản phẩm/bài tập lớn 25% (M4); Cuối kỳ: sản phẩm + vấn đáp cá nhân 50% (M4 + M1)

### SOFT2002 Kiến trúc phần mềm: ra quyết định cùng AI (3 TC, HK4)
AI đã đề xuất được kiến trúc, sơ đồ, API và bản nháp ADR trong vài phút; việc của kỹ sư là đặt đúng thuộc tính chất lượng, so sánh phương án, kiểm chứng bằng nguyên mẫu và chịu trách nhiệm về quyết định. Học phần dạy các kiểu kiến trúc ở mức đủ để phán đoán (phân lớp, modular monolith, sự kiện, vi dịch vụ), dành phần lớn thời gian cho thực hành: viết kịch bản thuộc tính chất lượng, cho AI sinh nhiều phương án, đánh giá đánh đổi kiểu ATAM rút gọn, hàm kiểm chứng kiến trúc (fitness function) trong CI, ghi ADR và bảo vệ trước hội đồng.

- CLO1: Thiết kế kiến trúc cho sản phẩm nhiều thành phần từ thuộc tính chất lượng đã đặc tả. (→ PLO3)
- CLO2: Đánh giá, chọn và bảo vệ phương án kiến trúc (kể cả do AI đề xuất) bằng ADR, nguyên mẫu và hàm kiểm chứng. (→ PLO3)

Giáo trình chính: Mark Richards, Neal Ford, Fundamentals of Software Architecture, 2nd ed., O'Reilly, 2025
Tham khảo: Ian Sommerville, Engineering Software Products: An Introduction to Modern Software Engineering, Pearson, 2020; Ford, Richards, Sadalage, Dehghani, Software Architecture: The Hard Parts; Ford, Parsons, Kua, Sadalage, Building Evolutionary Architectures, 2nd ed., O'Reilly
Khóa học tham chiếu: Generative AI for Software Development (3 khóa) (DeepLearning.AI · Coursera · 2024–2025); 17-313 Foundations of Software Engineering (bài AI for SE, Vibe coding) (Carnegie Mellon University · 2025–2026)

Kế hoạch 10 tuần:
1. Kiến trúc là các quyết định khó đảo ngược; vai trò của kỹ sư khi AI vẽ được kiến trúc.
2. Thuộc tính chất lượng và kịch bản đo được.
3. Kiểu kiến trúc cốt lõi: phân lớp, modular monolith, khách–chủ.
4. Thiết kế API và dữ liệu: AI sinh bản nháp, sinh viên rà soát hợp đồng.
5. Cho AI sinh 3 phương án, so sánh đánh đổi; giữa kỳ.
6. Kiến trúc hướng sự kiện và vi dịch vụ: khi nào nên, khi nào không.
7. Nguyên mẫu xương sống (walking skeleton) để kiểm chứng giả định.
8. ADR và hàm kiểm chứng kiến trúc chạy trong CI.
9. Kiến trúc cho ứng dụng có thành phần AI: cổng mô hình, đánh giá, rào chắn, chi phí.
10. Bảo vệ thiết kế: giải thích vì sao chọn và vì sao không chọn.

Đánh giá: Tự học trên Trợ giảng AI 5% (M2); Bài thực hành 20% (M3); Giữa kỳ: sản phẩm/bài tập lớn 25% (M4); Cuối kỳ: sản phẩm + vấn đáp cá nhân 50% (M4 + M1)

### PROG3002 Phát triển ứng dụng di động (3 TC, HK4)
Phát triển đa nền tảng với React Native hoặc Flutter: giao diện theo thành phần, điều hướng, dữ liệu, gọi API, lưu trữ, triển khai. Cập nhật: dùng AI agent theo đặc tả, kiểm thử giao diện tự động, tích hợp tính năng AI trên thiết bị di động.

- CLO1: Xây ứng dụng di động đa nền tảng kết nối API. (→ PLO4)
- CLO2: Dùng AI agent theo đặc tả và kiểm chứng bằng kiểm thử. (→ PLO4)
- CLO3: Thiết kế cấu trúc ứng dụng di động và phát hành bản thử nghiệm. (→ PLO3)

Giáo trình chính: Meta React Native Specialization (học liệu Coursera); Tài liệu React Native chính thức
Tham khảo: Sakhniuk, Boduch, React and React Native, 5th ed., Packt, 2024
Khóa học tham chiếu: Meta React Native Specialization (Meta · Coursera); Stanford CS146S The Modern Software Developer (Stanford University · 2025–2026)

Kế hoạch 10 tuần:
1. Tổng quan lập trình di động, mô hình phát triển.
2. Môi trường, ngôn ngữ, thành phần cơ bản.
3. Kiến trúc giao diện theo thành phần, quản lý trạng thái.
4. Thiết kế giao diện, nguyên tắc bố cục.
5. Giữa kỳ: nguyên mẫu giao diện.
6. Quản lý và hiển thị dữ liệu, gọi API.
7. Điều hướng, lưu trữ cục bộ.
8. Kiểm thử giao diện tự động; AI agent làm tính năng theo đặc tả, chỉ nhận khi qua kiểm thử.
9. Tích hợp tính năng AI và phát hành thử nghiệm.
10. Trình diễn, vấn đáp.

Đánh giá: Tự học trên Trợ giảng AI 5% (M2); Bài thực hành 20% (M3); Giữa kỳ: sản phẩm/bài tập lớn 25% (M4); Cuối kỳ: sản phẩm + vấn đáp cá nhân 50% (M4 + M1)

### SOFT2003 Hệ thống máy tính và mạng cho kỹ sư phần mềm (2 TC, HK4)
Tinh gọn từ 3 xuống 2 tín chỉ, học qua sự cố thật của ứng dụng: tiến trình, bộ nhớ, đồng thời; TCP/IP, HTTP, DNS, TLS; container. Bỏ chi tiết lớp vật lý, định tuyến; mỗi tuần một bài chẩn đoán: AI gợi ý nguyên nhân từ log, sinh viên kiểm chứng bằng công cụ đo.

- CLO1: Giải thích cách hệ điều hành và mạng ảnh hưởng đến ứng dụng. (→ PLO1)
- CLO2: Chẩn đoán sự cố hiệu năng và kết nối của ứng dụng, kiểm chứng giả thuyết do AI gợi ý. (→ PLO6)

Giáo trình chính: James Kurose, Keith Ross, Computer Networking: A Top-Down Approach, 9th ed., Pearson, 2025; Remzi & Andrea Arpaci-Dusseau, Operating Systems: Three Easy Pieces (sách mở)
Tham khảo: Peterson, Davie, Computer Networks: A Systems Approach (sách mở); Bryant, O'Hallaron, Computer Systems: A Programmer's Perspective
Khóa học tham chiếu: The Missing Semester of Your CS Education (bản 2026) (MIT CSAIL · 2026); 15-213 Introduction to Computer Systems (Carnegie Mellon University)

Kế hoạch 10 tuần:
1. Tiến trình, luồng; đọc thông tin tiến trình từ dòng lệnh.
2. Bộ nhớ, rò rỉ bộ nhớ; hệ tệp.
3. Đồng thời và tranh chấp dữ liệu qua ví dụ web.
4. TCP/IP qua công cụ: ping, traceroute, ss.
5. HTTP, HTTP/3 và QUIC, DNS, TLS (theo Kurose & Ross bản 9); giữa kỳ.
6. Container và ảo hóa.
7. Gỡ lỗi mạng: AI gợi ý từ log, kiểm chứng bằng công cụ đo.
8. Hiệu năng ứng dụng, bộ đệm.
9. Bài chẩn đoán tổng hợp.
10. Thi thực hành chẩn đoán sự cố.

Đánh giá: Tự học trên Trợ giảng AI 10% (M2); Thực hành hằng tuần 20% (M3); Giữa kỳ: thi thực hành trên máy 20% (M1); Cuối kỳ: thi tự luận/thực hành 50% (M1)

### SOFT1201 Studio 4: Ứng dụng di động nhóm (2 TC, HK4)
Học phần dự án xuyên suốt của học kỳ 4. Sinh viên làm nhóm 4–5 người, áp dụng đặc tả và kiến trúc vào sản phẩm di động, bắt đầu điều phối AI agent.

- CLO1: Đặc tả và thiết kế ứng dụng di động nhóm. (→ PLO2, PLO3)
- CLO2: Điều phối AI agent cài đặt tính năng theo đặc tả, chỉ nhận mã qua kiểm thử. (→ PLO4)
- CLO3: Bảo vệ phần đóng góp cá nhân khi không có AI. (→ PLO4)

Giáo trình chính: Ryan Singer, Shape Up (Basecamp, bản đọc trực tuyến miễn phí); Hướng dẫn Studio và rubric của Khoa
Tham khảo: Addy Osmani, Beyond Vibe Coding: From Coder to AI-Era Developer, O'Reilly, 2025
Khóa học tham chiếu: CSCI 1970 Agentic Studio (Brown University · 2026); Stanford CS146S The Modern Software Developer (Stanford University · 2025–2026); GitHub Spec Kit – Spec-Driven Development (GitHub · 2025–2026)

Kế hoạch 10 tuần:
1. Khởi động: chọn bài toán, phỏng vấn người dùng, viết đặc tả và tiêu chí chấp nhận cho bản đầu tiên của ứng dụng di động làm theo nhóm, viết từ đặc tả.
2. Thiết kế: phác thảo giao diện, dữ liệu, kiến trúc; chia việc; thiết lập kho mã, CI và quy ước dùng AI.
3. Sprint 1: lát cắt chức năng đầu tiên chạy được từ đầu đến cuối; AI agent cài đặt tính năng đầu tiên từ đặc tả.
4. Sprint 1 (tiếp): kiểm thử, review chéo; Sprint review 1 với giảng viên.
5. Sprint 2: mở rộng chức năng chính; kiểm thử giao diện tự động.
6. Sprint 2 (tiếp): đo chất lượng, sửa lỗi; Sprint review 2, đối chiếu nhật ký AI.
7. Sprint 3: hoàn thiện; phát hành bản thử nghiệm.
8. Sprint 3 (tiếp): thử nghiệm với người dùng thật, thu phản hồi; Sprint review 3.
9. Làm cứng sản phẩm: kiểm thử hồi quy, rà soát bảo mật, tài liệu, chuẩn bị trình diễn.
10. Demo Day: trình diễn trước hội đồng; vấn đáp cá nhân giải thích code; phản tư.

Đánh giá: Sprint review (3 lần) 30% (M4); Nhật ký AI và phản tư 10% (M3); Demo Day tuần 10 40% (M4); Vấn đáp cá nhân: giải thích code 20% (M1)

### INFO2011 Công nghệ phần mềm: sản phẩm và Agile (2 TC, HK5)
Tinh gọn từ 3 xuống 2 tín chỉ: chỉ giữ phần quy trình và quản lý sản phẩm, vì yêu cầu, kiến trúc, kiểm thử, DevOps và làm việc với AI agent đã có học phần riêng. Quản lý sản phẩm, Agile, Scrum/Kanban, ước lượng, Definition of Done, quản lý mã nguồn và review trong nhóm có AI agent; đo hiệu quả đội bằng chỉ số DORA. Thực hành trên chính sản phẩm của Studio 5.

- CLO1: Quản lý sản phẩm và dự án theo Agile. (→ PLO8)
- CLO2: Vận dụng quy trình kỹ nghệ phần mềm với AI agent có kiểm soát. (→ PLO4, PLO2)
- CLO3: Đo và cải tiến hiệu quả làm việc của nhóm. (→ PLO8)

Giáo trình chính: Ian Sommerville, Engineering Software Products: An Introduction to Modern Software Engineering, Pearson, 2020
Tham khảo: Titus Winters, Tom Manshreck, Hyrum Wright, Software Engineering at Google, O'Reilly, 2020 (bản đọc trực tuyến miễn phí); Google Cloud DORA, State of AI-assisted Software Development 2025
Khóa học tham chiếu: 17-313 Foundations of Software Engineering (bài AI for SE, Vibe coding) (Carnegie Mellon University · 2025–2026); Generative AI Software Engineering Specialization (Vanderbilt University · Coursera · 2025); Generative AI for Software Development (3 khóa) (DeepLearning.AI · Coursera · 2024–2025)

Kế hoạch 10 tuần:
1. Kỹ nghệ phần mềm theo định hướng sản phẩm; lập thỏa thuận làm việc với AI của nhóm.
2. Quản lý sản phẩm: tầm nhìn, lộ trình, backlog, MVP.
3. Scrum và Kanban; sprint, ước lượng, Definition of Done.
4. Quản lý mã nguồn: nhánh, pull request, review có bot AI.
5. Quy trình khi có AI agent trong đội: chia việc, quyền hạn; giữa kỳ.
6. Ước lượng và lập kế hoạch khi AI làm nhanh phần cài đặt.
7. Chỉ số DORA và đo hiệu quả đội.
8. Quản lý rủi ro và nợ kỹ thuật, kể cả nợ do mã AI sinh.
9. Hồi cứu (retrospective) dựa trên dữ liệu kho mã.
10. Bảo vệ quy trình và kết quả của nhóm.

Đánh giá: Tự học trên Trợ giảng AI 5% (M2); Bài thực hành 20% (M3); Giữa kỳ: sản phẩm/bài tập lớn 25% (M4); Cuối kỳ: sản phẩm + vấn đáp cá nhân 50% (M4 + M1)

### SOFT4003 Kiểm thử và đảm bảo chất lượng phần mềm với AI (3 TC, HK5)
Nền tảng ISTQB: nguyên lý, quy trình, kỹ thuật kiểm thử tĩnh và động, hộp đen, hộp trắng, quản lý kiểm thử. Kiểm thử tự động đơn vị, tích hợp, đầu cuối (Playwright); dùng AI sinh ca kiểm thử, dữ liệu thử và kịch bản; kiểm thử đột biến để đo chất lượng bộ kiểm thử; kiểm thử mã do AI sinh.

- CLO1: Thiết kế ca kiểm thử bằng kỹ thuật hộp đen, hộp trắng. (→ PLO5)
- CLO2: Xây bộ kiểm thử tự động có dùng AI và đo được chất lượng. (→ PLO5)
- CLO3: Lập kế hoạch kiểm thử và quản lý rủi ro khi dùng AI trong kiểm thử. (→ PLO5)

Giáo trình chính: Graham, van Veenendaal, Black, Foundations of Software Testing: ISTQB Certification (CTFL 4.0), 2024; ISTQB CT-GenAI Syllabus v1.1 (2026)
Tham khảo: Tài liệu Playwright chính thức; Addy Osmani, Beyond Vibe Coding: From Coder to AI-Era Developer, O'Reilly, 2025 – chương 8; ISTQB CT-AI v2.0 Syllabus
Khóa học tham chiếu: ISTQB CT-GenAI – Testing with Generative AI (v1.0 2025, v1.1 4/2026) (ISTQB · 2025–2026); ISTQB CT-AI v2.0 – AI Testing (ISTQB · 2026); Generative AI for Software Development (3 khóa) (DeepLearning.AI · Coursera · 2024–2025)

Kế hoạch 10 tuần:
1. Tổng quan kiểm thử, nguyên lý ISTQB; vì sao kiểm thử quan trọng hơn khi có AI.
2. Quy trình kiểm thử và tài liệu.
3. Kiểm thử trong vòng đời phát triển; các mức kiểm thử.
4. Kiểm thử tĩnh, review; AI hỗ trợ review.
5. Kỹ thuật hộp đen: phân hoạch, giá trị biên, bảng quyết định; giữa kỳ.
6. Kỹ thuật hộp trắng, độ bao phủ.
7. Kiểm thử tự động đơn vị và tích hợp; mẫu prompt sinh ca kiểm thử theo ISTQB CT-GenAI, đối chiếu với kỹ thuật hộp đen.
8. Kiểm thử đầu cuối với Playwright; kiểm thử đột biến.
9. Quản lý kiểm thử, ước lượng, báo cáo; rủi ro khi dùng AI tạo sinh trong kiểm thử: ảo giác, rò rỉ dữ liệu, thiên lệch.
10. Công cụ kiểm thử; bảo vệ bộ kiểm thử.

Đánh giá: Tự học trên Trợ giảng AI 5% (M2); Bài thực hành 20% (M3); Giữa kỳ: sản phẩm/bài tập lớn 25% (M4); Cuối kỳ: sản phẩm + vấn đáp cá nhân 50% (M4 + M1)

### INFO3008 DevOps, CI/CD và điện toán đám mây (3 TC, HK5)
Mô hình dịch vụ đám mây, ảo hóa, container, điều phối; hạ tầng như mã; CI/CD; giám sát và nhật ký; bảo mật đám mây; tối ưu chi phí. Cập nhật từ học phần Điện toán đám mây: chuyển trọng tâm từ lý thuyết sang thực hành DevOps, dùng AI để viết và rà soát cấu hình.

- CLO1: Triển khai ứng dụng container lên đám mây với CI/CD. (→ PLO6)
- CLO2: Thiết lập giám sát, cảnh báo và quản lý chi phí, dùng AI hỗ trợ có kiểm chứng. (→ PLO6)

Giáo trình chính: Gene Kim và cộng sự, The DevOps Handbook, 2nd ed., IT Revolution
Tham khảo: Google Cloud DORA, State of AI-assisted Software Development 2025; Google, Site Reliability Engineering (sách mở); Camille Fournier, Ian Nowland, Platform Engineering, O'Reilly, 2024
Khóa học tham chiếu: Gemini for DevOps Engineers (Google Cloud · Coursera); The Missing Semester of Your CS Education (bản 2026) (MIT CSAIL · 2026); DORA 2025 State of AI-assisted Software Development (Google Cloud)

Kế hoạch 10 tuần:
1. Tổng quan đám mây; mô hình IaaS, PaaS, SaaS.
2. Ảo hóa và container.
3. Lưu trữ và dữ liệu trên đám mây.
4. Kiến trúc đám mây.
5. CI: build, kiểm thử tự động; giữa kỳ.
6. CD: triển khai tự động, môi trường.
7. Hạ tầng như mã; AI viết và rà soát cấu hình, kiểm tra tự động bằng policy-as-code.
8. Giám sát, nhật ký, cảnh báo; AI giải thích log, sinh viên xác nhận bằng truy vấn và số liệu.
9. Bảo mật đám mây, quản lý bí mật.
10. Tối ưu chi phí; trình diễn pipeline.

Đánh giá: Tự học trên Trợ giảng AI 5% (M2); Bài thực hành 20% (M3); Giữa kỳ: sản phẩm/bài tập lớn 25% (M4); Cuối kỳ: sản phẩm + vấn đáp cá nhân 50% (M4 + M1)

### SOFT2004 Kỹ nghệ phần mềm với AI agent (3 TC, HK5)
Học phần đặc trưng của chương trình. Cách làm việc với trợ lý lập trình và AI agent trong toàn bộ vòng đời: kỹ thuật ngữ cảnh (context engineering), công cụ và giao thức kết nối (như MCP), quy trình đặc tả → kế hoạch → cài đặt → kiểm thử → review, rào chắn và quyền hạn, đo năng suất và chất lượng, khi nào không nên dùng AI.

- CLO1: Điều phối AI agent hoàn thành tác vụ nhiều bước theo đặc tả, kể cả agent song song. (→ PLO4)
- CLO2: Thiết lập ngữ cảnh, công cụ (MCP), rào chắn và đo chất lượng đầu ra của AI agent. (→ PLO4, PLO7)
- CLO3: Đánh giá phê phán năng suất, rủi ro và giới hạn của AI; tự điều chỉnh cách làm việc. (→ PLO10)

Giáo trình chính: Addy Osmani, Beyond Vibe Coding: From Coder to AI-Era Developer, O'Reilly, 2025; Học liệu mở Stanford CS146S và MIT Missing Semester 2026 (bài Agentic Coding)
Tham khảo: Hugging Face MCP Course (mở); OWASP Top 10 for Agentic Applications (12/2025); Google Cloud DORA, State of AI-assisted Software Development 2025
Khóa học tham chiếu: Stanford CS146S The Modern Software Developer (Stanford University · 2025–2026); Missing Semester 2026 – bài Agentic Coding (MIT CSAIL · 2026); Claude Code: Software Engineering with Generative AI Agents (Vanderbilt University · Coursera · 2025); CS 378 Agentic Coding (UT Austin · 2026); CSCI 1970 Agentic Studio (Brown University · 2026); Model Context Protocol Course (hợp tác với Anthropic) (Hugging Face · 2025)

Kế hoạch 10 tuần:
1. Từ trợ lý đến agent: agent harness hoạt động thế nào; dữ liệu năng suất và giới hạn (Stack Overflow 2025, METR, DORA 2025).
2. Kỹ thuật ngữ cảnh: tệp hướng dẫn dự án, ví dụ, ràng buộc; codebase ‘sẵn sàng cho agent’ (theo CS146S).
3. Quy trình đặc tả → kế hoạch → cài đặt → kiểm thử; vòng ngắn có bằng chứng: giới hạn một lượt, đọc bằng chứng rồi mới quyết định.
4. Công cụ và MCP: xây một máy chủ MCP nhỏ cho dữ liệu của dự án (theo Hugging Face MCP Course).
5. Rào chắn: kiểm thử, review, quyền hạn, sandbox; giữa kỳ: một tính năng làm bằng agent kèm bằng chứng kiểm chứng.
6. Nhiều agent song song trên nhiều nhánh git; chia việc, tích hợp và review mã do agent viết.
7. Bảo mật khi dùng agent theo OWASP Agentic Top 10: chèn lệnh, lạm dụng công cụ, rò rỉ bí mật.
8. Đo chất lượng và năng suất; tải nhận thức và mệt mỏi khi điều phối agent; khi nào không nên dùng AI.
9. Làm việc với codebase lớn và mã kế thừa: agent đọc, giải thích, tái cấu trúc có kiểm thử hồi quy.
10. Bảo vệ dự án: trình diễn, vấn đáp không AI, phản tư về cách làm việc với agent.

Đánh giá: Tự học trên Trợ giảng AI 5% (M2); Bài thực hành 20% (M3); Giữa kỳ: sản phẩm/bài tập lớn 25% (M4); Cuối kỳ: sản phẩm + vấn đáp cá nhân 50% (M4 + M1)

### SOFT1202 Studio 5: Sản phẩm cho cộng đồng trường (2 TC, HK5)
Học phần dự án xuyên suốt của học kỳ 5. Sinh viên làm nhóm theo Scrum, phục vụ người dùng thật trong trường, kết hợp kiểm thử, DevOps và AI agent.

- CLO1: Làm việc theo Scrum với người dùng trong trường. (→ PLO8)
- CLO2: Vận hành sản phẩm có CI/CD, kiểm thử tự động và giám sát. (→ PLO5, PLO6)
- CLO3: Trình bày chỉ số chất lượng và vận hành của sản phẩm. (→ PLO8)

Giáo trình chính: Ryan Singer, Shape Up (Basecamp, bản đọc trực tuyến miễn phí); Hướng dẫn Studio và rubric của Khoa
Tham khảo: Addy Osmani, Beyond Vibe Coding: From Coder to AI-Era Developer, O'Reilly, 2025
Khóa học tham chiếu: CSCI 1970 Agentic Studio (Brown University · 2026); Stanford CS146S The Modern Software Developer (Stanford University · 2025–2026); 17-313 Foundations of Software Engineering (bài AI for SE, Vibe coding) (Carnegie Mellon University · 2025–2026)

Kế hoạch 10 tuần:
1. Khởi động: chọn bài toán, phỏng vấn người dùng, viết đặc tả và tiêu chí chấp nhận cho sản phẩm nhóm cho người dùng trong trường, có kiểm thử tự động và triển khai tự động lên cloud.
2. Thiết kế: phác thảo giao diện, dữ liệu, kiến trúc; chia việc; thiết lập kho mã, CI và quy ước dùng AI.
3. Sprint 1: lát cắt chức năng đầu tiên chạy được từ đầu đến cuối; CI/CD và bộ kiểm thử tự động.
4. Sprint 1 (tiếp): kiểm thử, review chéo; Sprint review 1 với giảng viên.
5. Sprint 2: mở rộng chức năng chính; đo chất lượng mã do AI agent viết.
6. Sprint 2 (tiếp): đo chất lượng, sửa lỗi; Sprint review 2, đối chiếu nhật ký AI.
7. Sprint 3: hoàn thiện; giám sát sản phẩm đang chạy.
8. Sprint 3 (tiếp): thử nghiệm với người dùng thật, thu phản hồi; Sprint review 3.
9. Làm cứng sản phẩm: kiểm thử hồi quy, rà soát bảo mật, tài liệu, chuẩn bị trình diễn.
10. Demo Day: trình diễn trước hội đồng; vấn đáp cá nhân giải thích code; phản tư.

Đánh giá: Sprint review (3 lần) 30% (M4); Nhật ký AI và phản tư 10% (M3); Demo Day tuần 10 40% (M4); Vấn đáp cá nhân: giải thích code 20% (M1)

### SOFT3001 Học máy ứng dụng cho kỹ sư phần mềm (3 TC, HK6)
Học máy từ góc nhìn kỹ sư phần mềm: dữ liệu, mô hình cơ bản, mạng nơ-ron và transformer ở mức ứng dụng, đánh giá mô hình, dùng mô hình có sẵn qua API, triển khai mô hình. Thay học phần Học sâu và ứng dụng trong khối bắt buộc (học phần đó chuyển sang tự chọn).

- CLO1: Xây và đánh giá mô hình học máy cho bài toán sản phẩm. (→ PLO7, PLO1)
- CLO2: Chọn giữa tự huấn luyện và dùng mô hình có sẵn, có lập luận về chi phí, chất lượng và rủi ro. (→ PLO7)

Giáo trình chính: Aurélien Géron, Hands-On Machine Learning with Scikit-Learn and PyTorch, O'Reilly, 2025
Tham khảo: Christian Kästner, Machine Learning in Production: From Models to Products, MIT Press, 2025; Chip Huyen, Designing Machine Learning Systems, O'Reilly, 2022
Khóa học tham chiếu: Machine Learning Specialization (Andrew Ng) (DeepLearning.AI & Stanford Online · Coursera); 17-645 Machine Learning in Production / 11-695 AI Engineering (Carnegie Mellon University · 2026); 6.S191 Introduction to Deep Learning (MIT · cập nhật hằng năm)

Kế hoạch 10 tuần:
1. Học máy trong sản phẩm phần mềm: mô hình là một thành phần, yêu cầu và rủi ro (theo Kästner).
2. Dữ liệu: thu thập, làm sạch, gán nhãn.
3. Hồi quy và phân loại.
4. Đánh giá mô hình, quá khớp.
5. Mạng nơ-ron cơ bản; giữa kỳ.
6. Transformer và mô hình ngôn ngữ ở mức ứng dụng.
7. Dùng mô hình có sẵn qua API; nhúng và tìm kiếm.
8. Triển khai mô hình, phục vụ dự đoán; kiểm thử và giám sát mô hình trong sản phẩm.
9. Thiên lệch, công bằng, giải thích được.
10. Trình diễn dự án.

Đánh giá: Tự học trên Trợ giảng AI 5% (M2); Bài thực hành và eval 25% (M5); Giữa kỳ: nguyên mẫu 20% (M4); Cuối kỳ: hệ thống AI + báo cáo đánh giá + vấn đáp 50% (M5 + M1)

### SOFT3002 Bảo mật ứng dụng và an toàn mã do AI sinh (3 TC, HK6)
Mô hình hóa mối đe dọa, OWASP Top 10, xác thực và phân quyền, bảo mật API, chuỗi cung ứng phần mềm, phân tích tĩnh và động. Trọng tâm mới: lỗ hổng thường gặp trong mã do AI sinh, gói phụ thuộc giả mạo, chèn lệnh vào ứng dụng có AI, bảo mật khi dùng AI agent.

- CLO1: Phát hiện và khắc phục lỗ hổng phổ biến trong ứng dụng web và API. (→ PLO5)
- CLO2: Đánh giá rủi ro bảo mật của mã do AI sinh và của ứng dụng có thành phần AI, agent. (→ PLO5, PLO7)

Giáo trình chính: Andrew Hoffman, Web Application Security, 2nd ed., O'Reilly, 2024; OWASP Top 10:2025, OWASP Top 10 for LLM Applications 2025, OWASP Top 10 for Agentic Applications
Tham khảo: Addy Osmani, Beyond Vibe Coding: From Coder to AI-Era Developer, O'Reilly, 2025 – chương 8 (bảo mật mã do AI sinh)
Khóa học tham chiếu: CS 253 Web Security (Stanford University); OWASP Top 10:2025 (OWASP · 11/2025); OWASP Top 10 for Agentic Applications (OWASP GenAI Security Project · 12/2025); Agentic AI MOOC (CS294/194-196) (UC Berkeley RDI · Fall 2025)

Kế hoạch 10 tuần:
1. Tư duy bảo mật, mô hình hóa mối đe dọa.
2. OWASP Top 10:2025: kiểm soát truy cập, cấu hình sai, chèn mã, XSS; mục mới xử lý ngoại lệ.
3. Xác thực, phiên, phân quyền.
4. Bảo mật API.
5. Phân tích tĩnh, động; giữa kỳ.
6. Chuỗi cung ứng phần mềm (OWASP A03:2025), phụ thuộc, gói giả mạo và tên gói do AI ‘bịa’.
7. Lỗ hổng điển hình trong mã do AI sinh.
8. Bảo mật ứng dụng có LLM và agent: chèn lệnh, lạm dụng công cụ, rò rỉ dữ liệu (OWASP LLM và Agentic Top 10).
9. Ứng phó sự cố, công bố lỗ hổng có trách nhiệm.
10. Bảo vệ báo cáo đánh giá bảo mật.

Đánh giá: Tự học trên Trợ giảng AI 5% (M2); Bài thực hành 20% (M3); Giữa kỳ: sản phẩm/bài tập lớn 25% (M4); Cuối kỳ: sản phẩm + vấn đáp cá nhân 50% (M4 + M1)

### SOFT3007 Chủ đề hiện đại trong Kỹ thuật phần mềm (3 TC, HK6)
Học phần mở: chuẩn đầu ra, cách đánh giá và số tín chỉ cố định, còn nội dung là 1–2 chủ đề công nghệ hoặc kỹ thuật mới do Khoa công bố hằng năm, chưa kịp đưa vào học phần chính quy (ví dụ năm 2027: phát triển nhiều agent theo đặc tả, MCP và hệ sinh thái công cụ cho agent, đánh giá và quan sát hệ thống AI, mô hình nhỏ chạy trên thiết bị, hiện đại hóa hệ thống cũ bằng AI). Giảng viên dạy cùng chuyên gia doanh nghiệp. Sinh viên học nhanh từ tài liệu gốc, làm nguyên mẫu, đo đạc và viết khuyến nghị áp dụng theo thang Adopt / Trial / Assess / Hold; kết quả của lớp cập nhật vào Tech Radar của Khoa.

- CLO1: Tự học nhanh một công nghệ mới từ tài liệu gốc (tài liệu chính thức, mã nguồn, bài báo), có AI hỗ trợ và kiểm chứng nguồn. (→ PLO10)
- CLO2: Xây nguyên mẫu áp dụng công nghệ mới vào một bài toán phần mềm và đo được kết quả. (→ PLO4)
- CLO3: Đánh giá mức trưởng thành, rủi ro, chi phí và đưa ra khuyến nghị áp dụng có lập luận. (→ PLO3, PLO10)

Giáo trình chính: Tài liệu gốc của chủ đề năm học (tài liệu chính thức, mã nguồn, bài báo) do Khoa công bố; Thoughtworks, Build Your Own Technology Radar (phương pháp đánh giá công nghệ)
Tham khảo: Addy Osmani, Beyond Vibe Coding: From Coder to AI-Era Developer, O'Reilly, 2025; Chip Huyen, AI Engineering: Building Applications with Foundation Models, O'Reilly, 2025; Thoughtworks Technology Radar (bản mới nhất)
Khóa học tham chiếu: Special Topics courses (khối học phần chủ đề đặc biệt) (UC Santa Barbara CS); CSCI 2953-A Engineering Complex Systems with Generative AI (seminar thử nghiệm) (Brown University · 2027); Stanford CS146S The Modern Software Developer (Stanford University · 2025–2026); Build Your Own Technology Radar (Thoughtworks)

Kế hoạch 10 tuần:
1. Công bố chủ đề của năm; bản đồ công nghệ; vì sao chủ đề này quan trọng.
2. Học nhanh từ tài liệu gốc: đọc tài liệu chính thức, mã nguồn mẫu; AI tóm tắt, sinh viên kiểm chứng.
3. Seminar chuyên gia doanh nghiệp: chủ đề được dùng thế nào trong sản phẩm thật.
4. Tiêu chí đánh giá: chất lượng, chi phí, bảo mật, khả năng bảo trì, rủi ro khóa nhà cung cấp.
5. Thử nghiệm 1; giữa kỳ: demo kỹ thuật 5 phút.
6. Nguyên mẫu: áp dụng vào bài toán của Studio hoặc doanh nghiệp.
7. Nguyên mẫu (tiếp); so sánh với giải pháp hiện có.
8. Đo đạc, phân tích kết quả, ghi lại giới hạn.
9. Viết khuyến nghị Adopt / Trial / Assess / Hold và bài viết kỹ thuật.
10. Trình bày; cập nhật Tech Radar của Khoa; vấn đáp.

Đánh giá: Nhật ký tìm hiểu và tóm tắt tài liệu gốc 20% (M3); Demo kỹ thuật giữa kỳ 15% (M4); Nguyên mẫu và báo cáo đo đạc 35% (M4); Khuyến nghị áp dụng (Tech Radar) + vấn đáp 30% (M4 + M1)

### SOFT2101 Studio 6: Dự án doanh nghiệp (3 TC, HK6)
Học phần dự án xuyên suốt của học kỳ 6. Sinh viên làm việc với khách hàng doanh nghiệp thật, có chuyên gia doanh nghiệp cùng hướng dẫn và chấm. Kết thúc học kỳ là Cổng năng lực 2.

- CLO1: Làm rõ và quản lý yêu cầu với khách hàng doanh nghiệp. (→ PLO2)
- CLO2: Bàn giao sản phẩm đạt tiêu chuẩn chất lượng và bảo mật của doanh nghiệp, tuân thủ chính sách dữ liệu và AI. (→ PLO5, PLO9)
- CLO3: Giao tiếp chuyên nghiệp với khách hàng và đội. (→ PLO8)

Giáo trình chính: Ryan Singer, Shape Up (Basecamp, bản đọc trực tuyến miễn phí); Hướng dẫn Studio và rubric của Khoa
Tham khảo: Addy Osmani, Beyond Vibe Coding: From Coder to AI-Era Developer, O'Reilly, 2025
Khóa học tham chiếu: 17-313 Foundations of Software Engineering (bài AI for SE, Vibe coding) (Carnegie Mellon University · 2025–2026); Generative AI Software Engineering Specialization (Vanderbilt University · Coursera · 2025)

Kế hoạch 10 tuần:
1. Khởi động: chọn bài toán, phỏng vấn người dùng, viết đặc tả và tiêu chí chấp nhận cho sản phẩm giải bài toán thật của một công ty thuộc tập đoàn công nghệ cmc, kèm báo cáo bảo mật.
2. Thiết kế: phác thảo giao diện, dữ liệu, kiến trúc; chia việc; thiết lập kho mã, CI và quy ước dùng AI.
3. Sprint 1: lát cắt chức năng đầu tiên chạy được từ đầu đến cuối; làm rõ yêu cầu với khách hàng doanh nghiệp.
4. Sprint 1 (tiếp): kiểm thử, review chéo; Sprint review 1 với giảng viên.
5. Sprint 2: mở rộng chức năng chính; rà soát bảo mật và hiệu năng.
6. Sprint 2 (tiếp): đo chất lượng, sửa lỗi; Sprint review 2, đối chiếu nhật ký AI.
7. Sprint 3: hoàn thiện; bàn giao theo tiêu chuẩn doanh nghiệp.
8. Sprint 3 (tiếp): thử nghiệm với người dùng thật, thu phản hồi; Sprint review 3.
9. Làm cứng sản phẩm: kiểm thử hồi quy, rà soát bảo mật, tài liệu, chuẩn bị trình diễn.
10. Demo Day: trình diễn trước hội đồng có doanh nghiệp; vấn đáp cá nhân giải thích code; phản tư.

Đánh giá: Sprint review (3 lần) 30% (M4); Nhật ký AI và phản tư 10% (M3); Demo Day tuần 10 40% (M4); Vấn đáp cá nhân: giải thích code 20% (M1)

### SOFT3004 Phát triển ứng dụng mô hình ngôn ngữ lớn (3 TC, HK7)
Xây tính năng AI trong sản phẩm: thiết kế prompt và cấu trúc đầu ra, RAG, agent dùng công cụ, bộ nhớ, đánh giá (eval) tự động và có con người, giám sát, tối ưu chi phí và độ trễ, an toàn. Kế thừa chương LLM của học phần Xử lý ngôn ngữ tự nhiên và mở rộng thành học phần riêng.

- CLO1: Xây tính năng RAG hoặc agent hoạt động trong sản phẩm. (→ PLO7)
- CLO2: Thiết kế bộ đánh giá, phân tích lỗi và dùng nó để cải tiến hệ thống. (→ PLO7, PLO5)
- CLO3: Phân tích chi phí, độ trễ và rủi ro an toàn của tính năng AI. (→ PLO7)

Giáo trình chính: Chip Huyen, AI Engineering: Building Applications with Foundation Models, O'Reilly, 2025
Tham khảo: Jay Alammar, Maarten Grootendorst, Hands-On Large Language Models, O'Reilly, 2024; Lane, Dyshel, Natural Language Processing in Action, 2nd ed., Manning, 2025
Khóa học tham chiếu: Agentic AI (Andrew Ng) (DeepLearning.AI · Coursera · 2025, cập nhật 10/2026); Agentic AI MOOC (CS294/194-196) (UC Berkeley RDI · Fall 2025); AI Agents Course (Hugging Face · 2025); Agentic AI Nanodegree (nd900) (Udacity · 2025); 17-645 Machine Learning in Production / 11-695 AI Engineering (Carnegie Mellon University · 2026)

Kế hoạch 10 tuần:
1. Mô hình ngôn ngữ lớn trong sản phẩm; chọn mô hình.
2. Thiết kế prompt, đầu ra có cấu trúc.
3. Nhúng, cơ sở dữ liệu vector, RAG.
4. Đánh giá RAG; bộ dữ liệu đánh giá.
5. Mẫu thiết kế agent: phản tư, dùng công cụ, lập kế hoạch, đa agent; giữa kỳ: nguyên mẫu.
6. Bộ nhớ, luồng nhiều bước, phối hợp nhiều agent.
7. Phát triển dựa trên đánh giá: bộ dữ liệu đánh giá, phân tích lỗi theo từng bước của agent, AI chấm AI có kiểm định.
8. Giám sát, chi phí, độ trễ.
9. An toàn: chèn lệnh, rò rỉ, nội dung có hại; tuân thủ Luật Trí tuệ nhân tạo.
10. Trình diễn hệ thống và báo cáo đánh giá.

Đánh giá: Tự học trên Trợ giảng AI 5% (M2); Bài thực hành và eval 25% (M5); Giữa kỳ: nguyên mẫu 20% (M4); Cuối kỳ: hệ thống AI + báo cáo đánh giá + vấn đáp 50% (M5 + M1)

### SOFT3005 Hệ thống phân tán, dữ liệu và vận hành (3 TC, HK7)
Nhất quán, sao chép, phân vùng, hàng đợi thông điệp, luồng dữ liệu; thiết kế cho quy mô lớn; vận hành tin cậy (SRE): chỉ số SLO, cảnh báo, xử lý sự cố, hậu kiểm không đổ lỗi.

- CLO1: Thiết kế hệ thống chịu tải và chịu lỗi dựa trên nguyên lý hệ phân tán. (→ PLO3, PLO1)
- CLO2: Vận hành hệ thống theo chỉ số, xử lý sự cố có quy trình, dùng AI hỗ trợ có kiểm soát. (→ PLO6)

Giáo trình chính: Martin Kleppmann, Chris Riccomini, Designing Data-Intensive Applications, 2nd ed., O'Reilly, 2026
Tham khảo: Google, Site Reliability Engineering và The Site Reliability Workbook (sách mở)
Khóa học tham chiếu: 6.5840 Distributed Systems (MIT); Site Reliability Engineering & The Site Reliability Workbook (Google · sách mở); AI-driven Software Engineering (TU München · 2026)

Kế hoạch 10 tuần:
1. Hệ phân tán: thách thức.
2. Sao chép, nhất quán.
3. Phân vùng dữ liệu.
4. Hàng đợi, luồng sự kiện.
5. Bộ đệm, CDN; giữa kỳ.
6. Thiết kế hệ thống quy mô lớn.
7. SLO, chỉ số, cảnh báo.
8. Xử lý sự cố và hậu kiểm; AI hỗ trợ phân loại cảnh báo và tóm tắt sự cố, người quyết định cuối cùng.
9. Kiểm thử chịu lỗi, chaos.
10. Bảo vệ thiết kế hệ thống.

Đánh giá: Tự học trên Trợ giảng AI 5% (M2); Bài thực hành 20% (M3); Giữa kỳ: sản phẩm/bài tập lớn 25% (M4); Cuối kỳ: sản phẩm + vấn đáp cá nhân 50% (M4 + M1)

### INFO3001 Pháp lý, đạo đức nghề nghiệp và AI có trách nhiệm (2 TC, HK7)
Luật sở hữu trí tuệ, an toàn thông tin mạng, giao dịch điện tử, bảo vệ dữ liệu cá nhân, Luật Trí tuệ nhân tạo; đạo đức nghề nghiệp; quy định về dùng AI trong học tập và làm việc; giấy phép mã nguồn mở và bản quyền với mã do AI sinh.

- CLO1: Phân tích vấn đề pháp lý, đạo đức của một sản phẩm phần mềm có AI. (→ PLO9)
- CLO2: Đề xuất biện pháp tuân thủ và quản trị rủi ro AI cho sản phẩm. (→ PLO9, PLO7)

Giáo trình chính: Michael Quinn, Ethics for the Information Age, Pearson; Luật Trí tuệ nhân tạo 134/2025/QH15; Thông tư 49/2026/TT-BGDĐT
Tham khảo: Sara Baase, A Gift of Fire; Tài liệu OWASP GenAI Security Project về quản trị AI
Khóa học tham chiếu: Ethics of AI (MOOC) (University of Helsinki); Agentic AI MOOC (CS294/194-196) (UC Berkeley RDI · Fall 2025)

Kế hoạch 10 tuần:
1. Khái niệm cơ bản; pháp lý trong doanh nghiệp CNTT.
2. Đạo đức nghề nghiệp.
3. Đạo đức AI và trách nhiệm xã hội: minh bạch, công bằng, quyền con người (theo Ethics of AI, Helsinki).
4. Luật Trí tuệ nhân tạo; phân loại rủi ro hệ thống AI.
5. Luật an toàn thông tin mạng; giữa kỳ.
6. Tội phạm tin học.
7. Sở hữu trí tuệ, giấy phép mã nguồn mở, mã do AI sinh.
8. Bảo vệ dữ liệu cá nhân.
9. Quyền riêng tư và quyền tiếp cận thông tin.
10. Phân tích tình huống sản phẩm thật.

Đánh giá: Tự học trên Trợ giảng AI 5% (M2); Bài thực hành 20% (M3); Giữa kỳ: sản phẩm/bài tập lớn 25% (M4); Cuối kỳ: sản phẩm + vấn đáp cá nhân 50% (M4 + M1)

### SOFT3008 Nghiên cứu và đổi mới trong Kỹ thuật phần mềm (3 TC, HK7)
Học phần mở dạng dự án nghiên cứu: nhóm 2–3 sinh viên tham gia đề tài của giảng viên, phòng thí nghiệm hoặc doanh nghiệp. Đề tài thay đổi mỗi năm theo hướng nghiên cứu của Khoa, ví dụ: tái lập kết quả một bài báo mới (ICSE, FSE, ASE, arXiv), thực nghiệm so sánh công cụ AI trong phát triển phần mềm, xây bộ đánh giá (benchmark) cho bài toán tiếng Việt. Sản phẩm là mã và dữ liệu tái lập được cùng một bài báo ngắn hoặc poster, có thể gửi Hội nghị sinh viên nghiên cứu khoa học hoặc cuộc thi ACM Student Research Competition. Là cầu nối sang đồ án tốt nghiệp hướng nghiên cứu.

- CLO1: Xây dựng câu hỏi nghiên cứu và tổng quan tài liệu, dùng AI tìm và tóm tắt nhưng kiểm chứng từng nguồn. (→ PLO10)
- CLO2: Thiết kế và thực hiện thực nghiệm có đo lường, tái lập được. (→ PLO5)
- CLO3: Viết và trình bày kết quả theo chuẩn học thuật, khai báo trung thực việc dùng AI. (→ PLO9)

Giáo trình chính: Wohlin, Runeson, Höst, Ohlsson, Regnell, Wesslén, Experimentation in Software Engineering, 2nd ed., Springer, 2024; ACM SIGSOFT Empirical Standards for Software Engineering Research
Tham khảo: Bài báo của đề tài năm học (ICSE, FSE, ASE, arXiv); Quy định liêm chính học thuật và sử dụng AI của Trường (theo Thông tư 49/2026)
Khóa học tham chiếu: CS 197 Computer Science Research (Stanford University · 2026); 6.UAR Seminar in Undergraduate Advanced Research (SuperUROP) (MIT EECS); CS 6158 Software Engineering in the Era of AI (Cornell University · 2026); CS294 Disrupting Systems Research with AI (UC Berkeley · 2025); ACM Student Research Competition (ACM)

Kế hoạch 10 tuần:
1. Nghiên cứu trong kỹ thuật phần mềm là gì; giới thiệu đề tài của năm; lập nhóm.
2. Đọc bài báo hiệu quả; tìm tài liệu với AI và kiểm chứng trích dẫn.
3. Câu hỏi nghiên cứu, giả thuyết, đóng góp dự kiến.
4. Thiết kế thực nghiệm: biến, chỉ số, mối đe dọa đến tính hợp lệ.
5. Bảo vệ đề cương nghiên cứu; giữa kỳ.
6. Thực nghiệm vòng 1; nhật ký thực nghiệm.
7. Thực nghiệm vòng 2; đóng gói mã và dữ liệu để tái lập.
8. Phân tích kết quả, thống kê, biểu đồ.
9. Viết bài báo ngắn hoặc poster; liêm chính học thuật và khai báo AI.
10. Bảo vệ; chọn kết quả gửi hội nghị sinh viên.

Đánh giá: Đề cương nghiên cứu và tổng quan tài liệu 20% (M3); Nhật ký thực nghiệm hằng tuần 15% (M3); Kết quả thực nghiệm, mã và dữ liệu tái lập được 35% (M4); Bài báo ngắn hoặc poster + bảo vệ 30% (M3 + M1)

### SOFT2102 Studio 7: Tính năng AI có đánh giá (2 TC, HK7)
Học phần dự án xuyên suốt của học kỳ 7. Sinh viên xây tính năng AI cho sản phẩm có sẵn và chứng minh bằng số liệu rằng tính năng đó đáng tin.

- CLO1: Đặc tả và tích hợp một tính năng AI vào sản phẩm có sẵn. (→ PLO7)
- CLO2: Chứng minh độ tin cậy của tính năng AI bằng bộ đánh giá và kiểm thử. (→ PLO7, PLO5)
- CLO3: Bảo vệ thiết kế và kết quả đánh giá khi không có AI. (→ PLO7)

Giáo trình chính: Ryan Singer, Shape Up (Basecamp, bản đọc trực tuyến miễn phí); Hướng dẫn Studio và rubric của Khoa
Tham khảo: Addy Osmani, Beyond Vibe Coding: From Coder to AI-Era Developer, O'Reilly, 2025
Khóa học tham chiếu: Agentic AI (Andrew Ng) (DeepLearning.AI · Coursera · 2025, cập nhật 10/2026); Agentic AI Nanodegree (nd900) (Udacity · 2025)

Kế hoạch 10 tuần:
1. Khởi động: chọn bài toán, phỏng vấn người dùng, viết đặc tả và tiêu chí chấp nhận cho một tính năng ai (trợ lý, tìm kiếm thông minh hoặc agent) tích hợp vào sản phẩm, kèm báo cáo đánh giá độ tin cậy.
2. Thiết kế: phác thảo giao diện, dữ liệu, kiến trúc; chia việc; thiết lập kho mã, CI và quy ước dùng AI.
3. Sprint 1: lát cắt chức năng đầu tiên chạy được từ đầu đến cuối; tích hợp RAG hoặc agent vào sản phẩm.
4. Sprint 1 (tiếp): kiểm thử, review chéo; Sprint review 1 với giảng viên.
5. Sprint 2: mở rộng chức năng chính; xây bộ đánh giá và cải tiến theo chỉ số.
6. Sprint 2 (tiếp): đo chất lượng, sửa lỗi; Sprint review 2, đối chiếu nhật ký AI.
7. Sprint 3: hoàn thiện; giám sát chi phí, độ trễ, an toàn.
8. Sprint 3 (tiếp): thử nghiệm với người dùng thật, thu phản hồi; Sprint review 3.
9. Làm cứng sản phẩm: kiểm thử hồi quy, rà soát bảo mật, tài liệu, chuẩn bị trình diễn.
10. Demo Day: trình diễn trước hội đồng có doanh nghiệp; vấn đáp cá nhân giải thích code; phản tư.

Đánh giá: Sprint review (3 lần) 30% (M4); Nhật ký AI và phản tư 10% (M3); Demo Day tuần 10 40% (M4); Vấn đáp cá nhân: giải thích code 20% (M1)

### SOFT3901 Thực tập OJT tại doanh nghiệp (6 TC, HK8)
Sinh viên làm việc 10 tuần tại công ty thành viên Tập đoàn Công nghệ CMC hoặc đối tác, tham gia đội phát triển thật, có người hướng dẫn doanh nghiệp và giảng viên. Điều kiện: đạt Cổng năng lực 2.

- CLO1: Đóng góp vào hệ thống phần mềm đang vận hành trong doanh nghiệp. (→ PLO8, PLO6)
- CLO2: Tuân thủ quy trình, bảo mật và chính sách dùng AI của doanh nghiệp. (→ PLO9)

Giáo trình chính: Sổ tay thực tập OJT của Khoa và chính sách dùng AI của doanh nghiệp
Tham khảo: Titus Winters, Tom Manshreck, Hyrum Wright, Software Engineering at Google, O'Reilly, 2020 (bản đọc trực tuyến miễn phí)
Khóa học tham chiếu: SWEBOK Guide V4.0 (IEEE Computer Society · 2024 (cập nhật 9/2025)); 17-313 Foundations of Software Engineering (bài AI for SE, Vibe coding) (Carnegie Mellon University · 2025–2026)

Kế hoạch 10 tuần:
1. Tiếp nhận, tìm hiểu doanh nghiệp, quy trình, chính sách dùng AI.
2. Làm quen codebase và công cụ.
3. Nhận nhiệm vụ đầu tiên.
4. Làm việc theo sprint của đội.
5. Báo cáo giữa kỳ với giảng viên.
6. Đảm nhận tính năng hoặc cải tiến.
7. Review, kiểm thử, triển khai theo quy trình doanh nghiệp.
8. Hoàn thiện đóng góp.
9. Viết báo cáo thực tập.
10. Đánh giá của doanh nghiệp; bảo vệ trước giảng viên.

Đánh giá: Đánh giá của người hướng dẫn doanh nghiệp 50% (M4); Báo cáo thực tập và nhật ký tuần 30% (M3); Bảo vệ trước giảng viên 20% (M1)

### SOFT3006 Đổi mới sáng tạo và khởi nghiệp sản phẩm số (2 TC, HK8)
Tìm vấn đề đáng giải quyết, kiểm chứng ý tưởng, mô hình kinh doanh, đo lường sản phẩm, gọi vốn; khởi nghiệp với đội nhỏ có AI.

- CLO1: Kiểm chứng một ý tưởng sản phẩm bằng dữ liệu người dùng. (→ PLO10)
- CLO2: Trình bày mô hình kinh doanh của sản phẩm. (→ PLO10)

Giáo trình chính: Rob Fitzpatrick, The Mom Test; Y Combinator Startup School (học liệu mở)
Tham khảo: Eric Ries, The Lean Startup
Khóa học tham chiếu: Startup School (Y Combinator · miễn phí); How to Build a Startup (Steve Blank) (Udacity · miễn phí); 17-356 Software Engineering for Startups (Carnegie Mellon University)

Kế hoạch 10 tuần:
1. Tư duy khởi nghiệp.
2. Tìm và kiểm chứng vấn đề.
3. Phỏng vấn khách hàng.
4. Sản phẩm khả dụng tối thiểu làm trong vài ngày với AI agent; xác định điều cần đo.
5. Đo lường; giữa kỳ.
6. Mô hình kinh doanh.
7. Định giá, kênh.
8. Pháp lý khởi nghiệp.
9. Trình bày gọi vốn.
10. Ngày trình bày ý tưởng.

Đánh giá: Tự học trên Trợ giảng AI 5% (M2); Bài thực hành 20% (M3); Giữa kỳ: sản phẩm/bài tập lớn 25% (M4); Cuối kỳ: sản phẩm + vấn đáp cá nhân 50% (M4 + M1)

### SOFT3902 Đồ án tốt nghiệp (8 TC, HK9)
Sản phẩm có người dùng hoặc khách hàng thật: hệ thống cho doanh nghiệp, sản phẩm khởi nghiệp hoặc đề tài nghiên cứu ứng dụng. Có hồ sơ đặc tả, thiết kế, kiểm thử, đánh giá AI (nếu có), nhật ký AI và minh chứng người dùng. Bảo vệ trước hội đồng có đại diện doanh nghiệp.

- CLO1: Dẫn dắt toàn bộ vòng đời một sản phẩm từ yêu cầu, thiết kế, cài đặt đến kiểm chứng. (→ PLO2, PLO3, PLO4, PLO5)
- CLO2: Chứng minh giá trị sản phẩm và tính năng AI bằng dữ liệu người dùng và bộ đánh giá. (→ PLO7, PLO10)
- CLO3: Trình bày và bảo vệ mọi quyết định kỹ thuật khi không có AI. (→ PLO8)

Giáo trình chính: Hướng dẫn đồ án tốt nghiệp của Khoa
Tham khảo: Christian Kästner, Machine Learning in Production: From Models to Products, MIT Press, 2025; Chip Huyen, AI Engineering: Building Applications with Foundation Models, O'Reilly, 2025; Mark Richards, Neal Ford, Fundamentals of Software Architecture, 2nd ed., O'Reilly, 2025
Khóa học tham chiếu: 17-645 Machine Learning in Production / 11-695 AI Engineering (Carnegie Mellon University · 2026); Stanford CS146S The Modern Software Developer (Stanford University · 2025–2026); SWEBOK Guide V4.0 (IEEE Computer Society · 2024 (cập nhật 9/2025))

Kế hoạch 10 tuần:
1. Chốt đề tài, khách hàng, đặc tả.
2. Thiết kế và kế hoạch.
3. Phát triển vòng 1.
4. Mốc 1: trình diễn và góp ý.
5. Phát triển vòng 2.
6. Mốc 2: thử nghiệm người dùng.
7. Phát triển vòng 3, làm cứng.
8. Mốc 3: hồ sơ hoàn chỉnh.
9. Chuẩn bị bảo vệ.
10. Bảo vệ trước hội đồng.

Đánh giá: Tiến độ và sản phẩm qua 3 mốc 30% (M4); Sản phẩm cuối, người dùng/khách hàng thật 40% (M4); Bảo vệ trước hội đồng có doanh nghiệp 30% (M1)

## Hướng chuyên sâu

- **AI Engineering** (Kỹ sư ứng dụng AI, kỹ sư AI agent): SOFT4101 Kỹ thuật xây dựng AI agent; SOFT4102 MLOps và LLMOps
- **Product Engineering** (Kỹ sư sản phẩm, web/mobile, full-stack): SOFT4201 Phát triển sản phẩm đa nền tảng nâng cao; SOFT4202 Phân tích và tăng trưởng sản phẩm
- **Quality & Security** (Kỹ sư kiểm thử tự động, đánh giá AI, bảo mật ứng dụng): SOFT4301 Kiểm thử nâng cao và đánh giá hệ thống AI; SOFT4302 DevSecOps và an ninh chuỗi cung ứng phần mềm
- **Cloud & Platform** (Kỹ sư DevOps, cloud, platform, SRE): SOFT4401 Kỹ thuật nền tảng; SOFT4402 Hệ thống quy mô lớn và SRE nâng cao

## Cổng năng lực

- **Cổng năng lực 1** (Cuối học kỳ 3 (năm 1)): Bài thi lập trình và cấu trúc dữ liệu trên máy có kiểm soát, không AI; hồ sơ 3 sản phẩm; vấn đáp giải thích code. Điều kiện đăng ký Studio 4. Chưa đạt: học phụ đạo trong học kỳ 4 và thi lại.
- **Cổng năng lực 2** (Cuối học kỳ 6 (năm 2)): Thiết kế hệ thống trên bảng, review code trực tiếp, bài thi kiểm thử và bảo mật không AI; hồ sơ 6 sản phẩm. Điều kiện đăng ký Thực tập OJT. Chưa đạt: hoãn thực tập một học kỳ, có kế hoạch bổ trợ.
- **Cổng tốt nghiệp** (Học kỳ 9 (năm 3)): Bảo vệ đồ án tốt nghiệp trước hội đồng có doanh nghiệp; hồ sơ 9 sản phẩm; chuẩn đầu ra ngoại ngữ và năng lực số. Điều kiện xét tốt nghiệp.

## Chuyển đổi từ CTĐT hiện hành

- INFO2013 Nhập môn công nghệ thông tin (3 TC) → SOFT1001 Nhập môn Kỹ thuật phần mềm AI-native: Thay thế. Chuyển từ giới thiệu kiến thức chung sang làm sản phẩm ngay; giữ chương AI có trách nhiệm và mở rộng.
- PROG2005 Cơ sở lập trình (4 TC) → PROG2005 Cơ sở lập trình (Python, có trợ lý AI): Giữ, cập nhật. Thêm kiểm thử đơn vị, đọc mã AI sinh; giữ thi không AI.
- MATH2005 Toán rời rạc (3 TC) → MATH2005 Toán rời rạc và logic cho lập trình: Giữ, giảm 1 TC. Giữ logic, đếm, đồ thị qua bài cài đặt Python; chứng minh hình thức, hệ đếm, đại số Bool chuyển sang tự học.
- INFO2002 Cấu trúc dữ liệu và giải thuật (3 TC) → INFO2002 Cấu trúc dữ liệu và giải thuật: Giữ, cập nhật. Thi không AI; AI dùng để luyện và so sánh lời giải.
- INFO2007 Cơ sở dữ liệu (4 TC) → INFO2007 Cơ sở dữ liệu: Giữ, giảm 1 TC. Chuyển SQL Server sang PostgreSQL; rà soát SQL do AI sinh; cơ sở dữ liệu vector.
- PROG2006 Lập trình hướng đối tượng (4 TC) → PROG2006 Lập trình hướng đối tượng và mã sạch: Giữ, giảm 1 TC. Bỏ phần giao diện đồ họa; thêm tái cấu trúc mã AI sinh, kiểm thử.
- INFO2011 Công nghệ phần mềm (4 TC) → INFO2011 Công nghệ phần mềm: sản phẩm và Agile: Giữ, giảm 2 TC. Chỉ giữ quy trình và quản lý sản phẩm Agile trong đội có AI agent; yêu cầu, kiến trúc, kiểm thử, DevOps đã có học phần riêng.
- SOFT4003 Kiểm thử phần mềm (3 TC) → SOFT4003 Kiểm thử và đảm bảo chất lượng phần mềm với AI: Giữ, cập nhật lớn. Giữ nền tảng ISTQB; thêm Playwright, AI sinh ca kiểm thử, kiểm thử đột biến; chuyển từ 45 tiết lý thuyết sang thực hành.
- INFO3007 Mạng máy tính và truyền thông (3 TC) → SOFT2003 Hệ thống máy tính và mạng cho kỹ sư phần mềm: Thay thế, giảm 1 TC. Gộp hệ điều hành và mạng ở góc nhìn kỹ sư phần mềm, học qua chẩn đoán sự cố; bỏ chi tiết lớp vật lý, định tuyến.
- INFO3008 Điện toán đám mây (3 TC) → INFO3008 DevOps, CI/CD và điện toán đám mây: Giữ, cập nhật lớn. Chuyển từ 45 tiết lý thuyết sang thực hành DevOps, hạ tầng như mã, chi phí.
- PROG3002 Phát triển ứng dụng di động (3 TC) → PROG3002 Phát triển ứng dụng di động: Giữ, cập nhật. Thêm AI agent theo đặc tả, kiểm thử giao diện tự động.
- INFO3001 Pháp lý và đạo đức nghề nghiệp (2 TC) → INFO3001 Pháp lý, đạo đức nghề nghiệp và AI có trách nhiệm: Giữ, cập nhật. Thêm Luật Trí tuệ nhân tạo, Thông tư 49/2026, bản quyền mã AI sinh.
- BIGD4001 Học sâu và ứng dụng (3 TC) → SOFT3001 Học máy ứng dụng cho kỹ sư phần mềm: Thay thế (cũ chuyển tự chọn). Kỹ sư phần mềm cần dùng và triển khai mô hình hơn là nghiên cứu kiến trúc mạng.
- BIGD4003 Xử lý ngôn ngữ tự nhiên (3 TC) → SOFT3004 Phát triển ứng dụng mô hình ngôn ngữ lớn: Tách và mở rộng (cũ chuyển tự chọn). Chương 8 (LLM, RAG, agent) thành học phần riêng 10 tuần.

## Căn cứ pháp lý

- **Thông tư 54/2026/TT-BGDĐT** – Quy định chương trình đào tạo các trình độ của giáo dục đại học (30/6/2026): Chuẩn đầu ra đại học phải có năng lực số, trí tuệ nhân tạo, ngoại ngữ, khả năng thích ứng và học tập suốt đời; đo lường được; tối thiểu 120 tín chỉ. Chương trình đang thực hiện phải rà soát, hoàn thiện trong 36 tháng.
- **Thông tư 49/2026/TT-BGDĐT** – Ứng dụng công nghệ trong giáo dục đại học, giáo dục nghề nghiệp (hiệu lực 15/8/2026): Cơ sở đào tạo ban hành quy tắc ứng xử về sử dụng AI và quy định liêm chính học thuật; AI là công cụ hỗ trợ, không thay thế giảng viên; không công bố việc dùng AI khi có yêu cầu là vi phạm.
- **Luật Trí tuệ nhân tạo số 134/2025/QH15** – Hiệu lực 01/3/2026: Căn cứ cho nội dung AI có trách nhiệm, quản trị rủi ro AI trong học phần INFO3001, SOFT3004 và hướng chuyên sâu.
- **Quyết định 1528/QĐ-TTg** – Chương trình quốc gia phát triển nhân lực trí tuệ nhân tạo đến 2030, định hướng 2035 (11/8/2026): Đến 2030, 100% cơ sở giáo dục đại học triển khai quy định về sử dụng AI trong đào tạo, nghiên cứu, đánh giá; xây dựng Khung năng lực AI quốc gia.
