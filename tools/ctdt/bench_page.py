# -*- coding: utf-8 -*-
"""Trang ctdt/doi-sanh.html — đối sánh quốc tế và kiểm tra nhất quán chuẩn đầu ra. Được build_ctdt.py gọi."""

KEEP = """<div class="grid g3">
<div class="card"><span class="k">GIỮ NGUYÊN</span><h3>Mục tiêu, PLO và chỉ báo</h3><p>5 PO, 10 PLO, 20 PI không đổi. Đối sánh chỉ thay nội dung và học liệu bên trong học phần.</p></div>
<div class="card"><span class="k">GIỮ NGUYÊN</span><h3>Tín chỉ và cấu trúc</h3><p>Ở bản v2027.2: 123 tín chỉ, 43 học phần, 9 học kỳ, 6 khối kiến thức, thang M1–M5 không đổi. Bản v2027.3 điều chỉnh cấu trúc (giảm tiếng Anh, thêm 2 học phần mở), xem trang Triển khai.</p></div>
<div class="card"><span class="k">ĐIỀU CHỈNH</span><h3>Hai ánh xạ PLO</h3><p>Kiểm tra tự động phát hiện PLO5 chưa có học phần giới thiệu và PLO1 chưa có học phần đánh giá thành thạo; đã bổ sung PROG2005 (PLO5, I) và SOFT3005 (PLO1, M).</p></div></div>"""
USE = """<p class="note">Khóa học tham chiếu dùng để đối chiếu nội dung, phương pháp dạy và cách đánh giá, không phải để chuyển đổi tín chỉ. Các khóa mở (MIT, Stanford, Hugging Face, Google, Helsinki…) có thể giao làm học liệu tự học; việc công nhận chứng chỉ trực tuyến theo quy chế của Trường.</p>"""


