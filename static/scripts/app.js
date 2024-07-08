document.addEventListener("DOMContentLoaded", function () {
  // Load scroll position after content is loaded
  if (localStorage.getItem("scrollPosition")) {
    console.log(
      "Restoring scroll position:",
      localStorage.getItem("scrollPosition")
    );
    window.scrollTo(0, parseInt(localStorage.getItem("scrollPosition")));
  } else {
    console.log("No scroll position saved");
  }
});

window.addEventListener("beforeunload", function () {
  localStorage.setItem(
    "scrollPosition",
    window.scrollY || document.documentElement.scrollTop
  );
  console.log(
    "Saved scroll position:",
    window.scrollY || document.documentElement.scrollTop
  );
});
