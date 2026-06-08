/* rosetta-stone.js — shared interactivity for datasets, collections, releases pages */

// ─── Dataset page ─────────────────────────────────────────────────────────────

function initDatasetPage() {
  var table = document.getElementById("rsDatasetTable");
  if (!table || table.getAttribute("data-rs-init") === "1") return;
  table.setAttribute("data-rs-init", "1");

  var searchInput      = document.getElementById("rsSearch");
  var releaseFilter    = document.getElementById("rsReleaseFilter");
  var cdeFilter        = document.getElementById("rsCdeFilter");
  var collectionFilter = document.getElementById("rsCollectionFilter");
  var tagFilter        = document.getElementById("rsTagFilter");
  var countEl          = document.getElementById("rsCount");
  var rows             = Array.from(document.querySelectorAll(".rs-dataset-row"));

  if (!rows.length) return;

  function updateCount(n) {
    if (countEl) countEl.textContent = n + " of " + rows.length + " datasets shown";
  }

  function closeDetail(row) {
    // Used by filter hide — close drawer if open for this row
    var id = row.getAttribute("data-detail");
    var drawer = id ? document.getElementById(id) : null;
    if (drawer && drawer.classList.contains("rs-drawer--open")) {
      rsCloseAllDrawers();
    }
  }

  function applyFilters() {
    var q      = searchInput      ? searchInput.value.toLowerCase().trim()      : "";
    var selR   = releaseFilter    ? releaseFilter.value.toLowerCase().trim()    : "";
    var selC   = cdeFilter        ? cdeFilter.value.toLowerCase().trim()        : "";
    var selCol = collectionFilter ? collectionFilter.value.toLowerCase().trim() : "";
    var selTag = tagFilter        ? tagFilter.value.toLowerCase().trim()        : "";
    var vis = 0;

    rows.forEach(function(row) {
      var text    = (row.getAttribute("data-search")     || "").toLowerCase();
      var rowR    = (row.getAttribute("data-release")    || "").toLowerCase();
      var rowC    = (row.getAttribute("data-cde")        || "").toLowerCase();
      var rowCol  = (row.getAttribute("data-collection") || "").toLowerCase();
      var rowTags = (row.getAttribute("data-tags")       || "").toLowerCase();

      var cdeList = rowC.split("||").map(function(s){ return s.trim(); }).filter(Boolean);
      var tagList = rowTags.split("||").map(function(s){ return s.trim(); }).filter(Boolean);

      var ok = (
        (q      === "" || text.includes(q))              &&
        (selR   === "" || rowR === selR)                  &&
        (selC   === "" || cdeList.includes(selC))         &&
        (selCol === "" || rowCol === selCol)               &&
        (selTag === "" || tagList.includes(selTag))
      );

      row.style.display = ok ? "table-row" : "none";
      if (!ok) closeDetail(row);
      if (ok)  vis++;
    });
    updateCount(vis);
  }

  // Toggle handled by rsOpenDrawer / rsCloseDrawer (inline onclick on buttons)

  // Expand / collapse all visible — not meaningful with side drawer UX; disable
  var expandAllBtn   = document.getElementById("rsExpandAll");
  var collapseAllBtn = document.getElementById("rsCollapseAll");
  if (expandAllBtn)   expandAllBtn.style.display   = "none";
  if (collapseAllBtn) collapseAllBtn.style.display = "none";

  // Clear filters
  var clearBtn = document.getElementById("rsClearFilters");
  if (clearBtn) {
    clearBtn.addEventListener("click", function() {
      [searchInput, releaseFilter, cdeFilter, collectionFilter, tagFilter].forEach(function(el) {
        if (el) el.value = "";
      });
      applyFilters();
    });
  }

  // Wire filters
  [searchInput, releaseFilter, cdeFilter, collectionFilter, tagFilter].forEach(function(el) {
    if (!el) return;
    el.addEventListener(el.tagName === "INPUT" ? "input" : "change", applyFilters);
  });

  // Sortable columns
  var sortState = { col: -1, dir: "asc" };

  function versionNums(str) {
    var m = String(str).match(/\d+/g);
    return m ? m.map(Number) : [0];
  }
  function cmpVersions(a, b) {
    var av = versionNums(a), bv = versionNums(b);
    for (var i = 0; i < Math.max(av.length, bv.length); i++) {
      var d = (av[i] || 0) - (bv[i] || 0);
      if (d !== 0) return d;
    }
    return 0;
  }

  function sortTable(col, dir) {
    var tbody = table.querySelector("tbody");
    var allTr = Array.from(tbody.querySelectorAll("tr"));
    var pairs = [];
    for (var i = 0; i < allTr.length; i++) {
      if (allTr[i].classList.contains("rs-dataset-row")) {
        var nxt = allTr[i + 1];
        pairs.push({
          main:   allTr[i],
          detail: (nxt && nxt.classList.contains("rs-detail-row")) ? nxt : null
        });
      }
    }
    var verCols = { 3: true, 4: true, 5: true };
    pairs.sort(function(a, b) {
      var ac = a.main.querySelectorAll("td")[col];
      var bc = b.main.querySelectorAll("td")[col];
      var at = ac ? ac.textContent.trim() : "";
      var bt = bc ? bc.textContent.trim() : "";
      var cmp = verCols[col] ? cmpVersions(at, bt) : at.toLowerCase().localeCompare(bt.toLowerCase());
      return dir === "asc" ? cmp : -cmp;
    });
    pairs.forEach(function(p) {
      tbody.appendChild(p.main);
      if (p.detail) tbody.appendChild(p.detail);
    });
  }

  table.querySelectorAll("th.sortable").forEach(function(th) {
    th.addEventListener("click", function() {
      var col = parseInt(th.getAttribute("data-col"), 10);
      var dir = (sortState.col === col && sortState.dir === "asc") ? "desc" : "asc";
      sortState = { col: col, dir: dir };
      table.querySelectorAll(".rs-sort-icon").forEach(function(ic) {
        ic.className = "rs-sort-icon";
        ic.textContent = "⇅";
      });
      var icon = th.querySelector(".rs-sort-icon");
      if (icon) {
        icon.className = "rs-sort-icon " + dir;
        icon.textContent = dir === "asc" ? "↑" : "↓";
      }
      sortTable(col, dir);
    });
  });

  updateCount(rows.length);
}


