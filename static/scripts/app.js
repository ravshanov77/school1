window.addEventListener("beforeunload", function () {
  sessionStorage.setItem("scrollPosition", window.scrollY);
});

window.addEventListener("DOMContentLoaded", function () {
  const scrollPosition = sessionStorage.getItem("scrollPosition");
  if (scrollPosition) {
    window.scrollTo(0, parseInt(scrollPosition));
  }
});

function toggleFaq(element) {
  const faqItem = element.parentElement;
  faqItem.classList.toggle("open");
}
