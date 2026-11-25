# -*- coding: utf-8 -*-
# Lời dẫn 11 chương. Mỗi câu: hiển thị tiếng Việt, tiếng Anh. Bản đọc tiếng Việt được tạo bằng vi_say().
import re

NARR = [
 ([ "Đừng chỉ học viết code.",
    "Hãy học cách xây những phần mềm mà hàng triệu người dùng mỗi ngày, và có sản phẩm chạy thật ngay từ năm nhất.",
    "Đây là ngành Kỹ thuật phần mềm, Trường Đại học CMC."],
  [ "Don't just learn to write code.",
    "Learn to build software that millions of people use every day, and ship a real product in your very first year.",
    "This is Software Engineering at CMC University."]),
 ([ "Sáng nay bạn đã mở bao nhiêu ứng dụng?",
    "Chuyển khoản, gọi xe, học trực tuyến, đặt lịch khám.",
    "Đằng sau mỗi ứng dụng là một đội kỹ sư phần mềm."],
  [ "How many apps have you opened this morning?",
    "Banking, ride-hailing, online classes, booking a doctor.",
    "Behind every app is a team of software engineers."]),
 ([ "Nghề lập trình đang đổi luật chơi.",
    "Tám mươi tư phần trăm lập trình viên đã hoặc sắp dùng AI, nhưng gần một nửa không tin vào độ chính xác của nó.",
    "Doanh nghiệp cần người làm ra sản phẩm và chịu trách nhiệm về chất lượng, chứ không chỉ người gõ code."],
  [ "The rules of programming are changing.",
    "Eighty-four percent of developers use or plan to use AI, yet nearly half don't trust its accuracy.",
    "Companies need people who ship products and own their quality, not just people who type code."]),
 ([ "Kỹ sư phần mềm thời AI làm việc cùng trợ lý AI ở mọi bước: phân tích yêu cầu, thiết kế, lập trình, kiểm tra chất lượng, triển khai và vận hành.",
    "AI làm nhanh, còn kỹ sư quyết định và chịu trách nhiệm."],
  [ "In the age of AI, software engineers work with AI assistants at every step: requirements, design, coding, testing, deployment and operations.",
    "AI moves fast. Engineers decide, and take responsibility."]),
 ([ "Vì vậy, chương trình Kỹ thuật phần mềm định hướng AI-native cho bạn làm ra sản phẩm thật ngay từ học kỳ một.",
    "Mỗi năm có ba học kỳ, mỗi học kỳ học trong mười tuần, nên chỉ sau ba năm là bạn ra trường.",
    "Năm nhất, ứng dụng của riêng bạn chạy trên Internet.",
    "Năm hai, làm nhóm, làm cho người dùng thật và cho doanh nghiệp.",
    "Năm ba, thực tập, chuyên sâu, và tốt nghiệp với hồ sơ chín sản phẩm."],
  [ "That's why our AI-native Software Engineering program has you shipping real products from your first semester.",
    "With three ten-week semesters a year, you graduate in just three years.",
    "Year one: your own apps, live on the internet.",
    "Year two: team products for real users and for industry.",
    "Year three: an internship, a specialization, and graduation with a portfolio of nine products."]),
 ([ "Bạn học bốn năng lực mà kỹ sư thời AI cần: viết đặc tả rõ ràng, điều phối trợ lý và tác tử AI, kiểm chứng mọi dòng mã, và chịu trách nhiệm về sản phẩm.",
    "Học cùng AI, nhưng vẫn thi cả không AI để chắc nền tảng."],
  [ "You'll build the four skills AI-era engineers need: writing clear specifications, orchestrating AI assistants and agents, verifying every line of code, and owning the product.",
    "Learn with AI, but still pass exams without it, so your foundations are solid."]),
 ([ "Ở CMC, bạn học trong lòng một tập đoàn công nghệ.",
    "Hệ sinh thái Viện, Trường, Doanh nghiệp giúp sinh viên học qua dự án thực tế và thực tập tại các công ty thành viên ngay khi còn đi học."],
  [ "At CMC, you study inside a technology group.",
    "Our ecosystem of research institutes, university and member companies lets you learn through real projects and intern in industry while still in school."]),
 ([ "Lứa tuyển sinh năm 2027 sẽ ra trường khoảng năm 2030.",
    "Những vai trò đang lớn lên gồm kỹ sư phần mềm làm việc cùng AI, kỹ sư ứng dụng AI, kỹ sư đảm bảo chất lượng và đánh giá AI, kỹ sư nền tảng đám mây, và kỹ sư sản phẩm.",
    "Chạm vào từng vai trò để khám phá."],
  [ "The class of 2027 will graduate around 2030.",
    "Growing roles include AI-augmented software engineers, applied AI engineers, AI testing and evaluation engineers, cloud platform engineers, and product engineers.",
    "Tap any role to explore."]),
 ([ "Quỹ học bổng CMC, Vì bạn xứng đáng, trị giá chín mươi sáu tỷ đồng.",
    "Các mức ba mươi, năm mươi, bảy mươi và một trăm phần trăm học phí toàn khóa.",
    "Xét qua điểm thi, chứng chỉ IELTS hoặc giải học sinh giỏi."],
  [ "CMC's \"You Deserve It\" scholarship fund is worth ninety-six billion dong.",
    "Awards cover thirty, fifty, seventy, or one hundred percent of tuition for the whole program.",
    "They're based on exam scores, IELTS certificates, or academic awards."]),
 ([ "Có bốn cách để vào ngành: kỳ thi đánh giá năng lực CMC-TEST, xét học bạ, xét điểm thi tốt nghiệp trung học phổ thông, hoặc xét tuyển thẳng, ví dụ với IELTS từ 6.0.",
    "Tổ hợp là Toán nhân hai cộng hai môn bất kỳ."],
  [ "There are four ways in: the CMC-TEST aptitude exam, your high school transcript, your national graduation exam scores, or direct admission, for example with IELTS six point zero or higher.",
    "The subject combination is Math counted twice, plus any two subjects."]),
 ([ "Hãy viết dòng lệnh đầu tiên cho tương lai của bạn.",
    "Quét mã trên màn hình để đăng ký xét tuyển, hoặc gọi đường dây nóng tuyển sinh của Trường Đại học CMC."],
  [ "Make the first commit to your future.",
    "Scan the QR code to apply, or call the CMC University admissions hotline."]),
]

# Cách đọc cho giọng Việt (chỉ dùng khi tổng hợp tiếng nói; phụ đề vẫn giữ chữ gốc)
VI_SAY = [
  (r"\bAI-native\b", "ây ai nây típ"),
  (r"\bCMC-TEST\b", "xê em xê tét"),
  (r"\bCMC\b", "xê em xê"),
  (r"\bAI\b", "ây ai"),
  (r"\bIELTS\b", "ai en"),
  (r"\b6\.0\b", "sáu chấm không"),
  (r"\bInternet\b", "in tơ nét"),
  (r"\bcommit\b", "cơ mít"),
  (r"\bcode\b", "cốt"),
  (r"\bQR\b", "qui a"),
  (r"\b2027\b", "hai nghìn không trăm hai mươi bảy"),
  (r"\b2030\b", "hai nghìn không trăm ba mươi"),
]
def vi_say(t):
    for a, b in VI_SAY:
        t = re.sub(a, b, t)
    return t

EN_SAY = [(r"\bCMC-TEST\b", "C M C test"), (r"\bCMC\b", "C M C"), (r"\bIELTS\b", "eye-elts")]
def en_say(t):
    for a, b in EN_SAY:
        t = re.sub(a, b, t)
    return t
