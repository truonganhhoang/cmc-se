# -*- coding: utf-8 -*-
"""Dữ liệu CTĐT Kỹ thuật phần mềm AI-native, Trường Đại học CMC (bản đề xuất).
Nguồn duy nhất để sinh các trang ctdt/*.html và đồng bộ trang tuyển sinh."""

META = dict(
    name="Kỹ thuật phần mềm", name_en="Software Engineering", code="7480103", adm_code="SE",
    version="v2027.3 (đề xuất)", updated="23/11/2026", years=3, sems=9, weeks=10,
    level="Đại học (bậc 6, Khung trình độ quốc gia Việt Nam)", mode="Chính quy",
    unit="Khoa Công nghệ Thông tin và Truyền thông, Trường Đại học CMC",
    note="Bản đề xuất chỉnh sửa lớn chương trình đào tạo để Khoa, Hội đồng Khoa học & Đào tạo xem xét. "
         "Mã học phần mới, số tín chỉ và phân bổ học kỳ là dự kiến, chờ thẩm định và phê duyệt theo quy định.",
)

PHILOSOPHY = [
    ("Ship từ học kỳ 1", "Mỗi học kỳ 10 tuần kết thúc bằng Demo Day: sinh viên trình diễn một sản phẩm chạy thật. Sau 9 học kỳ, mỗi sinh viên có hồ sơ 9 sản phẩm."),
    ("AI là đồng nghiệp, kỹ sư là người chịu trách nhiệm", "AI có mặt ở mọi học phần chuyên môn với mức sử dụng được quy định cho từng bài đánh giá. Người ký tên vào sản phẩm luôn là sinh viên."),
    ("Nền tảng tinh gọn, không lùi", "Bớt giờ giảng lý thuyết cho những phần AI làm tốt hoặc sẽ sớm lỗi thời, dồn thời gian cho thực hành và phán đoán kỹ thuật. Phần cốt lõi vẫn thi không AI: hai cổng năng lực cuối năm 1 và năm 2 bảo đảm sinh viên tự đọc, tự viết, tự sửa và tự đánh giá được code, thiết kế do AI đưa ra."),
    ("Đặc tả trước, code sau", "Kỹ năng viết yêu cầu và đặc tả đủ rõ cho cả người lẫn AI agent được dạy riêng và chấm điểm từ năm 2."),
    ("Doanh nghiệp vào lớp học", "Từ học kỳ 6, đề bài Studio đến từ các công ty thuộc Tập đoàn Công nghệ CMC; học kỳ 8 là thực tập OJT."),
    ("Chương trình có changelog và học phần mở", "CTĐT được quản lý như phần mềm: có số phiên bản, ghi chép thay đổi, rà soát công nghệ mỗi năm. Hai học phần mở (Chủ đề hiện đại; Nghiên cứu và đổi mới) có chuẩn đầu ra cố định nhưng nội dung đổi hằng năm, đưa công nghệ mới vào lớp ngay mà không phải sửa chương trình."),
]

POS = [
    ("PO1", "Có nền tảng vững về khoa học máy tính và kỹ thuật phần mềm để hiểu, đánh giá và sửa được phần mềm, kể cả phần mềm do AI sinh ra."),
    ("PO2", "Xây dựng, kiểm chứng, triển khai và vận hành sản phẩm phần mềm có chất lượng, làm việc hiệu quả cùng trợ lý và tác tử AI."),
    ("PO3", "Thiết kế và tích hợp tính năng AI vào sản phẩm một cách an toàn, đo lường được và có trách nhiệm."),
    ("PO4", "Làm việc nhóm, giao tiếp chuyên nghiệp, sử dụng được tiếng Anh trong công việc kỹ thuật, làm việc với khách hàng và doanh nghiệp."),
    ("PO5", "Tuân thủ pháp luật và đạo đức nghề nghiệp; tự học, thích ứng với công nghệ thay đổi nhanh; có tư duy sản phẩm và khởi nghiệp."),
]

# PLO: (mã, nhóm theo TT54, mô tả, [PI], liên hệ PO)
PLOS = [
    ("PLO1", "Kiến thức", "Vận dụng kiến thức toán, khoa học máy tính và kỹ thuật phần mềm để phân tích và giải quyết bài toán phần mềm.",
     [("PI1.1", "Chọn và cài đặt đúng cấu trúc dữ liệu, giải thuật cho bài toán có ràng buộc hiệu năng, trong bài thi không dùng AI."),
      ("PI1.2", "Giải thích và sửa được lỗi trong mã nguồn của người khác hoặc do AI sinh ra.")], "PO1"),
    ("PLO2", "Kỹ năng", "Thu thập, phân tích và đặc tả yêu cầu rõ ràng, kiểm chứng được cho cả con người và AI agent.",
     [("PI2.1", "Viết câu chuyện người dùng, tiêu chí chấp nhận và đặc tả kỹ thuật đạt rubric đặc tả của Khoa."),
      ("PI2.2", "Đặc tả được một tính năng đủ để AI agent cài đặt và vượt qua bộ kiểm thử chấp nhận cho trước.")], "PO2"),
    ("PLO3", "Kỹ năng", "Thiết kế kiến trúc, dữ liệu, API và giao diện cho hệ thống phần mềm có quy mô.",
     [("PI3.1", "Lập và bảo vệ bản thiết kế kiến trúc có ghi chép quyết định (ADR) cho một sản phẩm nhiều thành phần."),
      ("PI3.2", "Thiết kế cơ sở dữ liệu và API đáp ứng yêu cầu chức năng và phi chức năng đã đặc tả.")], "PO1, PO2"),
    ("PLO4", "Kỹ năng", "Lập trình thành thạo và làm việc hiệu quả cùng trợ lý lập trình AI, AI agent theo quy trình có kiểm soát.",
     [("PI4.1", "Hoàn thành bài thực hành lập trình trong thời gian quy định cả khi có và không có AI."),
      ("PI4.2", "Điều phối AI agent hoàn thành một tác vụ nhiều bước, có nhật ký, đánh giá và từ chối được đề xuất sai.")], "PO2"),
    ("PLO5", "Kỹ năng", "Kiểm chứng chất lượng phần mềm bằng kiểm thử tự động, review, phân tích bảo mật và đo lường.",
     [("PI5.1", "Xây bộ kiểm thử tự động đạt ngưỡng bao phủ và phát hiện được lỗi gieo sẵn (mutation)."),
      ("PI5.2", "Phát hiện và khắc phục lỗ hổng bảo mật phổ biến trong mã do người và AI viết.")], "PO2"),
    ("PLO6", "Kỹ năng", "Triển khai và vận hành phần mềm trên đám mây với CI/CD, giám sát và quản lý sự cố.",
     [("PI6.1", "Thiết lập pipeline CI/CD triển khai tự động một sản phẩm lên môi trường đám mây."),
      ("PI6.2", "Đặt chỉ số, cảnh báo và xử lý một sự cố giả lập theo quy trình.")], "PO2"),
    ("PLO7", "Năng lực AI", "Xây dựng, đánh giá và quản trị tính năng AI trong sản phẩm phần mềm.",
     [("PI7.1", "Tích hợp mô hình ngôn ngữ (RAG hoặc agent) vào sản phẩm và đánh giá bằng bộ đánh giá (eval) có chỉ số."),
      ("PI7.2", "Lập hồ sơ rủi ro AI của sản phẩm: dữ liệu, an toàn, chi phí, tuân thủ Luật Trí tuệ nhân tạo.")], "PO3"),
    ("PLO8", "Kỹ năng", "Làm việc nhóm theo Agile, giao tiếp kỹ thuật, đọc hiểu và viết tài liệu kỹ thuật tiếng Anh, làm việc với khách hàng.",
     [("PI8.1", "Hoàn thành vai trò trong nhóm qua các sprint, được đánh giá chéo và theo dữ liệu kho mã."),
      ("PI8.2", "Viết tài liệu dự án bằng tiếng Anh (README, mô tả pull request, tệp ngữ cảnh cho AI agent) đạt rubric; trình bày sản phẩm rõ ràng trước khách hàng và hội đồng.")], "PO4"),
    ("PLO9", "Tự chủ và trách nhiệm", "Tuân thủ pháp luật, đạo đức nghề nghiệp và liêm chính học thuật khi sử dụng công nghệ và AI.",
     [("PI9.1", "Khai báo đầy đủ, trung thực việc dùng AI theo quy tắc ứng xử của Trường trong mọi sản phẩm học thuật."),
      ("PI9.2", "Phân tích được vấn đề pháp lý, đạo đức (dữ liệu cá nhân, sở hữu trí tuệ, AI) của một sản phẩm cụ thể.")], "PO5"),
    ("PLO10", "Năng lực số và học tập suốt đời", "Tự học, thích ứng công nghệ mới, có tư duy sản phẩm và đổi mới sáng tạo.",
     [("PI10.1", "Tự học và áp dụng một công nghệ chưa được dạy để hoàn thành sản phẩm, có báo cáo phản tư."),
      ("PI10.2", "Xây hồ sơ năng lực số gồm các sản phẩm, minh chứng đóng góp và kế hoạch phát triển nghề nghiệp.")], "PO5"),
]

AI_LADDER = [
    ("B1", "Hiểu và dùng an toàn", "Năm 1", "Biết AI làm được gì, sai ở đâu; đặt câu hỏi tốt; kiểm chứng câu trả lời; không đưa dữ liệu nhạy cảm vào công cụ công cộng."),
    ("B2", "Cộng tác", "Năm 1–2", "Lập trình cặp với AI, nhờ AI sinh test, review, giải thích; luôn hiểu và giải thích được mã mình nộp."),
    ("B3", "Điều phối", "Năm 2", "Viết đặc tả và ngữ cảnh cho AI agent, chia việc nhiều bước, đặt rào chắn (test, review, quyền hạn), đo chất lượng đầu ra."),
    ("B4", "Xây dựng", "Năm 3", "Xây tính năng AI trong sản phẩm: RAG, agent dùng công cụ; thiết kế bộ đánh giá (eval) và giám sát."),
    ("B5", "Quản trị", "Năm 3", "Đánh giá rủi ro, bảo mật, chi phí và tuân thủ pháp luật của hệ thống AI; ra quyết định khi nào không dùng AI."),
]

# Thang mức dùng AI trong đánh giá (tham khảo AI Assessment Scale - Perkins và cộng sự, 2024)
AI_LEVELS = [
    ("M1", "Không AI", "Làm độc lập trong phòng thi có kiểm soát. Dùng cho bài thi nền tảng và vấn đáp.", "#C44536"),
    ("M2", "AI hỗ trợ học", "Được hỏi AI để hiểu bài, lên ý tưởng; không nộp nội dung do AI tạo.", "#D98E04"),
    ("M3", "AI cộng tác có nhật ký", "AI được viết một phần sản phẩm; bắt buộc nhật ký AI và giải thích được mọi phần.", "#2F7D9A"),
    ("M4", "AI toàn phần có kiểm chứng", "Được dùng AI agent tự do; chấm cả kết quả lẫn quy trình kiểm chứng, review, kiểm thử.", "#2E7D4F"),
    ("M5", "Xây dựng AI", "Đối tượng đánh giá là chính hệ thống AI sinh viên xây và đánh giá.", "#5B4BB7"),
]

ASSESS = {
    "nen-tang": [("Tự học trên Trợ giảng AI", "10%", "M2"), ("Thực hành hằng tuần", "20%", "M3"), ("Giữa kỳ: thi thực hành trên máy", "20%", "M1"), ("Cuối kỳ: thi tự luận/thực hành", "50%", "M1")],
    "ky-nghe": [("Tự học trên Trợ giảng AI", "5%", "M2"), ("Bài thực hành", "20%", "M3"), ("Giữa kỳ: sản phẩm/bài tập lớn", "25%", "M4"), ("Cuối kỳ: sản phẩm + vấn đáp cá nhân", "50%", "M4 + M1")],
    "ai": [("Tự học trên Trợ giảng AI", "5%", "M2"), ("Bài thực hành và eval", "25%", "M5"), ("Giữa kỳ: nguyên mẫu", "20%", "M4"), ("Cuối kỳ: hệ thống AI + báo cáo đánh giá + vấn đáp", "50%", "M5 + M1")],
    "studio": [("Sprint review (3 lần)", "30%", "M4"), ("Nhật ký AI và phản tư", "10%", "M3"), ("Demo Day tuần 10", "40%", "M4"), ("Vấn đáp cá nhân: giải thích code", "20%", "M1")],
    "chung": [("Theo đề cương học phần chung của Trường", "", "M2")],
    "mo": [("Nhật ký tìm hiểu và tóm tắt tài liệu gốc", "20%", "M3"), ("Demo kỹ thuật giữa kỳ", "15%", "M4"), ("Nguyên mẫu và báo cáo đo đạc", "35%", "M4"), ("Khuyến nghị áp dụng (Tech Radar) + vấn đáp", "30%", "M4 + M1")],
    "nghien-cuu": [("Đề cương nghiên cứu và tổng quan tài liệu", "20%", "M3"), ("Nhật ký thực nghiệm hằng tuần", "15%", "M3"), ("Kết quả thực nghiệm, mã và dữ liệu tái lập được", "35%", "M4"), ("Bài báo ngắn hoặc poster + bảo vệ", "30%", "M3 + M1")],
    "thuc-tap": [("Đánh giá của người hướng dẫn doanh nghiệp", "50%", "M4"), ("Báo cáo thực tập và nhật ký tuần", "30%", "M3"), ("Bảo vệ trước giảng viên", "20%", "M1")],
    "do-an": [("Tiến độ và sản phẩm qua 3 mốc", "30%", "M4"), ("Sản phẩm cuối, người dùng/khách hàng thật", "40%", "M4"), ("Bảo vệ trước hội đồng có doanh nghiệp", "30%", "M1")],
}

