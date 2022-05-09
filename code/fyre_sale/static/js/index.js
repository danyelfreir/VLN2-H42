// ============ SEARCH BAR =============
const searchButton = document.getElementById('search-button');
const searchForm = document.getElementById('search-dropdown');
const searchFormInput = document.getElementById('search-form-input');
const searchDropdown = document.getElementById('cat-btn');
const background = document.getElementById('wrapper');
const searchResults = document.getElementById('search-results-list');
const loginButton = document.getElementById('login');
const profileMenu = document.getElementById('profile-menu');

searchButton.addEventListener('click', () => {
  searchForm.style.display = "flex";
});

background.addEventListener('click', () => {
  searchForm.style.display = 'none';
  profileMenu.style.display = 'none';
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
loginButton.addEventListener('click', () => {
  profileMenu.style.display = 'block';
})
