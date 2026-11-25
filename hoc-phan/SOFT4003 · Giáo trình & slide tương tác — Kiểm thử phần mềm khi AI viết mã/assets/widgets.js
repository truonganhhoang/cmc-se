/* SOFT4003 – thư viện hoạt động tương tác.
   Mỗi hoạt động: <div class="w" data-w="loai"><script type="application/json">{cấu hình}</script></div>
   W.mount(root) dựng tất cả hoạt động chưa dựng trong root. Kết quả lưu localStorage (bọc try/catch). */
(function () {
  "use strict";
  var W = (window.W = {});
  var NS = "s4003:";
  var LS = (W.LS = {
    get: function (k, d) { try { var v = localStorage.getItem(NS + k); return v == null ? d : JSON.parse(v); } catch (e) { return d; } },
    set: function (k, v) { try { localStorage.setItem(NS + k, JSON.stringify(v)); } catch (e) {} },
  });
  var REG = {};
  W.def = function (n, f) { REG[n] = f; };

  function h(tag, attrs) {
    var el = document.createElement(tag);
    if (attrs) for (var k in attrs) {
      var v = attrs[k]; if (v == null || v === false) continue;
      if (k === "html") el.innerHTML = v; else if (k === "text") el.textContent = v;
      else if (k.slice(0, 2) === "on") el.addEventListener(k.slice(2), v); else el.setAttribute(k, v === true ? "" : v);
    }
    for (var i = 2; i < arguments.length; i++) { var c = arguments[i]; if (c == null) continue; el.append(c.nodeType ? c : document.createTextNode(c)); }
    return el;
  }
  W.h = h;
  function esc(s) { return String(s).replace(/[&<>"]/g, function (c) { return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]; }); }
  W.esc = esc;
  function norm(s) { return String(s).normalize("NFD").replace(/[̀-ͯ]/g, "").replace(/đ/g, "d").toLowerCase().replace(/\s+/g, " ").trim(); }
  function shuffled(a, seed) {
    var r = a.slice(), s = seed || 7;
    for (var i = r.length - 1; i > 0; i--) { s = (s * 9301 + 49297) % 233280; var j = Math.floor((s / 233280) * (i + 1)); var t = r[i]; r[i] = r[j]; r[j] = t; }
    return r;
  }
  function copyText(text, btn) {
    var done = function () { if (btn) { var o = btn.textContent; btn.textContent = "Đã sao chép"; setTimeout(function () { btn.textContent = o; }, 1500); } };
    if (navigator.clipboard && navigator.clipboard.writeText) navigator.clipboard.writeText(text).then(done, fallback); else fallback();
    function fallback() { var t = h("textarea", { style: "position:fixed;opacity:0" }); t.value = text; document.body.append(t); t.select(); try { document.execCommand("copy"); done(); } catch (e) {} t.remove(); }
  }
  W.copy = copyText;
  W.done = function (id, s, m) {
    if (!id) return; var prev = LS.get("w:" + id, null);
    var rec = { s: s, m: m, best: Math.max(s, prev ? prev.best || 0 : 0), t: Date.now() };
    LS.set("w:" + id, rec);
    document.dispatchEvent(new CustomEvent("w-done", { detail: { id: id, rec: rec } }));
  };
  var LABEL = { quiz: "Trắc nghiệm", flash: "Thẻ ghi nhớ", order: "Sắp xếp", match: "Ghép cặp", classify: "Phân loại", spot: "Tìm lỗi",
    fill: "Tính và điền", bva: "Phòng lab giá trị biên", dtable: "Bảng quyết định", state: "Chuyển trạng thái", lab: "Phòng lab mã",
    prompt: "Prompt lab", locator: "Locator Playwright", risk: "Ma trận rủi ro", pert: "Ước lượng 3 điểm", form: "Biểu mẫu", poll: "Bình chọn", timer: "Hoạt động" };

  function shell(el, c, type) {
    el.innerHTML = "";
    var head = h("div", { class: "w-head" }, h("span", { class: "w-badge" }, c.badge || LABEL[type] || type), h("span", { class: "w-title", html: c.title || "" }));
    var body = h("div", { class: "w-body" });
    if (c.intro) body.append(h("p", { class: "w-intro", html: c.intro }));
    var status = h("span", { class: "w-status" });
    var foot = h("div", { class: "w-foot" });
    foot.append(status);
    el.append(head, body, foot);
    return {
      body: body, foot: foot,
      btn: function (label, fn, cls) { var b = h("button", { type: "button", class: "btn sm " + (cls || ""), onclick: fn }, label); foot.insertBefore(b, status); return b; },
      status: function (t, k) { status.textContent = t; status.className = "w-status " + (k || ""); },
    };
  }

  W.mount = function (root) {
    (root || document).querySelectorAll(".w[data-w]:not([data-on])").forEach(function (el) {
      el.setAttribute("data-on", "1");
      var c = {}; var s = el.querySelector('script[type="application/json"]');
      if (s) { try { c = JSON.parse(s.textContent); } catch (e) { el.append(h("p", { class: "w-err" }, "Lỗi cấu hình: " + e.message)); return; } }
      el._cfg = c;
      var f = REG[el.getAttribute("data-w")];
      if (!f) { el.append(h("p", { class: "w-err" }, "Chưa có hoạt động: " + el.getAttribute("data-w"))); return; }
      try { f(el, c); } catch (e) { console.error(e); el.append(h("p", { class: "w-err" }, "Lỗi hoạt động: " + e.message)); }
    });
  };
  function rerender(el, type) { REG[type](el, el._cfg); }

  /* ------------------------------------------------------------ QUIZ */
  W.def("quiz", function (el, c) {
    var S = shell(el, c, "quiz"), answered = 0, correct = 0, n = c.qs.length;
    c.qs.forEach(function (q, qi) {
      var multi = Array.isArray(q.ans), box = h("div", { class: "q" });
      box.append(h("div", { class: "q-t" }, h("span", { class: "q-n" }, String(qi + 1)), h("div", { html: q.q })));
      if (q.code) box.append(h("pre", { class: "code" }, h("code", { text: q.code })));
      var ol = h("div", { class: "opts" }), fb = h("div", { class: "fb" }), done = false;
      var btns = q.opts.map(function (o, i) {
        var b = h("button", { type: "button", class: "opt", "aria-pressed": "false" }, h("span", { class: "k" }, "ABCDEFGH"[i]), h("span", { html: o }));
        ol.append(b); return b;
      });
      function finish(sel) {
        done = true; var ans = multi ? q.ans : [q.ans];
        var ok = sel.length === ans.length && sel.every(function (x) { return ans.indexOf(x) >= 0; });
        btns.forEach(function (b, i) { b.disabled = true; if (ans.indexOf(i) >= 0) b.classList.add("right"); else if (sel.indexOf(i) >= 0) b.classList.add("wrong"); });
        fb.className = "fb show " + (ok ? "ok" : "no"); fb.innerHTML = "<b>" + (ok ? "Chính xác." : "Chưa đúng.") + "</b> " + (q.exp || "");
        answered++; if (ok) correct++; update();
      }
      if (!multi) btns.forEach(function (b, i) { b.addEventListener("click", function () { if (!done) finish([i]); }); });
      else {
        btns.forEach(function (b) { b.addEventListener("click", function () { if (!done) b.setAttribute("aria-pressed", String(b.getAttribute("aria-pressed") !== "true")); }); });
        var chk = h("button", { type: "button", class: "btn sm", style: "align-self:flex-start" }, "Kiểm tra");
        chk.onclick = function () {
          var sel = []; btns.forEach(function (b, i) { if (b.getAttribute("aria-pressed") === "true") sel.push(i); });
          if (!sel.length) { fb.className = "fb show"; fb.textContent = "Chọn ít nhất một đáp án."; return; }
          chk.remove(); finish(sel);
        };
        box.append(ol, h("span", { class: "q-hint" }, "Chọn tất cả đáp án đúng"), chk, fb); S.body.append(box); return;
      }
      box.append(ol, fb); S.body.append(box);
    });
    var res = h("div", { class: "result hidden" }); S.body.append(res);
    function update() {
      S.status(correct + "/" + answered + " đúng · đã làm " + answered + "/" + n);
      if (answered === n) {
        W.done(c.id, correct, n);
        var best = (LS.get("w:" + c.id, {}) || {}).best;
        res.classList.remove("hidden");
        res.innerHTML = "<b>" + correct + "/" + n + "</b><span>" + (correct / n >= 0.8 ? "Tốt lắm. Bạn đã nắm vững phần này." : correct / n >= 0.5 ? "Khá. Xem lại các câu sai và phần giải thích." : "Nên đọc lại mục liên quan rồi làm lại.") + (c.id && best != null ? " Điểm cao nhất: " + best + "/" + n + "." : "") + "</span>";
      }
    }
    S.btn("Làm lại", function () { rerender(el, "quiz"); }, "ghost");
    update(); if (!answered) S.status("Đã làm 0/" + n);
  });

  /* ------------------------------------------------------------ FLASHCARDS */
  W.def("flash", function (el, c) {
    var S = shell(el, c, "flash"), cards = c.cards.slice(), i = 0, known = LS.get("fc:" + (c.id || ""), {});
    var card = h("button", { type: "button", class: "fc", "aria-label": "Lật thẻ" }), meta = h("div", { class: "fc-meta" });
    S.body.append(card, meta);
    function draw() {
      var x = cards[i]; card.classList.remove("flip");
      card.innerHTML = ""; card.append(h("div", { class: "fc-in" }, h("div", { class: "fc-f", html: x[0] }), h("div", { class: "fc-b", html: x[1] })));
      var k = Object.keys(known).filter(function (t) { return known[t]; }).length;
      meta.innerHTML = "<span>Thẻ " + (i + 1) + "/" + cards.length + " · bấm để lật</span><span>Đã nhớ " + k + "/" + cards.length + "</span>";
      S.status(known[x[0]] ? "Bạn đã đánh dấu nhớ thẻ này" : "", known[x[0]] ? "ok" : "");
    }
    card.onclick = function () { card.classList.toggle("flip"); };
    S.btn("← Trước", function () { i = (i - 1 + cards.length) % cards.length; draw(); }, "ghost");
    S.btn("Chưa nhớ", function () { known[cards[i][0]] = false; LS.set("fc:" + (c.id || ""), known); i = (i + 1) % cards.length; draw(); }, "ghost");
    S.btn("Đã nhớ ✓", function () { known[cards[i][0]] = true; LS.set("fc:" + (c.id || ""), known); i = (i + 1) % cards.length; draw(); });
    S.btn("Xáo trộn", function () { cards = shuffled(cards, Date.now() % 1000); i = 0; draw(); }, "ghost");
    draw();
  });

  /* ------------------------------------------------------------ ORDER */
  W.def("order", function (el, c) {
    var S = shell(el, c, "order"), items = c.items.map(function (t, i) { return { t: t, i: i }; });
    var cur = shuffled(items, c.seed || 11); if (cur.every(function (x, k) { return x.i === k; })) cur.reverse();
    var ul = h("ol", { class: "ord" }); S.body.append(ul); var drag = null;
    function draw(mark) {
      ul.innerHTML = "";
      cur.forEach(function (x, k) {
        var li = h("li", { draggable: "true", class: mark ? (x.i === k ? "right" : "wrong") : "" }, h("span", { class: "i" }, String(k + 1)), h("span", { class: "t", html: x.t }),
          h("button", { type: "button", "aria-label": "Lên", onclick: function () { if (k > 0) { cur.splice(k - 1, 0, cur.splice(k, 1)[0]); draw(); } } }, "↑"),
          h("button", { type: "button", "aria-label": "Xuống", onclick: function () { if (k < cur.length - 1) { cur.splice(k + 1, 0, cur.splice(k, 1)[0]); draw(); } } }, "↓"));
        li.addEventListener("dragstart", function () { drag = k; li.classList.add("drag"); });
        li.addEventListener("dragend", function () { li.classList.remove("drag"); });
        li.addEventListener("dragover", function (e) { e.preventDefault(); });
        li.addEventListener("drop", function (e) { e.preventDefault(); if (drag == null || drag === k) return; cur.splice(k, 0, cur.splice(drag, 1)[0]); drag = null; draw(); });
        ul.append(li);
      });
    }
    S.btn("Kiểm tra", function () { var ok = cur.filter(function (x, k) { return x.i === k; }).length; draw(true); S.status(ok + "/" + cur.length + " vị trí đúng", ok === cur.length ? "ok" : "bad"); if (ok === cur.length) W.done(c.id, 1, 1); });
    S.btn("Xem đáp án", function () { cur = items.slice(); draw(true); S.status(c.exp ? "" : "Thứ tự đúng đã hiện"); if (c.exp) fbx.innerHTML = c.exp, fbx.className = "fb show"; }, "ghost");
    var fbx = h("div", { class: "fb" }); S.body.append(fbx);
    draw();
  });

  /* ------------------------------------------------------------ MATCH */
  W.def("match", function (el, c) {
    var S = shell(el, c, "match"), rights = shuffled(c.pairs.map(function (p) { return p[1]; }), c.seed || 5), rows = h("div", { class: "rows" });
    var sels = c.pairs.map(function (p) {
      var sel = h("select", { "aria-label": "Chọn cặp cho " + p[0].replace(/<[^>]+>/g, "") }, h("option", { value: "" }, "— chọn —"));
      rights.forEach(function (r) { sel.append(h("option", { value: r, html: r.replace(/<[^>]+>/g, "") })); });
      var row = h("div", { class: "row-i" }, h("span", { class: "t", html: "<b>" + p[0] + "</b>" }), sel);
      rows.append(row); return { row: row, sel: sel, ans: p[1] };
    });
    S.body.append(rows);
    S.btn("Kiểm tra", function () {
      var ok = 0; sels.forEach(function (x) { var r = x.sel.value === x.ans; x.row.className = "row-i " + (x.sel.value ? (r ? "right" : "wrong") : ""); if (r) ok++; });
      S.status(ok + "/" + sels.length + " cặp đúng", ok === sels.length ? "ok" : "bad"); if (ok === sels.length) W.done(c.id, 1, 1);
    });
    S.btn("Xem đáp án", function () { sels.forEach(function (x) { x.sel.value = x.ans; x.row.className = "row-i right"; }); }, "ghost");
  });

  /* ------------------------------------------------------------ CLASSIFY */
  W.def("classify", function (el, c) {
    var S = shell(el, c, "classify"), rows = h("div", { class: "rows" }), picks = [];
    c.items.forEach(function (it, i) {
      var seg = h("div", { class: "seg", role: "group" }), ex = h("div", { class: "ex hidden", html: it[2] || "" });
      c.buckets.forEach(function (b, bi) {
        seg.append(h("button", { type: "button", "aria-pressed": "false", onclick: function (e) {
          picks[i] = bi; seg.querySelectorAll("button").forEach(function (x) { x.setAttribute("aria-pressed", "false"); }); e.currentTarget.setAttribute("aria-pressed", "true");
        } }, b));
      });
      var row = h("div", { class: "row-i" }, h("span", { class: "t", html: it[0] }), seg, ex); rows.append(row); it._row = row; it._ex = ex;
    });
    S.body.append(rows);
    S.btn("Kiểm tra", function () {
      var ok = 0; c.items.forEach(function (it, i) {
        var r = picks[i] === it[1]; it._row.className = "row-i " + (picks[i] == null ? "" : r ? "right" : "wrong"); if (r) ok++;
        it._ex.classList.toggle("hidden", !(picks[i] != null && !r && it[2]));
        if (picks[i] != null && !r && !it[2]) { it._ex.classList.remove("hidden"); it._ex.innerHTML = "Đáp án: <b>" + c.buckets[it[1]] + "</b>"; }
      });
      S.status(ok + "/" + c.items.length + " đúng", ok === c.items.length ? "ok" : "bad"); W.done(c.id, ok, c.items.length);
    });
    S.btn("Xem đáp án", function () { c.items.forEach(function (it, i) { picks[i] = it[1]; it._row.className = "row-i right"; it._row.querySelectorAll(".seg button").forEach(function (b, bi) { b.setAttribute("aria-pressed", String(bi === it[1])); }); if (it[2]) { it._ex.classList.remove("hidden"); } }); }, "ghost");
  });

  /* ------------------------------------------------------------ SPOT (tìm dòng có vấn đề) */
  W.def("spot", function (el, c) {
    var S = shell(el, c, "spot"), box = h("div", { class: "spot " + (c.kind === "code" ? "code" : "") }), flags = {};
    var nBad = Object.keys(c.bad).length;
    c.lines.forEach(function (t, i) {
      var b = h("button", { type: "button", "aria-pressed": "false" }, h("span", { class: "ln" }, String(i + 1)), h("span", { html: c.kind === "code" ? esc(t) : t }));
      b.onclick = function () { if (box.dataset.checked) return; flags[i] = !flags[i]; b.setAttribute("aria-pressed", String(!!flags[i])); S.status("Đã đánh dấu " + Object.keys(flags).filter(function (k) { return flags[k]; }).length + " dòng"); };
      box.append(b);
    });
    S.body.append(box);
    S.status("Có " + nBad + " vấn đề cần tìm. Bấm vào dòng để đánh dấu.");
    S.btn("Kiểm tra", function () {
      box.dataset.checked = "1"; var found = 0, fp = 0;
      box.querySelectorAll("button").forEach(function (b, i) {
        var bad = c.bad[i] != null;
        b.className = bad ? (flags[i] ? "found" : "miss") : flags[i] ? "fp" : "";
        if (bad && flags[i]) found++; if (!bad && flags[i]) fp++;
        var note = bad ? c.bad[i] : flags[i] ? (c.ok && c.ok[i]) || "Dòng này không có vấn đề." : null;
        if (note) b.append(h("span", { class: "ex", html: (bad ? (flags[i] ? "✓ " : "Bỏ sót: ") : "✗ ") + note }));
      });
      S.status("Tìm đúng " + found + "/" + nBad + (fp ? " · " + fp + " dòng đánh dấu nhầm" : ""), found === nBad && !fp ? "ok" : "bad"); W.done(c.id, found, nBad);
    });
    S.btn("Làm lại", function () { rerender(el, "spot"); }, "ghost");
  });

  /* ------------------------------------------------------------ FILL (đáp án số / chữ) */
  W.def("fill", function (el, c) {
    var S = shell(el, c, "fill"), items = [];
    c.qs.forEach(function (q) {
      var inp = h("input", { type: "text", inputmode: typeof q.ans === "number" ? "decimal" : "text", "aria-label": "Đáp án" }), ex = h("span", { class: "ex hidden", html: q.exp || "" });
      var row = h("div", { class: "fill-q" }, h("span", { class: "t", html: q.q }), inp, q.unit ? h("span", { class: "chip" }, q.unit) : null, ex);
      S.body.append(row); items.push({ q: q, inp: inp, row: row, ex: ex });
    });
    function ok(q, v) {
      if (typeof q.ans === "number") { var x = parseFloat(String(v).replace(",", ".").replace("%", "")); return !isNaN(x) && Math.abs(x - q.ans) <= (q.tol || 0.001); }
      var acc = Array.isArray(q.ans) ? q.ans : [q.ans]; return acc.some(function (a) { return norm(a).replace(/\s/g, "") === norm(v).replace(/\s/g, ""); });
    }
    S.btn("Kiểm tra", function () { var k = 0; items.forEach(function (x) { var r = ok(x.q, x.inp.value); x.row.className = "fill-q " + (r ? "right" : "wrong"); x.ex.classList.toggle("hidden", r && !x.q.always); if (r) k++; }); S.status(k + "/" + items.length + " đúng", k === items.length ? "ok" : "bad"); W.done(c.id, k, items.length); });
    S.btn("Xem đáp án", function () { items.forEach(function (x) { x.inp.value = typeof x.q.ans === "number" ? String(x.q.ans).replace(".", ",") : Array.isArray(x.q.ans) ? x.q.ans[0] : x.q.ans; x.ex.classList.remove("hidden"); x.row.className = "fill-q right"; }); }, "ghost");
  });

  /* ------------------------------------------------------------ BVA / EP */
  function decs(step) { var s = String(step); return s.indexOf(".") >= 0 ? s.split(".")[1].length : 0; }
  W.def("bva", function (el, c) {
    var S = shell(el, c, "bva"), step = c.step || 1, d = decs(step), unit = c.unit || "";
    var fmt = function (x) { return x.toFixed(d).replace(".", ","); };
    var rnd = function (x) { return Math.round(x / step) * step; };
    var ctrl = h("div", { class: "opts-row" }), minI, maxI;
    if (c.editable) {
      minI = h("input", { type: "text", value: String(c.min).replace(".", ",") }); maxI = h("input", { type: "text", value: String(c.max).replace(".", ",") });
      ctrl.append(h("div", { class: "fld" }, h("label", {}, "Giá trị nhỏ nhất hợp lệ"), minI), h("div", { class: "fld" }, h("label", {}, "Giá trị lớn nhất hợp lệ"), maxI));
      minI.oninput = maxI.oninput = draw;
    }
    var mode = c.mode || 2, modeSeg = h("div", { class: "seg" });
    [2, 3].forEach(function (m) { modeSeg.append(h("button", { type: "button", "aria-pressed": String(m === mode), onclick: function (e) { mode = m; modeSeg.querySelectorAll("button").forEach(function (b) { b.setAttribute("aria-pressed", "false"); }); e.currentTarget.setAttribute("aria-pressed", "true"); draw(); } }, m + " giá trị")); });
    ctrl.append(h("div", { class: "fld" }, h("label", {}, "Phân tích giá trị biên"), modeSeg));
    var nl = h("div", { class: "nl" }), info = h("div", {}), vals = h("div", { class: "vals" });
    var guessWrap = h("div", { class: "fld" }), guess = h("input", { type: "text", placeholder: d ? "Ví dụ: 3,9; 4,0; 5,4" : "Ví dụ: 9, 10, 15, 16" });
    guessWrap.append(h("label", {}, "Bạn chọn những giá trị kiểm thử nào? (" + (d ? "cách nhau bởi dấu ;" : "cách nhau bởi dấu phẩy") + ")"), guess);
    var cmp = h("div", { class: "vals" }), showAns = !c.challenge;
    S.body.append(ctrl, nl, info);
    if (c.challenge) S.body.append(guessWrap, cmp);
    var ansWrap = h("div", { class: c.challenge ? "hidden" : "" }, h("div", { class: "fld" }, h("label", {}, "Giá trị kiểm thử theo BVA")), vals);
    S.body.append(ansWrap);
    function parts() {
      if (!c.editable) return c.parts;
      var lo = rnd(parseFloat(String(minI.value).replace(",", "."))), hi = rnd(parseFloat(String(maxI.value).replace(",", ".")));
      if (isNaN(lo) || isNaN(hi) || hi < lo) return null;
      var p = [{ lo: null, hi: rnd(lo - step), label: "Không hợp lệ (nhỏ)", valid: false }, { lo: lo, hi: hi, label: "Hợp lệ", valid: true }];
      if (c.max != null || c.editable) p.push({ lo: rnd(hi + step), hi: null, label: "Không hợp lệ (lớn)", valid: false });
      if (c.domainMin != null) p[0].lo = c.domainMin;
      return p;
    }
    function compute(P) {
      var bset = [], set = {};
      P.forEach(function (p) { if (p.lo != null) bset.push(p.lo); if (p.hi != null) bset.push(p.hi); });
      var add = function (x) { x = +rnd(x).toFixed(d); if (c.domainMin != null && x < c.domainMin) return; if (c.domainMax != null && x > c.domainMax) return; set[x] = 1; };
      bset.forEach(function (b) { add(b); if (mode === 3) { add(b - step); add(b + step); } });
      return Object.keys(set).map(Number).sort(function (a, b) { return a - b; });
    }
    function validOf(P, x) { for (var i = 0; i < P.length; i++) { var p = P[i]; if ((p.lo == null || x >= p.lo - 1e-9) && (p.hi == null || x <= p.hi + 1e-9)) return p; } return null; }
    function draw() {
      var P = parts(); if (!P) { info.textContent = "Nhập khoảng hợp lệ (nhỏ nhất ≤ lớn nhất)."; return; }
      var W0 = 900, H0 = 120, n = P.length, seg = (W0 - 40) / n, svg = '<svg viewBox="0 0 ' + W0 + " " + H0 + '" role="img" aria-label="Trục số các phân vùng">';
      P.forEach(function (p, i) {
        var x = 20 + i * seg, col = p.valid ? "var(--ok)" : "var(--bad)";
        svg += '<rect x="' + (x + 2) + '" y="30" width="' + (seg - 4) + '" height="26" rx="6" fill="' + col + '" opacity=".22" stroke="' + col + '"/>';
        svg += '<text x="' + (x + seg / 2) + '" y="48" text-anchor="middle" font-size="13" fill="var(--paper)" font-family="var(--f-body)">' + esc(p.label) + "</text>";
        var r = (p.lo == null ? "−∞" : fmt(p.lo)) + " … " + (p.hi == null ? "+∞" : fmt(p.hi));
        svg += '<text x="' + (x + seg / 2) + '" y="20" text-anchor="middle" font-size="12" fill="var(--muted)" font-family="var(--f-mono)">' + r + "</text>";
        if (i < n - 1) { var bx = x + seg; svg += '<line x1="' + bx + '" y1="26" x2="' + bx + '" y2="76" stroke="var(--amber)" stroke-width="2"/><text x="' + bx + '" y="94" text-anchor="middle" font-size="12" fill="var(--amber)" font-family="var(--f-mono)">' + fmt(P[i].hi) + " | " + fmt(P[i + 1].lo) + "</text>"; }
      });
      svg += "</svg>"; nl.innerHTML = svg;
      var V = compute(P); el._ans = V;
      info.innerHTML = "<span class=chip>" + P.length + " phân vùng (" + P.filter(function (p) { return p.valid; }).length + " hợp lệ)</span> <span class=chip>BVA " + mode + " giá trị: " + V.length + " giá trị kiểm thử</span>";
      vals.innerHTML = "";
      V.forEach(function (x) { var p = validOf(P, x); vals.append(h("span", { class: "val " + (p && p.valid ? "v" : "x"), title: p ? p.label : "" }, fmt(x) + unit)); });
    }
    if (c.challenge) {
      S.btn("So sánh với đáp án", function () {
        var P = parts(); if (!P) return; var V = compute(P), mine = {};
        guess.value.split(d ? /[;\s]+/ : /[;,\s]+/).forEach(function (t) { if (!t.trim()) return; var x = parseFloat(t.replace(",", ".")); if (!isNaN(x)) mine[+x.toFixed(d)] = 1; });
        cmp.innerHTML = ""; var hit = 0;
        V.forEach(function (x) { var ok = mine[x]; if (ok) hit++; cmp.append(h("span", { class: "val " + (ok ? "v" : "miss"), title: ok ? "Bạn đã chọn" : "Bạn bỏ sót" }, (ok ? "✓ " : "+ ") + fmt(x))); });
        Object.keys(mine).map(Number).filter(function (x) { return V.indexOf(x) < 0; }).forEach(function (x) { cmp.append(h("span", { class: "val extra", title: "Không phải giá trị biên" }, fmt(x))); });
        var extra = Object.keys(mine).length - hit;
        S.status("Trùng " + hit + "/" + V.length + (extra ? " · " + extra + " giá trị thừa" : ""), hit === V.length && !extra ? "ok" : "bad"); W.done(c.id, hit, V.length);
      });
      S.btn("Hiện đáp án", function () { ansWrap.classList.remove("hidden"); }, "ghost");
    }
    draw();
  });

  /* ------------------------------------------------------------ DECISION TABLE */
  W.def("dtable", function (el, c) {
    var S = shell(el, c, "dtable"), n = c.conds.length, cols = [], fn = new Function("c", "return (" + c.fn + ")(c)");
    var feas = c.feasible ? new Function("c", "return (" + c.feasible + ")(c)") : function () { return true; };
    for (var k = 0; k < 1 << n; k++) { var v = []; for (var j = 0; j < n; j++) v.push(!((k >> (n - 1 - j)) & 1)); if (feas(v)) cols.push(v); }
    var tw = h("div", { class: "tw" }), tbl = h("table", { class: "dt" }); tw.append(tbl); S.body.append(tw);
    var sels = [];
    function full() {
      var html = "<tr><th>Quy tắc</th>" + cols.map(function (_, i) { return "<th>R" + (i + 1) + "</th>"; }).join("") + "</tr><tr class=sec><td colspan=" + (cols.length + 1) + ">ĐIỀU KIỆN</td></tr>";
      c.conds.forEach(function (cn, j) { html += "<tr><td>" + cn + "</td>" + cols.map(function (v) { return '<td class="' + (v[j] ? "T" : "F") + '">' + (v[j] ? "Đ" : "S") + "</td>"; }).join("") + "</tr>"; });
      html += "<tr class=sec><td colspan=" + (cols.length + 1) + ">HÀNH ĐỘNG / KẾT QUẢ</td></tr><tr><td>" + (c.outLabel || "Kết quả") + "</td>" + cols.map(function (_, i) { return '<td data-i="' + i + '"></td>'; }).join("") + "</tr>";
      tbl.innerHTML = html; sels = [];
      tbl.querySelectorAll("td[data-i]").forEach(function (td, i) {
        var s = h("select", { "aria-label": "Kết quả R" + (i + 1) }, h("option", { value: "" }, "?")); c.outs.forEach(function (o) { s.append(h("option", { value: o }, o)); }); td.append(s); sels.push(s);
        if (c.prefill && c.prefill[i] != null) s.value = fn(cols[i]);
      });
    }
    function collapse() {
      var terms = cols.map(function (v) { return { v: v.map(function (b) { return b ? 1 : 0; }), o: fn(v), m: [cols.indexOf(v)] }; }), changed = true;
      while (changed) {
        changed = false; var used = {}, next = [];
        for (var a = 0; a < terms.length; a++) for (var b = a + 1; b < terms.length; b++) {
          var A = terms[a], B = terms[b]; if (A.o !== B.o) continue; var diff = -1, cnt = 0;
          for (var j = 0; j < n; j++) if (A.v[j] !== B.v[j]) { cnt++; diff = j; if (A.v[j] === 2 || B.v[j] === 2) cnt = 99; }
          if (cnt === 1) { var v = A.v.slice(); v[diff] = 2; var key = v.join("") + A.o; if (!next.some(function (t) { return t.k === key; })) next.push({ v: v, o: A.o, m: A.m.concat(B.m), k: key }); used[a] = used[b] = 1; changed = true; }
        }
        terms.forEach(function (t, i) { if (!used[i]) next.push(t); }); terms = next;
      }
      var need = {}; cols.forEach(function (_, i) { need[i] = 1; }); var pick = [];
      terms.sort(function (x, y) { return y.m.length - x.m.length; }).forEach(function (t) { if (t.m.some(function (i) { return need[i]; })) { pick.push(t); t.m.forEach(function (i) { delete need[i]; }); } });
      var html = "<tr><th>Quy tắc rút gọn</th>" + pick.map(function (_, i) { return "<th>R" + (i + 1) + "'</th>"; }).join("") + "</tr><tr class=sec><td colspan=" + (pick.length + 1) + ">ĐIỀU KIỆN</td></tr>";
      c.conds.forEach(function (cn, j) { html += "<tr><td>" + cn + "</td>" + pick.map(function (t) { var x = t.v[j]; return '<td class="' + (x === 2 ? "D" : x ? "T" : "F") + '">' + (x === 2 ? "–" : x ? "Đ" : "S") + "</td>"; }).join("") + "</tr>"; });
      html += "<tr class=sec><td colspan=" + (pick.length + 1) + ">KẾT QUẢ</td></tr><tr><td>" + (c.outLabel || "Kết quả") + "</td>" + pick.map(function (t) { return "<td>" + t.o + "</td>"; }).join("") + "</tr>";
      tbl.innerHTML = html; S.status(cols.length + " quy tắc đầy đủ → " + pick.length + " quy tắc sau khi rút gọn (– = không quan tâm)", "ok");
    }
    full();
    S.btn("Kiểm tra", function () {
      if (!sels.length) full(); var ok = 0;
      sels.forEach(function (s, i) { var r = s.value === fn(cols[i]); s.parentNode.className = s.value ? (r ? "right" : "wrong") : ""; if (r) ok++; });
      S.status(ok + "/" + cols.length + " quy tắc đúng", ok === cols.length ? "ok" : "bad"); W.done(c.id, ok, cols.length);
    });
    S.btn("Rút gọn bảng", collapse, "ghost");
    S.btn("Bảng đầy đủ", function () { full(); S.status(""); }, "ghost");
    S.status(cols.length + " quy tắc. Chọn kết quả cho từng cột.");
  });

  /* ------------------------------------------------------------ STATE TRANSITION */
  W.def("state", function (el, c) {
    var S = shell(el, c, "state"), cur = c.start, path = [], cases = [], covT = {}, covS = {}, covI = {}, last = null;
    var byId = {}; c.states.forEach(function (s) { byId[s.id] = s; });
    var T = c.trans.map(function (t) { return { f: t[0], e: t[1], to: t[2], k: t[0] + "|" + t[1] }; });
    var events = c.events || T.map(function (t) { return t.e; }).filter(function (e, i, a) { return a.indexOf(e) === i; });
    var invalidAll = []; c.states.forEach(function (s) { events.forEach(function (e) { if (!T.some(function (t) { return t.f === s.id && t.e === e; }) && !(c.final || []).includes(s.id)) invalidAll.push(s.id + "|" + e); }); });
    var wrap = h("div", { class: "sm" }), evs = h("div", { class: "evs" }), log = h("div", { class: "log" }), meters = h("div", { class: "meters" }), tblWrap = h("div", { class: "tw hidden" });
    S.body.append(wrap, h("div", { class: "fld" }, h("label", {}, "Sự kiện (bấm để kích hoạt từ trạng thái hiện tại)"), evs), log, meters, tblWrap);
    function arrow(t, i) {
      var a = byId[t.f], b = byId[t.to], w2 = 64, h2 = 22;
      if (t.f === t.to) { var x = a.x, y = a.y - h2; return { d: "M" + (x - 18) + " " + y + " C " + (x - 40) + " " + (y - 60) + ", " + (x + 40) + " " + (y - 60) + ", " + (x + 18) + " " + y, lx: x, ly: y - 52 }; }
      var dx = b.x - a.x, dy = b.y - a.y, L = Math.hypot(dx, dy), ux = dx / L, uy = dy / L;
      var back = T.some(function (o) { return o.f === t.to && o.to === t.f; });
      var off = back ? 16 : 0, nx = -uy * off, ny = ux * off;
      var clip = function (px, py, sx, sy) { var tx = Math.abs(sx) > 1e-6 ? w2 / Math.abs(sx) : 1e9, ty = Math.abs(sy) > 1e-6 ? h2 / Math.abs(sy) : 1e9, k = Math.min(tx, ty) + 4; return [px + sx * k, py + sy * k]; };
      var p1 = clip(a.x + nx, a.y + ny, ux, uy), p2 = clip(b.x + nx, b.y + ny, -ux, -uy);
      var mx = (p1[0] + p2[0]) / 2 + nx * 0.6, my = (p1[1] + p2[1]) / 2 + ny * 0.6;
      return { d: "M" + p1[0] + " " + p1[1] + " L" + p2[0] + " " + p2[1], lx: mx, ly: my - 6 };
    }
    function draw() {
      var Wd = c.w || 900, Hd = c.h || 360, svg = '<svg viewBox="0 0 ' + Wd + " " + Hd + '" role="img" aria-label="Sơ đồ chuyển trạng thái"><defs><marker id="arr" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="currentColor" style="color:var(--muted)"/></marker></defs>';
      T.forEach(function (t, i) { var g = arrow(t, i); svg += '<g class="tr' + (covT[t.k] ? " cov" : "") + (last === t.k ? " last" : "") + '"><path d="' + g.d + '"/><text x="' + g.lx + '" y="' + g.ly + '">' + esc(t.e) + "</text></g>"; });
      c.states.forEach(function (s) { svg += '<g class="st' + (s.id === cur ? " cur" : "") + (covS[s.id] ? " vis" : "") + '"><rect x="' + (s.x - 64) + '" y="' + (s.y - 22) + '" width="128" height="44" rx="12"/><text x="' + s.x + '" y="' + s.y + '">' + esc(s.label || s.id) + "</text></g>"; });
      svg += "</svg>"; wrap.innerHTML = svg;
      evs.innerHTML = ""; events.forEach(function (e) { evs.append(h("button", { type: "button", onclick: function () { fire(e); } }, e)); });
      var nT = Object.keys(covT).length, nS = Object.keys(covS).length, nI = Object.keys(covI).length;
      var pc = function (a, b) { return b ? Math.round((a / b) * 100) : 0; };
      meters.innerHTML = "";
      [["Trạng thái đã đi qua", nS, c.states.length], ["Chuyển trạng thái hợp lệ", nT, T.length], ["Chuyển không hợp lệ đã thử", nI, invalidAll.length]].forEach(function (m) {
        meters.append(h("div", { class: "meter", style: "--p:" + pc(m[1], m[2]) + "%" }, h("b", {}, pc(m[1], m[2]) + "%"), h("span", {}, m[0] + ": " + m[1] + "/" + m[2]), h("i")));
      });
      log.innerHTML = "<b>Ca hiện tại:</b> " + (path.length ? esc(c.start) + " → " + path.map(function (p) { return p.bad ? '<span class="bad">' + esc(p.e) + " ✗</span>" : esc(p.e) + " → " + esc(p.to); }).join(" → ") : esc(c.start) + " (chưa có sự kiện)") +
        (cases.length ? "<br><b>Đã lưu " + cases.length + " ca kiểm thử</b>" : "");
      var done = nT === T.length; S.status(done ? "Đạt 100% bao phủ chuyển trạng thái hợp lệ (0-switch) với " + (cases.length + (path.length ? 1 : 0)) + " ca" : "", done ? "ok" : "");
      if (done) W.done(c.id, 1, 1);
    }
    function fire(e) {
      var t = T.filter(function (x) { return x.f === cur && x.e === e; })[0];
      if (!t) { covI[cur + "|" + e] = 1; path.push({ e: e, bad: true }); last = null; draw(); return; }
      covT[t.k] = 1; covS[t.to] = 1; last = t.k; path.push({ e: e, to: t.to }); cur = t.to; draw();
    }
    covS[c.start] = 1;
    S.btn("Lưu ca, bắt đầu ca mới", function () { if (path.length) cases.push(path); path = []; cur = c.start; last = null; draw(); });
    S.btn("Xóa hết", function () { path = []; cases = []; covT = {}; covS = {}; covI = {}; cur = c.start; covS[c.start] = 1; last = null; draw(); }, "ghost");
    S.btn("Bảng trạng thái", function () {
      tblWrap.classList.toggle("hidden");
      var html = '<table class="dt"><tr><th>Trạng thái \\ Sự kiện</th>' + events.map(function (e) { return "<th>" + esc(e) + "</th>"; }).join("") + "</tr>";
      c.states.forEach(function (s) { html += "<tr><td>" + esc(s.label || s.id) + "</td>" + events.map(function (e) { var t = T.filter(function (x) { return x.f === s.id && x.e === e; })[0]; return "<td" + (t ? "" : ' class="D"') + ">" + (t ? esc(byId[t.to].label || t.to) : "–") + "</td>"; }).join("") + "</tr>"; });
      tblWrap.innerHTML = html + "</table>";
    }, "ghost");
    draw();
  });

  /* ------------------------------------------------------------ CODE LAB: chạy kiểm thử, bao phủ, đột biến */
  function makeExpect(fails) {
    function eq(a, b) { return JSON.stringify(a) === JSON.stringify(b); }
    function show(x) { try { return typeof x === "string" ? JSON.stringify(x) : JSON.stringify(x); } catch (e) { return String(x); } }
    return function expect(actual) {
      function mk(neg) {
        var chk = function (ok, msg) { if (neg ? ok : !ok) throw new Error((neg ? "not." : "") + msg); };
        return {
          toBe: function (e) { chk(Object.is(actual, e), "toBe: mong đợi " + show(e) + ", nhận " + show(actual)); },
          toEqual: function (e) { chk(eq(actual, e), "toEqual: mong đợi " + show(e) + ", nhận " + show(actual)); },
          toBeCloseTo: function (e, p) { p = p == null ? 2 : p; chk(Math.abs(actual - e) < Math.pow(10, -p) / 2, "toBeCloseTo: mong đợi ≈" + e + ", nhận " + show(actual)); },
          toBeTruthy: function () { chk(!!actual, "toBeTruthy: nhận " + show(actual)); },
          toBeFalsy: function () { chk(!actual, "toBeFalsy: nhận " + show(actual)); },
          toBeGreaterThan: function (e) { chk(actual > e, "toBeGreaterThan " + e + ": nhận " + show(actual)); },
          toBeLessThan: function (e) { chk(actual < e, "toBeLessThan " + e + ": nhận " + show(actual)); },
          toContain: function (e) { chk(actual != null && actual.indexOf(e) >= 0, "toContain " + show(e) + ": nhận " + show(actual)); },
          toThrow: function (m) {
            var threw = false, msg = ""; try { actual(); } catch (err) { threw = true; msg = String(err && err.message); }
            chk(threw && (!m || msg.indexOf(m) >= 0), "toThrow" + (m ? "(" + show(m) + ")" : "") + (threw ? ": thông báo là " + show(msg) : ": hàm không ném lỗi"));
          },
        };
      }
      var o = mk(false); o.not = mk(true); return o;
    };
  }
  W.runTests = function (code, fnName, impl) {
    var tests = [], expect = makeExpect();
    var test = function (n, f) { tests.push({ n: n, f: f }); };
    var describe = function (n, f) { f(); };
    try { new Function("test", "it", "describe", "expect", fnName, '"use strict";\n' + code)(test, test, describe, expect, impl); }
    catch (e) { return { error: "Lỗi cú pháp hoặc lỗi khi nạp kiểm thử: " + e.message, res: [] }; }
    var res = tests.map(function (t) { try { t.f(); return { n: t.n, ok: true }; } catch (e) { return { n: t.n, ok: false, m: e.message }; } });
    return { res: res };
  };
  W.def("lab", function (el, c) {
    var S = shell(el, c, "lab"), sut = c.sut, name = sut.name, key = "lab:" + (c.id || name);
    function build(inst) {
      var C = { s: {}, b: {} };
      var __s = function (i) { C.s[i] = (C.s[i] || 0) + 1; };
      var __b = function (i, v) { var r = (C.b[i] = C.b[i] || { t: 0, f: 0 }); r[v ? "t" : "f"]++; return v; };
      var fn = new Function("__s", "__b", '"use strict";\n' + inst + "\nreturn " + name + ";")(__s, __b);
      return { fn: fn, C: C };
    }
    var lines = sut.src.split("\n"), srcBox = h("div", { class: "src", "aria-label": "Mã nguồn đang kiểm thử" });
    function paint(C) {
      srcBox.innerHTML = "";
      lines.forEach(function (t, i) {
        var ln = i + 1, cls = "";
        if (C) {
          Object.keys(sut.smap || {}).forEach(function (sid) { if (sut.smap[sid] === ln) cls = C.s[sid] ? "cv" : "nc"; });
          Object.keys(sut.bmap || {}).forEach(function (bid) { if (sut.bmap[bid] === ln) { var r = C.b[bid]; cls = !r ? "nc" : r.t && r.f ? "cv" : "pb"; } });
        }
        srcBox.append(h("div", { class: cls }, h("span", {}, String(ln)), h("span", { text: t || " " })));
      });
    }
    paint(null);
    var ed = h("textarea", { class: "editor", spellcheck: "false", "aria-label": "Mã kiểm thử của bạn" }); ed.value = LS.get(key, null) || c.tests || "";
    ed.addEventListener("keydown", function (e) { if (e.key === "Tab") { e.preventDefault(); var s = ed.selectionStart; ed.value = ed.value.slice(0, s) + "  " + ed.value.slice(ed.selectionEnd); ed.selectionStart = ed.selectionEnd = s + 2; } e.stopPropagation(); });
    ed.addEventListener("input", function () { LS.set(key, ed.value); });
    var left = h("div", { class: "fld" }, h("label", {}, "Mã đang kiểm thử: " + name + "()" + (sut.note ? " · " + sut.note : "")), srcBox, h("div", { class: "legend", style: "font-size:.78em;color:var(--muted)", html: "<span style='color:var(--ok)'>■</span> đã chạy/đủ hai nhánh &nbsp; <span style='color:var(--amber)'>■</span> mới một nhánh &nbsp; <span style='color:var(--bad)'>■</span> chưa chạy" }));
    var right = h("div", { class: "fld" }, h("label", {}, "Kiểm thử của bạn (cú pháp giống Jest/Vitest: test, expect)"), ed);
    var grid = h("div", { class: "lab" }, left, right), out = h("div", { class: "fld" }), meters = h("div", { class: "meters" }), mutOut = h("div", {});
    S.body.append(grid, meters, out, mutOut);
    function nStmt() { return Object.keys(sut.smap || {}).length; }
    function nBr() { return Object.keys(sut.bmap || {}).length * 2; }
    function runAll() {
      var B = build(sut.inst), r = W.runTests(ed.value, name, B.fn);
      out.innerHTML = "";
      if (r.error) { out.append(h("div", { class: "fb show no", text: r.error })); S.status("Lỗi", "bad"); return null; }
      var ul = h("ul", { class: "res-list" });
      r.res.forEach(function (x) { ul.append(h("li", { class: x.ok ? "p" : "f" }, (x.ok ? "✓ " : "✗ ") + x.n, x.ok ? null : h("small", { text: x.m }))); });
      if (!r.res.length) ul.append(h("li", {}, "Chưa có kiểm thử nào. Viết test('tên', () => { expect(...).toBe(...) })"));
      out.append(h("label", { style: "font:600 .8em var(--f-mono);color:var(--muted)" }, "Kết quả trên mã gốc"), ul);
      paint(B.C);
      var s = Object.keys(B.C.s).length, b = 0; Object.keys(B.C.b).forEach(function (k) { if (B.C.b[k].t) b++; if (B.C.b[k].f) b++; });
      var pc = function (a, t) { return t ? Math.round((a / t) * 100) : 0; }, pass = r.res.filter(function (x) { return x.ok; }).length;
      meters.innerHTML = "";
      [["Kiểm thử đạt", pass, r.res.length], ["Bao phủ câu lệnh", s, nStmt()], ["Bao phủ nhánh (kết quả quyết định)", b, nBr()]].forEach(function (m) {
        meters.append(h("div", { class: "meter", style: "--p:" + pc(m[1], m[2]) + "%" }, h("b", {}, m[2] ? pc(m[1], m[2]) + "%" : "–"), h("span", {}, m[0] + ": " + m[1] + "/" + m[2]), h("i")));
      });
      S.status(pass + "/" + r.res.length + " kiểm thử đạt", pass === r.res.length && pass ? "ok" : "bad");
      return { r: r, pass: pass, sc: pc(s, nStmt()), bc: pc(b, nBr()) };
    }
    S.btn("▶ Chạy kiểm thử và đo bao phủ", function () { var x = runAll(); if (x && c.id) W.done(c.id + ":cov", x.bc, 100); });
    if (c.mutants && c.mutants.length) S.btn("🧬 Kiểm thử đột biến", function () {
      var base = runAll(); if (!base) return;
      if (base.pass !== base.r.res.length) { mutOut.innerHTML = '<div class="fb show no">Mọi kiểm thử phải đạt trên mã gốc trước khi chạy đột biến.</div>'; return; }
      var killed = 0, eqv = 0, rows = "";
      c.mutants.forEach(function (m) {
        var st;
        try { var B = build(m.inst), r = W.runTests(ed.value, name, B.fn); st = r.error || r.res.some(function (x) { return !x.ok; }) ? "k" : "s"; } catch (e) { st = "k"; }
        if (m.equiv) { eqv++; st = st === "k" ? "k" : "e"; }
        if (st === "k") killed++;
        rows += "<tr><td><b>" + esc(m.id) + "</b><br><small>" + esc(m.desc) + "</small></td><td class='diff'>" + (m.diff || []).map(function (l) { return "<span class='" + (l[0] === "-" ? "m" : "p") + "'>" + esc(l) + "</span>"; }).join("\n") + "</td><td><span class='tag " + st + "'>" + (st === "k" ? "Bị diệt" : st === "s" ? "Sống sót" : "Tương đương") + "</span>" + (st === "s" && m.hint ? "<br><small>Gợi ý: " + esc(m.hint) + "</small>" : "") + (st === "e" ? "<br><small>" + esc(m.equivNote || "Không kiểm thử nào phân biệt được: hành vi giống hệt mã gốc.") + "</small>" : "") + "</td></tr>";
      });
      var denom = c.mutants.length - eqv, score = denom ? Math.round((Math.min(killed, denom) / denom) * 100) : 0;
      mutOut.innerHTML = "<div class='meters' style='margin-bottom:.6em'><div class='meter' style='--p:" + score + "%'><b>" + score + "%</b><span>Điểm đột biến = diệt " + Math.min(killed, denom) + " / (" + c.mutants.length + " − " + eqv + " tương đương)</span><i></i></div></div><div class='tw'><table class='mut'><tr><th>Đột biến</th><th>Thay đổi</th><th>Kết quả</th></tr>" + rows + "</table></div>";
      if (c.id) W.done(c.id + ":mut", score, 100);
    }, "ghost");
    S.btn("Mã mẫu ban đầu", function () { ed.value = c.tests || ""; LS.set(key, ed.value); }, "ghost");
    if (c.solution) S.btn("Xem lời giải", function (e) { var b = e.currentTarget; if (!b.dataset.arm) { b.dataset.arm = 1; b.textContent = "Bấm lần nữa: thay mã bằng lời giải"; setTimeout(function () { delete b.dataset.arm; b.textContent = "Xem lời giải"; }, 4000); return; } delete b.dataset.arm; b.textContent = "Xem lời giải"; ed.value = c.solution; LS.set(key, ed.value); }, "ghost");
  });

  /* ------------------------------------------------------------ PROMPT LAB (CT-GenAI: 6 thành phần) */
  var PCOMP = [["role", "Vai trò (Role)", "Bạn là kỹ sư kiểm thử có kinh nghiệm với…"], ["context", "Bối cảnh (Context)", "Hệ thống, người dùng, phạm vi, điều đã biết…"],
    ["instruction", "Chỉ dẫn (Instruction)", "Nhiệm vụ cụ thể, một động từ rõ: thiết kế / rà soát / viết…"], ["input", "Dữ liệu đầu vào (Input data)", "Dán user story, tiêu chí chấp nhận, đoạn mã…"],
    ["constraints", "Ràng buộc (Constraints)", "Kỹ thuật bắt buộc, số lượng, điều không được làm, ngôn ngữ…"], ["format", "Định dạng đầu ra (Output format)", "Bảng cột…, JSON theo khóa…, Gherkin…"]];
  W.def("prompt", function (el, c) {
    var S = shell(el, c, "prompt"), key = "pl:" + (c.id || ""), saved = LS.get(key, {}) || {}, ins = {};
    if (c.task) S.body.append(h("div", { class: "fb show", html: "<b>Nhiệm vụ:</b> " + c.task }));
    var tech = saved._tech || "zero", techSeg = h("div", { class: "seg" });
    [["zero", "Zero-shot"], ["few", "Few-shot (kèm ví dụ)"], ["chain", "Prompt chaining (chia bước)"]].forEach(function (t) {
      techSeg.append(h("button", { type: "button", "aria-pressed": String(tech === t[0]), onclick: function (e) { tech = t[0]; techSeg.querySelectorAll("button").forEach(function (b) { b.setAttribute("aria-pressed", "false"); }); e.currentTarget.setAttribute("aria-pressed", "true"); exWrap.classList.toggle("hidden", tech !== "few"); chWrap.classList.toggle("hidden", tech !== "chain"); upd(); } }, t[1]));
    });
    S.body.append(h("div", { class: "fld" }, h("label", {}, "Kỹ thuật"), techSeg));
    var g = h("div", { class: "grid2" }); S.body.append(g);
    PCOMP.forEach(function (p) {
      var hint = (c.hints && c.hints[p[0]]) || p[2], ta = h("textarea", { placeholder: hint, rows: "3" }); ta.value = saved[p[0]] || "";
      ta.addEventListener("input", upd); ta.addEventListener("keydown", function (e) { e.stopPropagation(); }); ins[p[0]] = ta;
      g.append(h("div", { class: "fld" }, h("label", {}, p[1]), ta));
    });
    var ex = h("textarea", { placeholder: "Ví dụ mẫu: một đầu vào và đầu ra mong muốn", rows: "3" }); ex.value = saved._ex || ""; ex.addEventListener("input", upd); ex.addEventListener("keydown", function (e) { e.stopPropagation(); });
    var exWrap = h("div", { class: "fld " + (tech === "few" ? "" : "hidden") }, h("label", {}, "Ví dụ (few-shot)"), ex);
    var chWrap = h("div", { class: "fb show " + (tech === "chain" ? "" : "hidden"), html: c.chainNote || "<b>Prompt chaining:</b> chia việc thành nhiều prompt nối tiếp (ví dụ: 1. liệt kê điều kiện kiểm thử → bạn duyệt → 2. thiết kế ca kiểm thử cho điều kiện đã duyệt → bạn duyệt → 3. sinh mã). Kiểm tra kết quả từng bước trước khi sang bước sau." });
    var checks = h("ul", { class: "checks" }), out = h("div", { class: "pl-out", "aria-live": "polite" });
    S.body.append(exWrap, chWrap, h("div", { class: "grid2" }, h("div", { class: "fld" }, h("label", {}, "Tự kiểm tra prompt"), checks), h("div", { class: "fld" }, h("label", {}, "Prompt hoàn chỉnh"), out)));
    function val(k) { return (ins[k].value || "").trim(); }
    function upd() {
      var o = {}; PCOMP.forEach(function (p) { o[p[0]] = ins[p[0]].value; }); o._tech = tech; o._ex = ex.value; LS.set(key, o);
      var parts = [];
      PCOMP.forEach(function (p) { if (val(p[0])) parts.push("## " + p[1].replace(/ \(.+\)/, "") + "\n" + val(p[0])); });
      if (tech === "few" && ex.value.trim()) parts.push("## Ví dụ\n" + ex.value.trim());
      out.textContent = parts.join("\n\n") || "(Prompt sẽ hiện ở đây khi bạn điền các thành phần)";
      var rules = [
        [val("role").length >= 12, "Có vai trò cụ thể (ai, chuyên môn gì)"],
        [val("context").length >= 30, "Bối cảnh đủ: hệ thống, người dùng, phạm vi"],
        [/^(hãy |)?(thiết kế|liệt kê|rà soát|viết|sinh|tạo|phân tích|đánh giá|xác định|đề xuất|chuyển)/i.test(val("instruction")) || val("instruction").length >= 25, "Chỉ dẫn bắt đầu bằng hành động rõ ràng"],
        [val("input").length >= 40, "Có dữ liệu đầu vào thật (story, tiêu chí, mã…)"],
        [/\d|không|chỉ|tối đa|tối thiểu|bắt buộc|phải/i.test(val("constraints")), "Ràng buộc đo được (số lượng, kỹ thuật, điều cấm)"],
        [/bảng|json|csv|markdown|gherkin|given|cột|khóa|danh sách/i.test(val("format")), "Định dạng đầu ra máy hoặc người kiểm tra được"],
        [tech !== "few" || ex.value.trim().length >= 20, "Few-shot: có ít nhất một ví dụ"],
        [!/(mật khẩu|password|token|api[_ ]?key|số cccd|số tài khoản)/i.test(out.textContent), "Không chứa dữ liệu nhạy cảm"],
      ];
      checks.innerHTML = ""; var k = 0;
      rules.forEach(function (r) { checks.append(h("li", { class: r[0] ? "ok" : "no" }, r[1])); if (r[0]) k++; });
      S.status(k + "/" + rules.length + " tiêu chí", k === rules.length ? "ok" : ""); if (k === rules.length) W.done(c.id, 1, 1);
    }
    S.btn("Sao chép prompt", function (e) { W.copy(out.textContent, e.currentTarget); });
    if (c.sample) S.btn("Xem prompt mẫu", function () { PCOMP.forEach(function (p) { ins[p[0]].value = c.sample[p[0]] || ""; }); if (c.sample.ex) ex.value = c.sample.ex; upd(); }, "ghost");
    S.btn("Xóa", function () { PCOMP.forEach(function (p) { ins[p[0]].value = ""; }); ex.value = ""; upd(); }, "ghost");
    upd();
  });

  /* ------------------------------------------------------------ LOCATOR TRAINER (Playwright) */
  W.def("locator", function (el, c) {
    var S = shell(el, c, "locator"), mock = h("div", { class: "mock", "aria-label": "Trang mô phỏng" }), dom = {};
    c.page.forEach(function (row) {
      var r = Array.isArray(row) ? h("div", { class: "row" }) : null;
      (Array.isArray(row) ? row : [row]).forEach(function (e) {
        var node;
        if (e.tag === "input") { var inp = h("input", { type: e.type || "text", placeholder: e.placeholder || null, value: e.value || null, tabindex: "-1" }); node = e.label ? h("label", {}, e.label, inp) : inp; dom[e.id] = e.label ? node : inp; }
        else if (e.tag === "button") node = dom[e.id] = h("button", { type: "button", class: e.cls || "primary", tabindex: "-1" }, e.text);
        else if (e.tag === "a") node = dom[e.id] = h("button", { type: "button", class: "link", tabindex: "-1" }, e.text);
        else if (e.tag === "check") { var cb = h("input", { type: "checkbox", tabindex: "-1" }); node = dom[e.id] = h("label", { style: "flex-direction:row;align-items:center;gap:.4em" }, cb, e.label); }
        else node = dom[e.id] = h(e.tag || "div", { style: e.style || null }, e.text);
        (r || mock).append(node);
      });
      if (r) mock.append(r);
    });
    var els = []; c.page.forEach(function (row) { (Array.isArray(row) ? row : [row]).forEach(function (e) { els.push(e); }); });
    var ROLE = { button: "button", a: "link", h1: "heading", h2: "heading", check: "checkbox" };
    function role(e) { return e.role || (e.tag === "input" ? (e.type === "password" ? null : "textbox") : ROLE[e.tag] || null); }
    function aname(e) { return e.tag === "input" || e.tag === "check" ? e.aria || e.label || "" : e.aria || e.text || ""; }
    function txt(e) { return e.tag === "input" ? "" : e.tag === "check" ? e.label || "" : e.text || ""; }
    function nm(a, pat, exact) {
      a = (a || "").replace(/\s+/g, " ").trim();
      if (pat.re) return pat.re.test(a);
      return exact ? a === pat.s : a.toLowerCase().indexOf(pat.s.toLowerCase()) >= 0;
    }
    function parsePat(s) { var m = s.match(/^\/(.*)\/([a-z]*)$/); return m ? { re: new RegExp(m[1], m[2]) } : { s: s.replace(/^['"`]|['"`]$/g, "") }; }
    function evalLoc(q) {
      q = q.trim().replace(/^await\s+/, "").replace(/^page\./, "").replace(/\.(click|fill|check|press|hover)\(.*\)\s*;?$/, "").replace(/;$/, "");
      var m, opt = function (o, k) { var r = new RegExp(k + "\\s*:\\s*(\\/[^/]+\\/[a-z]*|'[^']*'|\"[^\"]*\"|true|false)").exec(o || ""); return r ? r[1] : null; };
      if ((m = q.match(/^getByRole\(\s*['"](\w+)['"]\s*(?:,\s*\{([\s\S]*)\})?\s*\)$/))) {
        var nmv = opt(m[2], "name"), ex = opt(m[2], "exact") === "true";
        return { kind: "role", stars: 3, hits: els.filter(function (e) { return role(e) === m[1] && (!nmv || nm(aname(e), parsePat(nmv), ex)); }) };
      }
      if ((m = q.match(/^getByLabel\(\s*(\/[^/]+\/[a-z]*|['"][^'"]*['"])\s*(?:,\s*\{([\s\S]*)\})?\s*\)$/))) { var ex2 = opt(m[2], "exact") === "true"; return { kind: "label", stars: 3, hits: els.filter(function (e) { return (e.tag === "input" || e.tag === "check") && e.label && nm(e.label, parsePat(m[1]), ex2); }) }; }
      if ((m = q.match(/^getByPlaceholder\(\s*(\/[^/]+\/[a-z]*|['"][^'"]*['"])\s*\)$/))) return { kind: "placeholder", stars: 2, hits: els.filter(function (e) { return e.placeholder && nm(e.placeholder, parsePat(m[1])); }) };
      if ((m = q.match(/^getByText\(\s*(\/[^/]+\/[a-z]*|['"][^'"]*['"])\s*(?:,\s*\{([\s\S]*)\})?\s*\)$/))) { var ex3 = opt(m[2], "exact") === "true"; return { kind: "text", stars: 2, hits: els.filter(function (e) { return txt(e) && nm(txt(e), parsePat(m[1]), ex3); }) }; }
      if ((m = q.match(/^getByTestId\(\s*['"]([^'"]+)['"]\s*\)$/))) return { kind: "testid", stars: 2, hits: els.filter(function (e) { return e.testid === m[1]; }) };
      if ((m = q.match(/^locator\(\s*['"](.+)['"]\s*\)$/))) {
        var css = m[1].trim(), hits = els.filter(function (e) {
          var mm;
          if ((mm = css.match(/^\[data-testid=['"]?([^'"\]]+)['"]?\]$/))) return e.testid === mm[1];
          if ((mm = css.match(/^#([\w-]+)$/))) return e.domid === mm[1];
          if ((mm = css.match(/^(\w+)?\.([\w-]+)$/))) return (!mm[1] || e.tag === mm[1]) && (e.css || "").split(" ").indexOf(mm[2]) >= 0;
          if ((mm = css.match(/^(\w+)$/))) return (e.tag === "check" ? "input" : e.tag) === mm[1];
          if ((mm = css.match(/^(\w+):nth-child\((\d+)\)$/)) || (mm = css.match(/^(\w+)\s*>>\s*nth=(\d+)$/))) return false;
          return false;
        });
        return { kind: "css", stars: /data-testid/.test(css) ? 2 : 1, hits: hits };
      }
      return { error: "Chưa nhận dạng được cú pháp. Thử: getByRole('button', { name: 'Đăng nhập' })" };
    }
    var tasks = h("ol", { class: "tasks" }), cur = 0, stars = LS.get("loc:" + (c.id || ""), {}) || {};
    c.tasks.forEach(function (t, i) { var li = h("li", { "data-stars": "" }, h("span", { html: (i + 1) + ". " + t.say })); li.onclick = function () { cur = i; drawTasks(); }; tasks.append(li); });
    function drawTasks() { tasks.querySelectorAll("li").forEach(function (li, i) { li.className = (i === cur ? "on " : "") + (stars[i] ? "done" : ""); li.setAttribute("data-stars", stars[i] ? "★★★".slice(0, stars[i]) : ""); }); }
    var inp = h("input", { type: "text", spellcheck: "false", placeholder: "page.getByRole('button', { name: '…' })", "aria-label": "Biểu thức locator" }), fb = h("div", { class: "fb" });
    inp.addEventListener("keydown", function (e) { e.stopPropagation(); if (e.key === "Enter") run(); });
    function run() {
      Object.keys(dom).forEach(function (k) { dom[k].classList.remove("hit", "hit-ok"); });
      var r = evalLoc(inp.value); if (r.error) { fb.className = "fb show no"; fb.textContent = r.error; return; }
      r.hits.forEach(function (e) { dom[e.id].classList.add("hit"); });
      var t = c.tasks[cur], ok = r.hits.length === 1 && r.hits[0].id === t.target;
      var msg = "Khớp " + r.hits.length + " phần tử. ";
      if (r.hits.length > 1) msg += "Playwright ở chế độ strict: thao tác trên locator khớp nhiều phần tử sẽ báo lỗi. Hãy thu hẹp (thêm name, exact: true…). ";
      if (r.hits.length === 0) msg += "Không tìm thấy phần tử nào. ";
      if (ok) {
        dom[t.target].classList.remove("hit"); dom[t.target].classList.add("hit-ok");
        msg = "Đúng phần tử, duy nhất. Độ bền: " + "★★★".slice(0, r.stars) + "☆☆☆".slice(0, 3 - r.stars) + ". " + (r.stars === 3 ? "Locator theo vai trò/nhãn mà người dùng nhìn thấy, ít gãy khi đổi giao diện." : r.stars === 2 ? "Dùng được. Ưu tiên getByRole/getByLabel nếu có thể." : "CSS phụ thuộc cấu trúc DOM, dễ gãy khi đổi giao diện.");
        stars[cur] = Math.max(stars[cur] || 0, r.stars); LS.set("loc:" + (c.id || ""), stars); drawTasks();
        var n = Object.keys(stars).length; S.status(n + "/" + c.tasks.length + " nhiệm vụ", n === c.tasks.length ? "ok" : ""); if (n === c.tasks.length) W.done(c.id, 1, 1);
      } else if (r.hits.length === 1) msg += "Nhưng đây không phải phần tử nhiệm vụ yêu cầu.";
      fb.className = "fb show " + (ok ? "ok" : "no"); fb.textContent = msg;
    }
    S.body.append(h("div", { class: "grid2" }, mock, h("div", { class: "fld" }, h("label", {}, "Nhiệm vụ (chọn một)"), tasks)), h("div", { class: "loc-in" }, inp, h("button", { type: "button", class: "btn sm", onclick: run }, "Thử")), fb);
    drawTasks(); S.status(Object.keys(stars).length + "/" + c.tasks.length + " nhiệm vụ");
  });

  /* ------------------------------------------------------------ RISK MATRIX */
  W.def("risk", function (el, c) {
    var S = shell(el, c, "risk"), rows = h("div", { class: "rows" }), val = c.items.map(function () { return { L: 0, I: 0 }; });
    var lv = ["", "Thấp", "Trung bình", "Cao"];
    c.items.forEach(function (it, i) {
      var mk = function (k) { var s = h("select", { "aria-label": k }); ["—", "1 · Thấp", "2 · TB", "3 · Cao"].forEach(function (t, j) { s.append(h("option", { value: j }, t)); }); s.onchange = function () { val[i][k] = +s.value; grid(); }; return s; };
      var row = h("div", { class: "row-i" }, h("span", { class: "t", html: "<b>R" + (i + 1) + "</b> " + it.t }), h("label", { style: "font-size:.8em;color:var(--muted)" }, "Khả năng ", mk("L")), h("label", { style: "font-size:.8em;color:var(--muted)" }, "Tác động ", mk("I")));
      rows.append(row); it._row = row;
    });
    var rm = h("div", { class: "rm" }), pri = h("div", { class: "fld" });
    S.body.append(rows, h("div", { class: "grid2" }, h("div", { class: "fld" }, h("label", {}, "Ma trận (dọc: khả năng, ngang: tác động)"), rm), pri));
    function grid() {
      rm.innerHTML = "";
      for (var L = 3; L >= 1; L--) { rm.append(h("div", { class: "ax" }, String(L))); for (var I = 1; I <= 3; I++) { var sc = L * I, cell = h("div", { class: "c " + (sc >= 6 ? "hi" : sc >= 3 ? "me" : "lo") }); val.forEach(function (v, i) { if (v.L === L && v.I === I) cell.append(h("span", { class: "dot" }, "R" + (i + 1))); }); rm.append(cell); } }
      rm.append(h("div")); ["Tác động 1", "2", "3"].forEach(function (t) { rm.append(h("div", { class: "ax" }, t)); });
      var list = val.map(function (v, i) { return { i: i, s: v.L * v.I }; }).filter(function (x) { return x.s; }).sort(function (a, b) { return b.s - a.s; });
      pri.innerHTML = "<label style='font:600 .8em var(--f-mono);color:var(--muted)'>Thứ tự ưu tiên kiểm thử (điểm = khả năng × tác động)</label>" + (list.length ? "<ol style='margin:.3em 0 0;padding-left:1.4em'>" + list.map(function (x) { return "<li><b>R" + (x.i + 1) + "</b> · " + x.s + " điểm · " + c.items[x.i].t + "</li>"; }).join("") + "</ol>" : "<p class='w-intro'>Chấm khả năng và tác động cho từng rủi ro.</p>");
    }
    S.btn("So sánh với gợi ý của giảng viên", function () {
      var d = 0; c.items.forEach(function (it, i) { var off = Math.abs(it.L - val[i].L) + Math.abs(it.I - val[i].I); d += off; var ex = it._row.querySelector(".ex") || h("div", { class: "ex" }); ex.innerHTML = "Gợi ý: khả năng " + it.L + ", tác động " + it.I + ". " + (it.why || ""); it._row.append(ex); it._row.className = "row-i " + (off === 0 ? "right" : off <= 1 ? "" : "wrong"); });
      S.status(d === 0 ? "Trùng hoàn toàn với gợi ý" : "Lệch tổng " + d + " bậc. Rủi ro là đánh giá có lý do: hãy so lập luận, không chỉ con số.", d <= c.items.length ? "ok" : "");
      W.done(c.id, 1, 1);
    });
    grid();
  });

  /* ------------------------------------------------------------ PERT (ước lượng 3 điểm) */
  W.def("pert", function (el, c) {
    var S = shell(el, c, "pert"), f = {};
    var g = h("div", { class: "grid3" });
    [["a", "Lạc quan (a)"], ["m", "Khả dĩ nhất (m)"], ["b", "Bi quan (b)"]].forEach(function (x) { var i = h("input", { type: "text", inputmode: "decimal", value: c[x[0]] != null ? String(c[x[0]]) : "" }); i.oninput = calc; f[x[0]] = i; g.append(h("div", { class: "fld" }, h("label", {}, x[1] + (c.unit ? " · " + c.unit : "")), i)); });
    var out = h("div", { class: "meters" }); S.body.append(g, out);
    function n(k) { return parseFloat(String(f[k].value).replace(",", ".")); }
    function calc() {
      var a = n("a"), m = n("m"), b = n("b"); out.innerHTML = "";
      if ([a, m, b].some(isNaN)) return; var E = (a + 4 * m + b) / 6, SD = (b - a) / 6, r = function (x) { return (Math.round(x * 100) / 100).toString().replace(".", ","); };
      [["E = (a + 4m + b) / 6", r(E)], ["Độ lệch chuẩn SD = (b − a) / 6", r(SD)], ["Khoảng ước lượng E ± SD", r(E - SD) + " – " + r(E + SD)]].forEach(function (x) { out.append(h("div", { class: "meter" }, h("b", {}, x[1]), h("span", {}, x[0]))); });
    }
    calc();
  });

  /* ------------------------------------------------------------ FORM (biểu mẫu có kiểm tra) */
  W.def("form", function (el, c) {
    var S = shell(el, c, "form"), key = "fm:" + (c.id || ""), saved = LS.get(key, {}) || {}, ins = {};
    var g = h("div", { class: c.cols === 1 ? "" : "grid2", style: c.cols === 1 ? "display:flex;flex-direction:column;gap:.8em" : "" }); S.body.append(g);
    c.fields.forEach(function (fd) {
      var i;
      if (fd.type === "select") { i = h("select", {}, h("option", { value: "" }, "— chọn —")); fd.opts.forEach(function (o) { i.append(h("option", { value: o }, o)); }); }
      else i = h(fd.type === "area" ? "textarea" : "input", { placeholder: fd.ph || "" });
      i.value = saved[fd.k] || ""; i.addEventListener("input", save); i.addEventListener("change", save); i.addEventListener("keydown", function (e) { e.stopPropagation(); }); ins[fd.k] = i;
      g.append(h("div", { class: "fld", style: fd.wide ? "grid-column:1/-1" : "" }, h("label", {}, fd.label + (fd.req ? " *" : "")), i, fd.hint ? h("span", { class: "hint", html: fd.hint }) : null));
    });
    var issues = h("ul", { class: "checks" }), prev = h("div", { class: "preview hidden" }); S.body.append(issues, prev);
    function save() { var o = {}; c.fields.forEach(function (fd) { o[fd.k] = ins[fd.k].value; }); LS.set(key, o); }
    S.btn("Kiểm tra", function () {
      issues.innerHTML = ""; var bad = 0;
      c.fields.forEach(function (fd) {
        var v = ins[fd.k].value.trim(), ok = true, why = "";
        if (fd.req && !v) { ok = false; why = "chưa điền"; }
        else if (fd.min && v.length < fd.min) { ok = false; why = "quá ngắn (cần chi tiết hơn)"; }
        else if (fd.re && v && !new RegExp(fd.re, "i").test(v)) { ok = false; why = fd.reMsg || "chưa đúng dạng"; }
        if (fd.req || v) { issues.append(h("li", { class: ok ? "ok" : "no" }, fd.label + (ok ? "" : ": " + why))); if (!ok) bad++; }
      });
      (c.rules || []).forEach(function (r) { var ok = new Function("v", "return (" + r[0] + ")")(Object.fromEntries(c.fields.map(function (fd) { return [fd.k, ins[fd.k].value.trim()]; }))); issues.append(h("li", { class: ok ? "ok" : "no" }, r[1])); if (!ok) bad++; });
      S.status(bad ? bad + " điểm cần sửa" : "Đầy đủ, có thể nộp", bad ? "bad" : "ok"); if (!bad) W.done(c.id, 1, 1);
    });
    S.btn("Xem bản Markdown", function () { prev.classList.remove("hidden"); prev.textContent = (c.mdTitle ? "## " + c.mdTitle + "\n" : "") + c.fields.map(function (fd) { return "**" + fd.label + ":** " + (ins[fd.k].value || "…"); }).join("\n"); }, "ghost");
    S.btn("Sao chép", function (e) { W.copy(c.fields.map(function (fd) { return fd.label + ": " + ins[fd.k].value; }).join("\n"), e.currentTarget); }, "ghost");
    if (c.sample) S.btn("Điền mẫu", function () { c.fields.forEach(function (fd) { if (c.sample[fd.k] != null) ins[fd.k].value = c.sample[fd.k]; }); save(); }, "ghost");
  });

  /* ------------------------------------------------------------ POLL (đếm giơ tay trên lớp) */
  W.def("poll", function (el, c) {
    var S = shell(el, c, "poll"), cnt = c.opts.map(function () { return 0; }), box = h("div", { class: "poll" });
    if (c.q) S.body.append(h("div", { class: "q-t", html: "<div>" + c.q + "</div>" }));
    var btns = c.opts.map(function (o, i) { var b = h("button", { type: "button", class: "pb" }, h("span", { html: "<b style='color:var(--muted);font-size:.8em'>" + "ABCDEFG"[i] + "</b>&nbsp; " + o }), h("b", {}, "0")); b.onclick = function () { cnt[i]++; draw(); }; box.append(b); return b; });
    var fb = h("div", { class: "fb" }); S.body.append(box, fb);
    function draw() { var t = cnt.reduce(function (a, b) { return a + b; }, 0) || 1; btns.forEach(function (b, i) { b.style.setProperty("--p", Math.round((cnt[i] / t) * 100) + "%"); b.lastChild.textContent = cnt[i]; }); S.status("Tổng " + cnt.reduce(function (a, b) { return a + b; }, 0) + " phiếu · bấm vào phương án để cộng phiếu"); }
    if (c.ans != null) S.btn("Hiện đáp án", function () { (Array.isArray(c.ans) ? c.ans : [c.ans]).forEach(function (i) { btns[i].classList.add("ans"); }); fb.className = "fb show ok"; fb.innerHTML = c.exp || ""; });
    S.btn("Đặt lại", function () { cnt = cnt.map(function () { return 0; }); btns.forEach(function (b) { b.classList.remove("ans"); }); fb.className = "fb"; draw(); }, "ghost");
    draw();
  });

  /* ------------------------------------------------------------ TIMER */
  W.def("timer", function (el, c) {
    var S = shell(el, c, "timer"), total = (c.min || 5) * 60, left = total, t = null;
    var clock = h("span", { class: "clock" }), box = h("div", { class: "timer" }, clock);
    if (c.steps) S.body.append(h("ol", { style: "margin:0;padding-left:1.3em", html: c.steps.map(function (s) { return "<li>" + s + "</li>"; }).join("") }));
    S.body.append(box);
    function fmt() { clock.textContent = String(Math.floor(left / 60)).padStart(2, "0") + ":" + String(left % 60).padStart(2, "0"); box.classList.toggle("end", left === 0); }
    function beep() { try { var a = new (window.AudioContext || window.webkitAudioContext)(), o = a.createOscillator(); o.frequency.value = 880; o.connect(a.destination); o.start(); setTimeout(function () { o.stop(); a.close(); }, 400); } catch (e) {} }
    var go = S.btn("Bắt đầu", function () {
      if (t) { clearInterval(t); t = null; go.textContent = "Tiếp tục"; return; }
      go.textContent = "Tạm dừng"; t = setInterval(function () { if (left > 0) { left--; fmt(); if (!left) { clearInterval(t); t = null; beep(); go.textContent = "Bắt đầu"; } } }, 1000);
    });
    S.btn("Đặt lại", function () { clearInterval(t); t = null; left = total; go.textContent = "Bắt đầu"; fmt(); }, "ghost");
    S.btn("+1 phút", function () { left += 60; fmt(); }, "ghost");
    fmt();
  });

  /* ------------------------------------------------------------ tiện ích chung: nút sao chép trong khối prompt/mã */
  document.addEventListener("click", function (e) {
    var b = e.target.closest("[data-copy]"); if (!b) return;
    var t = document.getElementById(b.getAttribute("data-copy")); if (t) W.copy(t.innerText, b);
  });
  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", function () { W.mount(); }); else W.mount();
})();
