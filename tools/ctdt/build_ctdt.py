# -*- coding: utf-8 -*-
"""Sinh các trang ctdt/*.html (tĩnh, đọc được không cần JavaScript) + ctdt.md + ctdt.json từ ctdt_data.py"""
import html, json, pathlib, shutil
import ctdt_data as D
import bench_page

E = html.escape
OUT = pathlib.Path("/home/claude/cmc-se/ctdt"); OUT.mkdir(parents=True, exist_ok=True)
C = D.COURSES
BY = {c["code"]: c for c in C}
TOTAL = sum(c["tc"] for c in C)
BLOCK_COLORS = {"dc": "#7A86A8", "csn": "#1B6F96", "nganh": "#0E1A3A", "studio": "#C77A00", "cs": "#5B4BB7", "tn": "#2E7D4F"}
LV = {k: (n, d, col) for k, n, d, col in D.AI_LEVELS}
PAGES = [("index.html", "Tổng quan"), ("chuan-dau-ra.html", "Chuẩn đầu ra"), ("khung-chuong-trinh.html", "Khung chương trình"),
         ("ke-hoach-dao-tao.html", "Kế hoạch 9 học kỳ"), ("hoc-phan.html", "Học phần"), ("doi-sanh.html", "Đối sánh quốc tế"), ("danh-gia-va-ai.html", "Đánh giá và AI"), ("trien-khai.html", "Triển khai")]

def block_sum(b): return sum(c["tc"] for c in C if c["block"] == b)
def sem_courses(s): return [c for c in C if c["sem"] == s]
def studio_of(s): return next((c for c in C if c["sem"] == s and c["block"] == "studio"), None)
def lv(code):
    parts = [p.strip() for p in code.replace("+", ",").split(",")]
    return " ".join(f'<span class="lv" title="{E(LV[p][0])}"><i style="background:{LV[p][2]}"></i>{p}</span>' for p in parts if p in LV)
def link(code, text=None):
    return f'<a href="hoc-phan.html#{code}" class="mono">{E(text or code)}</a>' if code in BY else E(text or code)

# old vs new stats
OLD = dict(n=14, lt=525, th=150, ai=5)
NEW_CODES = [r[3] for r in D.OLD_NEW]
new_lt = sum(BY[c]["lt"] for c in NEW_CODES); new_th = sum(BY[c]["th"] for c in NEW_CODES)
OLD_THEORY = round(OLD["lt"] / (OLD["lt"] + OLD["th"]) * 100)
NEW_THEORY = round(new_lt / (new_lt + new_th) * 100)
prof = [c for c in C if c["assess"] != "chung"]
prof_lt = sum(c["lt"] for c in prof); prof_th = sum(c["th"] for c in prof)
PROG_PRACTICE = round(prof_th / (prof_lt + prof_th) * 100)
AI_CORE = ["SOFT1001", "SOFT2001", "SOFT2004", "SOFT3001", "SOFT3002", "SOFT3004", "SOFT2102", "INFO3001"]
AI_CORE_TC = sum(BY[c]["tc"] for c in AI_CORE)

def page(fname, title, body, desc):
    nav = "".join(f'<a href="{f}"{" aria-current=\"page\"" if f == fname else ""}>{E(t)}</a>' for f, t in PAGES)
    crumbs = "" if fname == "index.html" else f'<div class="wrap crumbs"><a href="../index.html">Trang ngành</a> / <a href="index.html">Chương trình đào tạo</a> / {E(title)}</div>'
    return f"""<!DOCTYPE html>
<html lang="vi">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{E(title)} · CTĐT Kỹ thuật phần mềm CMC</title>
<meta name="description" content="{E(desc)}">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,700;12..96,800&family=Be+Vietnam+Pro:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500;600;700&display=swap&subset=vietnamese" rel="stylesheet">
<link rel="stylesheet" href="style.css">
</head>
<body>
<header class="top"><div class="wrap">
  <a class="brand" href="index.html"><i>SE</i><span>CTĐT Kỹ thuật phần mềm AI-native<small>Trường Đại học CMC · {E(D.META['version'])}</small></span></a>
  <nav class="nav" aria-label="Các trang chương trình đào tạo">{nav}<a href="../ho-so.html">Hồ sơ ngành ↗</a><a href="../index.html">Trang ngành ↗</a></nav>
</div></header>
{crumbs}
<main class="wrap">
{body}
</main>
<footer><div class="wrap">
  <div><b>{E(D.META['name'])} ({E(D.META['name_en'])})</b> · Mã ngành {D.META['code']} · {E(D.META['unit'])}</div>
  <div>{E(D.META['note'])} Cập nhật {D.META['updated']}.</div>
  <div>Bản văn bản cho trợ lý AI: <a href="ctdt.md">ctdt.md</a> · dữ liệu: <a href="ctdt.json">ctdt.json</a></div>
</div></footer>
<script src="app.js"></script>
</body>
</html>"""

def S(head, sub, inner, id_=""):
    return f'<section class="s"{f" id=\"{id_}\"" if id_ else ""}><div class="s-head"><h2>{head}</h2>{f"<p>{sub}</p>" if sub else ""}</div>{inner}</section>'

def table(heads, rows, nums=()):
    th = "".join(f'<th{" class=\"n\"" if i in nums else ""}>{h}</th>' for i, h in enumerate(heads))
    return f'<div class="tw"><table><thead><tr>{th}</tr></thead><tbody>{"".join(rows)}</tbody></table></div>'

def semester_map():
    out = ['<div class="years">']
    for y, tag, span, goal, ai in D.YEARS:
        out.append(f'<div class="year"><div class="ylab"><b>Năm {y} · {tag}</b><span>{span}<br>{E(goal)}</span></div>')
        for s in range(3 * y - 2, 3 * y + 1):
            st = studio_of(s); cs = [c for c in sem_courses(s) if c["block"] != "studio"]
            prod = st["product"] if st else ("Thực tập OJT: đóng góp vào hệ thống đang vận hành ở doanh nghiệp" if s == 8 else "Đồ án tốt nghiệp có người dùng thật")
            gate = next((g[0] for g in D.GATES if f"học kỳ {s} " in g[1].lower() or f"học kỳ {s}" == g[1].lower()), "")
            items = "".join(f"<li>{E(c['name'])}</li>" for c in cs if c["block"] not in ("dc",) or c["status"] != "chung")
            out.append(f'<div class="sem"><div class="h"><span>HỌC KỲ {s} · 10 TUẦN</span><span>{sum(c["tc"] for c in sem_courses(s))} TC</span></div>'
                       f'<div class="prod">{E(prod)}</div><ul>{items}</ul>{f"<div class=gate>◆ {E(gate)}</div>" if gate else ""}</div>')
        out.append('</div>')
    out.append('</div>')
    return "".join(out)

