// ============ SEARCH BAR =============
const searchButton = document.getElementById('search-button');
const searchForm = document.getElementById('search-dropdown');
const searchFormInput = document.getElementById('search-form-input');
const searchDropdown = document.getElementById('cat-btn');
const background = document.getElementById('site-content');
const searchResults = document.getElementById('search-results-list');
const loginButton = document.getElementById('login');
const profileMenu = document.getElementById('profile-menu');
const filterButton = document.getElementById('filtering-button');
const filterMenu = documet.getElementById('filter-menu')
const currentWindow = window.location.pathname;
const nrOfStars = 5;

searchButton.addEventListener('click', () => {
  searchForm.style.display = "flex";
});

if (currentWindow === "/items/") {
  searchButton.click();
};

background.addEventListener('click', (e) => {
  if ( window.location.pathname !== "/items/" ) {
    searchForm.style.display = 'none';
  };
  profileMenu.style.display = 'none';
  if ( e.target !== filterButton) {
    filterMenu.style.display = 'none';
  };
});

searchFormInput.addEventListener('keydown', async () => {
  const res = await fetch(`http://localhost:8000/items/api/search?name=${searchFormInput.value}`);
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
  profileMenu.style.display = 'block';
})


// ============ FILTER MENU ============
filterButton.addEventListener('click', (e) => {
  console.log(e.target);
  filterMenu.style.display = 'block';
});