BLOCKS = {
    "dc": "Giáo dục đại cương",
    "csn": "Cơ sở ngành",
    "nganh": "Kiến thức ngành",
    "studio": "Trục Studio sản phẩm",
    "cs": "Chuyên sâu và tự chọn",
    "tn": "Thực tập và tốt nghiệp",
}
STATUS = {"giu": "Giữ, cập nhật lớn", "thay": "Thay thế học phần cũ", "moi": "Mới", "chung": "Học phần chung", "gop": "Gộp, tái cấu trúc"}

def C(code, name, en, tc, lt, th, tu, sem, block, status, old="", prereq="", desc="", clos=(), weeks=(), assess="ky-nghe", refs="", plos=(), ai="", product="", kind="BB", track=""):
    return dict(code=code, name=name, en=en, tc=tc, lt=lt, th=th, tu=tu, sem=sem, block=block, status=status, old=old, prereq=prereq,
                desc=desc, clos=list(clos), weeks=list(weeks), assess=assess, refs=refs, plos=list(plos), ai=ai, product=product, kind=kind, track=track)

def studio(n, sem, tc, theme, product, focus, extra, prereq, plos, ai):
    weeks = [
        f"Khởi động: chọn bài toán, phỏng vấn người dùng, viết đặc tả và tiêu chí chấp nhận cho {product.lower()}.",
        f"Thiết kế: phác thảo giao diện, dữ liệu, kiến trúc; chia việc; thiết lập kho mã, CI và quy ước dùng AI.",
        f"Sprint 1: lát cắt chức năng đầu tiên chạy được từ đầu đến cuối; {focus[0]}.",
        f"Sprint 1 (tiếp): kiểm thử, review chéo; Sprint review 1 với giảng viên.",
        f"Sprint 2: mở rộng chức năng chính; {focus[1]}.",
        f"Sprint 2 (tiếp): đo chất lượng, sửa lỗi; Sprint review 2, đối chiếu nhật ký AI.",
        f"Sprint 3: hoàn thiện; {focus[2]}.",
        f"Sprint 3 (tiếp): thử nghiệm với người dùng thật, thu phản hồi; Sprint review 3.",
        "Làm cứng sản phẩm: kiểm thử hồi quy, rà soát bảo mật, tài liệu, chuẩn bị trình diễn.",
        "Demo Day: trình diễn trước hội đồng" + (" có doanh nghiệp" if sem >= 6 else "") + "; vấn đáp cá nhân giải thích code; phản tư.",
    ]
    return C(f"SOFT{n}", f"Studio {n - 1100 if n < 1200 else n - 1197}: {theme}", f"Software Studio: {theme}", tc, 5, 50 if tc == 2 else 75, 45 if tc == 2 else 70, sem, "studio", "moi",
             prereq=prereq, desc=f"Học phần dự án xuyên suốt của học kỳ {sem}. Sinh viên {extra}",
             clos=[("CLO1", "Đặc tả và lập kế hoạch một sản phẩm phần mềm theo nhu cầu người dùng thật."),
                   ("CLO2", "Xây dựng sản phẩm chạy được, có kiểm thử, dùng AI ở mức được phép và có nhật ký."),
                   ("CLO3", "Trình diễn, giải thích và bảo vệ được mọi phần mã nguồn của mình khi không có AI.")],
             weeks=weeks, assess="studio", plos=plos, ai=ai, product=product)

