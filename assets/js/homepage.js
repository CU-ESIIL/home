(() => {
  const root = document.querySelector(".oasis-homepage");
  if (!root) return;
  document.documentElement.classList.add("oasis-home-enhanced");

  const prefersReducedMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  const revealItems = root.querySelectorAll("[data-reveal]");

  if (!prefersReducedMotion && "IntersectionObserver" in window) {
    const observer = new IntersectionObserver(
      entries => {
        entries.forEach(entry => {
          if (entry.isIntersecting) {
            entry.target.classList.add("is-visible");
            observer.unobserve(entry.target);
          }
        });
      },
      {
        rootMargin: "0px 0px -10% 0px",
        threshold: 0.15,
      }
    );

    revealItems.forEach(item => observer.observe(item));
  } else {
    revealItems.forEach(item => item.classList.add("is-visible"));
  }

  if (prefersReducedMotion) return;

  const parallaxItems = root.querySelectorAll("[data-parallax]");
  if (!parallaxItems.length) return;

  const multipliers = {
    slow: 0.035,
    mid: 0.06,
    fast: 0.085,
  };

  const updateParallax = () => {
    const hero = root.querySelector(".oasis-home__hero-art");
    if (!hero) return;

    const rect = hero.getBoundingClientRect();
    const viewportHeight = window.innerHeight || document.documentElement.clientHeight;
    const progress = (viewportHeight - rect.top) / (viewportHeight + rect.height);
    const clamped = Math.max(0, Math.min(1, progress));

    parallaxItems.forEach(item => {
      const speed = multipliers[item.dataset.parallax] || multipliers.mid;
      const shift = (clamped - 0.5) * 34 * speed * 10;
      item.style.setProperty("--oasis-parallax-shift", `${shift.toFixed(2)}px`);
    });
  };

  updateParallax();
  window.addEventListener("scroll", updateParallax, { passive: true });
  window.addEventListener("resize", updateParallax);
})();
