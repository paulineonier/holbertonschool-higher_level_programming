document.addEventListener('DOMContentLoaded', () => {
  const characterDiv = document.getElementById('character');
  
  fetch('https://swapi-api.hbtn.io/api/people/5/?format=json')
    .then(response => response.json())
    .then(data => {
      characterDiv.textContent = data.name;
    })
    .catch(error => {
      console.error('Error fetching data:', error);
    });
});

