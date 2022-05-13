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
const filterMenu = document.getElementById('filter-menu');
const currentWindow = window.location.pathname;
const imagePopUp = document.getElementById("image-popup");
const nrOfStars = 5;
let currRating = document.getElementById("curr-rating-to-show")

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
  console.log(e.target);
  profileMenu.style.display = 'block';
})


// ============ FILTER MENU ============
filterButton.addEventListener('click', (e) => {
  filterMenu.style.display = 'block';
  console.log(filterMenu);
})
// ============ SCALE IMAGE ============
// function scaleImage(clickedImageId) {
//   var imageId = clickedImageId.replace('image_',''); //Nota þetta til að fá image id sem er í gagnagrunninum.
//   document.getElementById("image-scaled").src="??"; //setja inní réttan link hér.
//   imagePopUp.style.display = 'block';
// }

function sellerRating(curr_rating) {
  let profile_rating = parseInt(curr_rating);
  console.log(profile_rating)
  profile_rating = profile_rating / 2;
  console.log(profile_rating)
  // total number of stars
  const nrOfStars = 5;
  let ratingPercentage = (profile_rating / nrOfStars) * 100;
  let ratingPercentageRound = `${(Math.round(ratingPercentage / 10) * 10)}%`;
  document.querySelector(`.hotel_a .stars-inner`).style.width = ratingPercentageRound;
}
sellerRating(currRating.innerHTML);
