// Get the modal
var modal = document.getElementById("login_Modal");
var sidenav = document.getElementById("mySidenav")
//Buttons
var btn = document.getElementById("login");
var btncl = document.getElementById("cancel");
var btnsubm = document.getElementById("submit");
var btnsignup = document.getElementById("signup");

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
window.onclick = function(event) {
  if (event.target == modal) {
    modal.style.display = "none";
  }
}
<<<<<<< HEAD
=======

function openNav() {
  document.getElementById("mySidenav").style.width = "250px";
  document.getElementById("main").style.marginLeft = "250px";
}

function closeNav() {
  document.getElementById("mySidenav").style.width = "0";
  document.getElementById("main").style.marginLeft= "0";
}

window.onclick = function(event) {
  if (event.target == sidenav) {
    sidenav.style.display = "none";
  }
}
>>>>>>> 7513d9573a4fbedb4f7931be62bda3babc2d0221
