document.addEventListener('DOMContentLoaded', () => {
  const toggleHeader = document.getElementById('toggle_header');
  const header = document.querySelector('header');

  toggleHeader.addEventListener('click', () => {
    if (header.classList.contains('red')) {
      header.classList.replace('red', 'green');
    } else {
      header.classList.replace('green', 'red');
    }
  });
});

