---
hide:
  - toc
---

<!-- Static Header Section -->
<div class="static-header">
    <img id="header-img" src="https://raw.githubusercontent.com/CU-ESIIL/home/main/docs/assets/thumbnails/OASIS_header.png"
         alt="ESIIL OASIS Header">
</div>
<!-- Main Content -->
<div class="content">
    <h1 class="oasis-header">Open Analysis and Synthesis Infrastructure for Science</h1>
    <div class="search-bar">
      <form action="search/" method="get" class="search-form">
        <input type="search" name="q" placeholder="Search..." aria-label="Search" />
        <button type="submit" aria-label="Submit search">🔍</button>
      </form>
      <div class="tag-suggestions">
        <a href="./quickstart/" class="tag">Quickstart</a>
        <a href="./container-library/" class="tag">Containers</a>
        <a href="./analytics-library/" class="tag">Analytics</a>
        <a href="./data-library/" class="tag">Data Library</a>
        <a href="./resources/" class="tag">Resources</a>
      </div>
    </div>
    <p>Welcome to the <strong>OASIS</strong>, a hub for open analysis and synthesis in <strong>Environmental Data Science</strong>.</p>
</div>

<style>
  .search-bar {
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 10px;
    margin: 10px 0;
  }
  .search-form {
    position: relative;
    width: 100%;
    max-width: 500px;
  }
  .search-form input[type="search"] {
    width: 100%;
    padding: 10px 40px 10px 14px;
    border: 1px solid #ccc;
    border-radius: 20px;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  }
  .search-form button {
    position: absolute;
    top: 50%;
    right: 10px;
    transform: translateY(-50%);
    border: none;
    background: none;
    cursor: pointer;
    font-size: 1.2em;
  }
  .tag-suggestions {
    display: flex;
    flex-wrap: wrap;
    gap: 8px;
    justify-content: center;
  }
  .tag-suggestions .tag {
    padding: 5px 12px;
    text-decoration: none;
    border: 1px solid #ccc;
    border-radius: 15px;
    background: #f5f5f5;
    color: #333;
    font-size: 0.9em;
  }
  .tag-suggestions .tag:hover {
    background: #e0e0e0;
  }
</style>

<!-- Quick Start Button -->
<div class="qs-wrap">
  <a class="qs-btn" href="./quickstart/" role="button" aria-label="Open Quick Start">
    <img src="assets/thumbnails/quick_start_button.jpg" alt="Quick Start" />
    <!-- Corner badge -->
    <span class="qs-badge">CLICK</span>
    <!-- Bottom CTA bar -->
    <span class="qs-cta">
      <span class="qs-icon">▶</span>
      <span>Open Quick Start</span>
    </span>
  </a>
</div>

