let toDoList = [];
let completedList = [];

const form = document.querySelector(`form`);
let ul = document.querySelector(`#toDoList`);
// Add To Do item (does not save on reload)
form.addEventListener(`submit`, function (e) {
  e.preventDefault();

  let newToDo = document.querySelector(`#addToDo`).value;
  createTodo(newToDo);
  toDoList.push(newToDo);

  updateLocalStorage();

  form.reset();
});

// Strikethrough completed item

ul.addEventListener(`click`, function (e) {
  const targetTag = e.target.tagName.toLowerCase();

  if (e.target.classList.contains("todo-item")) {
    checkCompletion(e.target);
  } else if (targetTag === `button`) {
    const todo = e.target.previousElementSibling.innerText;

    removeItem(toDoList, todo);
    removeItem(completedList, todo);
    e.target.parentNode.remove();
  }

  updateLocalStorage();
});

const checkCompletion = (target) => {
  if (target.classList.contains("completed")) {
    removeItem(completedList, target.innerText);
    toDoList.push(target.innerText);

    target.classList.remove("completed");
  } else {
    removeItem(toDoList, target.innerText);
    completedList.push(target.innerText);

    target.classList.add("completed");
  }
  updateLocalStorage();
};

const removeItem = (arr, val) => {
  const idx = arr.indexOf(val);

  if (idx > -1) {
    arr.splice(idx, 1);

    return arr;
  }
};
// add items to local storage

const updateLocalStorage = () => {
  localStorage.setItem("todoList", JSON.stringify(toDoList));
  localStorage.setItem("completedList", JSON.stringify(completedList));
};

const checkLocalStorage = () => {
  let todoStorage = JSON.parse(localStorage.getItem("todoList"));
  let completedStorage = JSON.parse(localStorage.getItem("completedList"));

  if (todoStorage && completedStorage) {
    toDoList = JSON.parse(localStorage.getItem("todoList"));
    completedList = JSON.parse(localStorage.getItem("completedList"));
  } else if (todoStorage) {
    toDoList = JSON.parse(localStorage.getItem("todoList"));
  } else if (completedStorage) {
    completedList = JSON.parse(localStorage.getItem("completedList"));
  }
};

const addStorageTodos = () => {
  toDoList.forEach((val) => {
    createTodo(val);
  });
  completedList.forEach((val) => {
    createTodo(val);
    ul.lastElementChild.classList.add("completed");
  });
};

const createTodo = (val) => {
  // let newToDo = document.querySelector(`#addToDo`).value;
  let newLi = document.createElement(`li`);
  let removeButton = document.createElement(`button`);
  let newDiv = document.createElement("div");

  newDiv.innerText = val;
  newDiv.classList.add("todo-item");
  newLi.append(newDiv);

  removeButton.innerText = `Remove`;
  newLi.append(removeButton);

  ul.append(newLi);
};

checkLocalStorage();
addStorageTodos();
