// ─── Initialise dataset page ────────────────────────────────────────────────

function initializeDatasetPage() {
  var table = document.getElementById("datasetTable");
  if (!table) return;
  if (table.getAttribute("data-initialized") === "true") return;
  table.setAttribute("data-initialized", "true");

  var searchInput      = document.getElementById("datasetSearch");
  var tagFilter        = document.getElementById("tagFilter");
  var releaseFilter    = document.getElementById("releaseFilter");
  var cdeFilter        = document.getElementById("cdeFilter");
  var collectionFilter = document.getElementById("collectionFilter");
  var datasetCount     = document.getElementById("datasetCount");
  var rows             = Array.from(document.querySelectorAll(".dataset-row"));
  var buttons          = Array.from(document.querySelectorAll(".dataset-toggle"));

  if (!rows.length) return;

  // ── Count display ──────────────────────────────────────────────────────────
  function updateCount(n) {
    if (datasetCount) datasetCount.textContent = n + " of " + rows.length + " datasets shown";
  }

  // ── Close detail row ───────────────────────────────────────────────────────
  function closeDetail(row) {
    var id  = row.getAttribute("data-detail");
    var dr  = id ? document.getElementById(id) : null;
    var btn = row.querySelector(".dataset-toggle");
    if (dr)  dr.style.display = "none";
    if (btn) btn.textContent  = "View";
  }

  // ── Apply all active filters ───────────────────────────────────────────────
  function applyFilters() {
    var query      = searchInput      ? searchInput.value.toLowerCase().trim()      : "";
    var selTag     = tagFilter        ? tagFilter.value.toLowerCase().trim()        : "";
    var selRelease = releaseFilter    ? releaseFilter.value.toLowerCase().trim()    : "";
    var selCde     = cdeFilter        ? cdeFilter.value.toLowerCase().trim()        : "";
    var selCol     = collectionFilter ? collectionFilter.value.toLowerCase().trim() : "";

    var visible = 0;
    rows.forEach(function(row) {
      var text       = (row.getAttribute("data-search")     || "").toLowerCase();
      var tags       = (row.getAttribute("data-tags")       || "").toLowerCase();
      var rowRelease = (row.getAttribute("data-release")    || "").toLowerCase();
      var rowCde     = (row.getAttribute("data-cde")        || "").toLowerCase();
      var rowCol     = (row.getAttribute("data-collection") || "").toLowerCase();

      var tagList = tags.split("||").map(function(t){ return t.trim(); }).filter(Boolean);
      var cdeList = rowCde.split("||").map(function(t){ return t.trim(); }).filter(Boolean);

      var ok = (
        (query      === "" || text.includes(query))                       &&
        (selTag     === "" || tagList.includes(selTag))                   &&
        (selRelease === "" || rowRelease === selRelease)                   &&
        (selCde     === "" || cdeList.includes(selCde))                   &&
        (selCol     === "" || rowCol === selCol)
      );

      row.style.display = ok ? "table-row" : "none";
      if (!ok) closeDetail(row);
      if (ok)  visible++;
    });
    updateCount(visible);
  }

  // ── Toggle detail row ──────────────────────────────────────────────────────
  buttons.forEach(function(btn) {
    btn.addEventListener("click", function() {
      var id = btn.getAttribute("data-target");
      var dr = id ? document.getElementById(id) : null;
      if (!dr) return;
      var open = dr.style.display === "table-row";
      dr.style.display = open ? "none" : "table-row";
      btn.textContent  = open ? "View" : "Hide";
    });
  });

  // ── Wire up filters ────────────────────────────────────────────────────────
  [searchInput, tagFilter, releaseFilter, cdeFilter, collectionFilter].forEach(function(el) {
    if (el) el.addEventListener(el.tagName === "INPUT" ? "input" : "change", applyFilters);
  });

  // ── Sortable columns ───────────────────────────────────────────────────────
  var sortState = { col: -1, dir: "asc" };

  function versionVal(str) {
    // Parse "v4.0.2" → numeric tuple for comparison; fallback to string
    var nums = String(str).match(/\d+/g);
    if (!nums) return [0];
    return nums.map(Number);
  }

  function compareVersions(a, b) {
    var av = versionVal(a), bv = versionVal(b);
    for (var i = 0; i < Math.max(av.length, bv.length); i++) {
      var diff = (av[i] || 0) - (bv[i] || 0);
      if (diff !== 0) return diff;
    }
    return 0;
  }

  function sortTable(colIndex, dir) {
    var tbody = table.querySelector("tbody");
    // Collect pairs of [data-row, detail-row] to keep them together
    var pairs = [];
    var allRows = Array.from(tbody.querySelectorAll("tr"));
    for (var i = 0; i < allRows.length; i++) {
      if (allRows[i].classList.contains("dataset-row")) {
        var next = allRows[i + 1];
        pairs.push({
          main:   allRows[i],
          detail: (next && next.classList.contains("dataset-detail-row")) ? next : null
        });
      }
    }

    // Version-aware columns: 3 (dataset version), 4 (release), 5 (collection version)
    var versionCols = { 3: true, 4: true, 5: true };

    pairs.sort(function(a, b) {
      var aCell = a.main.querySelectorAll("td")[colIndex];
      var bCell = b.main.querySelectorAll("td")[colIndex];
      var aText = aCell ? aCell.textContent.trim() : "";
      var bText = bCell ? bCell.textContent.trim() : "";

      var cmp = versionCols[colIndex]
        ? compareVersions(aText, bText)
        : aText.toLowerCase().localeCompare(bText.toLowerCase());

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

      // Reset all icons
      table.querySelectorAll(".sort-icon").forEach(function(ic) {
        ic.className = "sort-icon";
        ic.textContent = "⇅";
      });
      // Set active icon
      var icon = th.querySelector(".sort-icon");
      if (icon) {
        icon.className = "sort-icon " + dir;
        icon.textContent = dir === "asc" ? "↑" : "↓";
      }

      sortTable(col, dir);
    });
  });

  updateCount(rows.length);
}