COURSES = [
 # ---------------- HỌC KỲ 1 ----------------
 C("SOFT1001", "Nhập môn Kỹ thuật phần mềm AI-native", "Introduction to AI-native Software Engineering", 3, 20, 25, 90, 1, "csn", "thay", old="INFO2013",
   desc="Nhập môn ngành theo hướng làm sản phẩm: phần mềm được làm ra thế nào, vai trò của kỹ sư phần mềm khi có AI, cách học hiệu quả với AI, máy tính và mạng ở mức đủ dùng, đạo đức và an toàn khi dùng AI. Sinh viên xây và đưa trang portfolio cá nhân lên Internet ngay trong 3 tuần đầu.",
   clos=[("CLO1", "Mô tả vòng đời phần mềm và các vai trò trong một đội phần mềm có AI."), ("CLO2", "Dùng Git, dòng lệnh, trình soạn thảo và trợ lý AI để làm và đưa một trang web lên Internet."), ("CLO3", "Áp dụng quy tắc dùng AI an toàn, trung thực và khai báo được việc dùng AI.")],
   weeks=["Ngành Kỹ thuật phần mềm, nghề kỹ sư phần mềm thời AI; cách học trong chương trình AI-native; quy tắc ứng xử về AI.",
          "Máy tính, hệ điều hành, tệp và dòng lệnh; môi trường phát triển trên cloud; Git và GitHub cơ bản.",
          "Web hoạt động thế nào: HTTP, HTML, CSS; xây và đưa portfolio cá nhân lên Internet.",
          "AI tạo sinh và mô hình ngôn ngữ: làm được gì, sai thế nào (ảo giác, thiên lệch); kỹ năng đặt câu hỏi và kiểm chứng.",
          "Thuật toán và lưu đồ; từ bài toán đến chương trình; dùng AI để giải thích, không để làm hộ.",
          "Vòng đời phần mềm và các vai trò: yêu cầu, thiết kế, lập trình, kiểm thử, vận hành; ai làm gì khi có AI agent.",
          "Mạng máy tính và Internet ở mức kỹ sư phần mềm cần: DNS, máy chủ, dịch vụ đám mây.",
          "Dữ liệu, quyền riêng tư và bảo mật cơ bản; Luật Trí tuệ nhân tạo và liêm chính học thuật.",
          "Làm việc nhóm, giao tiếp kỹ thuật, ghi nhật ký AI và phản tư.",
          "Trình bày portfolio và kế hoạch học tập cá nhân; kiểm tra cuối kỳ."],
   assess="ky-nghe", refs="Campbell và cộng sự, Digital Technology, Data, and Devices (2023); tài liệu nội bộ về quy tắc dùng AI của Trường.",
   plos=[("PLO9", "I"), ("PLO10", "I"), ("PLO4", "I")], ai="B1"),
 C("PROG2005", "Cơ sở lập trình (Python, có trợ lý AI)", "Programming Fundamentals", 4, 30, 30, 120, 1, "csn", "giu", old="PROG2005",
   desc="Tư duy lập trình và Python: biến, kiểu dữ liệu, rẽ nhánh, vòng lặp, hàm, cấu trúc dữ liệu có sẵn, xử lý tệp và ngoại lệ, kiểm thử đơn vị đầu tiên. Trợ lý AI được dùng như gia sư trong giờ thực hành; các bài thi đo năng lực lập trình độc lập, không dùng AI.",
   clos=[("CLO1", "Viết chương trình Python giải bài toán nhỏ, đúng và dễ đọc, không cần AI."), ("CLO2", "Đọc hiểu, tìm và sửa lỗi trong chương trình của người khác hoặc do AI sinh."), ("CLO3", "Viết kiểm thử đơn vị cho hàm do mình viết.")],
   weeks=["Giới thiệu Python, môi trường, biến, kiểu dữ liệu, nhập xuất; quy tắc dùng trợ lý AI trong học phần.",
          "Biểu thức, rẽ nhánh; đọc lỗi và gỡ lỗi; nhờ AI giải thích thông báo lỗi.",
          "Vòng lặp; mẫu bài toán đếm, tổng, tìm kiếm.",
          "Hàm, tham số, phạm vi biến; viết kiểm thử đơn vị đầu tiên.",
          "Chuỗi, danh sách, bộ; xử lý văn bản.",
          "Từ điển, tập hợp; bài toán dữ liệu nhỏ. Giữa kỳ: thi thực hành trên máy không AI.",
          "Tệp, ngoại lệ; đọc và ghi dữ liệu CSV/JSON.",
          "Lập trình hướng đối tượng mở đầu trong Python; module và thư viện.",
          "Trực quan hóa dữ liệu đơn giản; đọc mã do AI sinh và tìm lỗi cài cắm.",
          "Ôn tập, dự án nhỏ; thi cuối kỳ không AI."],
   assess="nen-tang", refs="Gaddis, Starting Out with Python (2021); Guzdial, Introduction to Computing and Programming in Python (2023).",
   plos=[("PLO1", "I"), ("PLO4", "I")], ai="B1–B2"),
 C("MATH2005", "Toán rời rạc và logic cho lập trình", "Discrete Mathematics and Logic for Programming", 2, 15, 15, 60, 1, "dc", "gop", old="MATH2005",
   desc="Tinh gọn từ 3 xuống 2 tín chỉ, giữ phần kỹ sư phần mềm dùng hằng ngày: logic (để đặc tả và kiểm thử), tập hợp, quan hệ, đếm, đồ thị và cây; mọi chủ đề học qua bài cài đặt Python. Bớt phần chứng minh hình thức và hệ đếm, đại số Bool chuyển thành tự học có Trợ giảng AI.",
   clos=[("CLO1", "Dùng logic, tập hợp, quan hệ để mô hình hóa và đặc tả bài toán tin học."), ("CLO2", "Giải bài toán đếm và đồ thị cơ bản, cài đặt được bằng Python.")],
   weeks=["Logic mệnh đề; điều kiện trong chương trình và đặc tả.", "Logic vị từ; tiền điều kiện, hậu điều kiện, bất biến.", "Tập hợp, quan hệ, hàm; ánh xạ sang kiểu dữ liệu Python.", "Phương pháp đếm; đếm số ca kiểm thử.", "Đệ quy và quy nạp qua bài lập trình; giữa kỳ.",
          "Đồ thị: khái niệm, biểu diễn bằng Python.", "Duyệt đồ thị; đường đi.", "Cây; cây quyết định.", "Ứng dụng: phụ thuộc gói, lập lịch, mạng xã hội.", "Ôn tập; thi cuối kỳ."],
   assess="nen-tang", refs="Rosen, Discrete Mathematics and Its Applications; Lehman, Leighton, Meyer, Mathematics for Computer Science.", plos=[("PLO1", "I")], ai="B1"),
 C("SOFT1101", "Studio 1: Sản phẩm số đầu tiên", "", 2, 0, 0, 0, 1, "studio", "moi"),
 C("POLI1001", "Triết học Mác – Lênin", "Marxist–Leninist Philosophy", 3, 0, 0, 0, 1, "dc", "chung", assess="chung"),

 # ---------------- HỌC KỲ 2 ----------------
 C("INFO2002", "Cấu trúc dữ liệu và giải thuật", "Data Structures and Algorithms", 3, 20, 25, 90, 2, "csn", "giu", old="INFO2002", prereq="PROG2005",
   desc="Kiểu dữ liệu trừu tượng, danh sách, ngăn xếp, hàng đợi, bảng băm, cây, đồ thị; sắp xếp, tìm kiếm; chia để trị, quy hoạch động; phân tích độ phức tạp. Đây là học phần nền tảng giữ thi không AI để bảo đảm năng lực tự giải bài toán; AI được dùng để luyện tập và so sánh lời giải. v2027.3 chuyển 10 tiết lý thuyết sang thực hành cài đặt, đo hiệu năng.",
   clos=[("CLO1", "Chọn và cài đặt cấu trúc dữ liệu phù hợp theo yêu cầu hiệu năng."), ("CLO2", "Phân tích độ phức tạp, so sánh và cải tiến lời giải, kể cả lời giải do AI đưa ra."), ("CLO3", "Giải bài toán thuật toán trong thời gian giới hạn không dùng AI.")],
   weeks=["Giới thiệu, phân tích độ phức tạp; luật dùng AI để luyện tập.", "Mảng, danh sách liên kết, ngăn xếp, hàng đợi.", "Bảng băm; sắp xếp cơ bản.", "Sắp xếp nâng cao, tìm kiếm nhị phân; so sánh với lời giải do AI sinh.",
          "Cây, cây nhị phân tìm kiếm.", "Cây cân bằng, heap; giữa kỳ thi thực hành không AI.", "Đồ thị: biểu diễn, duyệt.", "Đường đi ngắn nhất, cây khung.", "Chia để trị, quy hoạch động.", "Ôn tập; thi cuối kỳ không AI."],
   assess="nen-tang", refs="Goodrich, Tamassia, Goldwasser, Data Structures and Algorithms; Cormen và cộng sự, Introduction to Algorithms.", plos=[("PLO1", "R")], ai="B2"),
 C("INFO2007", "Cơ sở dữ liệu", "Databases", 3, 20, 25, 90, 2, "csn", "giu", old="INFO2007", prereq="PROG2005",
   desc="Mô hình quan hệ, SQL, mô hình E-R, chuẩn hóa, giao tác, chỉ mục; thực hành trên PostgreSQL. Bổ sung: dùng AI sinh và rà soát truy vấn, nhận diện truy vấn sai hoặc không an toàn; giới thiệu cơ sở dữ liệu vector cho ứng dụng AI.",
   clos=[("CLO1", "Thiết kế lược đồ cơ sở dữ liệu quan hệ chuẩn hóa từ yêu cầu."), ("CLO2", "Viết và tối ưu truy vấn SQL; phát hiện truy vấn sai, không an toàn do AI sinh."), ("CLO3", "Tích hợp cơ sở dữ liệu vào một ứng dụng.")],
   weeks=["Giới thiệu hệ cơ sở dữ liệu; PostgreSQL.", "Mô hình quan hệ, đại số quan hệ.", "SQL: truy vấn cơ bản.", "SQL nâng cao: kết nối, gộp nhóm, truy vấn con; rà soát SQL do AI sinh.",
          "Mô hình E-R; từ yêu cầu đến lược đồ.", "Chuẩn hóa; giữa kỳ.", "Giao tác, khóa, chỉ mục và hiệu năng.", "Bảo mật dữ liệu, SQL injection, phân quyền.", "Xu hướng: NoSQL, cơ sở dữ liệu vector cho ứng dụng AI.", "Ôn tập; thi cuối kỳ."],
   assess="nen-tang", refs="Silberschatz, Korth, Sudarshan, Database System Concepts.", plos=[("PLO3", "I"), ("PLO1", "R")], ai="B2"),
 C("PROG2101", "Phát triển web full-stack", "Full-stack Web Development", 3, 15, 30, 90, 2, "nganh", "moi", prereq="SOFT1001, PROG2005",
   desc="JavaScript/TypeScript, giao diện web theo thành phần, API REST, xác thực người dùng, kết nối cơ sở dữ liệu, triển khai lên cloud. Lập trình cặp với AI có nhật ký; mỗi sinh viên phải giải thích được toàn bộ mã của mình.",
   clos=[("CLO1", "Xây ứng dụng web có giao diện, API, đăng nhập và cơ sở dữ liệu."), ("CLO2", "Dùng trợ lý AI có kiểm soát: nhật ký, kiểm thử, giải thích được mã."), ("CLO3", "Triển khai ứng dụng web lên môi trường đám mây.")],
   weeks=["JavaScript hiện đại và TypeScript; công cụ phát triển.", "DOM, sự kiện, gọi API.", "Khung giao diện theo thành phần (React hoặc tương đương).", "Quản lý trạng thái, định tuyến, biểu mẫu.",
          "Máy chủ Node.js, API REST.", "Kết nối cơ sở dữ liệu; giữa kỳ: nộp ứng dụng có CRUD.", "Xác thực, phân quyền, bảo mật web cơ bản.", "Kiểm thử thành phần và API.", "Triển khai lên cloud; tên miền, HTTPS.", "Trình diễn ứng dụng, vấn đáp."],
   assess="ky-nghe", refs="Tài liệu MDN Web Docs; Sakhniuk, Boduch, React and React Native (2024).", plos=[("PLO4", "R"), ("PLO6", "I")], ai="B2"),
 C("SOFT1102", "Studio 2: Ứng dụng dữ liệu", "", 2, 0, 0, 0, 2, "studio", "moi"),
 C("POLI1002", "Kinh tế chính trị Mác – Lênin", "Marxist–Leninist Political Economy", 2, 0, 0, 0, 2, "dc", "chung", assess="chung"),

 # ---------------- HỌC KỲ 3 ----------------
 C("PROG2006", "Lập trình hướng đối tượng và mã sạch", "Object-oriented Programming and Clean Code", 3, 15, 30, 90, 3, "csn", "giu", old="PROG2006", prereq="PROG2005",
   desc="Đóng gói, kế thừa, đa hình, trừu tượng; mẫu thiết kế; tái cấu trúc và mã sạch; kiểm thử đơn vị. Cập nhật: thực hành tái cấu trúc mã do AI sinh, đánh giá thiết kế đề xuất bởi AI theo nguyên lý SOLID.",
   clos=[("CLO1", "Thiết kế lớp và quan hệ giữa các lớp theo nguyên lý hướng đối tượng."), ("CLO2", "Áp dụng mẫu thiết kế và tái cấu trúc mã, kể cả mã do AI sinh."), ("CLO3", "Viết kiểm thử đơn vị cho chương trình hướng đối tượng.")],
   weeks=["Lập trình trên ngôn ngữ hướng đối tượng (Java hoặc TypeScript); đóng gói.", "Kế thừa.", "Đa hình.", "Trừu tượng, giao diện; nguyên lý SOLID.", "Kiểu dữ liệu nâng cao, generic, collection; giữa kỳ.",
          "Mẫu thiết kế khởi tạo và cấu trúc.", "Mẫu thiết kế hành vi.", "Mã sạch và tái cấu trúc: thực hành trên mã do AI sinh.", "Kiểm thử đơn vị, mock.", "Dự án nhỏ; thi cuối kỳ."],
   assess="nen-tang", refs="Wu, An Introduction to Object-Oriented Programming with Java; Nesteruk, Design Patterns.", plos=[("PLO1", "R"), ("PLO3", "I"), ("PLO4", "R")], ai="B2"),
 C("MATH2101", "Toán cho AI: Đại số tuyến tính và Xác suất thống kê", "Mathematics for AI", 3, 20, 25, 90, 3, "dc", "moi",
   desc="Vectơ, ma trận, phép biến đổi tuyến tính, độ tương đồng; xác suất, phân phối, kỳ vọng, suy luận thống kê, kiểm định; ứng dụng trong học máy, tìm kiếm ngữ nghĩa và đánh giá A/B. Mọi chủ đề đều có bài thực hành Python.",
   clos=[("CLO1", "Vận dụng đại số tuyến tính để biểu diễn và xử lý dữ liệu, nhúng (embedding)."), ("CLO2", "Vận dụng xác suất thống kê để đánh giá mô hình và thử nghiệm sản phẩm.")],
   weeks=["Vectơ, độ dài, tích vô hướng; độ tương đồng cosine.", "Ma trận, phép nhân, hệ phương trình.", "Biến đổi tuyến tính; trị riêng ở mức ứng dụng.", "Nhúng văn bản và tìm kiếm ngữ nghĩa với Python.",
          "Xác suất, biến cố, xác suất có điều kiện; giữa kỳ.", "Biến ngẫu nhiên, phân phối.", "Thống kê mô tả, ước lượng.", "Kiểm định giả thuyết, thử nghiệm A/B.", "Chỉ số đánh giá mô hình: độ chính xác, độ nhạy, F1.", "Ôn tập; thi cuối kỳ."],
   assess="nen-tang", refs="Deisenroth, Faisal, Ong, Mathematics for Machine Learning.", plos=[("PLO1", "R"), ("PLO7", "I")], ai="B2"),
 C("ENGL2002", "Tiếng Anh kỹ thuật cho kỹ sư phần mềm", "Technical English for Software Engineers", 2, 10, 20, 60, 3, "dc", "gop", old="ENGL2001, ENGL3001",
   desc="Gộp Tiếng Anh chuyên ngành 1 (3 TC) và Giao tiếp kỹ thuật bằng tiếng Anh (2 TC) thành một học phần 2 tín chỉ, tập trung vào việc kỹ sư phần mềm thật sự làm bằng tiếng Anh: đọc tài liệu, đặc tả, mã nguồn; viết README, issue, mô tả pull request, tệp ngữ cảnh cho AI agent. Dùng AI dịch, tóm tắt và sửa văn có kiểm chứng; luyện thuyết trình kỹ thuật ngắn. Chuẩn đầu ra ngoại ngữ chung theo quy định của Trường.",
   clos=[("CLO1", "Đọc hiểu tài liệu kỹ thuật tiếng Anh, có dùng AI hỗ trợ và kiểm chứng được."), ("CLO2", "Viết tài liệu dự án ngắn bằng tiếng Anh cho người và cho AI agent.")],
   weeks=["Đọc tài liệu kỹ thuật: cấu trúc, từ vựng cốt lõi; dùng AI dịch và tóm tắt, kiểm chứng với bản gốc.", "Đọc tài liệu API và thông báo lỗi; tìm câu trả lời trong tài liệu chính thức.", "Viết README.", "Viết issue và báo lỗi tái hiện được.", "Mô tả pull request, nhận xét review; giữa kỳ.",
          "Viết đặc tả ngắn và tệp hướng dẫn dự án cho AI agent bằng tiếng Anh.", "Viết tài liệu thiết kế ngắn; AI góp ý độ rõ, sinh viên tự quyết định sửa.", "Email và tin nhắn công việc với khách hàng, đồng nghiệp nước ngoài.", "Thuyết trình kỹ thuật 3 phút.", "Bài cuối kỳ: hồ sơ tài liệu tiếng Anh của Studio 3."],
   assess="ky-nghe", plos=[("PLO8", "I")], ai="B1–B2"),
 C("SOFT3003", "Thiết kế trải nghiệm người dùng", "User Experience Design", 2, 15, 15, 60, 3, "nganh", "moi", prereq="PROG2101",
   desc="Nghiên cứu người dùng, thiết kế tương tác, nguyên mẫu, kiểm tra khả dụng, khả năng tiếp cận; thiết kế trải nghiệm cho tính năng AI (độ tin cậy, giải thích, sửa lỗi của AI). v2027.3 chuyển từ học kỳ 6 lên học kỳ 3 để đi cùng Studio 3 (sản phẩm có người dùng thật).",
   clos=[("CLO1", "Thiết kế và kiểm tra khả dụng một giao diện."), ("CLO2", "Thiết kế trải nghiệm phù hợp cho tính năng AI.")],
   weeks=["Trải nghiệm người dùng là gì.", "Nghiên cứu người dùng.", "Kiến trúc thông tin, luồng.", "Nguyên mẫu nhanh, dùng AI tạo nguyên mẫu.", "Kiểm tra khả dụng; giữa kỳ.",
          "Khả năng tiếp cận.", "Thiết kế cho tính năng AI: kỳ vọng, sai sót, quyền kiểm soát.", "Hệ thống thiết kế.", "Đo trải nghiệm.", "Bảo vệ thiết kế."],
   assess="ky-nghe", refs="Norman, The Design of Everyday Things; Google PAIR, People + AI Guidebook.", plos=[("PLO3", "R"), ("PLO2", "R")], ai="B2–B3"),
 C("SOFT1103", "Studio 3: Sản phẩm có người dùng", "", 2, 0, 0, 0, 3, "studio", "moi"),
 C("POLI1003", "Chủ nghĩa xã hội khoa học", "Scientific Socialism", 2, 0, 0, 0, 3, "dc", "chung", assess="chung"),

 # ---------------- HỌC KỲ 4 ----------------
 C("SOFT2001", "Kỹ nghệ yêu cầu và đặc tả cho người và AI agent", "Requirements and Specification for Humans and AI Agents", 3, 20, 25, 90, 4, "nganh", "moi", prereq="PROG2101",
   desc="Thu thập và phân tích yêu cầu, câu chuyện người dùng, tiêu chí chấp nhận, đặc tả kỹ thuật, truy vết yêu cầu. Trọng tâm mới: viết đặc tả đủ rõ để AI agent cài đặt đúng, phát triển hướng đặc tả (spec-driven) và kiểm thử chấp nhận tự động.",
   clos=[("CLO1", "Thu thập và phân tích yêu cầu từ người dùng thật."), ("CLO2", "Viết đặc tả kiểm chứng được cho người và AI agent."), ("CLO3", "Đánh giá mức độ đúng của phần mềm do AI cài đặt so với đặc tả.")],
   weeks=["Vai trò của yêu cầu; vì sao đặc tả quan trọng hơn khi có AI.", "Phỏng vấn, quan sát, chân dung người dùng; AI hỗ trợ tóm tắt phỏng vấn.", "Câu chuyện người dùng, tiêu chí chấp nhận.", "Yêu cầu phi chức năng: hiệu năng, bảo mật, khả dụng.",
          "Mô hình hóa: use case, luồng, trạng thái.", "Đặc tả kỹ thuật và hợp đồng API; giữa kỳ.", "Phát triển hướng đặc tả: đặc tả → AI agent → kiểm thử chấp nhận.", "Ngữ cảnh cho AI: tệp hướng dẫn dự án, ví dụ, ràng buộc.",
          "Truy vết và quản lý thay đổi yêu cầu.", "Bảo vệ bộ đặc tả và kết quả cài đặt bằng AI."],
   assess="ky-nghe", refs="Wiegers, Beatty, Software Requirements; tài liệu thực hành phát triển hướng đặc tả của Khoa.", plos=[("PLO2", "M"), ("PLO4", "R")], ai="B3"),
 C("SOFT2002", "Kiến trúc phần mềm: ra quyết định cùng AI", "Software Architecture: Decision-making with AI", 3, 15, 30, 90, 4, "nganh", "moi", prereq="PROG2006",
   desc="AI đã đề xuất được kiến trúc, sơ đồ, API và bản nháp ADR trong vài phút; việc của kỹ sư là đặt đúng thuộc tính chất lượng, so sánh phương án, kiểm chứng bằng nguyên mẫu và chịu trách nhiệm về quyết định. Học phần dạy các kiểu kiến trúc ở mức đủ để phán đoán (phân lớp, modular monolith, sự kiện, vi dịch vụ), dành phần lớn thời gian cho thực hành: viết kịch bản thuộc tính chất lượng, cho AI sinh nhiều phương án, đánh giá đánh đổi kiểu ATAM rút gọn, hàm kiểm chứng kiến trúc (fitness function) trong CI, ghi ADR và bảo vệ trước hội đồng.",
   clos=[("CLO1", "Thiết kế kiến trúc cho sản phẩm nhiều thành phần từ thuộc tính chất lượng đã đặc tả."), ("CLO2", "Đánh giá, chọn và bảo vệ phương án kiến trúc (kể cả do AI đề xuất) bằng ADR, nguyên mẫu và hàm kiểm chứng.")],
   weeks=["Kiến trúc là các quyết định khó đảo ngược; vai trò của kỹ sư khi AI vẽ được kiến trúc.", "Thuộc tính chất lượng và kịch bản đo được.", "Kiểu kiến trúc cốt lõi: phân lớp, modular monolith, khách–chủ.", "Thiết kế API và dữ liệu: AI sinh bản nháp, sinh viên rà soát hợp đồng.", "Cho AI sinh 3 phương án, so sánh đánh đổi; giữa kỳ.",
          "Kiến trúc hướng sự kiện và vi dịch vụ: khi nào nên, khi nào không.", "Nguyên mẫu xương sống (walking skeleton) để kiểm chứng giả định.", "ADR và hàm kiểm chứng kiến trúc chạy trong CI.", "Kiến trúc cho ứng dụng có thành phần AI: cổng mô hình, đánh giá, rào chắn, chi phí.", "Bảo vệ thiết kế: giải thích vì sao chọn và vì sao không chọn."],
   assess="ky-nghe", refs="Richards, Ford, Fundamentals of Software Architecture, 2nd ed. (2025); Ford và cộng sự, Building Evolutionary Architectures, 2nd ed.", plos=[("PLO3", "M")], ai="B2–B3"),
 C("PROG3002", "Phát triển ứng dụng di động", "Mobile Application Development", 3, 15, 30, 90, 4, "nganh", "giu", old="PROG3002", prereq="PROG2101",
   desc="Phát triển đa nền tảng với React Native hoặc Flutter: giao diện theo thành phần, điều hướng, dữ liệu, gọi API, lưu trữ, triển khai. Cập nhật: dùng AI agent theo đặc tả, kiểm thử giao diện tự động, tích hợp tính năng AI trên thiết bị di động.",
   clos=[("CLO1", "Xây ứng dụng di động đa nền tảng kết nối API."), ("CLO2", "Dùng AI agent theo đặc tả và kiểm chứng bằng kiểm thử."), ("CLO3", "Phát hành bản thử nghiệm cho người dùng.")],
   weeks=["Tổng quan lập trình di động, mô hình phát triển.", "Môi trường, ngôn ngữ, thành phần cơ bản.", "Kiến trúc giao diện theo thành phần, quản lý trạng thái.", "Thiết kế giao diện, nguyên tắc bố cục.", "Giữa kỳ: nguyên mẫu giao diện.",
          "Quản lý và hiển thị dữ liệu, gọi API.", "Điều hướng, lưu trữ cục bộ.", "Kiểm thử giao diện tự động; AI agent làm tính năng theo đặc tả.", "Tích hợp tính năng AI và phát hành thử nghiệm.", "Trình diễn, vấn đáp."],
   assess="ky-nghe", refs="Sakhniuk, Boduch, React and React Native (2024).", plos=[("PLO4", "R"), ("PLO3", "R")], ai="B3"),
 C("SOFT2003", "Hệ thống máy tính và mạng cho kỹ sư phần mềm", "Computer Systems and Networks for Software Engineers", 2, 15, 15, 60, 4, "csn", "thay", old="INFO3007",
   desc="Tinh gọn từ 3 xuống 2 tín chỉ, học qua sự cố thật của ứng dụng: tiến trình, bộ nhớ, đồng thời; TCP/IP, HTTP, DNS, TLS; container. Bỏ chi tiết lớp vật lý, định tuyến; mỗi tuần một bài chẩn đoán: AI gợi ý nguyên nhân từ log, sinh viên kiểm chứng bằng công cụ đo.",
   clos=[("CLO1", "Giải thích cách hệ điều hành và mạng ảnh hưởng đến ứng dụng."), ("CLO2", "Chẩn đoán sự cố hiệu năng và kết nối của ứng dụng.")],
   weeks=["Tiến trình, luồng; đọc thông tin tiến trình từ dòng lệnh.", "Bộ nhớ, rò rỉ bộ nhớ; hệ tệp.", "Đồng thời và tranh chấp dữ liệu qua ví dụ web.", "TCP/IP qua công cụ: ping, traceroute, ss.", "HTTP, DNS, TLS; giữa kỳ.",
          "Container và ảo hóa.", "Gỡ lỗi mạng: AI gợi ý từ log, kiểm chứng bằng công cụ đo.", "Hiệu năng ứng dụng, bộ đệm.", "Bài chẩn đoán tổng hợp.", "Thi thực hành chẩn đoán sự cố."],
   assess="nen-tang", refs="Kurose, Ross, Computer Networking, 9th ed. (2025); Arpaci-Dusseau, Operating Systems: Three Easy Pieces.", plos=[("PLO1", "R"), ("PLO6", "I")], ai="B2"),
 C("SOFT1201", "Studio 4: Ứng dụng di động nhóm", "", 2, 0, 0, 0, 4, "studio", "moi"),
 C("LAW1001", "Pháp luật đại cương", "Introduction to Law", 2, 0, 0, 0, 4, "dc", "chung", assess="chung"),

 # ---------------- HỌC KỲ 5 ----------------
 C("INFO2011", "Công nghệ phần mềm: sản phẩm và Agile", "Software Engineering: Products and Agile", 2, 10, 20, 60, 5, "nganh", "giu", old="INFO2011", prereq="SOFT2001",
   desc="Tinh gọn từ 3 xuống 2 tín chỉ: chỉ giữ phần quy trình và quản lý sản phẩm, vì yêu cầu, kiến trúc, kiểm thử, DevOps và làm việc với AI agent đã có học phần riêng. Quản lý sản phẩm, Agile, Scrum/Kanban, ước lượng, Definition of Done, quản lý mã nguồn và review trong nhóm có AI agent; đo hiệu quả đội bằng chỉ số DORA. Thực hành trên chính sản phẩm của Studio 5.",
   clos=[("CLO1", "Quản lý sản phẩm và dự án theo Agile."), ("CLO2", "Vận dụng quy trình kỹ nghệ phần mềm với AI agent có kiểm soát."), ("CLO3", "Đo và cải tiến hiệu quả làm việc của nhóm.")],
   weeks=["Kỹ nghệ phần mềm theo định hướng sản phẩm; lập thỏa thuận làm việc với AI của nhóm.", "Quản lý sản phẩm: tầm nhìn, lộ trình, backlog, MVP.", "Scrum và Kanban; sprint, ước lượng, Definition of Done.", "Quản lý mã nguồn: nhánh, pull request, review có bot AI.", "Quy trình khi có AI agent trong đội: chia việc, quyền hạn; giữa kỳ.",
          "Ước lượng và lập kế hoạch khi AI làm nhanh phần cài đặt.", "Chỉ số DORA và đo hiệu quả đội.", "Quản lý rủi ro và nợ kỹ thuật, kể cả nợ do mã AI sinh.", "Hồi cứu (retrospective) dựa trên dữ liệu kho mã.", "Bảo vệ quy trình và kết quả của nhóm."],
   assess="ky-nghe", refs="Sommerville, Engineering Software Products (2020); Winters và cộng sự, Software Engineering at Google.", plos=[("PLO8", "R"), ("PLO2", "R"), ("PLO4", "R")], ai="B3"),
 C("SOFT4003", "Kiểm thử và đảm bảo chất lượng phần mềm với AI", "Software Testing and Quality Assurance with AI", 3, 20, 25, 90, 5, "nganh", "giu", old="SOFT4003", prereq="PROG2006",
   desc="Nền tảng ISTQB: nguyên lý, quy trình, kỹ thuật kiểm thử tĩnh và động, hộp đen, hộp trắng, quản lý kiểm thử. Kiểm thử tự động đơn vị, tích hợp, đầu cuối (Playwright); dùng AI sinh ca kiểm thử, dữ liệu thử và kịch bản; kiểm thử đột biến để đo chất lượng bộ kiểm thử; kiểm thử mã do AI sinh.",
   clos=[("CLO1", "Thiết kế ca kiểm thử bằng kỹ thuật hộp đen, hộp trắng."), ("CLO2", "Xây bộ kiểm thử tự động có dùng AI và đo được chất lượng."), ("CLO3", "Lập và quản lý kế hoạch kiểm thử.")],
   weeks=["Tổng quan kiểm thử, nguyên lý ISTQB; vì sao kiểm thử quan trọng hơn khi có AI.", "Quy trình kiểm thử và tài liệu.", "Kiểm thử trong vòng đời phát triển; các mức kiểm thử.", "Kiểm thử tĩnh, review; AI hỗ trợ review.",
          "Kỹ thuật hộp đen: phân hoạch, giá trị biên, bảng quyết định; giữa kỳ.", "Kỹ thuật hộp trắng, độ bao phủ.", "Kiểm thử tự động đơn vị và tích hợp; AI sinh ca kiểm thử.", "Kiểm thử đầu cuối với Playwright; kiểm thử đột biến.",
          "Quản lý kiểm thử, ước lượng, báo cáo; kiểm thử mã do AI sinh.", "Công cụ kiểm thử; bảo vệ bộ kiểm thử."],
   assess="ky-nghe", refs="Graham, van Veenendaal, Black, Foundations of Software Testing ISTQB Certification (2024).", plos=[("PLO5", "M")], ai="B3"),
 C("INFO3008", "DevOps, CI/CD và điện toán đám mây", "DevOps, CI/CD and Cloud Computing", 3, 20, 25, 90, 5, "nganh", "giu", old="INFO3008", prereq="SOFT2003",
   desc="Mô hình dịch vụ đám mây, ảo hóa, container, điều phối; hạ tầng như mã; CI/CD; giám sát và nhật ký; bảo mật đám mây; tối ưu chi phí. Cập nhật từ học phần Điện toán đám mây: chuyển trọng tâm từ lý thuyết sang thực hành DevOps, dùng AI để viết và rà soát cấu hình.",
   clos=[("CLO1", "Triển khai ứng dụng container lên đám mây với CI/CD."), ("CLO2", "Thiết lập giám sát, cảnh báo và quản lý chi phí.")],
   weeks=["Tổng quan đám mây; mô hình IaaS, PaaS, SaaS.", "Ảo hóa và container.", "Lưu trữ và dữ liệu trên đám mây.", "Kiến trúc đám mây.", "CI: build, kiểm thử tự động; giữa kỳ.",
          "CD: triển khai tự động, môi trường.", "Hạ tầng như mã; AI viết và rà soát cấu hình.", "Giám sát, nhật ký, cảnh báo.", "Bảo mật đám mây, quản lý bí mật.", "Tối ưu chi phí; trình diễn pipeline."],
   assess="ky-nghe", refs="Comer, The Cloud Computing Book (2021); Kim và cộng sự, The DevOps Handbook.", plos=[("PLO6", "M")], ai="B3"),
 C("SOFT2004", "Kỹ nghệ phần mềm với AI agent", "Agentic Software Engineering", 3, 15, 30, 90, 5, "nganh", "moi", prereq="SOFT2001",
   desc="Học phần đặc trưng của chương trình. Cách làm việc với trợ lý lập trình và AI agent trong toàn bộ vòng đời: kỹ thuật ngữ cảnh (context engineering), công cụ và giao thức kết nối (như MCP), quy trình đặc tả → kế hoạch → cài đặt → kiểm thử → review, rào chắn và quyền hạn, đo năng suất và chất lượng, khi nào không nên dùng AI.",
   clos=[("CLO1", "Điều phối AI agent hoàn thành tác vụ nhiều bước theo đặc tả."), ("CLO2", "Thiết lập rào chắn và đo chất lượng đầu ra của AI agent."), ("CLO3", "Đánh giá phê phán năng suất, rủi ro và giới hạn của AI trong phát triển phần mềm.")],
   weeks=["Từ trợ lý đến agent: cách AI agent hoạt động; năng suất và giới hạn (dữ liệu khảo sát, thử nghiệm thực tế).", "Kỹ thuật ngữ cảnh: tệp hướng dẫn dự án, ví dụ, ràng buộc.", "Quy trình đặc tả → kế hoạch → cài đặt → kiểm thử.", "Công cụ và giao thức kết nối (MCP); agent dùng công cụ.",
          "Rào chắn: kiểm thử, review, quyền hạn, sandbox; giữa kỳ.", "Nhiều agent và chia việc; review mã do agent viết.", "Bảo mật khi dùng agent: rò rỉ bí mật, chèn lệnh (prompt injection).", "Đo chất lượng và năng suất; khi nào không nên dùng AI.", "Làm việc với codebase lớn và mã kế thừa.", "Bảo vệ dự án và phản tư."],
   assess="ky-nghe", refs="Tài liệu khóa Stanford CS146S The Modern Software Developer; CMU 15-113 Effective Coding with AI; báo cáo DORA 2025.", plos=[("PLO4", "M"), ("PLO7", "R"), ("PLO10", "R")], ai="B3"),
 C("SOFT1202", "Studio 5: Sản phẩm cho cộng đồng trường", "", 2, 0, 0, 0, 5, "studio", "moi"),

 # ---------------- HỌC KỲ 6 ----------------
 C("SOFT3001", "Học máy ứng dụng cho kỹ sư phần mềm", "Applied Machine Learning for Software Engineers", 3, 20, 25, 90, 6, "nganh", "thay", old="BIGD4001", prereq="MATH2101",
   desc="Học máy từ góc nhìn kỹ sư phần mềm: dữ liệu, mô hình cơ bản, mạng nơ-ron và transformer ở mức ứng dụng, đánh giá mô hình, dùng mô hình có sẵn qua API, triển khai mô hình. Thay học phần Học sâu và ứng dụng trong khối bắt buộc (học phần đó chuyển sang tự chọn).",
   clos=[("CLO1", "Xây và đánh giá mô hình học máy cho bài toán sản phẩm."), ("CLO2", "Chọn giữa tự huấn luyện và dùng mô hình có sẵn, có lập luận về chi phí và chất lượng.")],
   weeks=["Học máy trong sản phẩm phần mềm.", "Dữ liệu: thu thập, làm sạch, gán nhãn.", "Hồi quy và phân loại.", "Đánh giá mô hình, quá khớp.", "Mạng nơ-ron cơ bản; giữa kỳ.",
          "Transformer và mô hình ngôn ngữ ở mức ứng dụng.", "Dùng mô hình có sẵn qua API; nhúng và tìm kiếm.", "Triển khai mô hình, phục vụ dự đoán.", "Thiên lệch, công bằng, giải thích được.", "Trình diễn dự án."],
   assess="ai", refs="Chollet, Deep Learning with Python; Huyen, Designing Machine Learning Systems.", plos=[("PLO7", "R"), ("PLO1", "R")], ai="B4"),
 C("SOFT3002", "Bảo mật ứng dụng và an toàn mã do AI sinh", "Application Security and AI-generated Code Safety", 3, 20, 25, 90, 6, "nganh", "moi", prereq="PROG2101",
   desc="Mô hình hóa mối đe dọa, OWASP Top 10, xác thực và phân quyền, bảo mật API, chuỗi cung ứng phần mềm, phân tích tĩnh và động. Trọng tâm mới: lỗ hổng thường gặp trong mã do AI sinh, gói phụ thuộc giả mạo, chèn lệnh vào ứng dụng có AI, bảo mật khi dùng AI agent.",
   clos=[("CLO1", "Phát hiện và khắc phục lỗ hổng phổ biến trong ứng dụng web và API."), ("CLO2", "Đánh giá rủi ro bảo mật của mã do AI sinh và của ứng dụng có thành phần AI.")],
   weeks=["Tư duy bảo mật, mô hình hóa mối đe dọa.", "OWASP Top 10: chèn mã, XSS.", "Xác thực, phiên, phân quyền.", "Bảo mật API.", "Phân tích tĩnh, động; giữa kỳ.",
          "Chuỗi cung ứng phần mềm, phụ thuộc, gói giả mạo.", "Lỗ hổng điển hình trong mã do AI sinh.", "Bảo mật ứng dụng có LLM: chèn lệnh, rò rỉ dữ liệu.", "Ứng phó sự cố, công bố lỗ hổng có trách nhiệm.", "Bảo vệ báo cáo đánh giá bảo mật."],
   assess="ky-nghe", refs="OWASP Top 10 và OWASP Top 10 for LLM Applications; Hoffman, Web Application Security.", plos=[("PLO5", "M"), ("PLO7", "R")], ai="B3–B5"),
 C("SOFT3007", "Chủ đề hiện đại trong Kỹ thuật phần mềm", "Special Topics in Software Engineering", 3, 15, 30, 90, 6, "nganh", "moi", prereq="SOFT2004",
   desc="Học phần mở: chuẩn đầu ra, cách đánh giá và số tín chỉ cố định, còn nội dung là 1–2 chủ đề công nghệ hoặc kỹ thuật mới do Khoa công bố hằng năm, chưa kịp đưa vào học phần chính quy (ví dụ năm 2027: phát triển nhiều agent theo đặc tả, MCP và hệ sinh thái công cụ cho agent, đánh giá và quan sát hệ thống AI, mô hình nhỏ chạy trên thiết bị, hiện đại hóa hệ thống cũ bằng AI). Giảng viên dạy cùng chuyên gia doanh nghiệp. Sinh viên học nhanh từ tài liệu gốc, làm nguyên mẫu, đo đạc và viết khuyến nghị áp dụng theo thang Adopt / Trial / Assess / Hold; kết quả của lớp cập nhật vào Tech Radar của Khoa.",
   clos=[("CLO1", "Tự học nhanh một công nghệ mới từ tài liệu gốc (tài liệu chính thức, mã nguồn, bài báo), có AI hỗ trợ và kiểm chứng nguồn."), ("CLO2", "Xây nguyên mẫu áp dụng công nghệ mới vào một bài toán phần mềm và đo được kết quả."), ("CLO3", "Đánh giá mức trưởng thành, rủi ro, chi phí và đưa ra khuyến nghị áp dụng có lập luận.")],
   weeks=["Công bố chủ đề của năm; bản đồ công nghệ; vì sao chủ đề này quan trọng.", "Học nhanh từ tài liệu gốc: đọc tài liệu chính thức, mã nguồn mẫu; AI tóm tắt, sinh viên kiểm chứng.", "Seminar chuyên gia doanh nghiệp: chủ đề được dùng thế nào trong sản phẩm thật.", "Tiêu chí đánh giá: chất lượng, chi phí, bảo mật, khả năng bảo trì, rủi ro khóa nhà cung cấp.", "Thử nghiệm 1; giữa kỳ: demo kỹ thuật 5 phút.",
          "Nguyên mẫu: áp dụng vào bài toán của Studio hoặc doanh nghiệp.", "Nguyên mẫu (tiếp); so sánh với giải pháp hiện có.", "Đo đạc, phân tích kết quả, ghi lại giới hạn.", "Viết khuyến nghị Adopt / Trial / Assess / Hold và bài viết kỹ thuật.", "Trình bày; cập nhật Tech Radar của Khoa; vấn đáp."],
   assess="mo", refs="Tài liệu gốc của chủ đề năm học (tài liệu chính thức, mã nguồn, bài báo); Thoughtworks Technology Radar (phương pháp đánh giá công nghệ).", plos=[("PLO10", "R"), ("PLO4", "R"), ("PLO3", "R")], ai="B3–B5"),
 C("SOFT2101", "Studio 6: Dự án doanh nghiệp", "", 3, 0, 0, 0, 6, "studio", "moi"),
 C("POLI1004", "Lịch sử Đảng Cộng sản Việt Nam", "History of the Communist Party of Vietnam", 2, 0, 0, 0, 6, "dc", "chung", assess="chung"),

 # ---------------- HỌC KỲ 7 ----------------
 C("SOFT3004", "Phát triển ứng dụng mô hình ngôn ngữ lớn", "LLM Application Engineering: RAG, Agents and Evaluation", 3, 15, 30, 90, 7, "nganh", "moi", old="BIGD4003 (chương 8)", prereq="SOFT3001, SOFT2004",
   desc="Xây tính năng AI trong sản phẩm: thiết kế prompt và cấu trúc đầu ra, RAG, agent dùng công cụ, bộ nhớ, đánh giá (eval) tự động và có con người, giám sát, tối ưu chi phí và độ trễ, an toàn. Kế thừa chương LLM của học phần Xử lý ngôn ngữ tự nhiên và mở rộng thành học phần riêng.",
   clos=[("CLO1", "Xây tính năng RAG hoặc agent hoạt động trong sản phẩm."), ("CLO2", "Thiết kế bộ đánh giá và dùng nó để cải tiến hệ thống."), ("CLO3", "Phân tích chi phí, độ trễ và rủi ro của tính năng AI.")],
   weeks=["Mô hình ngôn ngữ lớn trong sản phẩm; chọn mô hình.", "Thiết kế prompt, đầu ra có cấu trúc.", "Nhúng, cơ sở dữ liệu vector, RAG.", "Đánh giá RAG; bộ dữ liệu đánh giá.", "Agent dùng công cụ; giữa kỳ: nguyên mẫu.",
          "Bộ nhớ, luồng nhiều bước, phối hợp nhiều agent.", "Eval tự động, AI chấm AI, đánh giá có con người.", "Giám sát, chi phí, độ trễ.", "An toàn: chèn lệnh, rò rỉ, nội dung có hại; tuân thủ Luật Trí tuệ nhân tạo.", "Trình diễn hệ thống và báo cáo đánh giá."],
   assess="ai", refs="Huyen, AI Engineering (2025); Lane, Dyshel, Natural Language Processing in Action (2025).", plos=[("PLO7", "M"), ("PLO5", "R")], ai="B4–B5"),
 C("SOFT3005", "Hệ thống phân tán, dữ liệu và vận hành", "Distributed Systems, Data and Reliability Engineering", 3, 15, 30, 90, 7, "nganh", "moi", prereq="INFO3008",
   desc="Nhất quán, sao chép, phân vùng, hàng đợi thông điệp, luồng dữ liệu; thiết kế cho quy mô lớn; vận hành tin cậy (SRE): chỉ số SLO, cảnh báo, xử lý sự cố, hậu kiểm không đổ lỗi.",
   clos=[("CLO1", "Thiết kế hệ thống chịu tải và chịu lỗi."), ("CLO2", "Vận hành hệ thống theo chỉ số, xử lý sự cố có quy trình.")],
   weeks=["Hệ phân tán: thách thức.", "Sao chép, nhất quán.", "Phân vùng dữ liệu.", "Hàng đợi, luồng sự kiện.", "Bộ đệm, CDN; giữa kỳ.",
          "Thiết kế hệ thống quy mô lớn.", "SLO, chỉ số, cảnh báo.", "Xử lý sự cố, hậu kiểm.", "Kiểm thử chịu lỗi, chaos.", "Bảo vệ thiết kế hệ thống."],
   assess="ky-nghe", refs="Kleppmann, Designing Data-Intensive Applications; Google, Site Reliability Engineering.", plos=[("PLO6", "M"), ("PLO3", "M")], ai="B3"),
 C("INFO3001", "Pháp lý, đạo đức nghề nghiệp và AI có trách nhiệm", "Law, Professional Ethics and Responsible AI", 2, 15, 15, 60, 7, "nganh", "giu", old="INFO3001",
   desc="Luật sở hữu trí tuệ, an toàn thông tin mạng, giao dịch điện tử, bảo vệ dữ liệu cá nhân, Luật Trí tuệ nhân tạo; đạo đức nghề nghiệp; quy định về dùng AI trong học tập và làm việc; giấy phép mã nguồn mở và bản quyền với mã do AI sinh.",
   clos=[("CLO1", "Phân tích vấn đề pháp lý, đạo đức của một sản phẩm phần mềm có AI."), ("CLO2", "Đề xuất biện pháp tuân thủ cho sản phẩm.")],
   weeks=["Khái niệm cơ bản; pháp lý trong doanh nghiệp CNTT.", "Đạo đức nghề nghiệp.", "Đạo đức AI và trách nhiệm xã hội.", "Luật Trí tuệ nhân tạo; phân loại rủi ro hệ thống AI.", "Luật an toàn thông tin mạng; giữa kỳ.",
          "Tội phạm tin học.", "Sở hữu trí tuệ, giấy phép mã nguồn mở, mã do AI sinh.", "Bảo vệ dữ liệu cá nhân.", "Quyền riêng tư và quyền tiếp cận thông tin.", "Phân tích tình huống sản phẩm thật."],
   assess="ky-nghe", refs="Quinn, Ethics for the Information Age (2020); Baase, A Gift of Fire.", plos=[("PLO9", "M"), ("PLO7", "R")], ai="B5"),
 C("SOFT3008", "Nghiên cứu và đổi mới trong Kỹ thuật phần mềm", "Software Engineering Research and Innovation Project", 3, 10, 35, 90, 7, "nganh", "moi", prereq="SOFT3007",
   desc="Học phần mở dạng dự án nghiên cứu: nhóm 2–3 sinh viên tham gia đề tài của giảng viên, phòng thí nghiệm hoặc doanh nghiệp. Đề tài thay đổi mỗi năm theo hướng nghiên cứu của Khoa, ví dụ: tái lập kết quả một bài báo mới (ICSE, FSE, ASE, arXiv), thực nghiệm so sánh công cụ AI trong phát triển phần mềm, xây bộ đánh giá (benchmark) cho bài toán tiếng Việt. Sản phẩm là mã và dữ liệu tái lập được cùng một bài báo ngắn hoặc poster, có thể gửi Hội nghị sinh viên nghiên cứu khoa học hoặc cuộc thi ACM Student Research Competition. Là cầu nối sang đồ án tốt nghiệp hướng nghiên cứu.",
   clos=[("CLO1", "Xây dựng câu hỏi nghiên cứu và tổng quan tài liệu, dùng AI tìm và tóm tắt nhưng kiểm chứng từng nguồn."), ("CLO2", "Thiết kế và thực hiện thực nghiệm có đo lường, tái lập được."), ("CLO3", "Viết và trình bày kết quả theo chuẩn học thuật, khai báo trung thực việc dùng AI.")],
   weeks=["Nghiên cứu trong kỹ thuật phần mềm là gì; giới thiệu đề tài của năm; lập nhóm.", "Đọc bài báo hiệu quả; tìm tài liệu với AI và kiểm chứng trích dẫn.", "Câu hỏi nghiên cứu, giả thuyết, đóng góp dự kiến.", "Thiết kế thực nghiệm: biến, chỉ số, mối đe dọa đến tính hợp lệ.", "Bảo vệ đề cương nghiên cứu; giữa kỳ.",
          "Thực nghiệm vòng 1; nhật ký thực nghiệm.", "Thực nghiệm vòng 2; đóng gói mã và dữ liệu để tái lập.", "Phân tích kết quả, thống kê, biểu đồ.", "Viết bài báo ngắn hoặc poster; liêm chính học thuật và khai báo AI.", "Bảo vệ; chọn kết quả gửi hội nghị sinh viên."],
   assess="nghien-cuu", refs="Wohlin và cộng sự, Experimentation in Software Engineering, 2nd ed., Springer (2024); ACM SIGSOFT Empirical Standards.", plos=[("PLO10", "R"), ("PLO5", "R"), ("PLO9", "R")], ai="B3–B5"),
 C("SOFT2102", "Studio 7: Tính năng AI có đánh giá", "", 2, 0, 0, 0, 7, "studio", "moi"),

 # ---------------- HỌC KỲ 8 ----------------
 C("SOFT3901", "Thực tập OJT tại doanh nghiệp", "On-the-job Training", 6, 0, 0, 0, 8, "tn", "giu",
   desc="Sinh viên làm việc 10 tuần tại công ty thành viên Tập đoàn Công nghệ CMC hoặc đối tác, tham gia đội phát triển thật, có người hướng dẫn doanh nghiệp và giảng viên. Điều kiện: đạt Cổng năng lực 2.",
   clos=[("CLO1", "Đóng góp vào hệ thống phần mềm đang vận hành trong doanh nghiệp."), ("CLO2", "Tuân thủ quy trình, bảo mật và chính sách dùng AI của doanh nghiệp.")],
   weeks=["Tiếp nhận, tìm hiểu doanh nghiệp, quy trình, chính sách dùng AI.", "Làm quen codebase và công cụ.", "Nhận nhiệm vụ đầu tiên.", "Làm việc theo sprint của đội.", "Báo cáo giữa kỳ với giảng viên.",
          "Đảm nhận tính năng hoặc cải tiến.", "Review, kiểm thử, triển khai theo quy trình doanh nghiệp.", "Hoàn thiện đóng góp.", "Viết báo cáo thực tập.", "Đánh giá của doanh nghiệp; bảo vệ trước giảng viên."],
   assess="thuc-tap", plos=[("PLO8", "M"), ("PLO6", "R"), ("PLO9", "R")], ai="B3–B5"),
 C("TRACK-1", "Học phần chuyên sâu 1", "Specialization course 1", 3, 0, 0, 0, 8, "cs", "moi", kind="TC", assess="ky-nghe"),
 C("SOFT3006", "Đổi mới sáng tạo và khởi nghiệp sản phẩm số", "Digital Product Innovation and Entrepreneurship", 2, 15, 15, 60, 8, "nganh", "moi",
   desc="Tìm vấn đề đáng giải quyết, kiểm chứng ý tưởng, mô hình kinh doanh, đo lường sản phẩm, gọi vốn; khởi nghiệp với đội nhỏ có AI.",
   clos=[("CLO1", "Kiểm chứng một ý tưởng sản phẩm bằng dữ liệu người dùng."), ("CLO2", "Trình bày mô hình kinh doanh của sản phẩm.")],
   weeks=["Tư duy khởi nghiệp.", "Tìm và kiểm chứng vấn đề.", "Phỏng vấn khách hàng.", "Sản phẩm khả dụng tối thiểu.", "Đo lường; giữa kỳ.", "Mô hình kinh doanh.", "Định giá, kênh.", "Pháp lý khởi nghiệp.", "Trình bày gọi vốn.", "Ngày trình bày ý tưởng."],
   assess="ky-nghe", plos=[("PLO10", "M")], ai="B2–B3"),
 C("POLI1005", "Tư tưởng Hồ Chí Minh", "Ho Chi Minh Ideology", 2, 0, 0, 0, 8, "dc", "chung", assess="chung"),

 # ---------------- HỌC KỲ 9 ----------------
 C("TRACK-2", "Học phần chuyên sâu 2", "Specialization course 2", 3, 0, 0, 0, 9, "cs", "moi", kind="TC", assess="ky-nghe"),
 C("ELEC-1", "Học phần tự chọn liên ngành", "Interdisciplinary elective", 3, 0, 0, 0, 9, "cs", "moi", kind="TC", assess="ky-nghe"),
 C("SOFT3902", "Đồ án tốt nghiệp", "Capstone Project", 8, 0, 0, 0, 9, "tn", "giu",
   desc="Sản phẩm có người dùng hoặc khách hàng thật: hệ thống cho doanh nghiệp, sản phẩm khởi nghiệp hoặc đề tài nghiên cứu ứng dụng. Có hồ sơ đặc tả, thiết kế, kiểm thử, đánh giá AI (nếu có), nhật ký AI và minh chứng người dùng. Bảo vệ trước hội đồng có đại diện doanh nghiệp.",
   clos=[("CLO1", "Dẫn dắt toàn bộ vòng đời một sản phẩm từ yêu cầu đến vận hành."), ("CLO2", "Chứng minh giá trị sản phẩm bằng dữ liệu người dùng."), ("CLO3", "Bảo vệ mọi quyết định kỹ thuật khi không có AI.")],
   weeks=["Chốt đề tài, khách hàng, đặc tả.", "Thiết kế và kế hoạch.", "Phát triển vòng 1.", "Mốc 1: trình diễn và góp ý.", "Phát triển vòng 2.", "Mốc 2: thử nghiệm người dùng.", "Phát triển vòng 3, làm cứng.", "Mốc 3: hồ sơ hoàn chỉnh.", "Chuẩn bị bảo vệ.", "Bảo vệ trước hội đồng."],
   assess="do-an", plos=[("PLO2", "M"), ("PLO3", "M"), ("PLO4", "M"), ("PLO5", "M"), ("PLO7", "M"), ("PLO8", "M"), ("PLO10", "M")], ai="B3–B5"),
]

