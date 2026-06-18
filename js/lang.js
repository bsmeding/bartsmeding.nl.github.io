// Set language immediately to prevent flash
document.documentElement.lang = localStorage.getItem('lang') || 'en';

window.toggleLang = function () {
  var next = document.documentElement.lang === 'en' ? 'nl' : 'en';
  document.documentElement.lang = next;
  localStorage.setItem('lang', next);
};

window.toggleMenu = function () {
  var links = document.querySelector('.nav-links');
  if (links) links.classList.toggle('open');
};

document.addEventListener('DOMContentLoaded', function () {
  // Highlight active nav link
  var page = window.location.pathname.split('/').pop() || 'index.html';
  document.querySelectorAll('.nav-links a[href]').forEach(function (a) {
    var href = a.getAttribute('href');
    if (href === page || (page === '' && href === 'index.html')) {
      a.classList.add('active');
    }
  });

  // Close menu on link click (mobile)
  document.querySelectorAll('.nav-links a').forEach(function (a) {
    a.addEventListener('click', function () {
      var links = document.querySelector('.nav-links');
      if (links) links.classList.remove('open');
    });
  });
});
