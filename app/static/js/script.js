window.onload = function(){
  n =  new Date();
  y = n.getFullYear();
  m = n.getMonth();
  d = n.getDate();

  var weekday = new Array(7);
  weekday[0] = "Sunday";
  weekday[1] = "Monday";
  weekday[2] = "Tuesday";
  weekday[3] = "Wednesday";
  weekday[4] = "Thursday";
  weekday[5] = "Friday";
  weekday[6] = "Saturday";

  var months = new Array(12);
  months[0] = "January";
  months[1] = "February";
  months[2] = "March";
  months[3] = "April";
  months[4] = "May";
  months[5] = "June";
  months[6] = "July";
  months[7] = "August";
  months[8] = "September";
  months[9] = "October";
  months[10] = "November";
  months[11] = "December";

  var day = weekday[n.getDay()];
  var month = months[m];

  document.getElementById("date").innerHTML = day + " - " + month + " " + d;

};
function showErrorDiv() {
  document.getElementById("error-div").style.display = "block";
}
function closeErrorDiv() {
  document.getElementById("error-div").style.display = "none";
}