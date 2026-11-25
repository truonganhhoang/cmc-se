# -*- coding: utf-8 -*-
"""Trang riêng 'Hồ sơ ngành' (ho-so.html) + khối giới thiệu ngắn trên trang ngành.
Dữ liệu lấy từ kb.py. Chạy: python3 hoso.py  (thay cho python3 kb.py)
"""
import json, re
import kb
from kb import E, ROOT

F = kb.FAQ
assert len(F) == 25, "Cập nhật FAQ_GROUPS khi thêm/bớt câu hỏi"
FAQ_GROUPS = [
    ("tuyen-sinh", "Tuyển sinh, học phí", [0, 1, 2, 3, 20, 11, 12, 13, 19]),
    ("chuong-trinh", "Chương trình học", [4, 5, 6, 14, 15, 21, 22, 24]),
    ("ai", "Học với AI", [7, 17, 8]),
    ("nghe", "Nghề nghiệp, chọn ngành", [16, 18, 9, 10]),
    ("cuoc-thi", "Cuộc thi Săn Bug", [23]),
]
assert sorted(i for _, _, ids in FAQ_GROUPS for i in ids) == list(range(25))
POPULAR = [(2, "Điểm chuẩn"), (1, "Tổ hợp xét tuyển"), (11, "Học bổng"), (12, "Học phí"), (13, "Tặng iPad"),
           (5, "Học mấy năm"), (14, "Học những gì"), (7, "Học với AI có mất gốc"), (16, "Ra trường làm gì"), (9, "Không giỏi Tin")]
PERSONAS = [
    ("Học sinh", "Mình có vào được, có hợp không?", [("#tuyen-sinh", "Cách xét tuyển và tính điểm"), ("#faq-6", "Năm nhất đã làm ra phần mềm?"), ("#phu-hop", "Ngành này có hợp với mình?"), ("index.html#san-bug", "Chơi Săn Bug, nhận giải")]),
    ("Phụ huynh", "Học có đáng, ra trường có việc?", [("#faq-11", "Học bổng 30–100%"), ("#faq-5", "Vì sao chỉ học 3 năm"), ("#faq-7", "Học với AI có mất gốc?"), ("#nghe-nghiep", "Ra trường làm gì")]),
    ("Thầy cô, cố vấn", "Chương trình khác gì, căn cứ đâu?", [("ctdt/index.html", "Chương trình đào tạo chi tiết"), ("#so-sanh", "So với CS, AI, IT"), ("#vi-sao", "Vì sao phải đổi mới"), ("#nguon", "Nguồn tham khảo")]),
    ("Trợ lý AI", "Bản văn bản để trích dẫn", [("ky-thuat-phan-mem-cmc.md", "Hồ sơ dạng Markdown"), ("ctdt/ctdt.md", "Chương trình đào tạo (Markdown)"), ("llms.txt", "llms.txt"), ("#tro-ly-ai", "Ghi chú khi trả lời")]),
]
SECTIONS = [("thong-tin", "Thông tin nhanh"), ("tuyen-sinh", "Tuyển sinh, học bổng"), ("hoc-gi", "Học gì trong 3 năm"), ("hoc-voi-ai", "Học với AI thế nào"),
            ("nghe-nghiep", "Nghề nghiệp"), ("phu-hop", "Có hợp với bạn?"), ("vi-sao", "Vì sao đổi mới"), ("hoi-dap", "Hỏi đáp"), ("tro-ly-ai", "Cho trợ lý AI"), ("nguon", "Nguồn")]
FACT_GROUPS = [("Ngành và chương trình", range(0, 9)), ("Tuyển sinh (số liệu mùa 2026)", range(9, 18)), ("Địa điểm, liên hệ", range(18, len(kb.FACTS)))]
REGISTER = "https://xettuyen.cmcu.edu.vn"; TEST = "https://thituyen.cmcu.edu.vn"; TEL = "tel:02471029999"

def sec(id_, num, title, sub, inner):
    return (f'<section class="hs" id="{id_}" aria-labelledby="{id_}-h"><div class="hs-head"><span class="num">{num:02d}</span>'
            f'<h2 id="{id_}-h">{title}</h2>{f"<p>{sub}</p>" if sub else ""}</div>{inner}</section>')

def faq_item(i, inline=False):
    """inline=True: bản lặp lại trong một mục nội dung, không mang id để tránh trùng với mục Hỏi đáp."""
    q, a = F[i]
    if inline:
        return f'<details class="qa"><summary><span>{E(q)}</span></summary><div class="qa-b"><p>{E(a)}</p></div></details>'
    return (f'<details class="qa" id="faq-{i}"><summary><span>{E(q)}</span></summary>'
            f'<div class="qa-b"><p>{E(a)}</p><button type="button" class="cp" data-link="faq-{i}">Sao chép liên kết</button></div></details>')

