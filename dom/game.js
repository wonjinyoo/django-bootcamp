var refresh = document.querySelector("#refresh");
var square = document.querySelectorAll(".square");

// Refresh
function clearBoard() {
  for (var i = 0; i < square.length; i++) {
    square[i].textContent = "";
  }
}

refresh.addEventListener("click", clearBoard);

// Board setting
function changeMarker() {
  if (this.textContent === "X") {
    this.textContent = "O";
  } else if (this.textContent === "O") {
    this.textContent = "";
  } else if (this.textContent === "") {
    this.textContent = "X";
  }
}

for (var i = 0; i < square.length; i++) {
  square[i].addEventListener("click", changeMarker);
}