# ------------------------------------------------------------------ index
def build_index():
    figs = [("3", "năm ra trường"), ("9", "học kỳ, mỗi kỳ 10 tuần"), (str(TOTAL), "tín chỉ"), ("9", "sản phẩm trong hồ sơ"), ("7", "học phần Studio"), ("2", "học phần mở đổi chủ đề hằng năm"), ("2", "cổng năng lực không AI")]
    fig = "".join(f'<div class="fig"><b>{a}</b><span>{b}</span></div>' for a, b in figs)
    hero = f"""<div class="hero"><span class="eyebrow">Chương trình đào tạo · {E(D.META['version'])}</span>
<h1>Kỹ thuật phần mềm <em>AI-native</em></h1>
<p class="lead">Chương trình đào tạo kỹ sư phần mềm lấy kỹ năng phát triển phần mềm cùng AI làm trọng tâm: học cùng AI ở mọi học phần chuyên môn, có sản phẩm chạy thật sau mỗi học kỳ 10 tuần, thi nền tảng không AI, và ra trường sau 3 năm với hồ sơ 9 sản phẩm.</p>
<div class="figs">{fig}</div>
<p class="note">{E(D.META['note'])}</p></div>"""
    why = f"""<div class="grid g3">
<div class="card"><span class="k">QUY ĐỊNH MỚI</span><h3>Chuẩn đầu ra phải có AI</h3><p>Thông tư 54/2026/TT-BGDĐT yêu cầu chuẩn đầu ra đại học có năng lực số, trí tuệ nhân tạo, ngoại ngữ, khả năng thích ứng và học tập suốt đời, đo lường được. Chương trình đang thực hiện phải rà soát, hoàn thiện trong 36 tháng.</p></div>
<div class="card"><span class="k">THỊ TRƯỜNG</span><h3>Nghề lập trình đã đổi</h3><p>84% lập trình viên dùng hoặc sắp dùng AI nhưng 46% không tin độ chính xác của nó (Stack Overflow 2025). Doanh nghiệp cần người làm ra sản phẩm và kiểm chứng được AI, vị trí chỉ biết code cơ bản đang thu hẹp.</p></div>
<div class="card"><span class="k">HIỆN TRẠNG CTĐT</span><h3>Nhiều lý thuyết, ít AI</h3><p>Trong {OLD['n']} đề cương hiện hành, {OLD_THEORY}% số tiết trên lớp là lý thuyết; {OLD['ai']}/{OLD['n']} học phần có nội dung hoặc hoạt động AI. Trợ giảng AI đã có nhưng mới dùng cho tự học (5% điểm).</p></div></div>"""
    phil = '<div class="grid g3">' + "".join(f'<div class="card"><span class="k">{i+1:02d}</span><h3>{E(t)}</h3><p>{E(d)}</p></div>' for i, (t, d) in enumerate(D.PHILOSOPHY)) + "</div>"
    bar = '<div class="bar">' + "".join(f'<span style="width:{block_sum(b)/TOTAL*100:.1f}%;background:{BLOCK_COLORS[b]}" title="{E(n)}">{block_sum(b)}</span>' for b, n in D.BLOCKS.items()) + "</div>"
    leg = '<div class="legend">' + "".join(f'<span><i style="background:{BLOCK_COLORS[b]}"></i>{E(n)}: {block_sum(b)} TC</span>' for b, n in D.BLOCKS.items()) + "</div>"
    cmp_rows = [
        ("Thời gian", "3 năm, 9 học kỳ × 10 tuần", "3 năm, 9 học kỳ × 10 tuần (giữ mô hình của Trường)"),
        ("Lý thuyết/thực hành (14 học phần chuyển đổi)", f"{OLD_THEORY}% số tiết là lý thuyết", f"{NEW_THEORY}% lý thuyết; toàn bộ học phần chuyên môn: {PROG_PRACTICE}% thực hành"),
        ("AI trong học phần", f"{OLD['ai']}/{OLD['n']} học phần có nội dung AI", "Mọi học phần chuyên môn quy định mức dùng AI M1–M5 cho từng bài đánh giá"),
        ("Học phần về AI cho phát triển phần mềm", "Học sâu, Xử lý ngôn ngữ tự nhiên (thuộc ngành AI)", f"{len(AI_CORE)} học phần, {AI_CORE_TC} tín chỉ trọng tâm AI cho kỹ sư phần mềm"),
        ("Sản phẩm", "Bài tập lớn theo từng học phần", "Trục 7 Studio: mỗi học kỳ một sản phẩm, Demo Day tuần 10"),
        ("Bảo đảm nền tảng", "Thi cuối kỳ từng học phần", "Thi nền tảng không AI + 2 cổng năng lực cuối năm 1, năm 2"),
        ("Doanh nghiệp", "Thực tập nghề nghiệp", "Đề bài Studio 6 từ Tập đoàn CMC, thực tập OJT học kỳ 8, hội đồng đồ án có doanh nghiệp"),
        ("Cập nhật chương trình", "Theo chu kỳ rà soát", "Phiên bản hằng năm có changelog"),
        ("Công nghệ mới chưa có trong chương trình", "Chờ chu kỳ sửa chương trình", "2 học phần mở (SOFT3007, SOFT3008): chuẩn đầu ra cố định, chủ đề và đề tài đổi hằng năm"),
        ("Tiếng Anh", "Học phần tiếng Anh chuyên ngành riêng", "2 TC tiếng Anh kỹ thuật + tài liệu tiếng Anh trong mọi học phần chuyên môn; chuẩn đầu ra ngoại ngữ theo quy định của Trường"),
    ]
    cmp = table(["Tiêu chí", "CTĐT hiện hành", "CTĐT đề xuất"], [f"<tr><td><b>{E(a)}</b></td><td>{E(b)}</td><td>{E(c)}</td></tr>" for a, b, c in cmp_rows])
    diff_rows = [
        ("Năm đầu", "Học lý thuyết nền tảng, sản phẩm thật thường đến từ năm 3", "Sản phẩm chạy trên Internet ngay học kỳ 1"),
        ("Vị trí của AI", "Một học phần tự chọn hoặc một chương", "Năng lực AI 5 bậc xuyên suốt, có học phần đặc trưng Kỹ nghệ phần mềm với AI agent"),
        ("Đánh giá", "Chủ yếu thi viết", "Sản phẩm + quy trình + nhật ký AI + vấn đáp, kèm thi không AI cho nền tảng"),
        ("Hồ sơ khi tốt nghiệp", "Bảng điểm và đồ án", "Hồ sơ 9 sản phẩm có minh chứng người dùng"),
        ("Thời gian", "Thường 4–4,5 năm", "3 năm"),
    ]
    diff = table(["", "Chương trình KTPM thông thường", "CMC AI-native"], [f"<tr><td><b>{E(a)}</b></td><td>{E(b)}</td><td>{E(c)}</td></tr>" for a, b, c in diff_rows])
    legal = '<div class="grid g2">' + "".join(f'<div class="card"><span class="k">{E(a)}</span><h3>{E(b)}</h3><p>{E(c)}</p></div>' for a, b, c in D.LEGAL) + "</div>"
    nexts = [("chuan-dau-ra.html", "Chuẩn đầu ra", "5 mục tiêu, 10 chuẩn đầu ra với 20 chỉ báo đo lường được, khung năng lực AI 5 bậc, ma trận học phần."),
             ("khung-chuong-trinh.html", "Khung chương trình", f"{len(C)} học phần theo 6 khối kiến thức, 4 hướng chuyên sâu, tự chọn, cổng năng lực."),
             ("ke-hoach-dao-tao.html", "Kế hoạch 9 học kỳ", "Học phần, sản phẩm và mức AI của từng học kỳ; nhịp 10 tuần với Demo Day."),
             ("hoc-phan.html", "Đề cương rút gọn", "Mô tả, chuẩn đầu ra, kế hoạch 10 tuần, cách đánh giá, giáo trình và khóa học tham chiếu của từng học phần."),
             ("doi-sanh.html", "Đối sánh quốc tế", "Khóa học tích hợp AI của Stanford, MIT, Harvard, CMU, Berkeley, Coursera, Udacity, edX; kiểm tra nhất quán chuẩn đầu ra, SWEBOK v4."),
             ("danh-gia-va-ai.html", "Đánh giá và AI", "Thang mức dùng AI M1–M5, quy tắc ứng xử, nhật ký AI, rubric, hệ sinh thái học tập."),
             ("trien-khai.html", "Triển khai", "Bảng chuyển đổi từ CTĐT cũ, lộ trình áp dụng khóa 2027, rủi ro, changelog.")]
    nx = '<div class="grid g3">' + "".join(f'<a class="card" href="{f}"><span class="k">{i+1:02d}</span><h3>{E(t)}</h3><p>{E(d)}</p><span class="go">Xem chi tiết →</span></a>' for i, (f, t, d) in enumerate(nexts)) + "</div>"
    new3 = '<div class="grid g3">' + "".join(f'<div class="card"><span class="k">{k}</span><h3>{E(t)}</h3><p>{E(d)}</p></div>' for k, t, d in [
        ("MỚI · 2 HỌC PHẦN MỞ", "Công nghệ mới vào lớp ngay năm nó xuất hiện", "SOFT3007 Chủ đề hiện đại (học kỳ 6) và SOFT3008 Nghiên cứu và đổi mới (học kỳ 7): chuẩn đầu ra, đánh giá cố định; chủ đề, đề tài do Khoa duyệt hằng năm, không phải sửa chương trình."),
        ("GIẢM · TIẾNG ANH", "5 → 2 tín chỉ", "Gộp hai học phần tiếng Anh thành ENGL2002 Tiếng Anh kỹ thuật (đọc, viết tài liệu kỹ thuật, có AI hỗ trợ). Tiếng Anh được dùng thật trong tài liệu của mọi học phần; chuẩn đầu ra ngoại ngữ theo quy định của Trường."),
        ("TINH GỌN · LÝ THUYẾT", f"Lý thuyết: 39% → {100 - PROG_PRACTICE}% số tiết", "MATH2005, SOFT2003, INFO2011 giảm còn 2 tín chỉ; nhiều học phần chuyển giờ lý thuyết sang thực hành. Kiến trúc phần mềm dạy theo cách ra quyết định cùng AI: AI sinh phương án, kỹ sư đánh giá và chịu trách nhiệm.")]) + "</div>"
    body = hero + S(f"Điểm mới của {D.META['version'].split()[0]}", 'Chi tiết thay đổi ở trang <a href="trien-khai.html#changelog">Triển khai</a>.', new3) + S("Vì sao cần chỉnh sửa lớn", "", why) + S("Sáu nguyên tắc thiết kế", "", phil) \
        + S("Cấu trúc khối kiến thức", f"Tổng {TOTAL} tín chỉ, chưa gồm Giáo dục thể chất và Giáo dục quốc phòng – an ninh.", bar + leg) \
        + S("Ba năm, chín học kỳ, chín sản phẩm", 'Mỗi ô là một học kỳ 10 tuần. Chi tiết ở trang <a href="ke-hoach-dao-tao.html">Kế hoạch 9 học kỳ</a>.', semester_map()) \
        + S("So với chương trình hiện hành", "", cmp) + S("Điểm khác biệt", "So với mô hình chương trình Kỹ thuật phần mềm thông thường.", diff) \
        + S("Căn cứ pháp lý", "", legal) + S("Đọc chi tiết", "", nx)
    return page("index.html", "Tổng quan", body, "Chương trình đào tạo Kỹ thuật phần mềm AI-native của Trường Đại học CMC: 3 năm, 9 học kỳ, 123 tín chỉ, 9 sản phẩm.")