STUDIO_SPECS = {
 "SOFT1101": (1101, 1, 2, "Sản phẩm số đầu tiên", "Trang portfolio cá nhân và một ứng dụng web nhỏ chạy trên Internet",
              ("trang portfolio đưa lên mạng ngay tuần 3", "thêm một ứng dụng nhỏ như sổ tay học tập hoặc trò chơi đố vui", "hoàn thiện giao diện và nội dung"),
              "làm cá nhân, tập quy trình làm ra một sản phẩm nhỏ hoàn chỉnh và tập dùng AI như gia sư.", "", [("PLO4", "I"), ("PLO10", "I")], "B1"),
 "SOFT1102": (1102, 2, 2, "Ứng dụng dữ liệu", "Ứng dụng quản lý dữ liệu nhỏ, ví dụ sổ điểm cá nhân hoặc thư viện sách của câu lạc bộ",
              ("thiết kế cơ sở dữ liệu và các thao tác cơ bản", "tìm kiếm, thống kê, xuất dữ liệu", "kiểm thử và xử lý dữ liệu lỗi"),
              "làm theo cặp, kết hợp kiến thức cơ sở dữ liệu và lập trình, dùng AI sinh dữ liệu thử.", "SOFT1101", [("PLO3", "I"), ("PLO4", "I")], "B2"),
 "SOFT1103": (1103, 3, 2, "Sản phẩm có người dùng", "Ứng dụng web có đăng nhập và cơ sở dữ liệu, có bạn bè trong lớp dùng thật",
              ("đăng nhập và dữ liệu người dùng", "tính năng chính theo phản hồi người dùng", "đo số người dùng và sửa lỗi họ báo"),
              "làm nhóm 2–3 người, đưa sản phẩm đến tay người dùng thật đầu tiên. Kết thúc học kỳ là Cổng năng lực 1.", "SOFT1102, PROG2101", [("PLO4", "R"), ("PLO8", "I"), ("PLO2", "I")], "B2"),
 "SOFT1201": (1201, 4, 2, "Ứng dụng di động nhóm", "Bản đầu tiên của ứng dụng di động làm theo nhóm, viết từ đặc tả",
              ("AI agent cài đặt tính năng đầu tiên từ đặc tả", "kiểm thử giao diện tự động", "phát hành bản thử nghiệm"),
              "làm nhóm 4–5 người, áp dụng đặc tả và kiến trúc vào sản phẩm di động, bắt đầu điều phối AI agent.", "SOFT1103", [("PLO2", "R"), ("PLO3", "R"), ("PLO4", "R")], "B3"),
 "SOFT1202": (1202, 5, 2, "Sản phẩm cho cộng đồng trường", "Sản phẩm nhóm cho người dùng trong trường, có kiểm thử tự động và triển khai tự động lên cloud",
              ("CI/CD và bộ kiểm thử tự động", "đo chất lượng mã do AI agent viết", "giám sát sản phẩm đang chạy"),
              "làm nhóm theo Scrum, phục vụ người dùng thật trong trường, kết hợp kiểm thử, DevOps và AI agent.", "SOFT1201", [("PLO5", "R"), ("PLO6", "R"), ("PLO8", "R")], "B3"),
 "SOFT2101": (2101, 6, 3, "Dự án doanh nghiệp", "Sản phẩm giải bài toán thật của một công ty thuộc Tập đoàn Công nghệ CMC, kèm báo cáo bảo mật",
              ("làm rõ yêu cầu với khách hàng doanh nghiệp", "rà soát bảo mật và hiệu năng", "bàn giao theo tiêu chuẩn doanh nghiệp"),
              "làm việc với khách hàng doanh nghiệp thật, có chuyên gia doanh nghiệp cùng hướng dẫn và chấm. Kết thúc học kỳ là Cổng năng lực 2.", "SOFT1202", [("PLO2", "M"), ("PLO5", "R"), ("PLO8", "R"), ("PLO9", "R")], "B3"),
 "SOFT2102": (2102, 7, 2, "Tính năng AI có đánh giá", "Một tính năng AI (trợ lý, tìm kiếm thông minh hoặc agent) tích hợp vào sản phẩm, kèm báo cáo đánh giá độ tin cậy",
              ("tích hợp RAG hoặc agent vào sản phẩm", "xây bộ đánh giá và cải tiến theo chỉ số", "giám sát chi phí, độ trễ, an toàn"),
              "xây tính năng AI cho sản phẩm có sẵn và chứng minh bằng số liệu rằng tính năng đó đáng tin.", "SOFT2101, SOFT3001", [("PLO7", "M"), ("PLO5", "R")], "B4–B5"),
}
_st = {}
for code, (n, sem, tc, theme, product, focus, extra, prereq, plos, ai) in STUDIO_SPECS.items():
    s = studio(n, sem, tc, theme, product, focus, extra, prereq, plos, ai)
    s["code"] = code
    s["name"] = f"Studio {list(STUDIO_SPECS).index(code) + 1}: {theme}"
    _st[code] = s
