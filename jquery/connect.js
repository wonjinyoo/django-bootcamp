// Player name setting
var playerOne = prompt("Player one: Enter your name. You will be 'BLUE'.");
var playerTwo = prompt("Player two: Enter your name. You will be 'RED'.");

// first player setting (player object)
var currentPlayer = {
  name: playerOne,
  color: "blue",
};

$("#intro").text(currentPlayer.name + ", it's now your turn!");

// Cell hover: color effect
// $("button").hover(
//   function () {
//     $(this).css("background-color", "#bdbdbd");
//   },
//   function () {
//     $(this).css("background-color", "#f0f0f0");
//   }
// );

// Cell click event
// change color of cell & to the next player
$("button").on("click", function () {
  var currentColor = $(this).css("backgroud-color");
  if (currentColor !== currentPlayer.color) {
    $(this).css("background-color", currentPlayer.color);
  }
  changePlayer();
});

// Change to next player
// Change intro header
function changePlayer() {
  if (currentPlayer.name === playerOne) {
    currentPlayer.name = playerTwo;
    currentPlayer.color = "red";
  } else {
    currentPlayer.name = playerOne;
    currentPlayer.color = "blue";
  }
  // change the text
  $("#intro").text(currentPlayer.name + ", it's now your turn!");
}