# ------------------------------------------------------------------ PLO
def build_plo():
    po = table(["Mã", "Mục tiêu chương trình"], [f'<tr><td class="code">{a}</td><td>{E(b)}</td></tr>' for a, b in D.POS])
    rows = []
    for code, grp, desc, pis, pos in D.PLOS:
        pi = "<br>".join(f'<span class="mono">{p}</span> {E(t)}' for p, t in pis)
        rows.append(f'<tr id="{code}"><td class="code">{code}</td><td><span class="pill">{E(grp)}</span></td><td><b>{E(desc)}</b><div style="margin-top:6px;font-size:13.5px;color:var(--muted)">{pi}</div></td><td class="code">{pos}</td></tr>')
    plo = table(["Mã", "Nhóm (TT 54/2026)", "Chuẩn đầu ra và chỉ báo đo lường (PI)", "Mục tiêu"], rows)
    tt54 = table(["Yêu cầu của Thông tư 54/2026", "Được đáp ứng bởi"], [
        "<tr><td>Năng lực số</td><td>PLO4, PLO6, PLO10 · hồ sơ năng lực số</td></tr>",
        "<tr><td>Nội dung về trí tuệ nhân tạo</td><td>PLO4 (PI4.2), PLO7, PLO9 (PI9.1) · khung năng lực AI B1–B5</td></tr>",
        "<tr><td>Năng lực ngoại ngữ</td><td>PLO8 (PI8.2) · ENGL2002 và tài liệu tiếng Anh trong các học phần chuyên môn · chuẩn đầu ra ngoại ngữ của Trường</td></tr>",
        "<tr><td>Khả năng thích ứng và học tập suốt đời</td><td>PLO10 (PI10.1, PI10.2)</td></tr>",
        "<tr><td>Đo lường được</td><td>Mỗi PLO có 2 chỉ báo gắn với bài đánh giá cụ thể; đo theo thang 5 mức của Trường</td></tr>"])
    lad = table(["Bậc", "Tên", "Thời điểm", "Sinh viên làm được"], [f'<tr><td class="code">{a}</td><td><b>{E(b)}</b></td><td>{E(c)}</td><td>{E(d)}</td></tr>' for a, b, c, d in D.AI_LADDER])
    plos = [p[0] for p in D.PLOS]
    mrows = []
    for c in C:
        if not c["plos"]: continue
        m = dict(c["plos"])
        cells = "".join(f'<td class="{m.get(p, "")}">{m.get(p, "")}</td>' for p in plos)
        mrows.append(f'<tr><td>{link(c["code"])} {E(c["name"])}</td>{cells}</tr>')
    mx = f'<div class="tw"><table class="mx"><thead><tr><th>Học phần</th>{"".join(f"<th>{p}</th>" for p in plos)}</tr></thead><tbody>{"".join(mrows)}</tbody></table></div>'
    body = f'<div class="hero"><span class="eyebrow">Chuẩn đầu ra</span><h1>Mục tiêu, chuẩn đầu ra và <em>năng lực AI</em></h1><p class="lead">Chuẩn đầu ra viết theo yêu cầu của Thông tư 54/2026/TT-BGDĐT: có năng lực số, AI, ngoại ngữ, khả năng thích ứng; mỗi chuẩn có chỉ báo quan sát và đo được.</p></div>' \
        + S("Mục tiêu chương trình (PO)", "", po) + S("Chuẩn đầu ra chương trình (PLO)", "Mỗi chỉ báo (PI) gắn với ít nhất một bài đánh giá trong học phần đạt mức M (thành thạo).", plo) \
        + S("Đáp ứng Thông tư 54/2026", "", tt54) + S("Khung năng lực AI cho kỹ sư phần mềm", "Năm bậc tăng dần qua 3 năm; mỗi học phần ghi rõ bậc năng lực AI hướng tới.", lad) \
        + S("Ma trận học phần – chuẩn đầu ra", "I: giới thiệu · R: củng cố · M: thành thạo và đánh giá chính thức.", mx)
    return page("chuan-dau-ra.html", "Chuẩn đầu ra", body, "Mục tiêu, 10 chuẩn đầu ra, 20 chỉ báo, khung năng lực AI 5 bậc và ma trận học phần của CTĐT Kỹ thuật phần mềm AI-native CMC.")