COURSES = [_st.get(c["code"], c) for c in COURSES]

TRACKS = [
    ("AI Engineering", "Kỹ sư ứng dụng AI, kỹ sư AI agent", [
        ("SOFT4101", "Kỹ thuật xây dựng AI agent", "Kiến trúc agent, công cụ, lập kế hoạch, bộ nhớ, đánh giá và an toàn; dựa trên khung khóa Stanford CS329Z, 10 tuần thực hành."),
        ("SOFT4102", "MLOps và LLMOps", "Triển khai, giám sát, đánh giá liên tục, tối ưu chi phí và độ trễ cho hệ thống học máy và mô hình ngôn ngữ.")]),
    ("Product Engineering", "Kỹ sư sản phẩm, web/mobile, full-stack", [
        ("SOFT4201", "Phát triển sản phẩm đa nền tảng nâng cao", "Web và mobile hiệu năng cao, ngoại tuyến, đồng bộ, khả năng tiếp cận, tính năng AI trên thiết bị."),
        ("SOFT4202", "Phân tích và tăng trưởng sản phẩm", "Đo lường hành vi người dùng, thử nghiệm A/B, phễu chuyển đổi, ra quyết định sản phẩm bằng dữ liệu.")]),
    ("Quality & Security", "Kỹ sư kiểm thử tự động, đánh giá AI, bảo mật ứng dụng", [
        ("SOFT4301", "Kiểm thử nâng cao và đánh giá hệ thống AI", "Kiểm thử theo thuộc tính, hiệu năng, hợp đồng; đánh giá và tấn công thử (red-teaming) hệ thống AI."),
        ("SOFT4302", "DevSecOps và an ninh chuỗi cung ứng phần mềm", "Bảo mật tự động trong CI/CD, SBOM, ký và xác thực bản phát hành, quản lý lỗ hổng.")]),
    ("Cloud & Platform", "Kỹ sư DevOps, cloud, platform, SRE", [
        ("SOFT4401", "Kỹ thuật nền tảng", "Hạ tầng như mã, Kubernetes, nền tảng tự phục vụ cho đội kỹ sư và AI agent."),
        ("SOFT4402", "Hệ thống quy mô lớn và SRE nâng cao", "Thiết kế cho hàng triệu người dùng, ngân sách lỗi, quản lý sự cố, tối ưu chi phí đám mây.")]),
]
ELECTIVES = [
    ("BIGD4001", "Học sâu và ứng dụng", "Chuyển từ khối bắt buộc sang tự chọn, giữ nội dung mạng hồi quy, mô hình sinh, transformer."),
    ("BIGD4003", "Xử lý ngôn ngữ tự nhiên", "Chuyển sang tự chọn; phần mô hình ngôn ngữ lớn đã tách thành học phần SOFT3004."),
    ("SOFT4501", "Phát triển trò chơi", "Thiết kế và lập trình trò chơi, dùng AI tạo nội dung có kiểm soát."),
    ("SOFT4502", "Phần mềm cho y tế và giáo dục số", "Bài toán phần mềm trong y tế và giáo dục: dữ liệu nhạy cảm, tiêu chuẩn liên thông, an toàn người dùng."),
    ("SOFT4503", "Fintech và hệ thống giao dịch", "Thanh toán, đối soát, an toàn giao dịch, tuân thủ."),
    ("SOFT4504", "IoT và hệ thống nhúng ứng dụng", "Thiết bị, cảm biến, nền tảng IoT, xử lý dữ liệu biên."),
]

