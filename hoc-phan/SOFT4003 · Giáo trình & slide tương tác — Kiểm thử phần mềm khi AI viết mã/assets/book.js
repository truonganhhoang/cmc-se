/* Giáo trình: mục lục theo cuộn, đánh dấu đã học, tiến độ chương, chủ đề sáng/tối, bước lab. */
(function () {
  "use strict";
  var $ = function (s, r) { return (r || document).querySelector(s); }, $$ = function (s, r) { return Array.prototype.slice.call((r || document).querySelectorAll(s)); };
  var root = document.documentElement, ch = document.body.getAttribute("data-ch") || "x", LS = window.W ? W.LS : { get: function (k, d) { return d; }, set: function () {} };
  var th = LS.get("theme-book", null); if (th) root.setAttribute("data-theme", th);
  $$("[data-theme-toggle]").forEach(function (b) { b.addEventListener("click", function () { var t = root.getAttribute("data-theme") === "light" ? "dark" : "light"; root.setAttribute("data-theme", t); LS.set("theme-book", t); }); });

  var secs = $$(".sec"), links = $$(".toc a[data-s]"), done = LS.get("done:" + ch, {}) || {};
  function ring() {
    var n = secs.length, d = secs.filter(function (s) { return done[s.id]; }).length;
    var quiz = LS.get("w:" + ch + "-final", null), q = quiz ? quiz.best / quiz.m : 0;
    var p = Math.round(((d / n) * 0.7 + q * 0.3) * 100);
    var r = $(".toc .ring"); if (!r) return;
    var C = 2 * Math.PI * 18;
    r.innerHTML = '<svg viewBox="0 0 46 46"><circle cx="23" cy="23" r="18" fill="none" stroke="var(--line)" stroke-width="5"/><circle cx="23" cy="23" r="18" fill="none" stroke="var(--amber)" stroke-width="5" stroke-linecap="round" stroke-dasharray="' + C + '" stroke-dashoffset="' + C * (1 - p / 100) + '" transform="rotate(-90 23 23)"/></svg><div><b>' + p + "%</b><span>" + d + "/" + n + " mục · kiểm tra " + (quiz ? quiz.best + "/" + quiz.m : "chưa làm") + "</span></div>";
    LS.set("prog:" + ch, { p: p, d: d, n: n, q: quiz ? quiz.best + "/" + quiz.m : null });
    links.forEach(function (a) { a.classList.toggle("done", !!done[a.getAttribute("data-s")]); var ck = a.querySelector(".ck"); if (ck) ck.textContent = done[a.getAttribute("data-s")] ? "✓" : "○"; });
  }
  $$(".done-btn").forEach(function (b) {
    var id = b.getAttribute("data-s"); b.setAttribute("aria-pressed", String(!!done[id])); b.textContent = done[id] ? "✓ Đã học xong mục này" : "Đánh dấu đã học xong mục này";
    b.addEventListener("click", function () { done[id] = !done[id]; LS.set("done:" + ch, done); b.setAttribute("aria-pressed", String(!!done[id])); b.textContent = done[id] ? "✓ Đã học xong mục này" : "Đánh dấu đã học xong mục này"; ring(); });
  });
  document.addEventListener("w-done", ring);

  var bar = $(".readbar i");
  function spy() {
    var y = window.scrollY + innerHeight * 0.3, k = 0;
    secs.forEach(function (s, i) { if (s.offsetTop <= y) k = i; });
    links.forEach(function (a, i) { a.classList.toggle("on", i === k); });
    if (bar) { var hgt = document.documentElement.scrollHeight - innerHeight; bar.style.width = (hgt > 0 ? (window.scrollY / hgt) * 100 : 0) + "%"; }
  }
  var tk = false; window.addEventListener("scroll", function () { if (!tk) { tk = true; requestAnimationFrame(function () { spy(); tk = false; }); } }, { passive: true });

  /* bước lab có ô đánh dấu */
  $$(".steps").forEach(function (ol, oi) {
    var key = "steps:" + ch + ":" + oi, st = LS.get(key, {}) || {};
    $$("li", ol).forEach(function (li, i) {
      var cb = li.querySelector("input"); if (!cb) return; cb.checked = !!st[i]; li.classList.toggle("ok", cb.checked);
      cb.addEventListener("change", function () { st[i] = cb.checked; LS.set(key, st); li.classList.toggle("ok", cb.checked); });
    });
  });
  ring(); spy();
})();