# ------------------------------------------------------------------ structure
def open_html():
    rules = table(["Cơ chế", "Quy định"], [f"<tr><td><b>{E(a)}</b></td><td>{E(b)}</td></tr>" for a, b in D.OPEN_POLICY["rules"]])
    cards = '<div class="grid g2">' + "".join(
        f'<div class="card"><span class="k">{link(code)} · HỌC KỲ {BY[code]["sem"]} · {BY[code]["tc"]} TC</span><h3>{E(BY[code]["name"])}</h3><p>{E(BY[code]["desc"])}</p>'
        f'<p style="margin-top:10px"><b>Chủ đề dự kiến năm học 2027–2028</b></p><ul style="margin:6px 0 0;padding-left:18px;font-size:14px">'
        + "".join(f'<li><b>{E(t)}</b>: {E(d)}</li>' for c2, t, d in D.TOPICS_2027 if c2 == code) + "</ul></div>"
        for code in ("SOFT3007", "SOFT3008")) + "</div>"
    return cards + '<div style="margin-top:16px">' + rules + "</div>"

def build_structure():
    rows = []
    for b, n in D.BLOCKS.items():
        cs = [c for c in C if c["block"] == b]
        rows.append(f'<tr class="grp"><td colspan="8">{E(n)} · {block_sum(b)} TC</td></tr>')
        for c in sorted(cs, key=lambda x: (x["sem"], x["code"])):
            hrs = "" if c["status"] == "chung" or c["code"].startswith(("TRACK", "ELEC")) else f'{c["lt"]}/{c["th"]}/{c["tu"]}'
            st = f'<span class="pill {c["status"]}">{E(D.STATUS[c["status"]])}</span>' + (f'<br><span class="mono" style="font-size:12px;color:var(--muted)">cũ: {E(c["old"])}</span>' if c["old"] and c["old"] != c["code"] else "")
            rows.append(f'<tr><td class="code">{link(c["code"])}</td><td>{E(c["name"])}{" <span class=pill>tự chọn</span>" if c["kind"]=="TC" else ""}</td><td class="n">{c["tc"]}</td><td class="n mono">{hrs}</td><td class="n">{c["sem"]}</td><td class="code">{E(c["prereq"])}</td><td>{E(c["ai"])}</td><td>{st}</td></tr>')
    rows.append(f'<tr class="sum"><td></td><td>Tổng</td><td class="n">{TOTAL}</td><td colspan="5"></td></tr>')
    tbl = table(["Mã", "Học phần", "TC", "LT/TH/Tự học", "HK", "Tiên quyết", "Bậc AI", "So với CTĐT cũ"], rows, nums=(2, 3, 4))
    tr = '<div class="grid g2">' + "".join(
        f'<div class="card"><span class="k">HƯỚNG {i+1}</span><h3>{E(t)}</h3><p>{E(j)}</p><ul style="margin:10px 0 0;padding-left:18px;font-size:14px">' + "".join(f'<li><span class="mono">{a}</span> <b>{E(b)}</b> (3 TC): {E(d)}<br><small style="color:var(--muted)">Tham chiếu: {"; ".join(E(n) for n, o, u, t in D.TRACK_BENCH.get(a, []))}</small></li>' for a, b, d in cs) + "</ul></div>"
        for i, (t, j, cs) in enumerate(D.TRACKS)) + "</div>"
    el = table(["Mã", "Học phần tự chọn liên ngành (3 TC)", "Ghi chú"], [f'<tr><td class="code">{a}</td><td>{E(b)}</td><td>{E(c)}</td></tr>' for a, b, c in D.ELECTIVES])
    gates = table(["Cổng", "Thời điểm", "Nội dung (không AI)", "Hệ quả"], [f'<tr><td><b>{E(a)}</b></td><td>{E(b)}</td><td>{E(c)}</td><td>{E(d)}</td></tr>' for a, b, c, d in D.GATES])
    body = f'<div class="hero"><span class="eyebrow">Khung chương trình</span><h1>{len(C)} học phần, <em>{TOTAL} tín chỉ</em></h1><p class="lead">Sáu khối kiến thức. Trục Studio là xương sống: mỗi học kỳ một học phần dự án tích hợp kiến thức của các học phần cùng kỳ. LT/TH/Tự học tính theo tiết và giờ như đề cương hiện hành của Khoa.</p></div>' \
        + S("Danh mục học phần", "Bấm mã học phần để xem đề cương rút gọn. Học phần chung (lý luận chính trị, pháp luật) theo đề cương chung của Trường.", tbl) \
        + S("Hai học phần mở", E(D.OPEN_POLICY["intro"]), open_html()) \
        + S("Bốn hướng chuyên sâu", "Chọn từ học kỳ 8: học 2 học phần của một hướng (6 TC) và làm đồ án tốt nghiệp theo hướng đó.", tr) \
        + S("Học phần tự chọn liên ngành", "Chọn 1 học phần ở học kỳ 9. Học sâu và Xử lý ngôn ngữ tự nhiên của CTĐT cũ được giữ ở đây.", el) \
        + S("Cổng năng lực", "Điều kiện chuyển giai đoạn, không tính tín chỉ.", gates) \
        + S("Ngoài khối lượng tín chỉ", "", '<div class="grid g2"><div class="card"><h3>Giáo dục thể chất, Giáo dục quốc phòng – an ninh</h3><p>Thực hiện theo quy định của Bộ Giáo dục và Đào tạo, không tính vào 123 tín chỉ.</p></div><div class="card"><h3>Chuẩn đầu ra ngoại ngữ</h3><p>Theo quy định chuẩn đầu ra ngoại ngữ của Trường (ngoài khối tín chỉ). ENGL2002 dạy đọc, viết tài liệu kỹ thuật; tiếng Anh được dùng thật qua tài liệu của các học phần chuyên môn và README, mô tả pull request của Studio.</p></div></div>')
    return page("khung-chuong-trinh.html", "Khung chương trình", body, f"Danh mục {len(C)} học phần, {TOTAL} tín chỉ, hướng chuyên sâu, tự chọn và cổng năng lực của CTĐT Kỹ thuật phần mềm AI-native CMC.")