GATES = [
    ("Cổng năng lực 1", "Cuối học kỳ 3 (năm 1)", "Bài thi lập trình và cấu trúc dữ liệu trên máy có kiểm soát, không AI; hồ sơ 3 sản phẩm; vấn đáp giải thích code.", "Điều kiện đăng ký Studio 4. Chưa đạt: học phụ đạo trong học kỳ 4 và thi lại."),
    ("Cổng năng lực 2", "Cuối học kỳ 6 (năm 2)", "Thiết kế hệ thống trên bảng, review code trực tiếp, bài thi kiểm thử và bảo mật không AI; hồ sơ 6 sản phẩm.", "Điều kiện đăng ký Thực tập OJT. Chưa đạt: hoãn thực tập một học kỳ, có kế hoạch bổ trợ."),
    ("Cổng tốt nghiệp", "Học kỳ 9 (năm 3)", "Bảo vệ đồ án tốt nghiệp trước hội đồng có doanh nghiệp; hồ sơ 9 sản phẩm; chuẩn đầu ra ngoại ngữ và năng lực số.", "Điều kiện xét tốt nghiệp."),
]

YEARS = [
    (1, "Build", "Học kỳ 1–3", "Lập trình được và có sản phẩm đầu tiên", "AI là gia sư, rồi trợ lý (bậc B1–B2)"),
    (2, "Team", "Học kỳ 4–6", "Làm nhóm, làm cho người dùng thật và cho doanh nghiệp", "AI là cộng sự, rồi một đội agent cần điều phối (B2–B3)"),
    (3, "Launch", "Học kỳ 7–9", "Xây tính năng AI, thực tập, tốt nghiệp", "AI là thành phần của sản phẩm và quy trình doanh nghiệp (B4–B5)"),
]