<style>
  /* Layout: centers the button */
  .qs-wrap {
    display: grid;
    place-items: center;
    padding: 1rem;
  }

  /* Button container */
  .qs-btn {
    position: relative;
    display: inline-block;
    max-width: 720px;              /* control size here */
    width: min(90vw, 720px);
    border-radius: 16px;
    overflow: hidden;
    text-decoration: none;
    outline: none;
    /* “buttony” depth + hover lift */
    box-shadow:
      0 6px 14px rgba(0,0,0,.25),
      inset 0 0 0 2px rgba(255,255,255,.08);
    transition: transform .18s ease, box-shadow .18s ease, filter .18s ease;
  }

  .qs-btn img {
    display: block;
    width: 100%;
    height: auto;
  }

  /* Subtle interactive glow ring */
  .qs-btn::after {
    content: "";
    position: absolute; inset: 0;
    border-radius: 16px;
    box-shadow: 0 0 0 0 rgba(56, 189, 248, 0.0);
    pointer-events: none;
    transition: box-shadow .18s ease;
  }

  /* Corner "CLICK" badge */
  .qs-badge {
    position: absolute;
    top: 12px; left: 12px;
    background: #34d399; /* emerald */
    color: #0b1220;
    font: 700 12px/1 system-ui, -apple-system, Segoe UI, Roboto, Inter, Arial, sans-serif;
    letter-spacing: .06em;
    padding: .4rem .55rem;
    border-radius: 10px;
    text-transform: uppercase;
    box-shadow: 0 2px 8px rgba(0,0,0,.25);
  }

  /* Bottom CTA bar */
  .qs-cta {
    position: absolute;
    left: 0; right: 0; bottom: 0;
    display: flex; align-items: center; justify-content: center; gap: .6rem;
    padding: .7rem 1rem;
    background: linear-gradient(180deg, rgba(0,0,0,0) 0%, rgba(0,0,0,.55) 35%, rgba(0,0,0,.75) 100%);
    color: #e6f6ff;
    font: 700 16px/1.2 system-ui, -apple-system, Segoe UI, Roboto, Inter, Arial, sans-serif;
    text-shadow: 0 1px 2px rgba(0,0,0,.65);
  }
  .qs-icon { display: inline-block; transform: translateY(1px); }

  /* Hover / focus states = feel like a pressable button */
  .qs-btn:hover,
  .qs-btn:focus-visible {
    transform: translateY(-2px);
    box-shadow:
      0 10px 22px rgba(0,0,0,.30),
      inset 0 0 0 2px rgba(255,255,255,.1);
    filter: saturate(1.08);
  }
  .qs-btn:hover::after,
  .qs-btn:focus-visible::after {
    box-shadow: 0 0 0 6px rgba(56, 189, 248, 0.25); /* cyan glow ring */
  }

  /* Active (mouse down) */
  .qs-btn:active {
    transform: translateY(0);
    box-shadow:
      0 6px 14px rgba(0,0,0,.25),
      inset 0 0 0 2px rgba(255,255,255,.08);
  }

  /* Optional: reduce motion respect */
  @media (prefers-reduced-motion: reduce) {
    .qs-btn { transition: none; }
    .qs-btn::after { transition: none; }
  }
</style>

<!-- Shared hover animation for linked images -->
<style>
  .library-item a,
  .gallery-item a,
  .template-item a {
    position: relative;
    display: inline-block;
    border-radius: 10px;
    overflow: hidden;
    box-shadow:
      0 6px 14px rgba(0,0,0,.25),
      inset 0 0 0 2px rgba(255,255,255,.08);
    transition: transform .18s ease, box-shadow .18s ease, filter .18s ease;
  }

  .library-item a::after,
  .gallery-item a::after,
  .template-item a::after {
    content: "";
    position: absolute;
    inset: 0;
    border-radius: inherit;
    box-shadow: 0 0 0 0 rgba(56,189,248,0.0);
    pointer-events: none;
    transition: box-shadow .18s ease;
  }

  .library-item a:hover,
  .library-item a:focus-visible,
  .gallery-item a:hover,
  .gallery-item a:focus-visible,
  .template-item a:hover,
  .template-item a:focus-visible {
    transform: translateY(-2px);
    box-shadow:
      0 10px 22px rgba(0,0,0,.30),
      inset 0 0 0 2px rgba(255,255,255,.1);
    filter: saturate(1.08);
  }

  .library-item a:hover::after,
  .library-item a:focus-visible::after,
  .gallery-item a:hover::after,
  .gallery-item a:focus-visible::after,
  .template-item a:hover::after,
  .template-item a:focus-visible::after {
    box-shadow: 0 0 0 6px rgba(56,189,248,0.25);
  }

  .library-item a:active,
  .gallery-item a:active,
  .template-item a:active {
    transform: translateY(0);
    box-shadow:
      0 6px 14px rgba(0,0,0,.25),
      inset 0 0 0 2px rgba(255,255,255,.08);
  }
</style>



---
## 📚 Data & Analytics Libraries

<div class="library-gallery">

  <div class="library-item">
    <a href="https://cu-esiil.github.io/data-library/" target="_blank">
      <img src="https://github.com/CU-ESIIL/home/blob/main/docs/assets/thumbnails/data_library.jpeg?raw=true" alt="Data Library">
    </a>
    <p><strong>Data Library</strong></p>
    <p>Organizational hub for ESIIL datasets.</p>
  </div>

  <div class="library-item">
    <a href="https://analytics-library.esiil.org" target="_blank">
      <img src="https://github.com/CU-ESIIL/home/blob/main/docs/assets/thumbnails/analytics_library.jpeg?raw=true" alt="Analytics Library">
    </a>
    <p><strong>Analytics Library</strong></p>
    <p>Repository for data harmonization and analytics.</p>
  </div>

  <div class="library-item">
    <a href="./container-library/">
      <img src="https://github.com/CU-ESIIL/home/blob/main/docs/assets/thumbnails/docker.jpeg?raw=true" alt="Container Image Library">
    </a>
    <p><strong>Container Image Library</strong></p>
    <p>Browse available container images for ESIIL computing.</p>
  </div>

  <div class="library-item">
    <a href="https://textbook.esiil.org" target="_blank">
      <img src="https://github.com/CU-ESIIL/home/blob/main/docs/assets/thumbnails/advanced_textbook.jpeg?raw=true" alt="Tutorials and Learning Resources">
    </a>
    <p><strong>Advanced Textbook</strong></p>
    <p>Comprehensive guide to environmental data science.</p>
  </div>

