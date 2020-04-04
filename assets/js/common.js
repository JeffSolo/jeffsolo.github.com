
function toggle_content(id) {
  element = document.getElementById(id);
  if (element) {
    if (element.style.display === "none") {
      element.style.display = "block";
    } else {
      element.style.display = "none";
    }
  }
};
