(() => {
  let cleanup = () => {};

  const HOME_CLASS = "oasis-home-template";
  const SECTION_CLASS = "oasis-section-template";
  const MOTION_CLASS = "oasis-motion-enhanced";

  const multipliers = {
    slow: 0.035,
    mid: 0.06,
    fast: 0.085,
  };

  function setTemplateClasses({ isHome, isSection, hasExperience }) {
    const root = document.documentElement;
    root.classList.toggle(HOME_CLASS, isHome);
    root.classList.toggle(SECTION_CLASS, isSection);
    root.classList.toggle(MOTION_CLASS, hasExperience);
  }

  function initReveal(root, cleanupFns) {
    const revealItems = Array.from(root.querySelectorAll("[data-reveal]"));
    if (!revealItems.length) return;

    const prefersReducedMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

    revealItems.forEach((item) => item.classList.remove("is-visible"));

    if (prefersReducedMotion || !("IntersectionObserver" in window)) {
      revealItems.forEach((item) => item.classList.add("is-visible"));
      return;
    }

    const observer = new IntersectionObserver(
      (entries) => {
        entries.forEach((entry) => {
          if (entry.isIntersecting) {
            entry.target.classList.add("is-visible");
            observer.unobserve(entry.target);
          }
        });
      },
      {
        rootMargin: "0px 0px -10% 0px",
        threshold: 0.15,
      },
    );

    revealItems.forEach((item) => observer.observe(item));
    cleanupFns.push(() => observer.disconnect());
  }

  function initParallax(root, cleanupFns) {
    const prefersReducedMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
    if (prefersReducedMotion) return;

    const hero = root.querySelector(".oasis-home__hero-art");
    const parallaxItems = Array.from(root.querySelectorAll("[data-parallax]"));

    if (!hero || !parallaxItems.length) return;

    const updateParallax = () => {
      const rect = hero.getBoundingClientRect();
      const viewportHeight = window.innerHeight || document.documentElement.clientHeight;
      const progress = (viewportHeight - rect.top) / (viewportHeight + rect.height);
      const clamped = Math.max(0, Math.min(1, progress));

      parallaxItems.forEach((item) => {
        const speed = multipliers[item.dataset.parallax] || multipliers.mid;
        const shift = (clamped - 0.5) * 34 * speed * 10;
        item.style.setProperty("--oasis-parallax-shift", `${shift.toFixed(2)}px`);
      });
    };

    updateParallax();
    window.addEventListener("scroll", updateParallax, { passive: true });
    window.addEventListener("resize", updateParallax);

    cleanupFns.push(() => {
      window.removeEventListener("scroll", updateParallax);
      window.removeEventListener("resize", updateParallax);
      parallaxItems.forEach((item) => item.style.removeProperty("--oasis-parallax-shift"));
    });
  }

  function initializePageExperience() {
    cleanup();

    const homeRoot = document.querySelector(".oasis-homepage");
    const sectionRoot = document.querySelector(".oasis-section-page");
    const experienceRoot = homeRoot || sectionRoot;

    setTemplateClasses({
      isHome: Boolean(homeRoot),
      isSection: Boolean(sectionRoot),
      hasExperience: Boolean(experienceRoot),
    });

    if (!experienceRoot) {
      cleanup = () => {};
      return;
    }

    const cleanupFns = [];
    initReveal(experienceRoot, cleanupFns);

    if (homeRoot) {
      initParallax(homeRoot, cleanupFns);
    }

    cleanup = () => {
      cleanupFns.forEach((fn) => fn());
      cleanupFns.length = 0;
    };
  }

  const scheduleInitialize = () => {
    window.requestAnimationFrame(() => {
      initializePageExperience();
    });
  };

  if (typeof document$ !== "undefined" && typeof document$.subscribe === "function") {
    document$.subscribe(() => {
      scheduleInitialize();
    });
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", scheduleInitialize, { once: true });
  } else {
    scheduleInitialize();
  }
})();
