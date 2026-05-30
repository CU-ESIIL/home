(() => {
  let cleanup = () => {};

  function initOasisRingParallax(root) {
    cleanup();

    const rings = Array.from(root.querySelectorAll("[data-oasis-ring]"));
    const prefersReducedMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

    if (!rings.length || prefersReducedMotion) {
      cleanup = () => {};
      return;
    }

    let rafId = 0;
    let ticking = false;

    // Keep the scroll effect subtle and reusable by writing only one CSS var.
    const update = () => {
      ticking = false;
      const viewportMid = (window.innerHeight || document.documentElement.clientHeight) / 2;

      rings.forEach((ring) => {
        const factor = Number.parseFloat(
          ring.getAttribute("data-oasis-ring-parallax") || "0.2",
        );
        const rect = ring.getBoundingClientRect();
        const ringMid = rect.top + (rect.height / 2);
        const shift = (viewportMid - ringMid) * factor;
        ring.style.setProperty("--oasis-ring-scroll-shift", `${shift.toFixed(2)}px`);
      });
    };

    const requestTick = () => {
      if (ticking) return;
      ticking = true;
      rafId = window.requestAnimationFrame(update);
    };

    update();
    window.addEventListener("scroll", requestTick, { passive: true });
    window.addEventListener("resize", requestTick);

    cleanup = () => {
      if (rafId) window.cancelAnimationFrame(rafId);
      window.removeEventListener("scroll", requestTick);
      window.removeEventListener("resize", requestTick);
      rings.forEach((ring) => ring.style.removeProperty("--oasis-ring-scroll-shift"));
    };
  }

  const initialize = () => {
    const root = document.querySelector(".oasis-homepage, .oasis-section-page") || document;
    initOasisRingParallax(root);
  };

  if (typeof document$ !== "undefined" && typeof document$.subscribe === "function") {
    document$.subscribe(() => {
      window.requestAnimationFrame(initialize);
    });
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", initialize, { once: true });
  } else {
    initialize();
  }
})();
