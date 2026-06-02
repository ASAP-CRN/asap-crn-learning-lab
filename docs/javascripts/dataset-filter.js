function initializeDatasetPage() {
  const table = document.getElementById("datasetTable");

  if (!table) {
    return;
  }

  if (table.getAttribute("data-initialized") === "true") {
    return;
  }

  table.setAttribute("data-initialized", "true");

  const searchInput = document.getElementById("datasetSearch");
  const tagFilter = document.getElementById("tagFilter");
  const datasetCount = document.getElementById("datasetCount");
  const rows = Array.from(document.querySelectorAll(".dataset-row"));
  const buttons = Array.from(document.querySelectorAll(".dataset-toggle"));

  if (!rows.length) {
    return;
  }

  function updateCount(visibleCount) {
    if (datasetCount) {
      datasetCount.textContent = visibleCount + " of " + rows.length + " datasets shown";
    }
  }

  function closeDetailRow(row) {
    const detailId = row.getAttribute("data-detail");
    const detailRow = document.getElementById(detailId);
    const button = row.querySelector(".dataset-toggle");

    if (detailRow) {
      detailRow.style.display = "none";
    }

    if (button) {
      button.textContent = "View";
    }
  }

  function applyFilters() {
    const query = searchInput ? searchInput.value.toLowerCase().trim() : "";
    const selectedTag = tagFilter ? tagFilter.value.toLowerCase().trim() : "";

    let visibleCount = 0;

    rows.forEach(function (row) {
      const text = row.getAttribute("data-search") || "";
      const tags = row.getAttribute("data-tags") || "";

      const tagList = tags
        .split("||")
        .map(function (tag) {
          return tag.trim();
        })
        .filter(Boolean);

      const matchesText = query === "" || text.includes(query);
      const matchesTag = selectedTag === "" || tagList.includes(selectedTag);

      const isVisible = matchesText && matchesTag;

      row.style.display = isVisible ? "table-row" : "none";

      if (!isVisible) {
        closeDetailRow(row);
      }

      if (isVisible) {
        visibleCount += 1;
      }
    });

    updateCount(visibleCount);
  }

  buttons.forEach(function (button) {
    button.addEventListener("click", function () {
      const targetId = button.getAttribute("data-target");
      const detailRow = document.getElementById(targetId);

      if (!detailRow) {
        return;
      }

      const isOpen = detailRow.style.display === "table-row";
      detailRow.style.display = isOpen ? "none" : "table-row";
      button.textContent = isOpen ? "View" : "Hide";
    });
  });

  if (searchInput) {
    searchInput.addEventListener("input", applyFilters);
  }

  if (tagFilter) {
    tagFilter.addEventListener("change", applyFilters);
  }

  updateCount(rows.length);
}

if (typeof document$ !== "undefined") {
  document$.subscribe(function () {
    initializeDatasetPage();
  });
} else {
  document.addEventListener("DOMContentLoaded", initializeDatasetPage);
}