// ─── Release tab switching ───────────────────────────────────────────────────
function dsTabSwitch(btn) {
  var panelId = btn.getAttribute("data-panel");
  if (!panelId) return;

  var tabGroup = btn.closest(".ds-release-tabs");
  if (tabGroup) {
    tabGroup.querySelectorAll(".ds-rtab").forEach(function(t) {
      t.classList.remove("ds-rtab--active");
    });
  }
  btn.classList.add("ds-rtab--active");

  var section = btn.closest(".ds-section");
  if (section) {
    section.querySelectorAll(".ds-panel-sections").forEach(function(p) {
      p.style.display = "none";
    });
  }
  var panel = document.getElementById(panelId);
  if (panel) panel.style.display = "flex";

  // Sync history table highlight — panel id ends with "-<release>"
  var parts   = panelId.split("-");
  var release = parts[parts.length - 1];
  var detailRow = btn.closest(".dataset-detail-row");
  if (detailRow) {
    detailRow.querySelectorAll(".ds-history-row").forEach(function(r) {
      r.classList.toggle("ds-history-row--active", r.getAttribute("data-release") === release);
    });
  }
}

// ─── Copy bucket path ────────────────────────────────────────────────────────
function dsCopyPath(btn) {
  var path = btn.getAttribute("data-path");
  if (!path) return;
  navigator.clipboard.writeText(path).catch(function(){});
  btn.textContent = "Copied!";
  btn.classList.add("ds-copy-btn--copied");
  setTimeout(function() {
    btn.textContent = "Copy";
    btn.classList.remove("ds-copy-btn--copied");
  }, 1500);
}

// ─── History row click → switch tab ─────────────────────────────────────────
document.addEventListener("click", function(e) {
  var row = e.target.closest(".ds-history-row");
  if (!row) return;
  var release = row.getAttribute("data-release");
  if (!release) return;
  var wrapper = row.closest(".dataset-detail");
  if (!wrapper) return;
  var tab = Array.from(wrapper.querySelectorAll(".ds-rtab")).find(function(t) {
    return (t.getAttribute("data-panel") || "").endsWith("-" + release);
  });
  if (tab) dsTabSwitch(tab);
});

// ─── MkDocs Material SPA compatibility ───────────────────────────────────────
if (typeof document$ !== "undefined") {
  document$.subscribe(function() { initializeDatasetPage(); });
} else {
  document.addEventListener("DOMContentLoaded", initializeDatasetPage);
}