# ------------------------------------------------------------------ plan
def build_plan():
    rh = [("1", "Khởi động, đặc tả", ""), ("2", "Thiết kế", ""), ("3", "Sprint 1", ""), ("4", "Sprint review 1", "r"), ("5", "Sprint 2", ""),
          ("6", "Review 2 · giữa kỳ", "r"), ("7", "Sprint 3", ""), ("8", "Review 3 · người dùng thử", "r"), ("9", "Làm cứng, ôn thi", ""), ("10", "Demo Day · thi cuối kỳ", "d")]
    rhythm = '<div class="rhythm">' + "".join(f'<div class="{k}"><b>T{a}</b>{E(b)}</div>' for a, b, k in rh) + "</div>"
    parts = []
    for y, tag, span, goal, ai in D.YEARS:
        yr = D.YEARS[y - 1]
        parts.append(f'<section class="s"><div class="s-head"><span class="eyebrow">Năm {y} · {tag} · {span}</span><h2>{E(goal)}</h2><p>Mức AI: {E(ai)}.</p></div>')
        for s in range(3 * y - 2, 3 * y + 1):
            cs = sem_courses(s); st = studio_of(s)
            rows = [f'<tr><td class="code">{link(c["code"])}</td><td>{E(c["name"])}</td><td class="n">{c["tc"]}</td><td>{E(c["ai"])}</td><td>{" ".join(dict.fromkeys(l for a in D.ASSESS[c["assess"]] for l in [a[2]]))}</td></tr>' for c in cs]
            prod = st["product"] if st else ("Đóng góp vào hệ thống đang vận hành tại doanh nghiệp" if s == 8 else "Đồ án tốt nghiệp có người dùng hoặc khách hàng thật")
            gate = next((g for g in D.GATES if f"học kỳ {s}" in g[1].lower()), None)
            parts.append(f'<h3 style="margin:18px 0 8px;font-size:20px">Học kỳ {s} · {sum(c["tc"] for c in cs)} TC</h3><p class="note" style="margin:0 0 10px"><b>Sản phẩm học kỳ:</b> {E(prod)}.{f" <b>{E(gate[0])}:</b> {E(gate[2])}" if gate else ""}</p>'
                         + table(["Mã", "Học phần", "TC", "Bậc AI", "Mức dùng AI trong đánh giá"], rows, nums=(2,)))
        parts.append("</section>")
    body = '<div class="hero"><span class="eyebrow">Kế hoạch đào tạo</span><h1>9 học kỳ × 10 tuần, <em>mỗi kỳ một sản phẩm</em></h1><p class="lead">Mỗi năm học có 3 học kỳ. Học phần Studio của học kỳ tích hợp kiến thức của các học phần cùng kỳ thành một sản phẩm, trình diễn ở Demo Day tuần 10.</p></div>' \
        + S("Nhịp 10 tuần của một học kỳ", "Áp dụng cho Studio; các học phần khác bố trí kiểm tra giữa kỳ tuần 5–6 và thi cuối kỳ tuần 10.", rhythm) \
        + S("Bản đồ 3 năm", "", semester_map()) + "".join(parts)
    return page("ke-hoach-dao-tao.html", "Kế hoạch 9 học kỳ", body, "Kế hoạch đào tạo 9 học kỳ, mỗi học kỳ 10 tuần, sản phẩm và mức dùng AI của từng học kỳ, CTĐT Kỹ thuật phần mềm AI-native CMC.")

# ------------------------------------------------------------------ courses
def build_courses():
    flt = '<div class="filters" role="group" aria-label="Lọc học phần"><button type="button" data-f="all" aria-pressed="true">Tất cả</button>' + "".join(
        f'<button type="button" data-f="hk{s}" aria-pressed="false">HK{s}</button>' for s in range(1, 10)) + \
        '<button type="button" data-f="studio" aria-pressed="false">Studio</button><button type="button" data-f="moi" aria-pressed="false">Học phần mới</button>' \
        '<label class="hidden" for="q">Tìm học phần</label><input id="q" type="search" placeholder="Tìm theo tên, mã, nội dung…"></div>'
    arts = []
    for c in sorted(C, key=lambda x: (x["sem"], x["block"] == "studio", C.index(x))):
        tags = f'hk{c["sem"]} {c["block"]} {c["status"]}'
        meta = [f'{c["tc"]} tín chỉ', f'Học kỳ {c["sem"]}', E(D.BLOCKS[c["block"]])]
        if c["lt"] or c["th"]: meta.append(f'LT {c["lt"]} · TH {c["th"]} · Tự học {c["tu"]} giờ')
        if c["prereq"]: meta.append(f'Tiên quyết: {E(c["prereq"])}')
        if c["ai"]: meta.append(f'Năng lực AI: {E(c["ai"])}')
        meta.append(E(D.STATUS[c["status"]]) + (f' (cũ: {E(c["old"])})' if c["old"] else ""))
        if c["status"] == "chung":
            body = '<p class="desc">Học phần chung theo đề cương thống nhất của Trường. Sinh viên được khuyến khích dùng Trợ giảng AI để tự học (mức M2).</p>'
        elif c["code"].startswith(("TRACK", "ELEC")):
            if c["code"].startswith("TRACK"):
                lst = "".join(f'<li><b>{E(t)}</b>: ' + "; ".join(f'<span class="mono">{a}</span> {E(b)}' for a, b, d in cs) + "</li>" for t, j, cs in D.TRACKS)
            else:
                lst = "".join(f'<li><span class="mono">{a}</span> {E(b)}</li>' for a, b, d in D.ELECTIVES)
            body = f'<p class="desc">Sinh viên chọn theo hướng chuyên sâu đã đăng ký.</p><ul class="clo">{lst}</ul><p style="font-size:14px;color:var(--muted)">Xem <a href="khung-chuong-trinh.html">Khung chương trình</a>.</p>'
        else:
            clo = "".join(f'<li><span class="mono">{a}</span> {E(b)} <span class="plo-tags">{" ".join(f"<a href=chuan-dau-ra.html#{x} class=ptag>{x}</a>" for x in m)}</span></li>' for a, b, m in c["clos"])
            plo = ", ".join(f'{p} ({m})' for p, m in c["plos"])
            wk = "".join(f'<li{" class=upd" if i in c["wk_new"] else ""}><span>{E(w)}</span></li>' for i, w in enumerate(c["weeks"]))
            asr = "".join(f'<tr><td>{E(a)}</td><td class="n">{E(b)}</td><td>{lv(l)}</td></tr>' for a, b, l in D.ASSESS[c["assess"]])
            prod = f'<p class="note" style="margin:8px 0 0"><b>Sản phẩm:</b> {E(c["product"])}.</p>' if c["product"] else ""
            res = ""
            if c["tb"] or c["bench"]:
                bl = "".join(f'<li>{f"<a href={chr(34)}{E(u)}{chr(34)}>{E(n)}</a>" if u else E(n)}<small>{E(o)}</small><span>{E(t)}</span></li>' for n, o, u, t in c["bench"])
                ch = "".join(f"<li>{E(x)}</li>" for x in c["changes"])
                sw = " ".join(f'<span class="pill">{k}</span>' for k in c["swebok"])
                res = f'''<div class="res"><div><h4>GIÁO TRÌNH CHÍNH</h4><ul class="clo">{"".join(f"<li>{E(x)}</li>" for x in c["tb"])}</ul>
<h4>TÀI LIỆU THAM KHẢO</h4><ul class="clo">{"".join(f"<li>{E(x)}</li>" for x in c["refs_list"]) or "<li>Theo giảng viên</li>"}</ul>
{f"<h4>VÙNG TRI THỨC SWEBOK V4</h4><p class=sw>{sw}</p>" if sw else ""}</div>
<div><h4>KHÓA HỌC THAM CHIẾU</h4><ul class="bench">{bl}</ul>{f"<h4>CẬP NHẬT TỪ ĐỐI SÁNH (V2027.2)</h4><ul class=clo>{ch}</ul>" if ch else ""}</div></div>'''
            body = f'''<p class="desc">{E(c["desc"])}</p>{prod}<div class="cols"><div><h4>KẾ HOẠCH 10 TUẦN{" <span class=updk>■ tuần cập nhật v2027.2</span>" if c["wk_new"] else ""}</h4><ol class="wk">{wk}</ol></div>
<div><h4>CHUẨN ĐẦU RA HỌC PHẦN → PLO</h4><ul class="clo">{clo}</ul><p style="font-size:13px;color:var(--muted);margin:6px 0 0">Đóng góp: {E(plo)}</p>
<h4>ĐÁNH GIÁ</h4><div class="tw"><table><thead><tr><th>Thành phần</th><th class="n">Trọng số</th><th>Mức AI</th></tr></thead><tbody>{asr}</tbody></table></div></div></div>{res}'''
        arts.append(f'<article class="course" id="{c["code"]}" data-tags="{tags}"><header><span class="code">{c["code"]}</span><h3>{E(c["name"])}</h3>{f"<span class=en>{E(c[chr(101)+chr(110)])}</span>" if c["en"] else ""}</header><div class="meta">{"".join(f"<span>{m}</span>" for m in meta)}</div>{body}</article>')
    body = f'<div class="hero"><span class="eyebrow">Đề cương rút gọn</span><h1>{len(C)} học phần, <em>từng tuần một</em></h1><p class="lead">Mô tả, chuẩn đầu ra, kế hoạch 10 tuần, cách đánh giá và mức dùng AI của từng học phần. Đề cương chi tiết đầy đủ sẽ viết theo mẫu đề cương của Trường khi chương trình được thông qua.</p></div>' \
        + flt + '<p id="cnt" class="mono" style="font-size:12.5px;color:var(--muted)"></p>' + "".join(arts)
    return page("hoc-phan.html", "Học phần", body, "Đề cương rút gọn các học phần CTĐT Kỹ thuật phần mềm AI-native CMC: mô tả, chuẩn đầu ra, kế hoạch 10 tuần, đánh giá và mức dùng AI.")

