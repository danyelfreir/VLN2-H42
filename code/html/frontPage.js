// Get the modal
const modal = document.getElementById("login_Modal");
// Get the sidenav
const sidenav = document.getElementById("mySidenav");
//
//Buttons
const btn = document.getElementById("login");
const btncl = document.getElementById("cancel");
const btnsubm = document.getElementById("submit");
const btnsignup = document.getElementById("signup");

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
btncl.onclick = function() {
  modal.style.display = "none";
}

//Click outside of window to close
//Does not work at the moment
window.onclick = function(event) {
  if (event.target == modal) {
    modal.style.display = "none";
  }
}

//Open sidenav
function openNav() {
  document.getElementById("mySidenav").style.width = "250px";
  document.getElementById("main").style.marginLeft = "250px";
}
//Close the sidenav
function closeNav() {
  document.getElementById("mySidenav").style.width = "0";
  document.getElementById("main").style.marginLeft= "0";
}
// This should close the sidenav if clicked outside of it
//Does not work at the moment
window.onclick = function(event) {
  if (event.target == sidenav) {
    sidenav.style.display = "none";
  }
}