</div>

<style>
  .library-gallery {
    display: flex;
    flex-wrap: nowrap; /* No wrapping */
    gap: 10px; /* Smaller gap so it fits */
    justify-content: center;
  }

  .library-item {
    width: calc(25% - 10px); /* 4 items per row */
    text-align: center;
  }

  .library-item img {
    width: 100%;
    max-width: 150px; /* Keep them smaller so text fits */
    border-radius: 10px;
    object-fit: cover;
    height: auto;
  }
</style>


<div class="tagline">
  Tags: environmental data science, synthesis, open science, analytics, ESIIL
</div>

---

## 🚀 **NSF Synthesis Working Groups**  

<div style="display: flex; flex-wrap: wrap; gap: 20px; justify-content: flex-start;">

  <div class="gallery-item">
    <a href="https://cu-esiil.github.io/BioViewPoint/" target="_blank">
      <img src="https://github.com/CU-ESIIL/home/blob/main/docs/assets/thumbnails/BioViewPoint.jpeg?raw=true" alt="BioViewPoint">
    </a>
    <p><strong>BioViewPoint</strong></p>
    <p>Visualization tools for biodiversity data.</p>
  </div>

  <div class="gallery-item">
    <a href="https://cu-esiil.github.io/ExtremeWildfire/" target="_blank">
      <img src="https://github.com/CU-ESIIL/home/blob/main/docs/assets/thumbnails/extreme_wildfire.jpeg?raw=true" alt="Extreme Wildfire">
    </a>
    <p><strong>Extreme Wildfire</strong></p>
    <p>Investigating extreme wildfire behavior.</p>
  </div>

  <div class="gallery-item">
    <a href="https://cu-esiil.github.io/fungal_dispersal/" target="_blank">
      <img src="https://github.com/CU-ESIIL/home/blob/main/docs/assets/thumbnails/fungal_dispersal.jpeg?raw=true" alt="Fungal Dispersal">
    </a>
    <p><strong>Fungal Dispersal</strong></p>
    <p>ESIIL working group on fungal dispersal.</p>
  </div>

  <div class="gallery-item">
    <a href="https://cu-esiil.github.io/macrophenology/" target="_blank">
      <img src="https://github.com/CU-ESIIL/home/blob/main/docs/assets/thumbnails/macrophenology.jpeg?raw=true" alt="Macrophenology">
    </a>
    <p><strong>Macrophenology</strong></p>
    <p>Macroecological patterns in phenology.</p>
  </div>

  <div class="gallery-item">
    <a href="https://cu-esiil.github.io/maka_sitomniya/" target="_blank">
      <img src="https://github.com/CU-ESIIL/home/blob/main/docs/assets/thumbnails/maka_sitomniya.jpeg?raw=true" alt="Maka-Sitomniya">
    </a>
    <p><strong>Maka-Sitomniya</strong></p>
    <p>Research on traditional ecological knowledge.</p>
  </div>

  <div class="gallery-item">
    <a href="https://cu-esiil.github.io/AI-for-Natural-Methane/" target="_blank">
      <img src="https://github.com/CU-ESIIL/home/blob/main/docs/assets/thumbnails/natural_methane.jpeg?raw=true" alt="AI for Natural Methane">
    </a>
    <p><strong>AI for Natural Methane</strong></p>
    <p>Harmonizing natural methane datasets using AI.</p>
  </div>

  <div class="gallery-item">
    <a href="https://cu-esiil.github.io/zooplankton_indicator_dataset/" target="_blank">
      <img src="https://github.com/CU-ESIIL/home/blob/main/docs/assets/thumbnails/zooplankton.jpeg?raw=true" alt="Zooplankton Indicator Dataset">
    </a>
    <p><strong>Zooplankton Indicator Dataset</strong></p>
    <p>Dataset and tools for zooplankton as environmental indicators.</p>
  </div>