# ------------------------------------------------------------------ assessment & AI
def build_assess():
    levels = '<div class="grid g3">' + "".join(f'<div class="card" style="border-top:5px solid {col}"><span class="k">{k}</span><h3>{E(n)}</h3><p>{E(d)}</p></div>' for k, n, d, col in D.AI_LEVELS) + "</div>"
    tmpl_names = {"nen-tang": "Học phần nền tảng", "ky-nghe": "Học phần kỹ nghệ", "ai": "Học phần xây dựng AI", "studio": "Studio", "mo": "Học phần mở: Chủ đề hiện đại", "nghien-cuu": "Học phần mở: Nghiên cứu và đổi mới", "thuc-tap": "Thực tập OJT", "do-an": "Đồ án tốt nghiệp"}
    tm = '<div class="grid g3">' + "".join(
        f'<div class="card"><h3>{E(tmpl_names[k])}</h3><div class="tw" style="margin-top:8px"><table><tbody>' + "".join(f'<tr><td>{E(a)}</td><td class="n">{E(b)}</td><td>{lv(l)}</td></tr>' for a, b, l in D.ASSESS[k]) + "</tbody></table></div>"
        f'<p style="margin-top:8px">Áp dụng cho: ' + ", ".join(c["code"] for c in C if c["assess"] == k)[:220] + "</p></div>" for k in tmpl_names) + "</div>"
    rules = ["Sinh viên được dùng AI trong học tập theo mức quy định cho từng bài đánh giá; mức được ghi trong đề cương và đề bài.",
             "Mọi bài ở mức M3, M4 phải nộp nhật ký AI theo mẫu của Khoa. Không khai báo hoặc khai báo không đầy đủ là vi phạm liêm chính học thuật theo Thông tư 49/2026/TT-BGDĐT.",
             "Sinh viên chịu trách nhiệm về toàn bộ nội dung mình nộp, kể cả phần do AI tạo ra, và phải giải thích được khi được hỏi.",
             "Không đưa dữ liệu cá nhân, dữ liệu của doanh nghiệp hoặc đề thi vào công cụ AI không được Trường hoặc doanh nghiệp cho phép.",
             "Bài mức M1 làm tại phòng thi không AI; mọi hình thức dùng AI trong bài M1 bị xử lý như gian lận thi cử.",
             "Giảng viên dùng AI hỗ trợ soạn học liệu, đề và nhận xét nhưng tự chịu trách nhiệm về kết quả chấm; AI không quyết định điểm.",
             "Tại doanh nghiệp, sinh viên tuân thủ chính sách dùng AI của doanh nghiệp khi chính sách đó chặt hơn quy định của Trường.",
             "Khoa rà soát quy tắc này mỗi năm cùng với changelog của chương trình."]
    rl = '<ol style="padding-left:20px;display:flex;flex-direction:column;gap:6px;max-width:80ch">' + "".join(f"<li>{E(r)}</li>" for r in rules) + "</ol>"
    log = table(["Trường thông tin", "Nội dung cần ghi"], [f"<tr><td><b>{E(a)}</b></td><td>{E(b)}</td></tr>" for a, b in [
        ("Công cụ và phiên bản", "Tên công cụ, mô hình, chế độ (trợ lý, agent)."), ("Mục đích", "Dùng để làm gì: giải thích, sinh mã, sinh kiểm thử, review…"),
        ("Đầu vào chính", "Câu lệnh hoặc đặc tả đã đưa cho AI (rút gọn)."), ("Đầu ra được dùng", "Phần nào của sản phẩm đến từ AI (tệp, hàm, commit)."),
        ("Kiểm chứng", "Đã kiểm chứng thế nào: kiểm thử, đọc lại, so với tài liệu, chạy thử."), ("Từ chối hoặc sửa", "Đề xuất nào của AI bị loại hoặc sửa, vì sao."), ("Phản tư", "Học được gì; lần sau làm khác thế nào.")]])
    scale = table(["Mức", "Tỷ lệ", "Điểm"], [f"<tr><td>{E(a)}</td><td>{E(b)}</td><td class=\"n\">{E(c)}</td></tr>" for a, b, c in [
        ("Fail – Below Expectations", "< 40%", "< 4"), ("Beginning – Needs Improvement", "40–54%", "4–5,4"), ("Developing – Marginally adequate", "55–69%", "5,5–6,9"),
        ("Sufficient – Meets Expectations", "70–84%", "7–8,5"), ("Exemplary – Exceeds Expectations", "85–100%", "8,6–10")]])
    rub = table(["Tiêu chí Studio", "Trọng số", "Mức Exemplary trông như thế nào"], [f'<tr><td><b>{E(a)}</b></td><td class="n">{b}</td><td>{E(c)}</td></tr>' for a, b, c in [
        ("Giá trị cho người dùng", "20%", "Có người dùng thật, có số liệu sử dụng và phản hồi, sản phẩm đã thay đổi theo phản hồi."),
        ("Chất lượng kỹ thuật", "25%", "Kiến trúc rõ ràng, kiểm thử tự động đạt ngưỡng, không lỗi nghiêm trọng, triển khai tự động."),
        ("Quy trình và làm nhóm", "15%", "Commit, pull request, review đều đặn; đóng góp cân đối, minh chứng từ kho mã."),
        ("Dùng AI có trách nhiệm", "15%", "Nhật ký đầy đủ, có ví dụ từ chối đề xuất sai của AI, có đo chất lượng mã AI sinh."),
        ("Bảo vệ cá nhân không AI", "20%", "Giải thích được mọi phần mã của mình, sửa lỗi trực tiếp khi được yêu cầu."),
        ("Trình bày", "5%", "Demo rõ ràng, đúng giờ, trả lời chất vấn tốt; README và mô tả sản phẩm bằng tiếng Anh từ năm 2.")]])
    gates = table(["Cổng", "Thời điểm", "Nội dung", "Hệ quả"], [f'<tr><td><b>{E(a)}</b></td><td>{E(b)}</td><td>{E(c)}</td><td>{E(d)}</td></tr>' for a, b, c, d in D.GATES])
    sys_ = '<div class="grid g3">' + "".join(f'<div class="card"><h3>{E(a)}</h3><p>{E(b)}</p></div>' for a, b in D.SYSTEMS) + "</div>"
    body = '<div class="hero"><span class="eyebrow">Đánh giá và AI</span><h1>Học cùng AI, <em>thi cả không AI</em></h1><p class="lead">Mỗi bài đánh giá có một mức dùng AI rõ ràng. Thang mức tham khảo AI Assessment Scale (Perkins và cộng sự, 2024), điều chỉnh cho kỹ thuật phần mềm và quy định của Thông tư 49/2026/TT-BGDĐT.</p></div>' \
        + S("Thang mức dùng AI M1–M5", "", levels) + S("Cấu trúc đánh giá theo loại học phần", "Trọng số cụ thể có thể điều chỉnh trong đề cương chi tiết, giữ nguyên mức AI.", tm) \
        + S("Quy tắc ứng xử về AI của Khoa (dự thảo)", "Đáp ứng yêu cầu ban hành quy tắc ứng xử về AI và quy định liêm chính học thuật theo Thông tư 49/2026/TT-BGDĐT.", rl) \
        + S("Mẫu nhật ký AI", "Bắt buộc cho mọi bài ở mức M3, M4; lưu trong kho mã cùng sản phẩm.", log) \
        + S("Rubric Studio", "Chấm theo thang 5 mức đang dùng trong đề cương của Khoa.", rub + '<div style="margin-top:12px">' + scale + "</div>") \
        + S("Cổng năng lực", "", gates) + S("Hệ sinh thái học tập số", "Kế thừa Trợ giảng AI và nền tảng edux đang có, bổ sung theo lộ trình.", sys_)
    return page("danh-gia-va-ai.html", "Đánh giá và AI", body, "Thang mức dùng AI M1–M5, quy tắc ứng xử về AI, nhật ký AI, rubric Studio, cổng năng lực của CTĐT Kỹ thuật phần mềm AI-native CMC.")