def build_bench(D, C, E, S, table, link, page):
    prof = [c for c in C if c["status"] != "chung" and not c["code"].startswith(("TRACK", "ELEC"))]
    checks, chain, cov = D.check_consistency()
    uniq = {}
    for c in prof:
        for n, o, u, t in c["bench"]:
            uniq.setdefault(n, dict(o=o, u=u, cs=[]))["cs"].append(c["code"])
    KEYS = ["Stanford", "MIT", "Harvard", "Carnegie Mellon", "Berkeley", "Brown", "UT Austin", "München", "Princeton", "Helsinki", "Vanderbilt",
            "Duke", "San Diego", "Google", "Meta", "DeepLearning.AI", "Udacity", "Hugging Face", "GitHub", "ISTQB", "OWASP", "IEEE", "Microsoft", "Y Combinator"]
    orgs = sorted({k for v in uniq.values() for k in KEYS if k in v["o"] or k in v["u"]})
    books = {x for c in prof for x in c["tb"] + c["refs_list"] if any(y in x for y in ("2024", "2025", "2026"))}
    nwk = sum(len(c["wk_new"]) for c in prof)
    figs = [(str(len(uniq)), "khóa học, chuẩn tham chiếu"), (str(len(orgs)), "trường, doanh nghiệp, tổ chức chuẩn"),
            (str(len(books)), "giáo trình, tài liệu xuất bản 2024–2026"), (str(nwk), "tuần học được cập nhật"),
            (str(sum(len(c["clos"]) for c in prof)), "CLO đã gắn PLO"),
            (f'{sum(1 for v in cov.values() if v)}/{len(cov)}', "vùng tri thức SWEBOK v4")]
    fig = "".join(f'<div class="fig"><b>{a}</b><span>{b}</span></div>' for a, b in figs)
    crit = '<div class="grid g4">' + "".join(f'<div class="card"><span class="k">TIÊU CHÍ</span><h3>{E(a)}</h3><p>{E(b)}</p></div>' for a, b in D.CRITERIA) + "</div>"

    def blink(n, u):
        return f'<a href="{E(u)}">{E(n)}</a>' if u else E(n)

    rows = [f'<tr><td class="code">{link(c["code"])}</td><td>{E(c["name"])}</td><td>{"<br>".join(E(x) for x in c["tb"])}</td>'
            f'<td>{"<br>".join(blink(n, u) + f" <small style=color:var(--muted)>({E(o)})</small>" for n, o, u, t in c["bench"])}</td></tr>' for c in prof]
    tbl = table(["Mã", "Học phần", "Giáo trình chính", "Khóa học tham chiếu"], rows)
    rev = table(["Khóa học, chuẩn tham chiếu", "Đơn vị · năm", "Dùng cho học phần"], [
        f'<tr><td>{blink(n, v["u"])}</td><td>{E(v["o"])}</td><td class="code">{" ".join(link(x) for x in dict.fromkeys(v["cs"]))}</td></tr>'
        for n, v in sorted(uniq.items(), key=lambda kv: (-len(kv[1]["cs"]), kv[0]))])
    chk = '<ul class="checks">' + "".join(
        f'<li class="{"ok" if ok else "bad"}"><b>{"✓" if ok else "✗"} {E(n)}</b><span>{E(d)}</span></li>' for n, ok, d in checks) + "</ul>"

    def cl(lst):
        return " ".join(f'{link(code)}<sub>HK{s}</sub>' for s, code in lst)
    ch = table(["PLO", "Giới thiệu (I)", "Củng cố (R)", "Thành thạo, đánh giá chính thức (M)"],
               [f'<tr><td class="code"><a href="chuan-dau-ra.html#{p}">{p}</a></td><td>{cl(v["I"])}</td><td>{cl(v["R"])}</td><td>{cl(v["M"])}</td></tr>' for p, v in chain.items()])
    sw = table(["Vùng tri thức SWEBOK v4", "Học phần đảm nhận"],
               [f'<tr><td><span class="pill">{k}</span> {E(n)}</td><td class="code">{" ".join(link(x) for x in cov[k])}</td></tr>' for k, n in D.SWEBOK_KA])
    body = ('<div class="hero"><span class="eyebrow">Đối sánh quốc tế · v2027.2</span><h1>Mỗi học phần có <em>khóa học tham chiếu</em> đã tích hợp AI</h1>'
            '<p class="lead">Nội dung, giáo trình và cách đánh giá của từng học phần được đối chiếu với khóa học 2024–2026 của các trường hàng đầu, nền tảng Coursera, Udacity, edX, Hugging Face và các chuẩn nghề nghiệp. '
            f'Chuẩn đầu ra được kiểm tra tự động để không lệch sau khi cập nhật.</p><div class="figs">{fig}</div></div>'
            + S("Tiêu chí chọn khóa học tham chiếu", "", crit) + S("Đổi gì, giữ gì", "", KEEP + USE)
            + S("Kiểm tra nhất quán chuẩn đầu ra", "Chạy tự động mỗi lần sinh lại chương trình từ dữ liệu.", chk)
            + S("Chuỗi Giới thiệu – Củng cố – Thành thạo của 10 PLO", "Bấm mã để xem học phần. HK: học kỳ.", ch)
            + S("Bảng đối sánh theo học phần", 'Điều tiếp thu từ từng khóa nằm trong trang <a href="hoc-phan.html">Học phần</a>.', tbl)
            + S("Danh mục nguồn tham chiếu", "Sắp theo số học phần sử dụng.", rev)
            + S("Đối chiếu SWEBOK v4 (IEEE Computer Society)", "Mỗi vùng tri thức có ít nhất một học phần đảm nhận.", sw))
    return page("doi-sanh.html", "Đối sánh quốc tế", body,
                "Đối sánh từng học phần CTĐT Kỹ thuật phần mềm AI-native CMC với khóa học tích hợp AI của Stanford, MIT, Harvard, CMU, Berkeley, Coursera, Udacity, edX; kiểm tra nhất quán chuẩn đầu ra.")
