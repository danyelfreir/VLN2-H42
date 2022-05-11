// ============ SEARCH BAR =============
const searchButton = document.getElementById('search-button');
const searchForm = document.getElementById('search-dropdown');
const searchFormInput = document.getElementById('search-form-input');
const searchDropdown = document.getElementById('cat-btn');
const background = document.getElementById('site-content');
const searchResults = document.getElementById('search-results-list');
const loginButton = document.getElementById('login');
const profileMenu = document.getElementById('profile-menu');
const filterButton = document.getElementById('filter-button');
const filterMenu = document.getElementById('filter-menu');

searchButton.addEventListener('click', () => {
  searchForm.style.display = "flex";
});

background.addEventListener('click', () => {
  searchForm.style.display = 'none';
  profileMenu.style.display = 'none';
  filterMenu.style.display = 'none';
});

searchFormInput.addEventListener('keydown', async () => {
  const res = await fetch(`http://localhost:8000/items/search?name=${searchFormInput.value}`);
  const data = await res.json();
  searchResults.innerHTML = '';
  data['results'].forEach(item => {
    let newLink = document.createElement('a');
    newLink.href = `http://localhost:8000/items/${item.id}`;
    newLink.id = 'search-result';
    newLink.innerHTML = `${item.name}`
    searchResults.appendChild(newLink);
  });
});
// =====================================

// ============ PROFILE MENU ===========
loginButton.addEventListener('click', (e) => {
  console.log("Is buttoning");
  profileMenu.style.display = 'block';
})


// ============ FILTER MENU ============
filterButton.addEventListener('click', (e) => {
  console.log(e.target);
  filterMenu.style.display = 'block';
})