OLD_NEW = [
    ("INFO2013", "Nhập môn công nghệ thông tin", 3, "SOFT1001", "Nhập môn Kỹ thuật phần mềm AI-native", "Thay thế", "Chuyển từ giới thiệu kiến thức chung sang làm sản phẩm ngay; giữ chương AI có trách nhiệm và mở rộng."),
    ("PROG2005", "Cơ sở lập trình", 4, "PROG2005", "Cơ sở lập trình (Python, có trợ lý AI)", "Giữ, cập nhật", "Thêm kiểm thử đơn vị, đọc mã AI sinh; giữ thi không AI."),
    ("MATH2005", "Toán rời rạc", 3, "MATH2005", "Toán rời rạc và logic cho lập trình", "Giữ, giảm 1 TC", "Giữ logic, đếm, đồ thị qua bài cài đặt Python; chứng minh hình thức, hệ đếm, đại số Bool chuyển sang tự học."),
    ("INFO2002", "Cấu trúc dữ liệu và giải thuật", 3, "INFO2002", "Cấu trúc dữ liệu và giải thuật", "Giữ, cập nhật", "Thi không AI; AI dùng để luyện và so sánh lời giải."),
    ("INFO2007", "Cơ sở dữ liệu", 4, "INFO2007", "Cơ sở dữ liệu", "Giữ, giảm 1 TC", "Chuyển SQL Server sang PostgreSQL; rà soát SQL do AI sinh; cơ sở dữ liệu vector."),
    ("PROG2006", "Lập trình hướng đối tượng", 4, "PROG2006", "Lập trình hướng đối tượng và mã sạch", "Giữ, giảm 1 TC", "Bỏ phần giao diện đồ họa; thêm tái cấu trúc mã AI sinh, kiểm thử."),
    ("INFO2011", "Công nghệ phần mềm", 4, "INFO2011", "Công nghệ phần mềm: sản phẩm và Agile", "Giữ, giảm 2 TC", "Chỉ giữ quy trình và quản lý sản phẩm Agile trong đội có AI agent; yêu cầu, kiến trúc, kiểm thử, DevOps đã có học phần riêng."),
    ("SOFT4003", "Kiểm thử phần mềm", 3, "SOFT4003", "Kiểm thử và đảm bảo chất lượng phần mềm với AI", "Giữ, cập nhật lớn", "Giữ nền tảng ISTQB; thêm Playwright, AI sinh ca kiểm thử, kiểm thử đột biến; chuyển từ 45 tiết lý thuyết sang thực hành."),
    ("INFO3007", "Mạng máy tính và truyền thông", 3, "SOFT2003", "Hệ thống máy tính và mạng cho kỹ sư phần mềm", "Thay thế, giảm 1 TC", "Gộp hệ điều hành và mạng ở góc nhìn kỹ sư phần mềm, học qua chẩn đoán sự cố; bỏ chi tiết lớp vật lý, định tuyến."),
    ("INFO3008", "Điện toán đám mây", 3, "INFO3008", "DevOps, CI/CD và điện toán đám mây", "Giữ, cập nhật lớn", "Chuyển từ 45 tiết lý thuyết sang thực hành DevOps, hạ tầng như mã, chi phí."),
    ("PROG3002", "Phát triển ứng dụng di động", 3, "PROG3002", "Phát triển ứng dụng di động", "Giữ, cập nhật", "Thêm AI agent theo đặc tả, kiểm thử giao diện tự động."),
    ("INFO3001", "Pháp lý và đạo đức nghề nghiệp", 2, "INFO3001", "Pháp lý, đạo đức nghề nghiệp và AI có trách nhiệm", "Giữ, cập nhật", "Thêm Luật Trí tuệ nhân tạo, Thông tư 49/2026, bản quyền mã AI sinh."),
    ("BIGD4001", "Học sâu và ứng dụng", 3, "SOFT3001", "Học máy ứng dụng cho kỹ sư phần mềm", "Thay thế (cũ chuyển tự chọn)", "Kỹ sư phần mềm cần dùng và triển khai mô hình hơn là nghiên cứu kiến trúc mạng."),
    ("BIGD4003", "Xử lý ngôn ngữ tự nhiên", 3, "SOFT3004", "Phát triển ứng dụng mô hình ngôn ngữ lớn", "Tách và mở rộng (cũ chuyển tự chọn)", "Chương 8 (LLM, RAG, agent) thành học phần riêng 10 tuần."),
]

LEGAL = [
    ("Thông tư 54/2026/TT-BGDĐT", "Quy định chương trình đào tạo các trình độ của giáo dục đại học (30/6/2026)", "Chuẩn đầu ra đại học phải có năng lực số, trí tuệ nhân tạo, ngoại ngữ, khả năng thích ứng và học tập suốt đời; đo lường được; tối thiểu 120 tín chỉ. Chương trình đang thực hiện phải rà soát, hoàn thiện trong 36 tháng."),
    ("Thông tư 49/2026/TT-BGDĐT", "Ứng dụng công nghệ trong giáo dục đại học, giáo dục nghề nghiệp (hiệu lực 15/8/2026)", "Cơ sở đào tạo ban hành quy tắc ứng xử về sử dụng AI và quy định liêm chính học thuật; AI là công cụ hỗ trợ, không thay thế giảng viên; không công bố việc dùng AI khi có yêu cầu là vi phạm."),
    ("Luật Trí tuệ nhân tạo số 134/2025/QH15", "Hiệu lực 01/3/2026", "Căn cứ cho nội dung AI có trách nhiệm, quản trị rủi ro AI trong học phần INFO3001, SOFT3004 và hướng chuyên sâu."),
    ("Quyết định 1528/QĐ-TTg", "Chương trình quốc gia phát triển nhân lực trí tuệ nhân tạo đến 2030, định hướng 2035 (11/8/2026)", "Đến 2030, 100% cơ sở giáo dục đại học triển khai quy định về sử dụng AI trong đào tạo, nghiên cứu, đánh giá; xây dựng Khung năng lực AI quốc gia."),
]

ROADMAP = [
    ("12/2026 – 01/2027", "Lấy ý kiến", "Khoa, giảng viên, doanh nghiệp Tập đoàn CMC, cựu sinh viên góp ý bản đề xuất; đối sánh chương trình trong và ngoài nước."),
    ("02 – 03/2027", "Hoàn thiện và thẩm định", "Viết đề cương chi tiết các học phần mới theo mẫu của Trường; thẩm định chương trình; ban hành quy tắc ứng xử về AI của Khoa."),
    ("03 – 08/2027", "Chuẩn bị triển khai", "Bồi dưỡng giảng viên về dạy học với AI; chuẩn bị Trợ giảng AI theo học phần, lớp học trên GitHub, phòng thi không AI, gói công cụ AI cho sinh viên; ký kết đề bài Studio 6 với doanh nghiệp."),
    ("Khóa 2027", "Áp dụng", "Áp dụng cho khóa tuyển sinh 2027; các khóa đang học chuyển đổi một phần theo bảng tương đương."),
    ("Hằng năm", "Phát hành phiên bản mới", "Rà soát công nghệ và phản hồi doanh nghiệp mỗi năm; cập nhật học phần theo changelog; rà soát toàn diện theo chu kỳ quy định."),
]

RISKS = [
    ("Sinh viên phụ thuộc AI, hổng nền tảng", "Thi nền tảng không AI, hai cổng năng lực, vấn đáp cá nhân giải thích code trong mọi Studio."),
    ("Gian lận và khai báo AI không trung thực", "Nhật ký AI bắt buộc, dữ liệu kho mã, vấn đáp; quy tắc ứng xử theo Thông tư 49/2026."),
    ("Giảng viên chưa quen dạy với AI", "Bồi dưỡng trước khi áp dụng, cặp giảng viên – chuyên gia doanh nghiệp cho học phần mới, chia sẻ học liệu chung."),
    ("Chi phí công cụ AI và hạ tầng", "Ưu tiên gói dành cho giáo dục, mô hình mã nguồn mở chạy nội bộ cho học phần nhạy cảm dữ liệu, hạn mức theo học phần."),
    ("Công nghệ thay đổi nhanh hơn chu kỳ cập nhật", "Changelog hằng năm; hai học phần mở SOFT3007, SOFT3008 đổi chủ đề mỗi năm không cần sửa chương trình; nội dung công cụ nằm trong Studio và hướng chuyên sâu; phần nền tảng tinh gọn và ổn định."),
    ("Giảm tiếng Anh làm yếu năng lực ngoại ngữ", "Giữ chuẩn đầu ra ngoại ngữ của Trường (ngoài tín chỉ); tài liệu tiếng Anh dùng trong mọi học phần chuyên môn; README, mô tả pull request của Studio từ năm 2 viết bằng tiếng Anh."),
    ("Học phần mở bị dạy tùy hứng, chất lượng không đều", "Đề cương khung cố định CLO và đánh giá; chủ đề được Hội đồng Khoa duyệt trước học kỳ; tiêu chí chọn chủ đề công khai; đánh giá lại chủ đề sau mỗi năm."),
    ("Tải học tập cao do 3 học kỳ mỗi năm", "Mỗi học kỳ 13–15 tín chỉ, Studio tích hợp kiến thức của các học phần cùng kỳ thay vì cộng thêm bài tập riêng."),
]

