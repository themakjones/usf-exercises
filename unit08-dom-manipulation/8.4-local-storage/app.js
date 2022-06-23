let toDoList = [];
let completedList = [];

const form = document.querySelector(`form`);
    let ul = document.querySelector(`#toDoList`);
    // Add To Do item (does not save on reload)
form.addEventListener(`submit`, function(e) {
    e.preventDefault();
    let newToDo = document.querySelector(`#addToDo`);
    let newLi = document.createElement(`li`);
    let removeButton = document.createElement(`button`);

    newLi.innerText = newToDo.value;
    newLi.append(removeButton);
    ul.append(newLi);
    removeButton.innerText = `Remove`;
    toDoList.push(newToDo.value);

    form.reset();
})

// Strikethrough completed item 

ul.addEventListener(`click`, function(e) {
    const targetTag = e.target.tagName.toLowerCase();
    
    if (targetTag === `li`) {
        e.target.className = `completed`;
        completedList.push(newToDo.value);
        // above line gives error bc newToDo is not defined
    } else if (targetTag === `button`) {
        e.target.parentNode.remove();
    }
})
// add items to local storage