# ------------------------------------------------------------------ rollout
def build_rollout():
    rows = [f'<tr><td class="code">{a}</td><td>{E(b)}</td><td class="n">{c}</td><td class="code">{link(d)}</td><td>{E(e)}</td><td class="n">{BY[d]["tc"]}</td><td><span class="pill">{E(f)}</span></td><td>{E(g)}</td></tr>' for a, b, c, d, e, f, g in D.OLD_NEW]
    mp = table(["Mã cũ", "Học phần cũ", "TC", "Mã mới", "Học phần mới", "TC", "Thay đổi", "Nội dung điều chỉnh"], rows, nums=(2, 5))
    new_list = [c for c in C if c["status"] == "moi" and not c["code"].startswith(("TRACK", "ELEC"))]
    nl = table(["Mã", "Học phần mới", "TC", "HK"], [f'<tr><td class="code">{link(c["code"])}</td><td>{E(c["name"])}</td><td class="n">{c["tc"]}</td><td class="n">{c["sem"]}</td></tr>' for c in new_list], nums=(2, 3))
    stats = f'''<div class="grid g4">
<div class="card"><span class="k">LÝ THUYẾT TRÊN LỚP</span><h3>{OLD_THEORY}% → {NEW_THEORY}%</h3><p>Tỷ lệ tiết lý thuyết của 14 học phần chuyển đổi.</p></div>
<div class="card"><span class="k">HỌC PHẦN CÓ AI</span><h3>{OLD['ai']}/{OLD['n']} → toàn bộ</h3><p>Mọi học phần chuyên môn quy định mức dùng AI cho từng bài đánh giá.</p></div>
<div class="card"><span class="k">TRỌNG TÂM AI</span><h3>{AI_CORE_TC} tín chỉ</h3><p>{len(AI_CORE)} học phần trọng tâm AI cho kỹ sư phần mềm, chưa kể 7 Studio.</p></div>
<div class="card"><span class="k">HỌC PHẦN MỚI</span><h3>{len(new_list)}</h3><p>Gồm 7 Studio, 2 học phần mở và các học phần đặc tả, kiến trúc, AI agent, bảo mật, LLM, vận hành.</p></div></div>'''
    tl = '<div class="tl">' + "".join(f"<div><small>{E(a)}</small><b>{E(b)}</b><p>{E(c)}</p></div>" for a, b, c in D.ROADMAP) + "</div>"
    rk = table(["Rủi ro", "Biện pháp"], [f"<tr><td><b>{E(a)}</b></td><td>{E(b)}</td></tr>" for a, b in D.RISKS])
    train = '<div class="grid g3">' + "".join(f'<div class="card"><h3>{E(a)}</h3><p>{E(b)}</p></div>' for a, b in [
        ("Dạy học với AI", "Thiết kế bài đánh giá theo thang M1–M5, chấm nhật ký AI, vấn đáp giải thích code."),
        ("Kỹ nghệ phần mềm với AI agent", "Giảng viên tự làm một dự án nhỏ bằng quy trình đặc tả → agent → kiểm thử trước khi dạy."),
        ("Huấn luyện Studio", "Vai trò giảng viên như khách hàng và quản lý sản phẩm; điều phối sprint review, Demo Day.")]) + "</div>"
    log = '<div class="tw"><table><tbody>' + "".join(f"<tr><td class=\"code\">{a}</td><td>{E(b)}</td></tr>" for a, b in D.CHANGELOG_3 + D.CHANGELOG_2 + [
        ("v2027.1", "Phiên bản đề xuất: mô hình Studio, khung năng lực AI 5 bậc, thang M1–M5, 2 cổng năng lực, 17 học phần mới, 4 hướng chuyên sâu."),
        ("v2027.1", "Giảm tín chỉ INFO2007, PROG2006, INFO2011 (4 → 3) để nhường chỗ cho Studio và học phần đặc tả, kiến trúc."),
        ("v2027.1", "INFO2013 thay bằng SOFT1001; INFO3007 thay bằng SOFT2003; BIGD4001, BIGD4003 chuyển sang tự chọn.")]) + "</tbody></table></div>"
    legal = table(["Văn bản", "Nội dung liên quan"], [f"<tr><td><b>{E(a)}</b><br><span style=\"font-size:13px;color:var(--muted)\">{E(b)}</span></td><td>{E(c)}</td></tr>" for a, b, c in D.LEGAL])
    src = "<ol style=\"padding-left:20px;font-size:14px\">" + "".join(f'<li>{f"<a href={chr(34)}{u}{chr(34)}>{E(t)}</a>" if u else E(t)}</li>' for t, u in D.SOURCES) + "</ol>"
    body = '<div class="hero"><span class="eyebrow">Triển khai</span><h1>Từ chương trình hiện hành <em>đến khóa 2027</em></h1><p class="lead">Chương trình kế thừa 14 học phần đã có đề cương, giữ mô hình 3 năm – 9 học kỳ của Trường, và đáp ứng thời hạn rà soát 36 tháng của Thông tư 54/2026/TT-BGDĐT.</p></div>' \
        + S("Thay đổi chính bằng số", "", stats) + S("Bảng chuyển đổi từ 14 học phần hiện hành", "Dùng để xét tương đương cho sinh viên các khóa đang học.", mp) \
        + S("Học phần mới cần viết đề cương", "", nl) + S("Lộ trình", "", tl) + S("Bồi dưỡng giảng viên", "", train) + S("Rủi ro và biện pháp", "", rk) \
        + S("Changelog", "Chương trình được quản lý theo phiên bản như phần mềm.", log, "changelog") + S("Căn cứ pháp lý", "", legal) + S("Nguồn tham khảo", "", src)
    return page("trien-khai.html", "Triển khai", body, "Bảng chuyển đổi từ CTĐT hiện hành, lộ trình áp dụng khóa 2027, bồi dưỡng giảng viên, rủi ro và changelog của CTĐT Kỹ thuật phần mềm AI-native CMC.")

