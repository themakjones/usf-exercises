let toDoList = [];
let completedList = [];

const form = document.querySelector(`form`);
    let ul = document.querySelector(`#toDoList`);
    // Add To Do item (does not save on reload)
form.addEventListener(`submit`, function(e) {
    e.preventDefault();
    let newToDo = document.querySelector(`#addToDo`).value;
    let newLi = document.createElement(`li`);
    let removeButton = document.createElement(`button`);
    let newDiv = document.createElement('div');

    newDiv.innerText = newToDo;
    newDiv.classList.add('todo-item')

    newLi.append(newDiv);
    newLi.append(removeButton);
    ul.append(newLi);
    removeButton.innerText = `Remove`;
    toDoList.push(newToDo);

    console.log(`todo list: ${toDoList}`)
    console.log(`completed list: ${completedList}`)

    form.reset();
})

// Strikethrough completed item 

ul.addEventListener(`click`, function(e) {
    const targetTag = e.target.tagName.toLowerCase();

    if (e.target.classList.contains('todo-item')) {

        checkCompletion(e.target);

    } else if (targetTag === `button`) {

        const todo = e.target.previousElementSibling.innerText;
        
        removeItem(toDoList, todo);
        removeItem(completedList, todo);
        e.target.parentNode.remove();
    }

    console.log(`todo list: ${toDoList}`)
    console.log(`completed list: ${completedList}`)
})

const checkCompletion = (target) => {

    if (target.classList.contains('completed')) {
    
        removeItem(completedList, target.innerText);
        toDoList.push(target.innerText);
        
        target.classList.remove('completed');

    } else {
    
        removeItem(toDoList, target.innerText);
        completedList.push(target.innerText);
        
        target.classList.add('completed');
    }
}

const removeItem = (arr, val) => {
    const idx = arr.indexOf(val);

    if (idx > -1) {
        arr.splice(idx, 1);

        return arr;
    }
}
// add items to local storage