</div>

<style>
  .gallery-item {
    width: calc(100% / 2 - 20px); /* Two per row on small screens */
    text-align: center;
  }

  .gallery-item img {
    width: 100%;
    max-width: 150px; /* Ensures uniform icon size */
    border-radius: 10px;
  }

  @media (min-width: 600px) {
    .gallery-item { width: calc(100% / 4 - 20px); } /* Four per row on tablets */
  }

  @media (min-width: 1000px) {
    .gallery-item { width: calc(100% / 7 - 20px); } /* Seven per row on desktops */
  }
</style>

---
## 🎓 **NSF Synthesis Postdoc Researcher Projects**  
These repositories represent postdoc-led research initiatives at ESIIL.

<div style="display: flex; flex-wrap: wrap; gap: 20px; justify-content: flex-start;">

  <div class="gallery-item">
    <a href="https://cu-esiil.github.io/Jim-s-Sandbox/" target="_blank">
      <img src="https://github.com/CU-ESIIL/home/blob/main/docs/assets/thumbnails/Jim_sandbox.jpeg?raw=true" alt="Jim's Sandbox">
    </a>
    <p><strong>Datacube Sandbox</strong></p>
    <p>Training and practice space for data cubes.</p>
  </div>

  <div class="gallery-item">
    <a href="https://cu-esiil.github.io/biotic_niche_modeling/" target="_blank">
      <img src="https://github.com/CU-ESIIL/home/blob/main/docs/assets/thumbnails/biotic_niche_modeling.jpeg?raw=true" alt="Biotic Niche Modeling">
    </a>
    <p><strong>Biotic Niche Modeling</strong></p>
    <p>Research on species niche dynamics.</p>
  </div>

  <div class="gallery-item">
    <a href="https://cu-esiil.github.io/nutrient-flows/" target="_blank">
      <img src="https://github.com/CU-ESIIL/home/blob/main/docs/assets/thumbnails/nutrient_flows.jpeg?raw=true" alt="Nutrient Flows">
    </a>
    <p><strong>Nutrient Flows</strong></p>
    <p>Analysis of seafood trade and sustainability.</p>
  </div>

  <div class="gallery-item">
    <a href="https://github.com/CU-ESIIL/LTER-material-legacies" target="_blank">
      <img src="https://github.com/CU-ESIIL/home/blob/main/docs/assets/thumbnails/LTER_material_legacies.jpeg?raw=true" alt="LTER Material Legacies">
    </a>
    <p><strong>LTER Material Legacies</strong></p>
    <p>Impact of dead tree legacies on forest resilience.</p>
  </div>

  <div class="gallery-item">
    <a href="https://cu-esiil.github.io/Team-Science/" target="_blank">
      <img src="https://github.com/CU-ESIIL/home/blob/main/docs/assets/thumbnails/team_science_postdoc.jpeg?raw=true" alt="Team Science">
    </a>
    <p><strong>Team Science</strong></p>
    <p>Studying scientific collaboration networks.</p>
  </div>

  <div class="gallery-item">
    <a href="https://github.com/CU-ESIIL/opt-decision-making" target="_blank">
      <img src="https://github.com/CU-ESIIL/home/blob/main/docs/assets/thumbnails/opt_decision_making.jpeg?raw=true" alt="Opt Decision Making">
    </a>
    <p><strong>Opt Decision Making</strong></p>
    <p>Optimization and decision science.</p>
  </div>

  <div class="gallery-item">
    <a href="https://cu-esiil.github.io/water_carbon_management/" target="_blank">
      <img src="https://github.com/CU-ESIIL/home/blob/main/docs/assets/thumbnails/water_carbon_dynamics.jpeg?raw=true" alt="Water Carbon Dynamics">
    </a>
    <p><strong>Water Carbon Dynamics</strong></p>
    <p>Investigating water-carbon interactions.</p>
  </div>

  <div class="gallery-item">
    <a href="https://cu-esiil.github.io/CulturalES_WildfireRx/" target="_blank">
      <img src="https://github.com/CU-ESIIL/home/blob/main/docs/assets/thumbnails/cultural_wildfire_Rx.jpeg?raw=true" alt="Cultural ES WildfireRx">
    </a>
    <p><strong>Cultural ES WildfireRx</strong></p>
    <p>Wildfire effects on cultural ecosystem services.</p>
  </div>

  <div class="gallery-item">
    <a href="https://cu-esiil.github.io/SCE-Wildfire/" target="_blank">
      <img src="https://github.com/CU-ESIIL/home/blob/main/docs/assets/thumbnails/SCE_wildfire.jpeg?raw=true" alt="SCE Wildfire">
    </a>
    <p><strong>SCE Wildfire</strong></p>
    <p>Socioecological impacts of wildfire.</p>
  </div>

 <div class="gallery-item">
    <a href="https://cu-esiil.github.io/tundra_shrub_expansion/" target="_blank">
      <img src="https://github.com/CU-ESIIL/home/blob/main/docs/assets/thumbnails/tundra_shrub_expansion.jpeg?raw=true" alt="Tundra Shrub Expansion">
    </a>
    <p><strong>Tundra Shrub Expansion</strong></p>
    <p>Remote sensing tools for alpine ecosystems.</p>
  </div>

