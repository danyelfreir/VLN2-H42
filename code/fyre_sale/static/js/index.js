// Get the modal
const modal = document.getElementById("modal");
const search = document.getElementById("search-dropdown");
//Buttons
const btn = document.getElementById("login");
// const btncl = document.getElementById("cancel");
const btnsubm = document.getElementById("submit");
const btnsignup = document.getElementById("form-signup");

const btnsearch = document.getElementById("search-button");
const searchForm = document.getElementById("search-form");

const header = document.querySelector('body');
// Variables
let searchOpen = false;


//display the login window
btn.onclick = function() {
  modal.style.display = "block";
}
//submit the login
btnsubm.onclick = function() {
  // temporary for testing remove and set a function call for
  // validating the login
  modal.style.display = "none";
}
//submit the login
btnsignup.onclick = function() {
  // temporary for testing remove and set a function call for
  // validating the login
  modal.style.display = "none";
}


//close the login window
// btncl.onclick = function() {
//   modal.style.display = "none";
// }

//Click outside of window to close
window.onclick = function(event) {
  if (event.target == modal) {
    modal.style.display = "none";
  }
  else if (searchOpen
        && event.target != btnsearch
        && event.target != searchForm
        && event.target != document.getElementById("search-form-input")
        && event.target != document.getElementById("search-form-button")
        && searchForm[0].value === '') {
    search.style.display = 'none';
    searchOpen = false;
  }
}

btnsearch.addEventListener('click', () => {
  if (!searchOpen) {
    search.style.display = 'flex';
    searchOpen = true;
  }
})

function closeNav() {
  document.getElementById("mySidenav").style.width = "0";}