/* SocialBrand Bots: site behaviour. No tracking, no cookies, no backend.
   Upvotes are stored in this browser only (localStorage). */
(function () {
  "use strict";
  var CFG = window.SB_CONFIG || { installLinks: {}, site: "https://bots.socialbrand.africa", brandLine: "By SocialBrand · socialbrand.africa" };
  var store = {
    get: function (k) { try { return window.localStorage.getItem(k); } catch (e) { return null; } },
    set: function (k, v) { try { window.localStorage.setItem(k, v); } catch (e) {} },
    del: function (k) { try { window.localStorage.removeItem(k); } catch (e) {} }
  };
  function $(s, r) { return (r || document).querySelector(s); }
  function $$(s, r) { return Array.prototype.slice.call((r || document).querySelectorAll(s)); }

  /* Toast */
  var toastEl;
  function toast(msg) {
    if (!toastEl) { toastEl = document.createElement("div"); toastEl.className = "toast"; toastEl.setAttribute("role", "status"); document.body.appendChild(toastEl); }
    toastEl.textContent = msg; toastEl.classList.add("show");
    clearTimeout(toastEl._t); toastEl._t = setTimeout(function () { toastEl.classList.remove("show"); }, 1600);
  }

  /* Clipboard with fallback for non-secure contexts */
  function copy(text) {
    if (navigator.clipboard && window.isSecureContext) {
      return navigator.clipboard.writeText(text).catch(function () { return legacyCopy(text); });
    }
    return legacyCopy(text);
  }
  function legacyCopy(text) {
    return new Promise(function (resolve, reject) {
      var ta = document.createElement("textarea");
      ta.value = text; ta.setAttribute("readonly", ""); ta.style.position = "fixed"; ta.style.opacity = "0";
      document.body.appendChild(ta); ta.select();
      try { document.execCommand("copy") ? resolve() : reject(new Error("copy failed")); } catch (e) { reject(e); }
      document.body.removeChild(ta);
    });
  }
  function flashBtn(btn) {
    if (!btn) return;
    var orig = btn.getAttribute("data-label") || btn.textContent;
    btn.setAttribute("data-label", orig);
    btn.textContent = "Copied!"; btn.classList.add("copied");
    setTimeout(function () { btn.textContent = orig; btn.classList.remove("copied"); }, 1400);
  }
  function textOf(id) {
    var el = document.getElementById(id);
    if (!el) return "";
    return (el.tagName === "TEXTAREA" ? el.value : el.textContent).replace(/^\n+|\s+$/g, "");
  }

  document.addEventListener("click", function (e) {
    var b = e.target.closest("[data-copy]");
    if (b) {
      e.preventDefault();
      copy(textOf(b.getAttribute("data-copy"))).then(function () { flashBtn(b); }, function () { toast("Select the text and copy it by hand"); });
      return;
    }
    var s = e.target.closest("[data-toggle]");
    if (s) {
      var el = document.getElementById(s.getAttribute("data-toggle"));
      if (el) { el.classList.toggle("truncated"); s.textContent = el.classList.contains("truncated") ? "Show all" : "Show less"; }
      return;
    }
    var u = e.target.closest("[data-upvote]");
    if (u) { e.preventDefault(); e.stopPropagation(); toggleVote(u.getAttribute("data-upvote")); return; }
    var sh = e.target.closest("[data-share]");
    if (sh) { e.preventDefault(); e.stopPropagation(); openShare(sh); return; }
    if (e.target.closest("[data-close-share]") || (e.target.id === "share-modal")) { closeShare(); }
  });

  /* Upvotes (this device only) */
  function voted(slug) { return store.get("sb-upvote-" + slug) === "1"; }
  function toggleVote(slug) {
    if (voted(slug)) store.del("sb-upvote-" + slug); else store.set("sb-upvote-" + slug, "1");
    renderVotes();
    if (voted(slug)) toast("Upvoted. Saved on this device.");
  }
  function renderVotes() {
    $$("[data-upvote]").forEach(function (b) {
      var on = voted(b.getAttribute("data-upvote"));
      b.classList.toggle("voted", on);
      b.setAttribute("aria-pressed", on ? "true" : "false");
      b.textContent = on ? "▲ Upvoted" : "▲ Upvote";
    });
  }

  /* Install links from config */
  function renderInstall() {
    $$("[data-install]").forEach(function (box) {
      var slug = box.getAttribute("data-install");
      var link = (CFG.installLinks || {})[slug] || "";
      box.innerHTML = "";
      if (link) {
        var a = document.createElement("a");
        a.href = link; a.target = "_blank"; a.rel = "noopener";
        a.className = "btn-secondary";
        a.textContent = "One-click install (secondary)";
        var p = document.createElement("div");
        p.className = "meta mt-1"; p.textContent = "Plain link: " + link;
        box.appendChild(a); box.appendChild(p);
      } else {
        var s = document.createElement("span");
        s.className = "install-soon"; s.textContent = "Install link coming soon";
        box.appendChild(s);
      }
    });
    $$("[data-install-cta]").forEach(function (a) {
      var link = (CFG.installLinks || {})[a.getAttribute("data-install-cta")] || "";
      if (link) { a.href = link; a.target = "_blank"; a.rel = "noopener"; }
    });
  }

  /* Share: the sharer's own version of the card. No credit system. */
  var current = null;
  function cleanHandle(v) {
    v = (v || "").trim().replace(/[^A-Za-z0-9_@.\-]/g, "").slice(0, 32);
    if (v && v.charAt(0) !== "@") v = "@" + v;
    return v;
  }
  function cleanName(v) { return (v || "").replace(/[<>"]/g, "").trim().slice(0, 40); }
  function shareUrl() {
    var h = cleanHandle($("#share-handle").value), n = cleanName($("#share-name").value);
    var u = CFG.site + "/bots/" + current.slug;
    var q = [];
    if (h) q.push("by=" + encodeURIComponent(h));
    if (n) q.push("name=" + encodeURIComponent(n));
    return u + (q.length ? "?" + q.join("&") : "");
  }
  function sharedByLabel() {
    var h = cleanHandle($("#share-handle").value) || "@handle", n = cleanName($("#share-name").value);
    return "Shared by " + (n ? n + " (" + h + ")" : h);
  }
  function shareText() {
    return sharedByLabel() + "\n\n" + current.name + " " + current.version + ": " + current.pitch +
      "\n\nFree, full open text. " + CFG.brandLine + "\n" + shareUrl();
  }
  function updatePreview() {
    if (!current) return;
    $("#shared-by-label").textContent = sharedByLabel();
    $("#share-url").textContent = shareUrl();
  }
  function openShare(btn) {
    current = {
      slug: btn.getAttribute("data-share"), name: btn.getAttribute("data-name"),
      version: btn.getAttribute("data-version"), pitch: btn.getAttribute("data-pitch"),
      avatar: btn.getAttribute("data-avatar"), color: btn.getAttribute("data-color") || "#FF2E9A"
    };
    $("#share-title").textContent = "Share " + current.name;
    $("#share-bot-name").textContent = current.name;
    $("#share-bot-meta").textContent = current.version + " · " + CFG.brandLine;
    $("#share-bot-pitch").textContent = current.pitch;
    var img = $("#share-avatar"); img.src = current.avatar; img.alt = current.name + " avatar";
    var saved = store.get("sb-share-handle"); if (saved && !$("#share-handle").value) $("#share-handle").value = saved;
    var savedN = store.get("sb-share-name"); if (savedN && !$("#share-name").value) $("#share-name").value = savedN;
    updatePreview();
    $("#share-modal").style.display = "flex";
    $("#share-handle").focus();
  }
  function closeShare() { var m = $("#share-modal"); if (m) m.style.display = "none"; }
  function persistShare() {
    store.set("sb-share-handle", cleanHandle($("#share-handle").value));
    store.set("sb-share-name", cleanName($("#share-name").value));
  }
  function wrap(ctx, text, x, y, maxW, lh, maxLines) {
    var words = text.split(" "), line = "", lines = 0;
    for (var i = 0; i < words.length; i++) {
      var test = line ? line + " " + words[i] : words[i];
      if (ctx.measureText(test).width > maxW && line) {
        ctx.fillText(line, x, y); y += lh; line = words[i]; lines++;
        if (lines >= maxLines - 1) { var rest = words.slice(i).join(" "); while (ctx.measureText(rest + "…").width > maxW && rest.length) rest = rest.slice(0, -1); ctx.fillText(rest + (rest.length < words.slice(i).join(" ").length ? "…" : ""), x, y); return; }
      } else line = test;
    }
    if (line) ctx.fillText(line, x, y);
  }
  function downloadCard() {
    var c = document.createElement("canvas"); c.width = 1200; c.height = 630;
    var ctx = c.getContext("2d");
    var img = new Image();
    img.onload = function () {
      ctx.fillStyle = "#0A0A0A"; ctx.fillRect(0, 0, 1200, 630);
      ctx.strokeStyle = "#262626"; ctx.lineWidth = 2; ctx.strokeRect(24, 24, 1152, 582);
      ctx.font = "900 30px Archivo, Arial, sans-serif";
      var lbl = sharedByLabel(), w = ctx.measureText(lbl).width + 36;
      ctx.fillStyle = "#FF2E9A"; ctx.fillRect(60, 60, w, 52);
      ctx.fillStyle = "#000"; ctx.fillText(lbl, 81, 98); ctx.fillStyle = "#fff"; ctx.fillText(lbl, 78, 95);
      ctx.drawImage(img, 60, 150, 360, 360);
      ctx.font = "900 64px Archivo, Arial, sans-serif";
      var nm = current.name.toUpperCase();
      ctx.fillStyle = "#000"; wrap(ctx, nm, 464, 214, 690, 66, 2);
      ctx.fillStyle = "#fff"; wrap(ctx, nm, 460, 210, 690, 66, 2);
      ctx.font = "500 28px Archivo, Arial, sans-serif"; ctx.fillStyle = "#A3A3A3";
      wrap(ctx, current.pitch, 460, nm.length > 18 ? 370 : 300, 690, 38, 4);
      ctx.font = "600 24px 'JetBrains Mono', monospace"; ctx.fillStyle = "#B6FF00";
      ctx.fillText(current.version + " · " + CFG.brandLine, 460, 520);
      ctx.fillStyle = "#00E5FF"; ctx.fillText("bots.socialbrand.africa", 460, 560);
      c.toBlob(function (blob) {
        var a = document.createElement("a"); a.href = URL.createObjectURL(blob);
        a.download = current.slug + "-shared-card.png"; document.body.appendChild(a); a.click();
        setTimeout(function () { URL.revokeObjectURL(a.href); a.remove(); }, 500);
      }, "image/png");
    };
    img.src = current.avatar;
  }
  function wireShare() {
    if (!$("#share-modal")) return;
    ["#share-handle", "#share-name"].forEach(function (s) { $(s).addEventListener("input", updatePreview); });
    $("#share-copy-text").addEventListener("click", function () { persistShare(); copy(shareText()).then(function () { toast("Share text copied"); }); });
    $("#share-copy-link").addEventListener("click", function () { persistShare(); copy(shareUrl()).then(function () { toast("Link copied"); }); });
    $("#share-download").addEventListener("click", function () { persistShare(); downloadCard(); });
    $("#share-x").addEventListener("click", function () {
      persistShare();
      window.open("https://x.com/intent/post?text=" + encodeURIComponent(shareText()), "_blank", "noopener");
    });
  }

  /* Visitor arrived on someone's shared link: show their name on the page */
  function sharedBanner() {
    var el = $("#shared-banner"); if (!el) return;
    var p = new URLSearchParams(window.location.search);
    var h = cleanHandle(p.get("by")), n = cleanName(p.get("name"));
    if (!h && !n) return;
    $("#shared-banner-text").textContent = "Shared by " + (n && h ? n + " (" + h + ")" : (n || h)) + " · built by SocialBrand · socialbrand.africa";
    el.classList.add("show");
  }

  /* Catalogue search, chips and sort */
  function wireCatalogue() {
    var input = $("#hero-search"), grid = $("#catalogue");
    if (!input || !grid) return;
    function filter() {
      var q = input.value.trim().toLowerCase(), shown = 0;
      $$(".card", grid).forEach(function (c) {
        var hit = !q || (c.getAttribute("data-search") || "").indexOf(q) !== -1;
        c.classList.toggle("hidden", !hit); if (hit) shown++;
      });
      $("#no-results").classList.toggle("hidden", shown > 0);
    }
    input.addEventListener("input", filter);
    $("#hero-search-form").addEventListener("submit", function (e) { e.preventDefault(); filter(); grid.scrollIntoView({ behavior: "smooth", block: "start" }); });
    $$("[data-chip]").forEach(function (ch) {
      ch.addEventListener("click", function () { input.value = ch.getAttribute("data-chip"); filter(); grid.scrollIntoView({ behavior: "smooth", block: "start" }); });
    });
    var orig = $$(".card", grid);
    $$("[data-sort]").forEach(function (b) {
      b.addEventListener("click", function () {
        $$("[data-sort]").forEach(function (x) { x.classList.toggle("on", x === b); });
        var cards = orig.slice();
        if (b.getAttribute("data-sort") === "upvoted") {
          cards.sort(function (a, c) { return (voted(c.getAttribute("data-slug")) ? 1 : 0) - (voted(a.getAttribute("data-slug")) ? 1 : 0); });
        }
        cards.forEach(function (c) { grid.appendChild(c); });
      });
    });
  }

  document.addEventListener("keydown", function (e) {
    if ((e.ctrlKey || e.metaKey) && (e.key === "k" || e.key === "K")) {
      var i = $("#hero-search");
      e.preventDefault();
      if (i) i.focus(); else window.location.href = "/#catalogue";
    }
    if (e.key === "Escape") closeShare();
  });


  /* ---- Bento v1: compact nav, scroll reveal, mobile folds ---- */
  var REDUCED = window.matchMedia && window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  function wireNav() {
    var nav = document.querySelector(".nav"), btn = nav && nav.querySelector(".nav-toggle");
    if (!btn) return;
    function set(open) { nav.classList.toggle("open", open); btn.setAttribute("aria-expanded", open ? "true" : "false"); }
    btn.addEventListener("click", function (e) { e.stopPropagation(); set(!nav.classList.contains("open")); });
    $$(".nav-menu a").forEach(function (a) { a.addEventListener("click", function () { set(false); }); });
    document.addEventListener("click", function (e) { if (nav.classList.contains("open") && !nav.contains(e.target)) set(false); });
    document.addEventListener("keydown", function (e) { if (e.key === "Escape" && nav.classList.contains("open")) { set(false); btn.focus(); } });
  }
  function wireReveal() {
    var els = $$(".reveal");
    if (!els.length) return;
    if (REDUCED || !("IntersectionObserver" in window)) { els.forEach(function (el) { el.classList.add("in"); }); return; }
    var queue = [], timer = null;
    function flush() {
      var el = queue.shift();
      if (el) el.classList.add("in");
      timer = queue.length ? setTimeout(flush, 60) : null;
    }
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (!en.isIntersecting) return;
        io.unobserve(en.target); queue.push(en.target);
        if (!timer) timer = setTimeout(flush, 0);
      });
    }, { rootMargin: "0px 0px -6% 0px", threshold: 0.08 });
    els.forEach(function (el) { io.observe(el); });
  }
  function animateDetails(d) {
    var sum = d.querySelector("summary"), body = d.querySelector(".fold-body");
    if (!sum || !body || !body.animate) return;
    sum.addEventListener("click", function (e) {
      if (REDUCED) return;
      e.preventDefault();
      if (d.open) {
        var h = body.offsetHeight;
        var an = body.animate([{ height: h + "px", opacity: 1 }, { height: "0px", opacity: 0 }], { duration: 280, easing: "ease-out" });
        an.onfinish = function () { d.open = false; };
      } else {
        d.open = true;
        var h2 = body.offsetHeight;
        body.animate([{ height: "0px", opacity: 0 }, { height: h2 + "px", opacity: 1 }], { duration: 320, easing: "ease-out" });
      }
    });
  }
  function wireFolds() {
    var mobile = window.matchMedia && window.matchMedia("(max-width: 639px)").matches;
    $$("details[data-fold-mobile]").forEach(function (d) {
      if (mobile && !(location.hash && d.querySelector(location.hash.replace(/[^\w#-]/g, "")))) d.open = false;
      animateDetails(d);
    });
  }
  function init() { renderVotes(); renderInstall(); wireShare(); sharedBanner(); wireCatalogue(); wireNav(); wireFolds(); wireReveal(); }
  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", init); else init();
})();
