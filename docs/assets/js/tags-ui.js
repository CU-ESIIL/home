(function(){
  function basePath() {
    var loc = document.querySelector("link[rel='canonical']");
    if (loc && loc.href) {
      try {
        var url = new URL(loc.href);
        return url.pathname.replace(/\/[^\/]*$/, '/');
      } catch(e){}
    }
    var p = window.location.pathname;
    return p.endsWith("/") ? p : p.replace(/\/[^\/]*$/, "/");
  }

  function parseDate(s) {
    if (!s) return 0;
    var d = new Date(s);
    return isNaN(d.getTime()) ? 0 : d.getTime();
  }

  function applySort(items, mode) {
    if (mode === "alpha") {
      return items.slice().sort((a,b) => a.title.localeCompare(b.title));
    }
    if (mode === "weight") {
      return items.slice().sort((a,b) => {
        const w = (b.weight||0) - (a.weight||0);
        if (w !== 0) return w;
        return parseDate(b.date) - parseDate(a.date);
      });
    }
    // default: recent
    return items.slice().sort((a,b) => parseDate(b.date) - parseDate(a.date));
  }

  function renderResults(listEl, items) {
    listEl.innerHTML = "";
    items.forEach(function(it){
      var li = document.createElement("li");
      var a = document.createElement("a");
      a.href = "/" + it.path.replace(/^\//, "");
      a.textContent = it.title;
      var small = document.createElement("small");
      small.textContent = it.date || "";
      li.appendChild(a);
      if (small.textContent) {
        li.appendChild(document.createTextNode(" "));
        li.appendChild(small);
      }
      listEl.appendChild(li);
    });
  }

  function init() {
    var root = basePath();
    var jsonUrl = root + "assets/tags.json";
    fetch(jsonUrl).then(r => r.json()).then(data => {
      var pages = data.pages || [];
      var tags = data.tags || [];

      // Build tag index
      var byTag = {};
      pages.forEach(function(p){
        (p.tags || []).forEach(function(t){
          (byTag[t] = byTag[t] || []).push(p);
        });
      });

      var tagSelect = document.getElementById("tag-select");
      var sortSelect = document.getElementById("sort-select");
      var filterInput = document.getElementById("filter-input");
      var results = document.getElementById("tag-results");

      tags.forEach(function(t){
        var opt = document.createElement("option");
        opt.value = t;
        opt.textContent = t;
        tagSelect.appendChild(opt);
      });

      function update() {
        var t = tagSelect.value;
        var mode = sortSelect.value;
        var q = (filterInput.value || "").toLowerCase();
        var items = (byTag[t] || []);
        items = applySort(items, mode);
        if (q) {
          items = items.filter(it => (it.title || "").toLowerCase().includes(q));
        }
        renderResults(results, items);
      }

      tagSelect.addEventListener("change", update);
      sortSelect.addEventListener("change", update);
      filterInput.addEventListener("input", update);

      // Initialize with first tag if available
      if (tags.length) {
        tagSelect.value = tags[0];
      }
      update();
    }).catch(function(err){
      console.warn("Failed to load tags.json", err);
    });
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }
})();