def build_page():
    core, _ = kb.total_credits()
    # ---- hero
    chips = "".join(f'<a class="chip" href="#faq-{i}">{E(t)}</a>' for i, t in POPULAR)
    figs = [("3", "năm, 9 học kỳ × 10 tuần"), (str(core), "tín chỉ"), ("9", "sản phẩm khi ra trường"), ("SE", "mã xét tuyển · 7480103"), ("80", "chỉ tiêu mùa 2026"), ("25,3", "điểm trúng tuyển THPT 2026")]
    fig = "".join(f'<div class="fig"><b>{a}</b><span>{b}</span></div>' for a, b in figs)
    hero = f'''<div class="hero hs-hero"><span class="eyebrow">Hồ sơ ngành · cập nhật {kb.UPDATED}</span>
<h1>Ngành Kỹ thuật phần mềm CMC, <em>hỏi gì cũng có</em></h1>
<p class="lead">Mọi thông tin về ngành trên một trang: tuyển sinh, học bổng, học gì trong 3 năm, học với AI thế nào, ra trường làm gì. Gõ câu hỏi, hoặc chọn câu hay được hỏi.</p>
<form class="search" role="search" onsubmit="return false"><label for="hq" class="sr">Tìm trong hồ sơ ngành</label>
<svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="11" cy="11" r="7"/><path d="m20 20-4-4"/></svg>
<input id="hq" type="search" autocomplete="off" placeholder="Ví dụ: điểm chuẩn, học bổng, iPad, học mấy năm…"><button type="button" id="hq-x" class="hidden" aria-label="Xóa">×</button></form>
<div id="hres" class="hres" aria-live="polite"></div>
<div class="chips" aria-label="Câu hỏi hay gặp">{chips}</div>
<div class="figs">{fig}</div></div>'''
    pers = '<div class="persona">' + "".join(
        f'<div class="card"><span class="k">{E(t)}</span><h3>{E(q)}</h3><ul>' + "".join(f'<li><a href="{h}">{E(x)}</a></li>' for h, x in links) + "</ul></div>"
        for t, q, links in PERSONAS) + "</div>"
    # ---- 1 facts
    facts = '<div class="facts">' + "".join(
        f'<div class="fgrp"><h3>{E(g)}</h3><dl>' + "".join(f'<div><dt>{E(kb.FACTS[i][0])}</dt><dd>{E(kb.FACTS[i][1])}</dd></div>' for i in rng) + "</dl></div>"
        for g, rng in FACT_GROUPS) + f'</div><p class="note">{E(kb.NOTE)}</p>'
    # ---- 2 admission
    methods = '<div class="grid g2">' + "".join(f'<div class="card"><span class="k">PHƯƠNG THỨC {i+1}</span><h3>{E(t)}</h3><p>{E(d)}</p></div>' for i, (t, d) in enumerate(kb.ADMIT)) + "</div>"
    formula = f'''<div class="formula"><div><span class="k">CÁCH TÍNH ĐIỂM (thang 40)</span><p><b>{E(kb.SCORE_FORMULA.split(". ")[0])}.</b><br>{E(". ".join(kb.SCORE_FORMULA.split(". ")[1:]))}</p></div>
<a class="btn" href="index.html#tinh-diem">Tính điểm của bạn →</a></div>'''
    perks = '<div class="grid g3">' + "".join(f'<div class="card"><span class="k">{E(kb.FACTS[i][0]).upper()}</span><p>{E(kb.FACTS[i][1])}</p></div>' for i in (14, 15, 16)) + "</div>"
    cta = f'<div class="cta"><a class="btn" href="{REGISTER}">Đăng ký xét tuyển</a><a class="btn ghost" href="{TEST}">Đăng ký thi CMC-TEST</a><a class="btn ghost" href="{TEL}">Hotline 024 7102 9999</a></div>'
    adm = methods + formula + perks + '<h3 class="sub">Câu hỏi về tuyển sinh</h3>' + "".join(faq_item(i, True) for i in (2, 20, 12)) + cta
    # ---- 3 program
    tabs = '<div class="ytabs" role="tablist">' + "".join(
        f'<button type="button" role="tab" id="yt{y}" aria-controls="yp{y}" aria-selected="{"true" if y == 0 else "false"}">Năm {y+1}<small>{E(kb.YEARS[y][1])}</small></button>' for y in range(3)) + "</div>"
    panels = []
    for y in range(3):
        when, head, know, skill, resp, prod = kb.YEARS[y]
        sems = []
        for s in range(3 * y, 3 * y + 3):
            name, theme, cs, sp, ai = kb.SEMS[s]
            tc = sum(c for _, c, _ in cs)
            lis = "".join(f'<li><span>{E(re.sub(r"^[A-Z]{4}\d{4} ", "", n))}</span><b>{c}</b></li>' for n, c, _ in cs)
            sems.append(f'<div class="semc"><div class="h"><span>{E(name).upper()}</span><span>{tc} TC</span></div><div class="t">{E(theme.split(": ", 1)[-1])}</div>'
                        f'<p class="p"><b>Sản phẩm:</b> {E(sp)}</p><p class="ai"><b>AI:</b> {E(ai)}</p>'
                        f'<details><summary>{len(cs)} học phần</summary><ul>{lis}</ul></details></div>')
        panels.append(f'''<div class="ypanel" role="tabpanel" id="yp{y}" aria-labelledby="yt{y}" data-y="{y}">
<div class="yhead"><div><span class="k">{E(when)}</span><h3>{E(head)}</h3></div>
<dl><div><dt>Kiến thức</dt><dd>{E(know)}</dd></div><div><dt>Kỹ năng</dt><dd>{E(skill)}</dd></div><div><dt>Sản phẩm</dt><dd>{E(prod)}</dd></div></dl></div>
<div class="sems">{"".join(sems)}</div></div>''')
    tracks = '<h3 class="sub">Bốn hướng chuyên sâu (từ học kỳ 8)</h3><div class="grid g4">' + "".join(f'<div class="card"><h3>{E(t)}</h3><p>{E(c)}</p><p class="job">→ {E(j)}</p></div>' for t, c, j in kb.TRACKS["tracks"]) + "</div>"
    prog = tabs + "".join(panels) + tracks + '<p class="more"><a class="btn ghost" href="ctdt/index.html">Xem chương trình đào tạo chi tiết: chuẩn đầu ra, 43 học phần, kế hoạch 10 tuần →</a></p>'
    # ---- 4 AI
    prin = '<ol class="prin">' + "".join(f'<li><b>{E(t)}</b><span>{E(d)}</span></li>' for t, d in kb.PRINCIPLES) + "</ol>"
    lights = '<div class="lights">' + "".join(f'<div class="l{i}"><b>{E(t)}</b><p>{E(d)}</p></div>' for i, (t, d) in enumerate(kb.AI_POLICY)) + "</div>"
    assess = '<ul class="ticks">' + "".join(f"<li>{E(x)}</li>" for x in kb.ASSESS) + "</ul>"
    systems = '<div class="grid g3 sys">' + "".join(f'<div class="card"><h3>{E(t)}</h3><p>{E(d)}</p></div>' for t, d in kb.SYSTEMS) + f'</div><p class="small">{E(kb.SYSTEMS_NOTE)}</p>'
    ai = ('<h3 class="sub">Quy tắc dùng AI: xanh, vàng, đỏ</h3>' + lights + '<h3 class="sub">7 nguyên tắc của chương trình</h3>' + prin
          + '<h3 class="sub">Sinh viên được đánh giá thế nào</h3>' + assess + '<h3 class="sub">Hệ sinh thái học tập số</h3>' + systems + faq_item(7, True))
    # ---- 5 careers
    car = '<div class="grid g2 careers">' + "".join(f'<div class="card"><h3>{E(t)}</h3><p>{E(d)}</p></div>' for t, d in kb.CAREERS) + f'</div><p class="note"><b>Nơi làm việc:</b> {E(kb.WORKPLACES)}</p>' + faq_item(8, True)
    # ---- 6 fit
    fit = ('<div class="fit"><p class="k">ĐÁNH DẤU NHỮNG ĐIỀU ĐÚNG VỚI BẠN</p>' + "".join(f'<label><input type="checkbox"> <span>{E(x)}</span></label>' for x in kb.FIT)
           + f'<p id="fitr" class="fitr" aria-live="polite">Chọn để xem gợi ý.</p><p class="small">{E(kb.NOFIT)}</p><a class="btn ghost" href="index.html#trac-nghiem">Làm trắc nghiệm hướng nghiệp 1 phút →</a></div>')
    cmp_ = ('<h3 class="sub" id="so-sanh">So với các ngành gần</h3><div class="tw"><table><thead><tr><th>Ngành</th><th>Trọng tâm</th><th>Phù hợp nếu bạn</th></tr></thead><tbody>'
            + "".join(f'<tr{" class=me" if i == 0 else ""}><td><b>{E(t)}</b></td><td>{E(c)}</td><td>{E(f)}</td></tr>' for i, (t, c, f) in enumerate(kb.COMPARE)) + f'</tbody></table></div><p class="small">{E(kb.COMPARE_NOTE)}</p>')
    # ---- 7 why
    why = '<div class="grid g2">' + "".join(f'<div class="card"><span class="k">{i+1:02d}</span><h3>{E(t)}</h3><p>{E(d)}</p></div>' for i, (t, d) in enumerate(kb.WHY)) + "</div>"
    # ---- 8 FAQ
    gf = f'<div class="gchips" role="group" aria-label="Lọc câu hỏi"><button type="button" data-g="all" aria-pressed="true">Tất cả ({len(F)})</button>' + "".join(
        f'<button type="button" data-g="{g}" aria-pressed="false">{E(n)} ({len(ids)})</button>' for g, n, ids in FAQ_GROUPS) + "</div>"
    groups = "".join(f'<div class="fg" data-g="{g}"><h3 class="sub">{E(n)}</h3>' + "".join(faq_item(i) for i in ids) + "</div>" for g, n, ids in FAQ_GROUPS)
    faq = gf + '<div class="faqwrap">' + groups + f'</div><p class="note">Chưa thấy câu trả lời? Gọi hotline <a href="{TEL}">024 7102 9999</a> hoặc xem <a href="https://cmcu.edu.vn">cmcu.edu.vn</a>.</p>'
    # ---- 9 AI note, 10 sources
    ainote = ('<ul class="ticks">' + "".join(f"<li>{E(x)}</li>" for x in kb.AI_NOTE) + "</ul>"
              + '<div class="cta"><a class="btn ghost" href="ky-thuat-phan-mem-cmc.md">Hồ sơ ngành (.md)</a><a class="btn ghost" href="ctdt/ctdt.md">Chương trình đào tạo (.md)</a><a class="btn ghost" href="llms.txt">llms.txt</a></div>')
    src = '<ol class="src">' + "".join(f'<li><a href="{E(u)}">{E(t)}</a></li>' for t, u in kb.SOURCES) + "</ol>"

    body = [sec("thong-tin", 1, "Thông tin nhanh", "", facts),
            sec("tuyen-sinh", 2, "Tuyển sinh, học bổng", "Số liệu mùa tuyển sinh 2026 để tham khảo; mùa 2027 theo đề án chính thức của Trường.", adm),
            sec("hoc-gi", 3, "Học gì trong 3 năm", "Mỗi năm 3 học kỳ, mỗi học kỳ 10 tuần và một sản phẩm. Chọn năm để xem.", prog),
            sec("hoc-voi-ai", 4, "Học với AI thế nào", "Học cùng AI, nhưng vẫn thi nền tảng không AI và phải giải thích được mọi dòng code mình nộp.", ai),
            sec("nghe-nghiep", 5, "Nghề nghiệp khi ra trường", "Lứa tuyển sinh 2027 ra trường khoảng năm 2030.", car),
            sec("phu-hop", 6, "Ngành này có hợp với bạn?", "", fit + cmp_),
            sec("vi-sao", 7, "Vì sao chương trình đổi mới", "Những gì dữ liệu ngành phần mềm đang cho thấy.", why),
            sec("hoi-dap", 8, "Hỏi đáp", f"{len(F)} câu hỏi học sinh và phụ huynh hay hỏi.", faq),
            sec("tro-ly-ai", 9, "Ghi chú cho trợ lý AI và chatbot", "Dành cho ChatGPT, Gemini, Copilot… khi trả lời về ngành.", ainote),
            sec("nguon", 10, "Nguồn tham khảo", "", src)]
    toc = '<nav class="toc" aria-label="Mục lục hồ sơ"><b>Mục lục</b>' + "".join(f'<a href="#{i}" data-s="{i}"><span>{n+1:02d}</span>{E(t)}</a>' for n, (i, t) in enumerate(SECTIONS)) + "</nav>"

    # search index
    idx = [dict(t=q, s=a, h=f"#faq-{i}", k="Hỏi đáp") for i, (q, a) in enumerate(F)]
    idx += [dict(t=k, s=v, h="#thong-tin", k="Thông tin") for k, v in kb.FACTS]
    idx += [dict(t=t, s=d, h="#tuyen-sinh", k="Tuyển sinh") for t, d in kb.ADMIT]
    idx += [dict(t=t, s=d, h="#nghe-nghiep", k="Nghề nghiệp") for t, d in kb.CAREERS]
    idx += [dict(t=t, s=d, h="#hoc-voi-ai", k="Học với AI") for t, d in kb.SYSTEMS + kb.AI_POLICY + kb.PRINCIPLES]
    idx += [dict(t=t, s=c + " Việc làm: " + j, h="#hoc-gi", k="Chuyên sâu") for t, c, j in kb.TRACKS["tracks"]]
    for s, (name, theme, cs, sp, ai_) in enumerate(kb.SEMS):
        idx.append(dict(t=f"{name}: {theme.split(': ', 1)[-1]}", s="Sản phẩm: " + sp + ". Học phần: " + ", ".join(re.sub(r"^[A-Z]{4}\d{4} ", "", n) for n, _, _ in cs), h=f"#hoc-gi", k="Học gì", y=s // 3))
    idx += [dict(t=t, s=d, h="#vi-sao", k="Vì sao đổi mới") for t, d in kb.WHY]
    idx_js = json.dumps(idx, ensure_ascii=False).replace("</", "<\\/")

    ld = kb.build_jsonld()
    return f"""<!DOCTYPE html>
<html lang="vi">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Hồ sơ ngành Kỹ thuật phần mềm – Trường Đại học CMC: tuyển sinh, học bổng, chương trình 3 năm</title>
<meta name="description" content="Mọi thông tin về ngành Kỹ thuật phần mềm (SE) Trường Đại học CMC: tổ hợp Toán ×2, điểm chuẩn 2026, học bổng 30–100%, học 3 năm 9 học kỳ, {core} tín chỉ, học cùng AI, 9 sản phẩm, nghề nghiệp, hỏi đáp.">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,700;12..96,800&family=Be+Vietnam+Pro:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500;600;700&display=swap&subset=vietnamese" rel="stylesheet">
<link rel="stylesheet" href="ctdt/style.css">
<style>{CSS}</style>
{ld}
</head>
<body>
<a class="skip" href="#noi-dung">Bỏ qua đến nội dung</a>
<header class="top"><div class="wrap">
  <a class="brand" href="index.html"><i>SE</i><span>Kỹ thuật phần mềm<small>Trường Đại học CMC</small></span></a>
  <nav class="nav" aria-label="Điều hướng chính"><a href="index.html">Trang ngành</a><a href="ho-so.html" aria-current="page">Hồ sơ ngành</a><a href="ctdt/index.html">Chương trình đào tạo</a><a href="{REGISTER}">Đăng ký xét tuyển ↗</a></nav>
</div></header>
<main class="wrap" id="noi-dung">
{hero}
{pers}
<div class="layout">{toc}<div class="content">{"".join(body)}</div></div>
</main>
<a href="#noi-dung" class="totop" aria-label="Lên đầu trang">↑</a>
<div id="toast" class="toast" role="status"></div>
<footer><div class="wrap">
  <div><b>Ngành Kỹ thuật phần mềm (Software Engineering) – Trường Đại học CMC</b> · Mã xét tuyển SE · Hotline 024 7102 9999</div>
  <div>{E(kb.NOTE)} Cập nhật {kb.UPDATED}.</div>
</div></footer>
<script>window.HS_INDEX={idx_js};</script>
<script>{JS}</script>
</body>
</html>"""

CSS = r"""
.sr,.skip:not(:focus){position:absolute;width:1px;height:1px;overflow:hidden;clip:rect(0 0 0 0);white-space:nowrap}
.skip:focus{position:fixed;top:8px;left:8px;z-index:50;background:var(--accent);color:#0A1433;padding:8px 12px;border-radius:8px}
html{scroll-behavior:smooth;scroll-padding-top:76px}
.hs-hero{padding-bottom:10px}
.search{position:relative;display:flex;align-items:center;max-width:720px;margin-top:22px}
.search svg{position:absolute;left:18px;width:22px;height:22px;fill:none;stroke:var(--muted);stroke-width:2.2;stroke-linecap:round}
.search input{width:100%;font:500 18px/1.2 var(--f-body);padding:17px 50px 17px 52px;border-radius:16px;border:2px solid var(--line);background:var(--card);color:var(--ink);box-shadow:0 6px 22px rgba(10,20,51,.07)}
.search input:focus{outline:none;border-color:var(--accent)}
.search button{position:absolute;right:10px;border:0;background:var(--bg);color:var(--muted);width:32px;height:32px;border-radius:50%;font-size:20px;cursor:pointer}
.hres{max-width:720px;display:flex;flex-direction:column;gap:6px;margin-top:8px}
.hres:empty{display:none}
.hres a{display:block;text-decoration:none;color:inherit;background:var(--card);border:1px solid var(--line);border-radius:12px;padding:10px 14px}
.hres a:hover,.hres a:focus-visible{border-color:var(--accent)}
.hres a small{font:600 11px/1 var(--f-mono);color:var(--cyan);text-transform:uppercase;letter-spacing:.04em}
.hres a b{display:block;margin:4px 0 2px;font-size:15.5px}
.hres a span{font-size:14px;color:var(--muted);display:-webkit-box;-webkit-line-clamp:2;-webkit-box-orient:vertical;overflow:hidden}
.hres mark{background:var(--accent-bg);color:inherit;border-radius:3px;padding:0 1px}
.hres .none{font-size:14.5px;color:var(--muted);padding:6px 2px}
.chips{display:flex;flex-wrap:wrap;gap:8px;margin-top:16px;max-width:900px}
.chip{text-decoration:none;color:var(--ink);background:var(--card);border:1px solid var(--line);border-radius:999px;padding:7px 13px;font-size:14px;font-weight:500}
.chip:hover{border-color:var(--accent);color:var(--accent)}
.persona{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:12px;margin:22px 0 8px}
@media (max-width:980px){.persona{grid-template-columns:repeat(2,minmax(0,1fr))}}
@media (max-width:520px){.persona{grid-template-columns:1fr}}
.persona h3{font-size:17px;margin-bottom:8px}
.persona ul{list-style:none;margin:0;padding:0;display:flex;flex-direction:column;gap:5px;font-size:14.5px}
.persona li a{text-decoration:none}
.persona li a::before{content:"→ ";color:var(--accent)}
.persona li a:hover{text-decoration:underline}
.layout{display:grid;grid-template-columns:220px minmax(0,1fr);gap:40px;align-items:start;margin-top:16px}
.toc{position:sticky;top:76px;display:flex;flex-direction:column;gap:1px;padding:4px 0}
.toc b{font:600 12px/1 var(--f-mono);color:var(--muted);margin:0 0 10px 10px}
.toc a{display:flex;gap:10px;padding:7px 10px;border-radius:8px;text-decoration:none;color:var(--muted);font-size:14.5px;border-left:3px solid transparent}
.toc a span{font:500 11.5px/1.9 var(--f-mono);opacity:.7}
.toc a:hover{color:var(--ink);background:var(--card)}
.toc a.on{color:var(--ink);font-weight:600;background:var(--card);border-left-color:var(--accent)}
@media (max-width:980px){
  .layout{grid-template-columns:1fr;gap:0}
  .toc{top:0;z-index:5;flex-direction:row;overflow-x:auto;gap:6px;background:var(--bg);padding:10px 0;margin:0 -20px;padding-left:20px;padding-right:20px;border-bottom:1px solid var(--line);scrollbar-width:none}
  .toc::-webkit-scrollbar{display:none}
  .toc b{display:none}
  .toc a{flex:none;border:1px solid var(--line);border-radius:999px;padding:6px 12px;background:var(--card);font-size:13.5px}
  .toc a span{display:none}
  .toc a.on{border-color:var(--accent);background:var(--accent-bg)}
  html{scroll-padding-top:64px}
}
.hs{padding:34px 0 30px;border-top:1px solid var(--line)}
.hs:first-child{border-top:0;padding-top:8px}
.hs-head{display:grid;grid-template-columns:auto 1fr;column-gap:14px;align-items:baseline;margin-bottom:18px}
.hs-head .num{font:700 14px/1 var(--f-mono);color:var(--accent)}
.hs-head h2{font-size:clamp(24px,3vw,32px)}
.hs-head p{grid-column:2;margin:6px 0 0;color:var(--muted)}
h3.sub{font-size:18px;margin:26px 0 12px}
.small{font-size:13.5px;color:var(--muted)}
.btn{display:inline-flex;align-items:center;gap:6px;padding:11px 18px;border-radius:11px;background:var(--accent);color:#fff;font-weight:700;text-decoration:none;font-size:15px;border:2px solid var(--accent)}
@media (prefers-color-scheme:dark){:root:not([data-theme="light"]) .btn{color:#0A1433}}
.btn.ghost{background:transparent;color:var(--ink);border-color:var(--line)}
.btn:hover{filter:brightness(1.05)} .btn.ghost:hover{border-color:var(--accent)}
.cta{display:flex;flex-wrap:wrap;gap:10px;margin-top:18px}
.more{margin:18px 0 0;max-width:none}
.facts{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:14px}
@media (max-width:1100px){.facts{grid-template-columns:1fr}}
.fgrp{background:var(--card);border:1px solid var(--line);border-radius:14px;padding:16px 18px}
.fgrp h3{font-size:15px;font-family:var(--f-mono);color:var(--cyan);letter-spacing:0;margin-bottom:6px}
.fgrp dl{margin:0}
.fgrp dl div{padding:9px 0;border-bottom:1px dashed var(--line)}
.fgrp dl div:last-child{border-bottom:0}
.fgrp dt{font-size:12.5px;color:var(--muted)}
.fgrp dd{margin:2px 0 0;font-size:14.5px;font-weight:500}
.formula{display:flex;flex-wrap:wrap;gap:16px;align-items:center;justify-content:space-between;background:var(--navy);color:#EEF0F7;border-radius:14px;padding:18px 20px;margin:14px 0}
.formula .k{font:600 12px/1 var(--f-mono);color:#FFB547}
.formula p{margin:6px 0 0;color:#C6CCE2;font-size:15px}
.formula p b{color:#fff;font-size:17px}
.formula .btn{background:#FFB547;border-color:#FFB547;color:#0A1433}
.qa{background:var(--card);border:1px solid var(--line);border-radius:12px;margin-bottom:8px;scroll-margin-top:90px}
.qa summary{list-style:none;cursor:pointer;padding:14px 46px 14px 16px;font-weight:600;position:relative;font-size:15.5px}
.qa summary::-webkit-details-marker{display:none}
.qa summary::after{content:"+";position:absolute;right:16px;top:50%;transform:translateY(-50%);font:600 22px/1 var(--f-mono);color:var(--accent)}
.qa[open] summary::after{content:"–"}
.qa[open]{border-color:var(--accent)}
.qa-b{padding:0 16px 14px}
.qa-b p{margin:0;font-size:15px}
.qa .cp{margin-top:10px;border:0;background:none;color:var(--muted);font:500 12px/1 var(--f-mono);cursor:pointer;padding:0;text-decoration:underline}
.qa.flash{box-shadow:0 0 0 4px var(--accent-bg)}
.ytabs{display:grid;grid-template-columns:repeat(3,1fr);gap:8px;margin-bottom:14px}
.ytabs button{text-align:left;border:1px solid var(--line);background:var(--card);color:var(--ink);border-radius:12px;padding:12px 14px;cursor:pointer;font:700 18px/1.2 var(--f-display)}
.ytabs button small{display:block;font:400 13px/1.35 var(--f-body);color:var(--muted);margin-top:4px}
.ytabs button[aria-selected="true"]{background:var(--navy);color:#fff;border-color:var(--navy)}
.ytabs button[aria-selected="true"] small{color:#C6CCE2}
@media (max-width:640px){.ytabs button small{display:none}}
.js .ypanel:not(.on){display:none}
.ypanel{margin-bottom:10px}
.no-js .ypanel{margin-bottom:26px}
.yhead{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,2fr);gap:18px;background:var(--card);border:1px solid var(--line);border-radius:14px;padding:16px 18px;margin-bottom:10px}
@media (max-width:800px){.yhead{grid-template-columns:1fr}}
.yhead .k{font:600 12px/1 var(--f-mono);color:var(--cyan)}
.yhead h3{font-size:20px;margin-top:6px}
.yhead dl{margin:0;display:flex;flex-direction:column;gap:8px}
.yhead dt{font:600 11.5px/1 var(--f-mono);color:var(--muted);text-transform:uppercase}
.yhead dd{margin:3px 0 0;font-size:14.5px}
.sems{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:10px}
@media (max-width:900px){.sems{grid-template-columns:1fr}}
.semc{background:var(--card);border:1px solid var(--line);border-radius:14px;padding:14px 16px;display:flex;flex-direction:column;gap:6px}
.semc .h{display:flex;justify-content:space-between;font:600 12px/1 var(--f-mono);color:var(--muted)}
.semc .t{font:700 17px/1.25 var(--f-display);color:var(--accent)}
.semc p{margin:0;font-size:14px}
.semc .ai{color:var(--muted)}
.semc details{margin-top:auto;border-top:1px dashed var(--line);padding-top:8px}
.semc summary{cursor:pointer;font:600 13px/1.4 var(--f-mono);color:var(--cyan)}
.semc ul{list-style:none;margin:8px 0 0;padding:0;font-size:13.5px}
.semc li{display:flex;justify-content:space-between;gap:10px;padding:3px 0}
.semc li b{font-family:var(--f-mono);font-weight:600;color:var(--muted)}
.job{margin-top:8px!important;color:var(--ink)!important;font-weight:500}
.lights{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:10px}
@media (max-width:800px){.lights{grid-template-columns:1fr}}
.lights div{background:var(--card);border:1px solid var(--line);border-radius:12px;padding:14px 16px;border-top:5px solid}
.lights .l0{border-top-color:#2E7D4F}.lights .l1{border-top-color:#D98E04}.lights .l2{border-top-color:#C44536}
.lights p{margin:6px 0 0;font-size:14.5px;color:var(--muted)}
.prin{counter-reset:p;list-style:none;margin:0;padding:0;display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:10px}
@media (max-width:700px){.prin{grid-template-columns:1fr}}
.prin li{counter-increment:p;background:var(--card);border:1px solid var(--line);border-radius:12px;padding:12px 14px 12px 48px;position:relative;font-size:14.5px}
.prin li::before{content:counter(p);position:absolute;left:14px;top:12px;width:24px;height:24px;border-radius:50%;background:var(--accent-bg);color:var(--accent);font:700 13px/24px var(--f-mono);text-align:center}
.prin b{display:block}
.prin span{color:var(--muted)}
.ticks{list-style:none;margin:0;padding:0;display:flex;flex-direction:column;gap:8px;max-width:80ch}
.ticks li{padding-left:28px;position:relative}
.ticks li::before{content:"✓";position:absolute;left:4px;color:var(--accent);font-weight:700}
.careers .card{padding:12px 16px}
.careers h3{font-size:16px}
.fit{background:var(--card);border:1px solid var(--line);border-radius:14px;padding:18px 20px;display:flex;flex-direction:column;gap:8px;max-width:820px}
.fit .k{font:600 12px/1 var(--f-mono);color:var(--cyan);margin:0 0 4px}
.fit label{display:flex;gap:12px;align-items:flex-start;padding:10px 12px;border:1px solid var(--line);border-radius:10px;cursor:pointer;font-size:15px}
.fit label:has(input:checked){border-color:var(--accent);background:var(--accent-bg)}
.fit input{width:20px;height:20px;accent-color:var(--accent);margin:1px 0 0;flex:none}
.fitr{font-weight:600;margin:6px 0 0}
.fit .btn{align-self:flex-start}
tr.me td{background:var(--accent-bg)}
.gchips{display:flex;flex-wrap:wrap;gap:6px;margin-bottom:6px}
.gchips button{border:1px solid var(--line);background:var(--card);color:var(--ink);border-radius:999px;padding:7px 13px;font:500 13.5px/1 var(--f-body);cursor:pointer}
.gchips button[aria-pressed="true"]{background:var(--ink);color:var(--bg);border-color:var(--ink)}
.fg.hide{display:none}
.src{font-size:14px;padding-left:22px;display:flex;flex-direction:column;gap:4px}
.totop{position:fixed;right:18px;bottom:18px;width:44px;height:44px;border-radius:50%;background:var(--navy);color:#fff;display:grid;place-items:center;text-decoration:none;font-size:20px;opacity:0;pointer-events:none;transition:opacity .2s;box-shadow:0 6px 18px rgba(0,0,0,.2)}
.totop.show{opacity:1;pointer-events:auto}
.toast{position:fixed;left:50%;bottom:24px;transform:translateX(-50%);background:var(--navy);color:#fff;padding:10px 16px;border-radius:10px;font-size:14px;opacity:0;transition:opacity .2s;pointer-events:none}
.toast.on{opacity:1}
@media print{.top,.toc,.search,.hres,.chips,.persona,.totop,.gchips,.ytabs,.cp,.cta{display:none!important}.js .ypanel{display:block!important}.qa .qa-b{display:block}.layout{display:block}}
"""

JS = r"""
(function(){
  document.documentElement.classList.add('js');
  var $=function(s,r){return (r||document).querySelector(s)}, $$=function(s,r){return Array.prototype.slice.call((r||document).querySelectorAll(s))};
  function norm(s){return (s||'').normalize('NFD').replace(/[̀-ͯ]/g,'').replace(/đ/g,'d').replace(/Đ/g,'D').toLowerCase()}
  function esc(s){return s.replace(/[&<>"]/g,function(c){return {'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]})}
  var toastT; function toast(m){var t=$('#toast'); t.textContent=m; t.classList.add('on'); clearTimeout(toastT); toastT=setTimeout(function(){t.classList.remove('on')},1800)}

  /* ---- year tabs ---- */
  var tabs=$$('.ytabs button'), panels=$$('.ypanel');
  function showYear(y){tabs.forEach(function(b,i){b.setAttribute('aria-selected',i===y)}); panels.forEach(function(p,i){p.classList.toggle('on',i===y)})}
  tabs.forEach(function(b,i){b.addEventListener('click',function(){showYear(i)}); b.addEventListener('keydown',function(e){
    if(e.key==='ArrowRight'||e.key==='ArrowLeft'){var n=(i+(e.key==='ArrowRight'?1:2))%3; showYear(n); tabs[n].focus()}})});
  showYear(0);

  /* ---- open & highlight a target ---- */
  function go(id,y){
    var el=document.getElementById(id); if(!el) return;
    if(typeof y==='number') showYear(y);
    var fg=el.closest('.fg'); if(fg&&fg.classList.contains('hide')) setGroup('all');
    if(el.tagName==='DETAILS'){el.open=true; el.classList.add('flash'); setTimeout(function(){el.classList.remove('flash')},1600)}
    el.scrollIntoView({block:'start'});
  }

  /* ---- search ---- */
  var IDX=(window.HS_INDEX||[]).map(function(d){d.n=norm(d.t+' '+d.s); d.nt=norm(d.t); return d});
  var q=$('#hq'), res=$('#hres'), x=$('#hq-x');
  function hl(text,toks){var out=esc(text); toks.forEach(function(t){ if(t.length<2) return;
      var nt=norm(text), i=nt.indexOf(t); if(i<0) return; var orig=text.substr(i,t.length); out=out.split(esc(orig)).join('<mark>'+esc(orig)+'</mark>')}); return out}
  function search(){
    var v=q.value.trim(); x.classList.toggle('hidden',!v);
    if(!v){res.innerHTML='';return}
    var toks=norm(v).split(/\s+/).filter(Boolean);
    var hits=IDX.map(function(d){var sc=0; for(var i=0;i<toks.length;i++){ if(d.n.indexOf(toks[i])<0) return null; if(d.nt.indexOf(toks[i])>=0) sc+=3; else sc+=1 }
        if(d.k==='Hỏi đáp') sc+=2; return {d:d,sc:sc}}).filter(Boolean).sort(function(a,b){return b.sc-a.sc}).slice(0,6);
    if(!hits.length){res.innerHTML='<div class="none">Chưa tìm thấy. Thử từ khóa ngắn hơn (ví dụ “học phí”, “AI”), xem <a href="#hoi-dap">mục Hỏi đáp</a> hoặc gọi 024 7102 9999.</div>'; return}
    res.innerHTML=hits.map(function(h){var d=h.d; return '<a href="'+d.h+'"'+(typeof d.y==='number'?' data-y="'+d.y+'"':'')+'><small>'+esc(d.k)+'</small><b>'+hl(d.t,toks)+'</b><span>'+hl(d.s,toks)+'</span></a>'}).join('');
  }
  q.addEventListener('input',search);
  q.addEventListener('keydown',function(e){ if(e.key==='Enter'){var a=$('a',res); if(a){e.preventDefault(); a.click()}} if(e.key==='Escape'){q.value='';search()} });
  x.addEventListener('click',function(){q.value='';search();q.focus()});

  /* ---- intercept in-page links ---- */
  document.addEventListener('click',function(e){
    var a=e.target.closest('a[href^="#"]'); if(!a) return;
    var id=a.getAttribute('href').slice(1); if(!id||!document.getElementById(id)) return;
    e.preventDefault(); go(id, a.dataset.y?+a.dataset.y:undefined);
    try{history.replaceState(null,'','#'+id)}catch(_){}
  });

  /* ---- FAQ groups ---- */
  var gb=$$('.gchips button'), fgs=$$('.fg');
  function setGroup(g){gb.forEach(function(b){b.setAttribute('aria-pressed',b.dataset.g===g)}); fgs.forEach(function(f){f.classList.toggle('hide',g!=='all'&&f.dataset.g!==g)})}
  gb.forEach(function(b){b.addEventListener('click',function(){setGroup(b.dataset.g)})});

  /* ---- copy link ---- */
  $$('.qa .cp').forEach(function(b){b.addEventListener('click',function(){
    var u=location.href.split('#')[0]+'#'+b.dataset.link;
    var ok=function(){toast('Đã sao chép liên kết câu hỏi')}, fail=function(){try{history.replaceState(null,'','#'+b.dataset.link)}catch(_){} toast('Liên kết đã hiện trên thanh địa chỉ')};
    if(navigator.clipboard&&navigator.clipboard.writeText) navigator.clipboard.writeText(u).then(ok,fail); else fail();
  })});

  /* ---- fit checklist ---- */
  var fit=$$('.fit input'), fr=$('#fitr');
  fit.forEach(function(c){c.addEventListener('change',function(){var n=fit.filter(function(x){return x.checked}).length;
    fr.textContent=['Chọn để xem gợi ý.','Có 1 điểm hợp. Hãy thử làm một trang web nhỏ hoặc học Python miễn phí để xem mình có thích không.','Khá hợp. Ngành sẽ giúp bạn biến sở thích đó thành sản phẩm thật.','Rất hợp với Kỹ thuật phần mềm.','Đúng chất kỹ sư phần mềm. Hẹn gặp bạn ở học kỳ 1!'][n]})});

  /* ---- scrollspy + to top ---- */
  var links=$$('.toc a'), secs=links.map(function(a){return document.getElementById(a.dataset.s)}), top=$('.totop'), tocEl=$('.toc');
  function spy(){var y=window.scrollY+innerHeight*0.35, cur=0; secs.forEach(function(s,i){ if(s&&s.offsetTop<=y) cur=i });
    links.forEach(function(a,i){var on=i===cur&&window.scrollY>secs[0].offsetTop-200; if(on!==a.classList.contains('on')){a.classList.toggle('on',on); if(on&&tocEl.scrollWidth>tocEl.clientWidth) tocEl.scrollTo({left:a.offsetLeft-20,behavior:'smooth'})}});
    top.classList.toggle('show',window.scrollY>900)}
  var tk=false; window.addEventListener('scroll',function(){ if(!tk){tk=true; requestAnimationFrame(function(){spy();tk=false})} },{passive:true}); spy();

  /* ---- hash on load: #faq-3 or #q=... ---- */
  function fromHash(){var h=decodeURIComponent(location.hash.slice(1)); if(!h) return;
    if(h.indexOf('q=')===0){q.value=h.slice(2); search(); q.focus(); q.scrollIntoView({block:'center'}); return}
    go(h)}
  fromHash(); window.addEventListener('hashchange',fromHash);
})();
"""

def build_teaser():
    core, _ = kb.total_credits()
    chips = "".join(f'<a class="hs-chip" href="ho-so.html#faq-{i}">{E(t)}</a>' for i, t in POPULAR[:8])
    facts = "".join(f'<li><span>{E(k)}</span><b>{E(v)}</b></li>' for k, v in [
        ("Mã xét tuyển", "SE · mã ngành 7480103"), ("Thời gian", f"3 năm · 9 học kỳ × 10 tuần · {core} tín chỉ"),
        ("Tổ hợp (2026)", "Toán ×2 + 2 môn bất kỳ, thang 40"), ("Điểm trúng tuyển 2026", "25,3 (THPT) · 28,36 (học bạ)"),
        ("Học bổng (2026)", "30% – 100% học phí toàn khóa"), ("Hotline", "024 7102 9999")])
    return f'''<section id="ho-so"><div class="wrap">
<div class="sec-head"><span class="eyebrow">// hồ sơ ngành</span><h2>Hỏi gì về ngành cũng có câu trả lời</h2>
<p>Tuyển sinh, học bổng, học gì trong 3 năm, học với AI thế nào, ra trường làm gì và {len(F)} câu hỏi hay gặp, gom trên một trang riêng dễ tra cứu.</p></div>
<div class="hs-teaser">
  <div>
    <form class="hs-search" role="search" onsubmit="var v=this.q.value.trim();location.href='ho-so.html'+(v?'#q='+encodeURIComponent(v):'');return false">
      <label for="hs-q" class="sr-only" style="position:absolute;width:1px;height:1px;overflow:hidden;clip:rect(0 0 0 0)">Tìm trong hồ sơ ngành</label>
      <input id="hs-q" name="q" type="search" placeholder="Gõ câu hỏi: học phí, điểm chuẩn, iPad…"><button type="submit">Tìm</button>
    </form>
    <div class="hs-chips">{chips}</div>
    <a class="hs-open" href="ho-so.html">Mở hồ sơ ngành đầy đủ →</a>
  </div>
  <ul class="hs-facts">{facts}</ul>
</div>
<style>
.hs-teaser{{display:grid;grid-template-columns:minmax(0,1.2fr) minmax(0,1fr);gap:24px;align-items:start}}
@media (max-width:860px){{.hs-teaser{{grid-template-columns:1fr}}}}
.hs-search{{display:flex;gap:8px}}
.hs-search input{{flex:1;min-width:0;padding:15px 16px;border-radius:12px;border:1px solid var(--line);background:var(--ink-2);color:var(--paper);font-size:17px}}
.hs-search input:focus{{outline:none;border-color:var(--amber)}}
.hs-search button{{padding:0 20px;border-radius:12px;border:0;background:var(--amber);color:var(--ink);font-weight:700;cursor:pointer}}
.hs-chips{{display:flex;flex-wrap:wrap;gap:8px;margin:14px 0 18px}}
.hs-chip{{padding:7px 12px;border-radius:999px;border:1px solid var(--line);color:var(--paper);text-decoration:none;font-size:14px}}
.hs-chip:hover{{border-color:var(--amber);color:var(--amber)}}
.hs-open{{display:inline-block;padding:12px 18px;border-radius:12px;background:var(--amber);color:var(--ink);font-weight:700;text-decoration:none}}
.hs-facts{{list-style:none;margin:0;padding:6px 18px;border:1px solid var(--line);border-radius:14px;background:var(--ink-2)}}
.hs-facts li{{display:flex;flex-direction:column;gap:2px;padding:10px 0;border-bottom:1px dashed var(--line)}}
.hs-facts li:last-child{{border-bottom:0}}
.hs-facts span{{font:500 12px/1.2 var(--f-mono);color:var(--muted)}}
.hs-facts b{{font-weight:600;font-size:15.5px}}
</style>
</div></section>'''

def run():
    p = ROOT / "index.html"
    s = p.read_text(encoding="utf-8")
    s = re.sub(r"<!--KB-START-->.*?<!--KB-END-->", lambda m: "<!--KB-START-->\n" + build_teaser() + "\n<!--KB-END-->", s, flags=re.S)
    prog_ld = kb.build_jsonld().split("\n")[0]  # trang ngành: chỉ giữ EducationalOccupationalProgram; FAQPage nằm ở ho-so.html
    s = re.sub(r"<!--LD-START-->.*?<!--LD-END-->", lambda m: "<!--LD-START-->\n" + prog_ld + "\n<!--LD-END-->", s, flags=re.S)
    s = s.replace('<a href="#ho-so">Hồ sơ ngành</a>', '<a href="ho-so.html">Hồ sơ ngành</a>')
    p.write_text(s, encoding="utf-8")
    (ROOT / "ho-so.html").write_text(build_page(), encoding="utf-8")
    md = kb.build_md().replace("ctdt/index.html và ctdt/ctdt.md", "ctdt/index.html và ctdt/ctdt.md; trang hồ sơ: ho-so.html")
    (ROOT / "ky-thuat-phan-mem-cmc.md").write_text(md, encoding="utf-8")
    ll = kb.build_llms().replace("- [Trang giới thiệu tương tác]", "- [Hồ sơ ngành (trang web)](/ky-thuat-phan-mem/ho-so.html): tra cứu tuyển sinh, học bổng, chương trình, hỏi đáp\n- [Trang giới thiệu tương tác]")
    (ROOT / "llms.txt").write_text(ll, encoding="utf-8")
    print("ok: ho-so.html, teaser, md, llms")

if __name__ == "__main__":
    run()