// ─── Release tab switching ─────────────────────────────────────────────────────

function rsTabSwitch(btn) {
  var panelId = btn.getAttribute("data-panel");
  if (!panelId) return;

  var tabGroup = btn.closest(".rs-release-tabs");
  if (tabGroup) {
    tabGroup.querySelectorAll(".rs-rtab").forEach(function(t) {
      t.classList.remove("rs-rtab--active");
    });
  }
  btn.classList.add("rs-rtab--active");

  var section = btn.closest(".rs-section");
  if (section) {
    section.querySelectorAll(".rs-panel-sections").forEach(function(p) {
      p.style.display = "none";
    });
  }
  var panel = document.getElementById(panelId);
  if (panel) panel.style.display = "flex";

  // Sync history table row highlight
  // Panel id format: <prefix>-<release>  where release may contain dots/digits
  // We stored data-release on each history row for reliable matching
  var parts   = panelId.split("-");
  var release = parts[parts.length - 1];
  var detailTr = btn.closest(".rs-detail-row");
  if (detailTr) {
    detailTr.querySelectorAll(".rs-history-row").forEach(function(r) {
      r.classList.toggle(
        "rs-history-row--active",
        r.getAttribute("data-release") === release
      );
    });
  }
}


// ─── History row click → switch tab ───────────────────────────────────────────

document.addEventListener("click", function(e) {
  var row = e.target.closest(".rs-history-row");
  if (!row) return;
  var release = row.getAttribute("data-release");
  if (!release) return;
  var wrapper = row.closest(".rs-detail");
  if (!wrapper) return;
  var tab = Array.from(wrapper.querySelectorAll(".rs-rtab")).find(function(t) {
    return (t.getAttribute("data-panel") || "").endsWith("-" + release);
  });
  if (tab) rsTabSwitch(tab);
});


// ─── Side drawer ──────────────────────────────────────────────────────────────

function rsOpenDrawer(btn) {
  var id      = btn.getAttribute("data-target");
  var drawer  = id ? document.getElementById(id) : null;
  var overlay = document.getElementById("rsDrawerOverlay");
  if (!drawer) return;

  // Close any already-open drawer first
  rsCloseAllDrawers();

  drawer.classList.add("rs-drawer--open");
  if (overlay) overlay.classList.add("rs-drawer-overlay--visible");

  // Highlight the triggering row
  var row = btn.closest(".rs-dataset-row");
  if (row) row.classList.add("rs-dataset-row--active");

  // Update button label
  btn.textContent = "Close";
}

function rsCloseDrawer(closeBtn) {
  var drawer  = closeBtn.closest(".rs-drawer");
  var overlay = document.getElementById("rsDrawerOverlay");
  if (!drawer) return;
  _rsCloseDrawer(drawer, overlay);
}

function rsCloseAllDrawers() {
  var overlay = document.getElementById("rsDrawerOverlay");
  document.querySelectorAll(".rs-drawer--open").forEach(function(d) {
    _rsCloseDrawer(d, overlay);
  });
}

function _rsCloseDrawer(drawer, overlay) {
  drawer.classList.remove("rs-drawer--open");
  if (overlay) overlay.classList.remove("rs-drawer-overlay--visible");

  // Un-highlight the row and reset its button
  var id  = drawer.id;
  var row = document.querySelector('.rs-dataset-row[data-detail="' + id + '"]');
  if (row) {
    row.classList.remove("rs-dataset-row--active");
    var btn = row.querySelector(".rs-toggle");
    if (btn) btn.textContent = "View";
  }
}

// Close drawer on Escape key
document.addEventListener("keydown", function(e) {
  if (e.key === "Escape") rsCloseAllDrawers();
});




function rsCopyPath(btn) {
  var path = btn.getAttribute("data-path");
  if (!path) return;
  navigator.clipboard.writeText(path).catch(function() {});
  btn.textContent = "Copied!";
  btn.classList.add("rs-copy-btn--copied");
  setTimeout(function() {
    btn.textContent = "Copy";
    btn.classList.remove("rs-copy-btn--copied");
  }, 1500);
}


// ─── MkDocs Material SPA compatibility ─────────────────────────────────────────

function rsInit() {
  initDatasetPage();
}

if (typeof document$ !== "undefined") {
  document$.subscribe(rsInit);
} else {
  document.addEventListener("DOMContentLoaded", rsInit);
}