</div>

<style>
  .gallery-item img {
    width: 100%;
    max-width: 150px;
    border-radius: 10px;
    object-fit: cover;
    height: 150px;
  }
</style>

---

## 🔬 **Staff and Affiliate Research Projects**  
These repositories represent broader research efforts contributing to environmental data science.

| Name | Description | Link |
|------|------------|------|
| **[SpectralBEF](https://cu-esiil.github.io/spectralBEF/)** | Spectral analysis of biodiversity-ecosystem functioning. | 🔗 Website |
| **[GEDI-ECOSTRESS Data Project](https://github.com/CU-ESIIL/GEDI-ECOSTRESS_data_project)** | Aligning GEDI and ECOSTRESS datasets for ML applications. | 🔗 GitHub |

---

## 🎟️ **Events & Summits**  
Major ESIIL-hosted and affiliated events.

<div class="template-gallery">


  <div class="template-item">
    <a href="https://cu-esiil.github.io/Innovation-Summit-2025/" target="_blank">
      <img src="https://github.com/CU-ESIIL/home/blob/main/docs/assets/thumbnails/innovation_summit_2025.jpeg?raw=true" alt="Innovation Summit 2025">
    </a>
    <p><strong>Innovation Summit 2025</strong></p>
    <p>Official repository for the ESIIL Innovation Summit 2025.</p>
  </div>

  <div class="template-item">
    <a href="https://cu-esiil.github.io/FIRE-plan-2024/" target="_blank">
      <img src="https://github.com/CU-ESIIL/home/blob/main/docs/assets/thumbnails/fire_plan.jpeg?raw=true" alt="FIRE Plan 2024">
    </a>
    <p><strong>FIRE Plan 2024</strong></p>
    <p>Planning and strategy for fire management.</p>
  </div>

  <div class="template-item">
    <a href="https://cu-esiil.github.io/Innovation-Summit-2024/" target="_blank">
      <img src="https://github.com/CU-ESIIL/home/blob/main/docs/assets/thumbnails/innovation_summit_2024.jpeg?raw=true" alt="Innovation Summit 2024">
    </a>
    <p><strong>Innovation Summit 2024</strong></p>
    <p>Official repo for the ESIIL Innovation Summit 2024.</p>
  </div>

  <div class="template-item">
    <a href="https://cu-esiil.github.io/forest-carbon-codefest/" target="_blank">
      <img src="https://github.com/CU-ESIIL/home/blob/main/docs/assets/thumbnails/FCC.jpeg?raw=true" alt="Forest Carbon Codefest">
    </a>
    <p><strong>Forest Carbon Codefest</strong></p>
    <p>Hands-on coding event for forest carbon research.</p>
  </div>

  <div class="template-item">
    <a href="https://cu-esiil.github.io/HYR-SENSE/" target="_blank">
      <img src="https://github.com/CU-ESIIL/home/blob/main/docs/assets/thumbnails/hyr-sense.jpeg?raw=true" alt="HYR-SENSE">
    </a>
    <p><strong>HYR-SENSE</strong></p>
    <p>Remote sensing.</p>
  </div>


  
  <div class="template-item">
    <a href="https://cu-esiil.github.io/agu-2023_innovation_session/" target="_blank">
      <img src="https://github.com/CU-ESIIL/home/blob/main/docs/assets/thumbnails/AGU_innovation_summit.jpeg?raw=true" alt="AGU 2023 Innovation Session">
    </a>
    <p><strong>AGU 2023 Innovation Session</strong></p>
    <p>Maximizing Stakeholder Engagement in Open Environmental Data Science.</p>
  </div>

</div>

<style>
  .template-gallery {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
    gap: 20px;
    justify-content: center;
  }

  .template-item {
    text-align: center;
  }

  .template-item img {
    width: 100%;
    aspect-ratio: 1 / 1;
    border-radius: 10px;
    object-fit: cover;
  }
</style>

---

## 🛠️ **OASIS Templates & Reusable Frameworks**  
Templates to streamline project development and research collaboration.

<div class="template-gallery">

  

  <div class="template-item">
    <a href="https://cu-esiil.github.io/Postdoc_OASIS/" target="_blank">
      <img src="https://github.com/CU-ESIIL/home/blob/main/docs/assets/thumbnails/postdoc_oasis.jpeg?raw=true" alt="Postdoc OASIS">
    </a>
    <p><strong>Postdoc OASIS</strong></p>
    <p>Template for postdoc research documentation.</p>
  </div>


  <div class="template-item">
    <a href="https://cu-esiil.github.io/Working_group_OASIS/" target="_blank">
      <img src="https://github.com/CU-ESIIL/home/blob/main/docs/assets/thumbnails/working_group_oasis.jpeg?raw=true" alt="Working Group OASIS">
    </a>
    <p><strong>Working Group OASIS</strong></p>
    <p>Central hub for information on ESIIL working groups.</p>
  </div>

  
  <div class="template-item">
    <a href="https://github.com/CU-ESIIL/base-gh-pages" target="_blank">
      <img src="https://github.com/CU-ESIIL/home/blob/main/docs/assets/thumbnails/base_github_page.jpeg?raw=true" alt="Base GitHub Pages">
    </a>
    <p><strong>Base GitHub Pages</strong></p>
    <p>Starter repository for GitHub Pages projects.</p>
  </div>
  
  <div class="template-item">
    <a href="https://cu-esiil.github.io/Education_OASIS/" target="_blank">
      <img src="https://github.com/CU-ESIIL/home/blob/main/docs/assets/thumbnails/edu_oasis.jpeg?raw=true" alt="Education OASIS">
    </a>
    <p><strong>Education OASIS</strong></p>
    <p>Template for ESIIL education students to create their own OASIS.</p>
  </div>

  <div class="template-item">
    <a href="https://cu-esiil.github.io/Slideshow_OASIS/" target="_blank">
      <img src="https://github.com/CU-ESIIL/home/blob/main/docs/assets/thumbnails/slideshow_OASIS.jpeg?raw=true" alt="Slideshow OASIS">
    </a>
    <p><strong>Slideshow OASIS</strong></p>
    <p>Basic slideshow template for presentations.</p>
  </div>

</div>

<style>
  .template-gallery {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
    gap: 20px;
    justify-content: center;
  }

  .template-item {
    text-align: center;
  }

  .template-item img {
    width: 100%;
    aspect-ratio: 1 / 1;
    border-radius: 10px;
    object-fit: cover;
  }
</style>

---

## 📖 **Tutorials**  
Guides and walkthroughs to help researchers and students learn new tools and techniques.

| Name | Description | Link |
|------|------------|------|
| **[Haskell Data Cube](https://github.com/CU-ESIIL/Haskell-data-cube)** | Creating data cubes with multi-source remote sensing data. | 🔗 GitHub |
| **[CI/CD Demo](https://github.com/CU-ESIIL/CI_CD_Demo)** | Demonstration repository for continuous integration and deployment. | 🔗 GitHub |
| **[Haskell API Demo](https://github.com/CU-ESIIL/Haskell-api-demo)** | Sensing the Earth workshop demonstration. | 🔗 GitHub |

---

## 🏗️ **CI Infrastructure & Tools**  
Repositories focused on software, data infrastructure, and computational tools.

<div class="template-gallery">

  <div class="template-item">
    <a href="https://github.com/CU-ESIIL/docker" target="_blank">
      <img src="https://github.com/CU-ESIIL/home/blob/main/docs/assets/thumbnails/docker.jpeg?raw=true" alt="Docker">
    </a>
    <p><strong>Docker</strong></p>
    <p>Private repository for containerized workflows and CI/CD.</p>
  </div>

  <div class="template-item">
    <a href="https://github.com/CU-ESIIL/cyverse-utils" target="_blank">
      <img src="https://github.com/CU-ESIIL/home/blob/main/docs/assets/thumbnails/cyverse_utils.jpeg?raw=true" alt="CyVerse Utils">
    </a>
    <p><strong>CyVerse Utils</strong></p>
    <p>Utilities for working with CyVerse infrastructure.</p>
  </div>

  <div class="template-item">
    <a href="https://cu-esiil.github.io/OASISDockerDemo/" target="_blank">
      <img src="https://github.com/CU-ESIIL/home/blob/main/docs/assets/thumbnails/oasis_docker_demo.jpeg?raw=true" alt="OASIS Docker Demo">
    </a>
    <p><strong>OASIS Docker Demo</strong></p>
    <p>Public demonstration of Dockerized workflows.</p>
  </div>

  <div class="template-item">
    <a href="https://cu-esiil.github.io/Min_docker_demo/" target="_blank">
      <img src="https://github.com/CU-ESIIL/home/blob/main/docs/assets/thumbnails/mini_docker_demo.jpeg?raw=true" alt="Min Docker Demo">
    </a>
    <p><strong>Min Docker Demo</strong></p>
    <p>Minimal demonstration for Docker containers.</p>
  </div>

  <div class="template-item">
    <a href="https://github.com/CU-ESIIL/cyverse-issues" target="_blank">
      <img src="https://github.com/CU-ESIIL/home/blob/main/docs/assets/thumbnails/cyverse_issues.jpeg?raw=true" alt="CyVerse Issues">
    </a>
    <p><strong>CyVerse Issues</strong></p>
    <p>Documenting known issues in CyVerse workflows.</p>
  </div>

  <div class="template-item">
    <a href="./dev-schedule/" target="_blank">
      <img src="https://github.com/CU-ESIIL/home/blob/main/docs/gantt_chart.png?raw=true" alt="Development Schedule">
    </a>
    <p><strong>Development Schedule</strong></p>
    <p>Living task list and timeline for OASIS development.</p>
  </div>

  </div>

<style>
  .template-gallery {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
    gap: 20px;
    justify-content: center;
  }

  .template-item {
    text-align: center;
  }

  .template-item img {
    width: 100%;
    aspect-ratio: 1 / 1;
    border-radius: 10px;
    object-fit: cover;
  }
</style>

---

## 🎓 **Teaching Resources**  
Repositories containing materials for courses, workshops, and tutorials.

| Name | Description | Link |
|------|------------|------|
| **[Pre-Innovation Summit Training](https://cu-esiil.github.io/pre-innovation-summit-training/)** | Repository for all things pre-innovation-summit-training. | 🔗 Website |
| **[EDS Demo](https://cu-esiil.github.io/eds_demo/)** | Example repository for environmental data science education. | 🔗 Website |
| **[Git & GitHub Fundamentals](https://github.com/CU-ESIIL/git-github-fundamentals-eculler)** | GitHub Classroom-created fundamentals course. | 🔗 GitHub |
| **[WG PI Orientation](https://cu-esiil.github.io/WG_PI_Orientation/)** | Orientation materials for ESIIL working group PIs. | 🔗 Website |



---




## ❌ **To Be Deleted**  
These repositories are marked for removal.

| Name | Description | Link |
|------|------------|------|
| **[Shannon-Boldt](https://github.com/CU-ESIIL/Shannon-Boldt)** | Private repository, marked for deletion. | 🔗 GitHub |
| **[Ty Ed Demo](https://cu-esiil.github.io/Ty_ed_demo/)** | One-time use education repository. | 🔗 Website |
| **[Ty Test](https://cu-esiil.github.io/Ty_test/)** | Single-use education test repository. | 🔗 Website |

---

# 🏛️ **Group Sub-Repositories**

This section contains sub-repositories from various events, including the **Innovation Summit, HYR-SENSE, FCC24, and Hackathon 2023**. These repos represent collaborative breakout group projects and associated work.

---

## 🌟 **Innovation Summit 2024 Breakout Groups**

| Name | Description | Link |
|------|------------|------|
| **[Innovation-Summit-2024__3](https://github.com/CU-ESIIL/Innovation-Summit-2024__3)** | Breakout group 3 from the Innovation Summit 2024. | 🔗 GitHub |
| **[Innovation-Summit-2024__4](https://github.com/CU-ESIIL/Innovation-Summit-2024__4)** | Breakout group 4 from the Innovation Summit 2024. | 🔗 GitHub |
| **[Innovation-Summit-2024__5](https://github.com/CU-ESIIL/Innovation-Summit-2024__5)** | Breakout group 5 from the Innovation Summit 2024. | 🔗 GitHub |
| **[Innovation-Summit-2024__6](https://github.com/CU-ESIIL/Innovation-Summit-2024__6)** | Breakout group 6 from the Innovation Summit 2024. | 🔗 GitHub |

---

## 🌍 **HYR-SENSE Workshop Group Repositories**

| Name | Description | Link |
|------|------------|------|
| **[HYR-SENSE-Alaska](https://github.com/CU-ESIIL/HYR-SENSE-Alaska)** | HYR-SENSE Alaska breakout group. | 🔗 GitHub |
| **[HYR-SENSE-Tyler](https://github.com/CU-ESIIL/HYR-SENSE-Tyler)** | HYR-SENSE Tyler breakout project. | 🔗 GitHub |
| **[HYR-SENSE-VTaho](https://github.com/CU-ESIIL/HYR-SENSE-VTaho)** | HYR-SENSE Vermont-Tahoe research group. | 🔗 GitHub |
| **[HYR-SENSE-MaryB](https://github.com/CU-ESIIL/HYR-SENSE-MaryB)** | HYR-SENSE research led by Mary B. | 🔗 GitHub |

---

## 🔬 **FCC24 Group Repositories**

| Name | Description | Link |
|------|------------|------|
| **[FCC24_Group_1](https://github.com/CU-ESIIL/FCC24_Group_1)** | Group 1 from FCC24. | 🔗 GitHub |
| **[FCC24_Group_2](https://github.com/CU-ESIIL/FCC24_Group_2)** | Group 2 from FCC24. | 🔗 GitHub |
| **[FCC24_Group_3](https://github.com/CU-ESIIL/FCC24_Group_3)** | Group 3 from FCC24. | 🔗 GitHub |
| **[FCC24_Group_4](https://github.com/CU-ESIIL/FCC24_Group_4)** | Group 4 from FCC24. | 🔗 GitHub |
| **[FCC24_Group_5](https://github.com/CU-ESIIL/FCC24_Group_5)** | Group 5 from FCC24. | 🔗 GitHub |
| **[FCC24_Group_6](https://github.com/CU-ESIIL/FCC24_Group_6)** | Group 6 from FCC24. | 🔗 GitHub |

---

## 🚀 **Hackathon 2023 Group Repositories**

| Name | Description | Link |
|------|------------|------|
| **[hackathon2023_A](https://github.com/CU-ESIIL/hackathon2023_A)** | Breakout group A from Hackathon 2023. | 🔗 GitHub |
| **[hackathon2023_B](https://github.com/CU-ESIIL/hackathon2023_B)** | Breakout group B from Hackathon 2023. | 🔗 GitHub |
| **[hackathon2023_C](https://github.com/CU-ESIIL/hackathon2023_C)** | Breakout group C from Hackathon 2023. | 🔗 GitHub |
| **[hackathon2023_D](https://github.com/CU-ESIIL/hackathon2023_D)** | Breakout group D from Hackathon 2023. | 🔗 GitHub |
| **[hackathon2023_E](https://github.com/CU-ESIIL/hackathon2023_E)** | Breakout group E from Hackathon 2023. | 🔗 GitHub |
| **[hackathon2023_F](https://github.com/CU-ESIIL/hackathon2023_F)** | Breakout group F from Hackathon 2023. | 🔗 GitHub |
| **[hackathon2023_G](https://github.com/CU-ESIIL/hackathon2023_G)** | Breakout group G from Hackathon 2023. | 🔗 GitHub |

---



📧 **Contact**: [esiil-support@cu.edu](mailto:esiil-support@cu.edu)




