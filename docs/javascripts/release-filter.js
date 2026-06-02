function initializeReleasePage() {
  const searchInput = document.getElementById("releaseSearch");
  const releaseCount = document.getElementById("releaseCount");
  const cards = Array.from(document.querySelectorAll(".release-card"));
  const modals = Array.from(document.querySelectorAll(".release-modal"));

  if (!cards.length) {
    return;
  }

  function updateCount(visibleCount) {
    if (releaseCount) {
      releaseCount.textContent = visibleCount + " of " + cards.length + " releases shown";
    }
  }

  function closeAllModals() {
    modals.forEach(function (modal) {
      modal.style.display = "none";
    });
  }

  cards.forEach(function (card) {
    card.addEventListener("click", function (event) {
      if (event.target.closest("a")) {
        return;
      }

      const modalId = card.getAttribute("data-modal");
      const modal = document.getElementById(modalId);

      if (modal) {
        modal.style.display = "flex";
      }
    });
  });

  modals.forEach(function (modal) {
    modal.addEventListener("click", function (event) {
      if (event.target === modal || event.target.getAttribute("data-close") === "true") {
        closeAllModals();
      }
    });
  });

  document.addEventListener("keydown", function (event) {
    if (event.key === "Escape") {
      closeAllModals();
    }
  });

  if (searchInput) {
    searchInput.addEventListener("input", function () {
      const query = searchInput.value.toLowerCase().trim();
      let visibleCount = 0;

      cards.forEach(function (card) {
        const text = card.getAttribute("data-search") || "";
        const isVisible = text.includes(query);

        card.style.display = isVisible ? "block" : "none";

        if (isVisible) {
          visibleCount += 1;
        }
      });

      updateCount(visibleCount);
    });
  }

  updateCount(cards.length);
}

if (typeof document$ !== "undefined") {
  document$.subscribe(function () {
    initializeReleasePage();
  });
} else {
  document.addEventListener("DOMContentLoaded", initializeReleasePage);
}
