document.addEventListener('DOMContentLoaded', () => {
  const addItem = document.getElementById('add_item');
  const myList = document.querySelector('.my_list');

  addItem.addEventListener('click', () => {
    const newItem = document.createElement('li');
    newItem.textContent = 'Item';
    myList.appendChild(newItem);
  });
});

