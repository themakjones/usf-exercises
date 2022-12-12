const gameContainer = document.getElementById("game");

const COLORS = [
  "red",
  "blue",
  "green",
  "orange",
  "purple",
  "red",
  "blue",
  "green",
  "orange",
  "purple"
];

let guess1 = '';
let guess2 = '';

// here is a helper function to shuffle an array
// it returns the same array with values shuffled
// it is based on an algorithm called Fisher Yates if you want ot research more
function shuffle(array) {
  let counter = array.length;

  // While there are elements in the array
  while (counter > 0) {
    // Pick a random index
    let index = Math.floor(Math.random() * counter);

    // Decrease counter by 1
    counter--;

    // And swap the last element with it
    let temp = array[counter];
    array[counter] = array[index];
    array[index] = temp;
  }

  return array;
}

let shuffledColors = shuffle(COLORS);

// this function loops over the array of colors
// it creates a new div and gives it a class with the value of the color
// it also adds an event listener for a click for each card
function createDivsForColors(colorArray) {
  let id = 0;

  for (let color of colorArray) {
    // create a new div
    const newDiv = document.createElement("div");

    // give it a class attribute for the value we are looping over
    newDiv.classList.add(color);
    newDiv.id = id;
    id ++
    // call a function handleCardClick when a div is clicked on
    newDiv.addEventListener("click", handleCardClick);

    // append the div to the element with an id of game
    gameContainer.append(newDiv);
  }
}

// TODO: Implement this function!
function handleCardClick(event) {
  addGuess(event.target);
}

let addGuess = (target) => {
  if (! guess1 && guess1.id != target.id) {
    guess1 = target;

    guess1.style.backgroundColor = guess1.classList[0];

  } else if (! guess2 && guess1.id != target.id) {
    guess2 = target;

    guess2.style.backgroundColor = guess2.classList[0];

    checkGuess();
  }
}

let checkGuess = () => {
  if (guess1.style.backgroundColor == guess2.style.backgroundColor) {
    guess1 = '';
    guess2 = '';
  } else {
    setTimeout(() => {
      guess1.style.backgroundColor = '';
      guess2.style.backgroundColor = '';

      guess1 = '';
      guess2 = '';
    }, 1500)
  }
}

// when the DOM loads
createDivsForColors(shuffledColors);