SYSTEMS = [
    ("Trợ giảng AI theo học phần", "Đã dùng trong các đề cương hiện hành của Khoa; mở rộng cho mọi học phần, chỉ dùng học liệu của học phần, hỏi gợi mở thay vì đưa đáp án; điểm tự học 5–10%."),
    ("Nền tảng edux.cmcu.edu.vn", "Học liệu tương tác theo chương, ngân hàng câu hỏi và sinh đề thi, quản lý đồ án tốt nghiệp."),
    ("Lớp học trên GitHub và chấm tự động", "Mỗi bài là một kho mã; mỗi lần nộp tự chạy kiểm thử như quy trình CI ở doanh nghiệp."),
    ("Review code có AI hỗ trợ", "Bot nhận xét pull request về lỗi, bảo mật, cách viết; giảng viên và trợ giảng duyệt."),
    ("Môi trường lập trình trên cloud", "Môi trường chuẩn hóa chạy trên trình duyệt, không cần máy cấu hình mạnh."),
    ("Nhật ký sử dụng AI", "Mẫu nhật ký thống nhất cho mọi bài M3–M4: câu lệnh, phần AI làm, cách kiểm chứng; căn cứ chấm điểm và liêm chính học thuật."),
    ("Phòng thi không AI", "Máy cấu hình khóa, chỉ mở trình soạn thảo và tài liệu cho phép, dùng cho thi nền tảng và cổng năng lực."),
    ("Cố vấn học tập và cảnh báo sớm", "Dữ liệu học tập giúp phát hiện sớm sinh viên gặp khó, gợi ý phụ đạo trước cổng năng lực."),
    ("Hồ sơ 9 sản phẩm", "Trang hồ sơ năng lực của mỗi sinh viên, cập nhật sau mỗi Demo Day, liên kết mã nguồn và bản chạy thử."),
]

SOURCES = [
    ("Thông tư 54/2026/TT-BGDĐT: chuẩn đầu ra phải có năng lực số và AI (Giáo dục Việt Nam)", "https://giaoduc.net.vn/bo-gddt-yeu-cau-chuong-trinh-dao-tao-dai-hoc-phai-tich-hop-nang-luc-so-va-tri-tue-nhan-tao-post261430.gd"),
    ("Thông tư 54/2026: điều khoản chuyển tiếp 36 tháng (Luật sư Việt Nam)", "https://lsvn.vn/chuan-dau-ra-dai-hoc-phai-co-yeu-cau-ve-nang-luc-so-tri-tue-nhan-tao-a176035.html"),
    ("Thông tư 49/2026/TT-BGDĐT: hành vi vi phạm khi dùng AI (Đại biểu Nhân dân)", "https://daibieunhandan.vn/6-hanh-vi-vi-pham-khi-dung-ai-trong-hoc-tap-nghien-cuu-khoa-hoc-10422783.html"),
    ("Quyết định 1528/QĐ-TTg về nhân lực trí tuệ nhân tạo (Bộ Xây dựng)", "https://moc.gov.vn/vn/tin-tuc/1305/96246/phat-trien-nhan-luc-tri-tue-nhan-tao-dap-ung-cac-nganh-cong-nghe-chien-luoc.aspx"),
    ("Stack Overflow Developer Survey 2025 – AI", "https://survey.stackoverflow.co/2025/ai"),
    ("DORA 2025 State of AI-assisted Software Development", "https://dora.dev/dora-report-2025/"),
    ("Stanford Digital Economy Lab – Canaries in the Coal Mine?", "https://digitaleconomy.stanford.edu/publication/canaries-in-the-coal-mine/"),
    ("CMU 15-113 Effective Coding with AI", "https://www.cs.cmu.edu/~113/bestPractices.html"),
    ("Chương trình đào tạo Kỹ thuật phần mềm hiện hành của Khoa (15 đề cương chi tiết học phần, tệp nội bộ)", ""),
]

# ======================================================================
# v2027.2 — đối sánh quốc tế (ctdt_bench.py)
# ======================================================================
import ctdt_bench as _BN
META["version"] = "v2027.3 (đề xuất)"
for _c in COURSES:
    _b = _BN.BENCH.get(_c["code"])
    _c.update(tb=[], refs_list=[], bench=[], changes=[], swebok=[], wk_new=[])
    if _c["clos"] and len(_c["clos"][0]) == 2:
        _c["clos"] = [(k, t, []) for k, t in _c["clos"]]
    if not _b:
        continue
    _c["tb"], _c["refs_list"], _c["bench"], _c["changes"], _c["swebok"] = _b["tb"], _b["refs"], _b["bench"], _b["changes"], _b["swebok"]
    if _b.get("plos"):
        _c["plos"] = list(_b["plos"])
    _c["clos"] = [tuple(x) for x in _b["clos"]]
    for _i, _w in _b.get("weeks", {}).items():
        _c["weeks"][_i] = _w
    _c["wk_new"] = sorted(_b.get("weeks", {}))
TRACK_BENCH = _BN.TRACK_BENCH
CHANGELOG_2 = _BN.CHANGELOG_2
CRITERIA = _BN.CRITERIA
SWEBOK_KA = _BN.SWEBOK_KA
BENCH_SOURCES = _BN.U

def check_consistency():
    """Trả về (danh sách kiểm tra [(tên, đạt?, chi tiết)], bảng chuỗi PLO)."""
    res = []
    prof = [c for c in COURSES if c["status"] != "chung" and not c["code"].startswith(("TRACK", "ELEC"))]
    plo_codes = [p[0] for p in PLOS]
    bad = [f'{c["code"]} {k}' for c in prof for k, t, m in c["clos"] if not m]
    res.append(("Mọi CLO gắn ít nhất một PLO", not bad, ", ".join(bad) or f"{sum(len(c['clos']) for c in prof)} CLO đều đã gắn PLO"))
    bad = [f'{c["code"]} {k}→{p}' for c in prof for k, t, m in c["clos"] for p in m if p not in dict(c["plos"])]
    res.append(("PLO của CLO nằm trong ánh xạ PLO của học phần", not bad, ", ".join(bad) or "Khớp"))
    bad = [f'{c["code"]} {p}' for c in prof for p, _ in c["plos"] if not any(p in m for _, _, m in c["clos"])]
    res.append(("Mỗi PLO của học phần được ít nhất một CLO đảm nhận", not bad, ", ".join(bad) or "Khớp"))
    chain = {}
    for p in plo_codes:
        lv = {"I": [], "R": [], "M": []}
        for c in COURSES:
            for q, l in c["plos"]:
                if q == p: lv[l].append((c["sem"], c["code"]))
        chain[p] = {k: sorted(v) for k, v in lv.items()}
    bad = [p for p in plo_codes if not all(chain[p][k] for k in "IRM")]
    res.append(("Mỗi PLO có đủ chuỗi Giới thiệu – Củng cố – Thành thạo", not bad, ", ".join(bad) or "10/10 PLO"))
    bad = [p for p in plo_codes if chain[p]["I"] and chain[p]["M"] and min(chain[p]["I"])[0] > max(chain[p]["M"])[0]]
    res.append(("Giới thiệu đến trước Thành thạo", not bad, ", ".join(bad) or "Đúng thứ tự cho cả 10 PLO"))
    bad = [c["code"] for c in prof if len(c["weeks"]) != 10]
    res.append(("Mọi học phần có kế hoạch đủ 10 tuần", not bad, ", ".join(bad) or f"{len(prof)} học phần"))
    bad = [c["code"] for c in prof if not c["tb"]]
    res.append(("Mọi học phần có giáo trình chính", not bad, ", ".join(bad) or "Đủ"))
    bad = [c["code"] for c in prof if c["block"] != "dc" and c["code"] not in ("SOFT3901", "SOFT3902") and not c["bench"]]
    res.append(("Học phần chuyên môn có khóa học tham chiếu", not bad, ", ".join(bad) or "Đủ"))
    cov = {k: [c["code"] for c in prof if k in c["swebok"]] for k, _ in SWEBOK_KA}
    bad = [k for k, v in cov.items() if not v]
    res.append(("18 vùng tri thức SWEBOK v4 đều có học phần đảm nhận", not bad, ", ".join(bad) or "18/18"))
    return res, chain, cov


# ======================================================================
# v2027.3 — giảm tiếng Anh, tinh gọn lý thuyết, thêm 2 học phần mở
# ======================================================================
OPEN_POLICY = dict(
    intro="Hai học phần mở có đề cương khung: số tín chỉ, chuẩn đầu ra (CLO), cách đánh giá và mức dùng AI là cố định và được phê duyệt một lần cùng chương trình; còn chủ đề, tài liệu và đề tài được Khoa cập nhật mỗi năm. Nhờ vậy công nghệ mới vào lớp học ngay năm nó xuất hiện, không phải chờ chu kỳ sửa chương trình.",
    rules=[
        ("Ai duyệt chủ đề", "Hội đồng Khoa học và Đào tạo của Khoa duyệt danh mục chủ đề, đề tài trước mỗi năm học ít nhất 1 tháng; công bố trên trang chương trình đào tạo."),
        ("Tiêu chí chọn chủ đề", "Đã có sản phẩm hoặc công cụ dùng thật trong ngành trong khoảng 2 năm gần đây; có tài liệu gốc công khai; có giảng viên hoặc chuyên gia doanh nghiệp dạy được; có hạ tầng thực hành; phục vụ được chuẩn đầu ra cố định."),
        ("Ai dạy", "Giảng viên của Khoa phụ trách, mời chuyên gia doanh nghiệp (Tập đoàn CMC và đối tác) dạy 30–50% thời lượng; có thể dùng một khóa MOOC mới làm học liệu."),
        ("Đánh giá chủ đề", "Cuối năm, Khoa xem kết quả học tập, phản hồi sinh viên và doanh nghiệp để quyết định: giữ chủ đề, thay chủ đề, hoặc chuyển nội dung vào học phần chính quy trong phiên bản chương trình kế tiếp."),
        ("Lối vào chương trình chính quy", "Chủ đề nào đã ổn định qua 2 năm và được doanh nghiệp xác nhận là năng lực bắt buộc sẽ được đưa vào học phần chính quy ở phiên bản sau, như cách SOFT2004 và SOFT3004 đã được hình thành."),
    ],
)

TOPICS_2027 = [
    ("SOFT3007", "Phát triển nhiều agent theo đặc tả", "Spec-driven development với nhiều AI agent chạy song song; kỹ năng agent (agent skills); review mã do agent viết."),
    ("SOFT3007", "MCP và hệ sinh thái công cụ cho agent", "Xây máy chủ MCP cho hệ thống của doanh nghiệp; quyền hạn, bảo mật, đánh giá."),
    ("SOFT3007", "Đánh giá và quan sát hệ thống AI", "Bộ eval, theo dõi, chi phí và chất lượng của ứng dụng LLM trong vận hành."),
    ("SOFT3007", "Mô hình nhỏ chạy trên thiết bị", "SLM trên điện thoại, máy tính cá nhân; quyền riêng tư, độ trễ, chi phí."),
    ("SOFT3007", "Hiện đại hóa hệ thống cũ bằng AI", "Đọc hiểu, viết kiểm thử và chuyển đổi codebase cũ với AI agent; quản lý rủi ro."),
    ("SOFT3008", "Tái lập nghiên cứu về AI trong kỹ thuật phần mềm", "Chọn một bài báo gần đây (ICSE, FSE, ASE, arXiv), tái lập và mở rộng thực nghiệm."),
    ("SOFT3008", "Bộ đánh giá cho bài toán phần mềm tiếng Việt", "Xây benchmark đặc tả, kiểm thử hoặc tài liệu tiếng Việt để đo các mô hình, agent."),
    ("SOFT3008", "Đề tài doanh nghiệp và phòng thí nghiệm", "Đề tài do giảng viên, phòng thí nghiệm của Trường hoặc doanh nghiệp Tập đoàn CMC đặt hàng."),
]

CHANGELOG_3 = [
    ("v2027.3", "Giảm tiếng Anh từ 5 xuống 2 tín chỉ: gộp ENGL2001 (3 TC) và ENGL3001 (2 TC) thành ENGL2002 Tiếng Anh kỹ thuật cho kỹ sư phần mềm (2 TC, học kỳ 3). Chuẩn đầu ra ngoại ngữ theo quy định của Trường; tài liệu tiếng Anh dùng xuyên suốt các học phần chuyên môn."),
    ("v2027.3", "Thêm 2 học phần mở: SOFT3007 Chủ đề hiện đại trong Kỹ thuật phần mềm (3 TC, học kỳ 6) và SOFT3008 Nghiên cứu và đổi mới trong Kỹ thuật phần mềm (3 TC, học kỳ 7); chuẩn đầu ra cố định, chủ đề do Khoa duyệt hằng năm."),
    ("v2027.3", "Tinh gọn lý thuyết nền tảng: MATH2005 (3 → 2 TC), SOFT2003 (3 → 2 TC), INFO2011 (3 → 2 TC); chuyển giờ lý thuyết sang thực hành ở INFO2002, PROG2006, MATH2101, SOFT2002, SOFT3005, INFO3001."),
    ("v2027.3", "SOFT2002 đổi thành Kiến trúc phần mềm: ra quyết định cùng AI. AI sinh phương án, sinh viên đặt thuộc tính chất lượng, đánh giá đánh đổi, kiểm chứng bằng nguyên mẫu và hàm kiểm chứng trong CI."),
    ("v2027.3", "Sắp lại học kỳ: SOFT3003 Thiết kế trải nghiệm lên học kỳ 3 (đi cùng Studio 3); LAW1001 sang học kỳ 4. Tổng giữ 123 tín chỉ; mỗi học kỳ 13–15 tín chỉ."),
    ("v2027.3", "PLO8 và PO4 viết lại: đọc hiểu và viết tài liệu kỹ thuật tiếng Anh thay cho yêu cầu thuyết trình bằng tiếng Anh tại Demo Day."),
]
