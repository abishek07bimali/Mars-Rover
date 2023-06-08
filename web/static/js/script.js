// script.js

let hamMenuIcon = document.getElementById("ham-menu");
let navBar = document.getElementById("nav-bar");
let navLinks = navBar.querySelectorAll("li");

hamMenuIcon.addEventListener("click", () => {
  navBar.classList.toggle("active");
  hamMenuIcon.classList.toggle("fa-times");
});
navLinks.forEach((navLinks) => {
  navLinks.addEventListener("click", () => {
    navBar.classList.remove("active");
    hamMenuIcon.classList.toggle("fa-times");
  });
});

document.addEventListener('DOMContentLoaded', () => {
  // Get the sidebar links
  const sidebarLinks = document.querySelectorAll(' ul li a');
  const pages = document.querySelectorAll('.page');

  // Show the initial page
  showPage(pages[0]);
  sidebarLinks[0].classList.add('active');

  // Add event listeners to the sidebar links
  sidebarLinks.forEach((link, index) => {
    link.addEventListener('click', (event) => {
      event.preventDefault();

      // Remove active class from all sidebar links
      sidebarLinks.forEach(link => {
        link.classList.remove('active');
      });

      // Add active class to the clicked link
      link.classList.add('active');

      // Show the target page
      showPage(pages[index]);
    });
  });

  // Function to show a specific page
  function showPage(page) {
    // Hide all pages
    pages.forEach(item => {
      item.style.display = 'none';
    });

    // Show the target page
    page.style.display = 'block';
  }
});

