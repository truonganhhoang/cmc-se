/* Trình chiếu tương tác: bước hiện (fragment), ghi chú giảng viên, tổng quan, vẽ, bút laser, chế độ tự học, hẹn giờ. */
(function () {
  "use strict";
  var $ = function (s, r) { return (r || document).querySelector(s); }, $$ = function (s, r) { return Array.prototype.slice.call((r || document).querySelectorAll(s)); };
  var root = document.documentElement, body = document.body;
  try { var th = localStorage.getItem("s4003:theme"); if (th) root.setAttribute("data-theme", th); } catch (e) {}
  var vp = $(".vp"), stage = $(".stage"), slides = $$(".slide", stage), N = slides.length, cur = 0;
  var deckId = body.getAttribute("data-deck") || "deck";
  var prog = $(".prog i"), ttl = $(".hud .ttl"), num = $(".st-num"), cap = $(".cap"), np = $(".notes-panel .nb"), nnext = $(".notes-panel .next"), nhead = $(".notes-panel header span");

  function fit() {
    var w = vp.clientWidth, hh = vp.clientHeight, s = Math.min(w / 1600, hh / 900);
    stage.style.transform = "scale(" + s + ")";
    stage.style.left = Math.max(0, (w - 1600 * s) / 2) + "px"; stage.style.top = Math.max(0, (hh - 900 * s) / 2) + "px";
    stage._s = s;
  }
  window.addEventListener("resize", fit);

  function frags(sl) { return $$(".f", sl); }
  function show(i, step) {
    i = Math.max(0, Math.min(N - 1, i));
    var changed = i !== cur || !slides[i].classList.contains("on");
    slides.forEach(function (s, k) { s.classList.toggle("on", k === i); });
    cur = i; var fr = frags(slides[i]);
    var st = step == null ? 0 : step === "all" ? fr.length : step;
    fr.forEach(function (f, k) { f.classList.toggle("vis", k < st); });
    slides[i]._step = st;
    if (changed) { clearInk(); }
    var t = slides[i].getAttribute("data-title") || "";
    if (ttl) ttl.innerHTML = "<b>" + (i + 1) + "/" + N + "</b> · " + t;
    if (num) num.textContent = String(i + 1).padStart(2, "0") + " / " + String(N).padStart(2, "0");
    if (prog) prog.style.width = ((i + 1) / N) * 100 + "%";
    var note = $(".notes", slides[i]);
    if (np) np.innerHTML = note ? note.innerHTML : "<p class='muted'>Không có ghi chú.</p>";
    if (nhead) nhead.textContent = "Slide " + (i + 1) + "/" + N + " · " + t;
    if (nnext) nnext.textContent = i < N - 1 ? "Tiếp theo: " + (slides[i + 1].getAttribute("data-title") || "") : "Slide cuối";
    if (cap) { var plain = note ? note.textContent.replace(/\s+/g, " ").trim() : ""; cap.innerHTML = plain ? "<div>" + plain.slice(0, 420) + (plain.length > 420 ? "…" : "") + "</div>" : ""; }
    try { history.replaceState(null, "", "#" + (i + 1)); localStorage.setItem("s4003:deck:" + deckId, String(i)); } catch (e) {}
    $$(".ov-item").forEach(function (o, k) { o.classList.toggle("cur", k === i); });
  }
  function next() { var sl = slides[cur], fr = frags(sl), st = sl._step || 0; if (st < fr.length) { fr[st].classList.add("vis"); sl._step = st + 1; } else if (cur < N - 1) show(cur + 1, 0); }
  function prev() { var sl = slides[cur], fr = frags(sl), st = sl._step || 0; if (st > 0) { fr[st - 1].classList.remove("vis"); sl._step = st - 1; } else if (cur > 0) show(cur - 1, "all"); }

  /* toggles */
  function tog(cls, force) { var on = body.classList.toggle(cls, force); $$('[data-tog="' + cls + '"]').forEach(function (b) { b.setAttribute("aria-pressed", String(on)); }); if (cls === "show-notes") setTimeout(fit, 260); return on; }
  /* ink */
  var ink = $("#ink"), ctx = ink.getContext("2d"), drawing = false, last = null;
  ink.width = 1600; ink.height = 900;
  function clearInk() { ctx.clearRect(0, 0, 1600, 900); }
  function pt(e) { var r = stage.getBoundingClientRect(), s = stage._s || 1; return [(e.clientX - r.left) / s, (e.clientY - r.top) / s]; }
  ink.addEventListener("pointerdown", function (e) { drawing = true; last = pt(e); ink.setPointerCapture(e.pointerId); });
  ink.addEventListener("pointermove", function (e) { if (!drawing) return; var p = pt(e); ctx.strokeStyle = "#FFB547"; ctx.lineWidth = 5; ctx.lineCap = "round"; ctx.beginPath(); ctx.moveTo(last[0], last[1]); ctx.lineTo(p[0], p[1]); ctx.stroke(); last = p; });
  ink.addEventListener("pointerup", function () { drawing = false; });
  var laser = $("#laser");
  stage.addEventListener("pointermove", function (e) { if (!body.classList.contains("lasering")) return; var p = pt(e); laser.style.left = p[0] + "px"; laser.style.top = p[1] + "px"; });

  /* clock */
  var t0 = null, tick = null, clockEl = $(".hud .clock");
  function clock(on) {
    if (on === false || tick) { clearInterval(tick); tick = null; clockEl.textContent = "⏱"; return; }
    t0 = Date.now(); tick = setInterval(function () { var s = Math.floor((Date.now() - t0) / 1000); clockEl.textContent = String(Math.floor(s / 60)).padStart(2, "0") + ":" + String(s % 60).padStart(2, "0"); }, 1000); clockEl.textContent = "00:00";
  }

  /* overview */
  var ov = $(".ov-grid"), built = false;
  function buildOv() {
    if (built) return; built = true;
    slides.forEach(function (s, k) {
      var it = document.createElement("button"); it.type = "button"; it.className = "ov-item";
      var th = document.createElement("div"); th.className = "ov-thumb"; var inner = document.createElement("div");
      var cl = s.cloneNode(true); cl.classList.add("on"); $$("[id]", cl).forEach(function (x) { x.removeAttribute("id"); });
      inner.append(cl); th.append(inner); it.append(th);
      var sp = document.createElement("span"); sp.textContent = (k + 1) + ". " + (s.getAttribute("data-title") || ""); it.append(sp);
      it.onclick = function () { tog("overview", false); show(k, 0); };
      ov.append(it);
      requestAnimationFrame(function () { inner.style.transform = "scale(" + th.clientWidth / 1600 + ")"; });
    });
    window.addEventListener("resize", function () { $$(".ov-thumb", ov).forEach(function (t) { t.firstChild.style.transform = "scale(" + t.clientWidth / 1600 + ")"; }); });
  }

  /* keyboard */
  var jump = "";
  document.addEventListener("keydown", function (e) {
    var t = e.target, tag = (t.tagName || "").toLowerCase();
    if (tag === "input" || tag === "textarea" || tag === "select" || t.isContentEditable) return;
    if (e.ctrlKey || e.metaKey || e.altKey) return;
    var k = e.key;
    if (/^\d$/.test(k)) { jump += k; return; }
    if (k === "Enter" && jump) { show(parseInt(jump, 10) - 1, 0); jump = ""; return; }
    jump = "";
    if (k === "ArrowRight" || k === "PageDown" || (k === " " && tag !== "button")) { e.preventDefault(); next(); }
    else if (k === "ArrowLeft" || k === "PageUp") { e.preventDefault(); prev(); }
    else if (k === "Home") show(0, 0); else if (k === "End") show(N - 1, "all");
    else if (k === "o" || k === "O") { buildOv(); tog("overview"); }
    else if (k === "n" || k === "N") tog("show-notes");
    else if (k === "s" || k === "S") tog("selfstudy");
    else if (k === "d" || k === "D") { tog("lasering", false); tog("drawing"); }
    else if (k === "c" || k === "C") clearInk();
    else if (k === "l" || k === "L") { tog("drawing", false); tog("lasering"); }
    else if (k === "b" || k === "B" || k === ".") tog("blackout");
    else if (k === "t" || k === "T") clock();
    else if (k === "f" || k === "F") fs();
    else if (k === "?" || k === "h" || k === "H") tog("show-help");
    else if (k === "Escape") { tog("overview", false); tog("show-help", false); tog("blackout", false); tog("drawing", false); tog("lasering", false); }
  });
  function fs() { try { if (!document.fullscreenElement) root.requestFullscreen(); else document.exitFullscreen(); } catch (e) {} }

  /* touch swipe (bỏ qua khi chạm trong hoạt động) */
  var sx = null;
  vp.addEventListener("touchstart", function (e) { if (e.target.closest(".w") || body.classList.contains("drawing")) { sx = null; return; } sx = e.touches[0].clientX; }, { passive: true });
  vp.addEventListener("touchend", function (e) { if (sx == null) return; var dx = e.changedTouches[0].clientX - sx; if (Math.abs(dx) > 50) (dx < 0 ? next : prev)(); sx = null; });

  /* HUD buttons */
  $$("[data-act]").forEach(function (b) {
    b.addEventListener("click", function () {
      var a = b.getAttribute("data-act");
      if (a === "next") next(); else if (a === "prev") prev();
      else if (a === "ov") { buildOv(); tog("overview"); }
      else if (a === "fs") fs(); else if (a === "clock") clock();
      else if (a === "theme") { var th = root.getAttribute("data-theme") === "light" ? "dark" : "light"; root.setAttribute("data-theme", th); try { localStorage.setItem("s4003:theme", th); } catch (e) {} }
      else if (a === "draw") { tog("lasering", false); tog("drawing"); }
      else if (a === "laser") { tog("drawing", false); tog("lasering"); }
      else tog(a);
      b.blur();
    });
  });

  fit();
  var start = parseInt((location.hash || "").replace("#", ""), 10);
  if (!start) { try { start = parseInt(localStorage.getItem("s4003:deck:" + deckId), 10) + 1; } catch (e) {} }
  show((start || 1) - 1, 0);
  if (/[?&]self/.test(location.search)) tog("selfstudy", true);
  window.addEventListener("hashchange", function () { var n = parseInt(location.hash.replace("#", ""), 10); if (n && n - 1 !== cur) show(n - 1, 0); });
})();
