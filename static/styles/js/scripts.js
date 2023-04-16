/* scripts.js */
// Scroll to top button
const scrollToTopButton = document.querySelector('.scroll-to-top');

window.addEventListener('scroll', function () {
    if (window.scrollY > 300) {
        // Show the button when the page is scrolled down 300px
        scrollToTopButton.style.display = 'block';
    } else {
        // Hide the button when the page is scrolled up
        scrollToTopButton.style.display = 'none';
    }
});

scrollToTopButton.addEventListener('click', function () {
    // Smoothly scroll the page to the top
    window.scrollTo({
        top: 0,
        behavior: 'smooth'
    });
});