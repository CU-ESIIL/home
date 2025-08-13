---
title: Quick Start
---

<style>
@import url('https://fonts.googleapis.com/css2?family=Overpass:wght@400;600;700;800&display=swap');

:root{
      --navy:#0f2747;
      --sky:#7db6ff;
      --ink:#0b1220;
      --bg:#fafbfc;
      --card:#ffffff;
      --border:rgba(15,39,71,.12);
      --shadow:0 1px 2px rgba(15,39,71,.06), 0 6px 18px rgba(15,39,71,.08);

      --btn-h:72px;
      --btn-radius:999px;
      --gap:18px;
      --grid-max:1100px;
    }

    html,body{margin:0;background:var(--bg);color:var(--ink);font-family:'Overpass',system-ui,-apple-system,Segoe UI,Roboto,Ubuntu,'Helvetica Neue',Arial,sans-serif;-webkit-font-smoothing:antialiased}

    /* Parallax hero */
    .hero{height:40vh;min-height:260px;background:radial-gradient(circle at center,var(--sky),var(--navy)) fixed;display:flex;align-items:center;justify-content:center;text-align:center;color:#fff}
    .hero-inner{background:rgba(15,39,71,.6);padding:24px 32px;border-radius:12px}
    .hero h1{margin:0;font-size:2.2rem;font-weight:800;letter-spacing:.4px}
    .hero p{margin:8px 0 0;font-size:1.1rem;opacity:.9}

    .wrap{max-width:var(--grid-max);margin:40px auto;padding:0 16px}

    /* Tag cloud */
    .tag-cloud{display:flex;flex-wrap:wrap;justify-content:center;gap:12px;margin-bottom:var(--gap)}
    .tag-cloud a{text-decoration:none;color:var(--navy);background:rgba(125,182,255,.2);padding:4px 10px;border-radius:8px;transition:background .2s,font-size .2s}
    .tag-cloud a:hover{background:rgba(125,182,255,.35)}
    .tag-cloud a:nth-child(2n){font-size:1.1rem}
    .tag-cloud a:nth-child(3n){font-size:.9rem}

    /* Grid of links */
    .grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(320px,1fr));gap:var(--gap)}

    /* Modern pill buttons */
    .pill{
      --bg1:#ffffff; --bg2:#f4f7fb; --fg:var(--navy);
      position:relative;display:flex;align-items:center;gap:14px;
      min-height:var(--btn-h);padding:14px 22px 14px 18px;border-radius:var(--btn-radius);
      background:linear-gradient(135deg,var(--bg1),var(--bg2));
      color:var(--fg);text-decoration:none;border:1px solid var(--border);
      box-shadow:var(--shadow);
      transition:transform .15s ease, box-shadow .2s ease, background-position .4s ease, border-color .2s ease;
      background-size:200% 200%;
    }
    .pill:hover{transform:translateY(-2px);box-shadow:0 6px 24px rgba(15,39,71,.16);background-position:100% 0;border-color:rgba(15,39,71,.22)}
    .pill:active{transform:translateY(0) scale(.995)}
    .pill:focus-visible{outline:3px solid rgba(125,182,255,.45);outline-offset:2px}

    .icon{width:36px;height:36px;flex:0 0 36px;display:grid;place-items:center;transition:transform .25s ease, color .25s ease}
    .pill svg{display:block;width:100%;height:100%;stroke:currentColor;fill:none;stroke-width:1.8}
    .pill:hover .icon{transform:translateX(2px)}

    .label{font-weight:700;font-size:1.05rem;line-height:1.15}
    .note{font-weight:400;font-size:.82rem;opacity:.65}

    /* Right chevron indicator */
    .chev{margin-left:auto;width:16px;height:16px;color:var(--navy);opacity:.65;transition:transform .2s ease, opacity .2s ease;
      background:currentColor;
      -webkit-mask:url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24'><path d='M9 6l6 6-6 6' fill='none' stroke='%23000' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'/></svg>") center / contain no-repeat;
              mask:url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24'><path d='M9 6l6 6-6 6' fill='none' stroke='%23000' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'/></svg>") center / contain no-repeat;
    }
    .pill:hover .chev{transform:translateX(3px);opacity:.9}

    /* Subtle color variants */
    .is-sky{--bg1:#f5faff;--bg2:#eaf3ff}
    .is-ink{--bg1:#0f2747;--bg2:#0b1d35;--fg:#e9f3ff;color:var(--fg)}

    /* Respect reduced motion */
    @media (prefers-reduced-motion:reduce){
      .pill,.icon,.chev{transition:none}
    }
    @media (max-width:480px){
      :root{--btn-h:64px}
      .label{font-size:1rem}
      .icon{width:30px;height:30px}
    }
</style>

<header class="hero">
    <div class="hero-inner">
      <h1>Quick Start</h1>
      <p class="subtitle">Jump into OASIS with these starter resources</p>
    </div>
  </header>

  <div class="wrap">
    <div class="tag-cloud" role="navigation" aria-label="Tag cloud">
      <a href="./cyverse.html">CyVerse</a>
      <a href="./r.html">R</a>
      <a href="./python.html">Python</a>
      <a href="./github.html">GitHub</a>
      <a href="./docker.html">Docker</a>
      <a href="./oasis.html">OASIS</a>
      <a href="./data-library/">Data</a>
      <a href="./analytics-library.html">Analytics</a>
      <a href="./container-library.html">Containers</a>
    </div>
    <div class="grid" role="list">
      <!-- Quick Start Page -->
      <a class="pill is-ink" href="./" role="listitem" aria-label="Quick Start Page">
        <div class="icon" aria-hidden="true">
          <svg viewBox="0 0 24 24"><path d="M12 2l2.2 4.5 5 .7-3.6 3.5.9 5-4.5-2.3L8.4 15l.9-5L5.7 7.2l5-.7L12 2z"/></svg>
        </div>
        <div class="text">
          <div class="label">QUICK START PAGE</div>
          <div class="note">overview & orientation</div>
        </div>
        <span class="chev" aria-hidden="true"></span>
      </a>

      <!-- Starting with CyVerse -->
      <a class="pill is-sky" href="./cyverse.html" role="listitem" aria-label="Starting with CyVerse">
        <div class="icon" aria-hidden="true">
          <svg viewBox="0 0 24 24"><path d="M6 16h10a4 4 0 0 0 0-8 5.5 5.5 0 0 0-10.5 2A3.5 3.5 0 0 0 6 16z"/></svg>
        </div>
        <div class="label">Starting with CyVerse</div>
        <span class="chev" aria-hidden="true"></span>
      </a>

      <!-- Starting with R -->
      <a class="pill" href="./r.html" role="listitem" aria-label="Starting with R">
        <div class="icon" aria-hidden="true">
          <svg viewBox="0 0 24 24"><path d="M4 12.5c0-3.6 3.6-6.5 8-6.5s8 2.9 8 6.5-3.6 6.5-8 6.5H9"/><path d="M9 18V9h4a3 3 0 0 1 0 6h-4l6 3"/></svg>
        </div>
        <div class="label">Starting with R</div>
        <span class="chev" aria-hidden="true"></span>
      </a>

      <!-- Starting with Python -->
      <a class="pill is-sky" href="./python.html" role="listitem" aria-label="Starting with Python">
        <div class="icon" aria-hidden="true">
          <svg viewBox="0 0 24 24"><path d="M7 12a5 5 0 0 1 5-5h3a2 2 0 0 1 2 2v2H9a2 2 0 0 0 0 4h6"/><circle cx="14.5" cy="9.5" r=".75"/></svg>
        </div>
        <div class="label">Starting with Python</div>
        <span class="chev" aria-hidden="true"></span>
      </a>

      <!-- Starting with GitHub -->
      <a class="pill" href="./github.html" role="listitem" aria-label="Starting with GitHub">
        <div class="icon" aria-hidden="true">
          <svg viewBox="0 0 24 24"><path d="M12 3c-5 0-9 4-9 9a9 9 0 0 0 6 8.6c.4.1.5-.2.5-.4v-2.1c-2.2.5-2.7-1-2.7-1-.4-1-1-1.2-1-1.2-.8-.6.1-.6.1-.6 1 .1 1.5 1 1.5 1 .9 1.5 2.4 1.1 3 .8.1-.6.3-1.1.6-1.3-1.8-.2-3.7-.9-3.7-4A3.2 3.2 0 0 1 8.6 9a3 3 0 0 1 .1-2.2s.7-.2 2.2.9a7.6 7.6 0 0 1 4 0c1.5-1.1 2.2-.9 2.2-.9.3.7.3 1.5.1 2.2A3.2 3.2 0 0 1 17 12c0 3.1-1.9 3.8-3.7 4 .3.2.6.8.6 1.6v2.3c0 .2.1.5.6.4A9 9 0 0 0 21 12c0-5-4-9-9-9z"/></svg>
        </div>
        <div class="label">Starting with GitHub</div>
        <span class="chev" aria-hidden="true"></span>
      </a>

      <!-- Starting Docker Container -->
      <a class="pill is-sky" href="./docker.html" role="listitem" aria-label="Starting Docker Container">
        <div class="icon" aria-hidden="true">
          <svg viewBox="0 0 24 24"><path d="M4 14h8M3 12h8M3 10h8M12 16c2 2 5 2 7-.5 1.3-1.6 1.2-3.7.4-5.5-1 .6-2 .8-3 .7"/><path d="M10 6h3v3h-3zM6 6h3v3H6zM6 10h3v3H6zM10 10h3v3h-3zM14 10h3v3h-3z"/></svg>
        </div>
        <div class="label">Starting Docker Container</div>
        <span class="chev" aria-hidden="true"></span>
      </a>

      <!-- Starting with OASIS -->
      <a class="pill" href="./oasis.html" role="listitem" aria-label="Starting with OASIS">
        <div class="icon" aria-hidden="true">
          <svg viewBox="0 0 24 24"><path d="M3 12c3-3 6-3 9 0s6 3 9 0"/><path d="M3 16c3-2 6-2 9 0s6 2 9 0"/><path d="M3 8c3-2 6-2 9 0s6 2 9 0"/></svg>
        </div>
        <div class="label">Starting with OASIS</div>
        <span class="chev" aria-hidden="true"></span>
      </a>

      <!-- Data Library -->
      <a class="pill is-sky" href="./data-library/" role="listitem" aria-label="Data Library">
        <div class="icon" aria-hidden="true">
          <svg viewBox="0 0 24 24"><path d="M5 5h4v14H5zM10 7h4v12h-4zM15 9h4v10h-4z"/></svg>
        </div>
        <div class="label">Data Library</div>
        <span class="chev" aria-hidden="true"></span>
      </a>

      <!-- Analytics Library -->
      <a class="pill" href="./analytics-library.html" role="listitem" aria-label="Analytics Library">
        <div class="icon" aria-hidden="true">
          <svg viewBox="0 0 24 24"><path d="M10 14l-2 2a4 4 0 0 1-6-6l3-3a4 4 0 0 1 6 0"/><path d="M14 10l2-2a4 4 0 0 1 6 6l-3 3a4 4 0 0 1-6 0"/></svg>
        </div>
        <div class="label">Analytics Library</div>
        <span class="chev" aria-hidden="true"></span>
      </a>

      <!-- Container Image Library -->
      <a class="pill is-sky" href="./container-library.html" role="listitem" aria-label="Container Image Library">
        <div class="icon" aria-hidden="true">
          <svg viewBox="0 0 24 24"><path d="M3 12h18"/><path d="M8 12h13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h6v8"/></svg>
        </div>
        <div class="label">Container Image Library</div>
        <span class="chev" aria-hidden="true"></span>
      </a>

      <!-- Advanced Textbook -->
      <a class="pill" href="./advanced-textbook.html" role="listitem" aria-label="Advanced Textbook">
        <div class="icon" aria-hidden="true">
          <svg viewBox="0 0 24 24"><path d="M5 4h14v16H5z"/><path d="M5 8h14"/><path d="M8 4v16"/></svg>
        </div>
        <div class="label">Advanced Textbook</div>
        <span class="chev" aria-hidden="true"></span>
      </a>

    </div>

    <!-- Minimal inline test cases -->
    <div class="tests" id="tests" style="margin-top:28px;padding:12px 14px;border:1px dashed rgba(15,39,71,.2);border-radius:12px;background:#fff">
      <h2 style="margin:0 0 10px;font-size:1rem;color:var(--navy)">Self‑tests</h2>
      <pre id="test-log" style="margin:0;font-size:.9rem;white-space:pre-wrap">Running…</pre>
    </div>
  </div>

  <script>
    (function(){
      const out = document.getElementById('test-log');
      const logs = [];
      function ok(cond, msg){
        const line = (cond ? '✔ ' : '✖ ') + msg; logs.push(line);
        if(!cond) console.error(msg); else console.log(msg);
      }
      try{
        const pills = document.querySelectorAll('.pill');
        ok(pills.length === 11, 'All 11 quick links are present');
        const allHaveLabels = Array.from(document.querySelectorAll('.grid [role="listitem"]')).every(el => el.getAttribute('aria-label') || el.textContent.trim().length > 0);
        ok(allHaveLabels, 'Each quick link has an accessible label or text');
      }catch(e){ logs.push('✖ Exception during tests: ' + e.message); }
      out.textContent = logs.join('\n');
    })();
  </script>