APP_JS = """(function(){
  var btns=document.querySelectorAll('.filters button'), q=document.getElementById('q'), arts=document.querySelectorAll('article.course'), cnt=document.getElementById('cnt');
  if(!arts.length) return;
  var f='all';
  function apply(){ var s=(q&&q.value||'').toLowerCase().trim(), n=0;
    arts.forEach(function(a){ var ok=(f==='all'||(' '+a.dataset.tags+' ').indexOf(' '+f+' ')>=0)&&(!s||a.textContent.toLowerCase().indexOf(s)>=0); a.classList.toggle('hidden',!ok); if(ok)n++; });
    if(cnt) cnt.textContent=n+' học phần'; }
  btns.forEach(function(b){ b.addEventListener('click',function(){ f=b.dataset.f; btns.forEach(function(x){x.setAttribute('aria-pressed',x===b)}); apply(); }); });
  if(q) q.addEventListener('input',apply);
  apply();
  if(location.hash){ var t=document.getElementById(location.hash.slice(1)); if(t) t.scrollIntoView(); }
})();"""

def build_md():
    L = [f"# CTĐT Kỹ thuật phần mềm AI-native – Trường Đại học CMC ({D.META['version']})", "", f"> {D.META['note']} Cập nhật {D.META['updated']}.", "",
         f"- Thời gian: 3 năm, 9 học kỳ, mỗi học kỳ 10 tuần; tổng {TOTAL} tín chỉ (chưa gồm GDTC, GDQP-AN).", "- Mỗi học kỳ có một học phần Studio làm ra một sản phẩm; tốt nghiệp với hồ sơ 9 sản phẩm.",
         "- Hai cổng năng lực không AI cuối năm 1 và năm 2; thang mức dùng AI M1–M5 cho từng bài đánh giá.", "", "## Nguyên tắc", ""]
    L += [f"- **{t}:** {d}" for t, d in D.PHILOSOPHY]
    L += ["", "## Mục tiêu (PO)", ""] + [f"- **{a}:** {b}" for a, b in D.POS]
    L += ["", "## Chuẩn đầu ra (PLO)", ""]
    for code, grp, desc, pis, pos in D.PLOS:
        L.append(f"- **{code}** ({grp}): {desc}"); L += [f"  - {p}: {t}" for p, t in pis]
    L += ["", "## Khung năng lực AI", ""] + [f"- **{a} {b}** ({c}): {d}" for a, b, c, d in D.AI_LADDER]
    L += ["", "## Thang mức dùng AI trong đánh giá", ""] + [f"- **{k} {n}:** {d}" for k, n, d, _ in D.AI_LEVELS]
    L += ["", "## Kế hoạch 9 học kỳ", ""]
    for s in range(1, 10):
        cs = sem_courses(s); st = studio_of(s)
        L.append(f"### Học kỳ {s} ({sum(c['tc'] for c in cs)} TC)")
        if st: L.append(f"Sản phẩm: {st['product']}.")
        L += [f"- {c['code']} {c['name']} – {c['tc']} TC" for c in cs]; L.append("")
    L += ["## Đề cương rút gọn", ""]
    for c in C:
        if c["status"] == "chung" or c["code"].startswith(("TRACK", "ELEC")): continue
        L += [f"### {c['code']} {c['name']} ({c['tc']} TC, HK{c['sem']})", c["desc"], ""]
        L += [f"- {a}: {b} (→ {', '.join(m)})" for a, b, m in c["clos"]]
        if c["tb"]: L += ["", "Giáo trình chính: " + "; ".join(c["tb"])]
        if c["refs_list"]: L += ["Tham khảo: " + "; ".join(c["refs_list"])]
        if c["bench"]: L += ["Khóa học tham chiếu: " + "; ".join(f"{n} ({o})" for n, o, u, t in c["bench"])]
        L += ["", "Kế hoạch 10 tuần:"] + [f"{i+1}. {w}" for i, w in enumerate(c["weeks"])]
        L += ["", "Đánh giá: " + "; ".join(f"{a} {b} ({l})" for a, b, l in D.ASSESS[c["assess"]]), ""]
    L += ["## Hướng chuyên sâu", ""] + [f"- **{t}** ({j}): " + "; ".join(f"{a} {b}" for a, b, d in cs) for t, j, cs in D.TRACKS]
    L += ["", "## Cổng năng lực", ""] + [f"- **{a}** ({b}): {c} {d}" for a, b, c, d in D.GATES]
    L += ["", "## Chuyển đổi từ CTĐT hiện hành", ""] + [f"- {a} {b} ({c} TC) → {d} {e}: {f}. {g}" for a, b, c, d, e, f, g in D.OLD_NEW]
    L += ["", "## Căn cứ pháp lý", ""] + [f"- **{a}** – {b}: {c}" for a, b, c in D.LEGAL]
    return "\n".join(L) + "\n"

if __name__ == "__main__":
    shutil.copy("/home/claude/ctdt/style.css", OUT / "style.css")
    (OUT / "app.js").write_text(APP_JS, encoding="utf-8")
    for fn, f in [("index.html", build_index), ("chuan-dau-ra.html", build_plo), ("khung-chuong-trinh.html", build_structure), ("ke-hoach-dao-tao.html", build_plan),
                  ("hoc-phan.html", build_courses), ("doi-sanh.html", lambda: bench_page.build_bench(D, C, E, S, table, link, page)), ("danh-gia-va-ai.html", build_assess), ("trien-khai.html", build_rollout)]:
        (OUT / fn).write_text(f(), encoding="utf-8")
    (OUT / "ctdt.md").write_text(build_md(), encoding="utf-8")
    (OUT / "ctdt.json").write_text(json.dumps(dict(meta=D.META, pos=D.POS, plos=D.PLOS, courses=C, tracks=D.TRACKS, gates=D.GATES), ensure_ascii=False, indent=1), encoding="utf-8")
    print("built", TOTAL, "TC;", len(C), "courses; theory", OLD_THEORY, "->", NEW_THEORY, "; practice prof", PROG_PRACTICE, "; AI core TC", AI_CORE_TC)
