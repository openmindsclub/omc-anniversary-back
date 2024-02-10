function getCharacterWidth(character) {
    var span = document.createElement("span");
    span.textContent = character;
    document.body.appendChild(span);
    var width = span.offsetWidth;
    document.body.removeChild(span);
    return width;
}

var maxLength = document.querySelector(".input").clientWidth;


function Ternimal_Input() {
    //update the max length incase of a resize
    maxLength = document.querySelector(".input").clientWidth

    const currentInpt = document.activeElement.className;
    const inptIndx = currentInpt.split("input")[1];
    
    // Calculate the value dynamically based on screen width
    var screenWidth = window.innerWidth;
    var charLength = (13.75 / 1280) * screenWidth;

    var newLength = charLength * document.getElementsByClassName(currentInpt)[0].value.length;
    newLength = (newLength > maxLength) ? maxLength : newLength;
    document.querySelector(`.Blink${inptIndx}`).style.transform = `translateX(${newLength}px)`
}


function endCursor() //move to the end
{
    const currentInpt = document.activeElement.className;
    const len = document.getElementsByClassName(currentInpt)[0].value.length;

    var input = document.getElementsByClassName(currentInpt)[0];

    input.setSelectionRange(len, len);
    input.focus()
}


document.getElementsByClassName("form-body")[0].addEventListener('keydown', endCursor);
document.getElementsByClassName("form-body")[0].addEventListener('input', Ternimal_Input);

//set all cursors on reload
const indxs = ["", 1, 2, 3, 4];
for (let i = 0; i < 5; i++) {
    const inputElement = document.getElementsByClassName(`input${indxs[i]}`)[0];
    inputElement.value = ''; // Clear input value
    const blinkCursor = document.querySelector(`.Blink${indxs[i]}`);
    blinkCursor.style.transform = `translateX(0px)`; // Move cursor to the beggining
}