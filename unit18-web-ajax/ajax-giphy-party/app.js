const form = document.querySelector(`#gifSearch`);
const removeBtn = document.getElementById(`removeBtn`);
const container = document.querySelector(`#gifContainer`);

async function getGif(q) {
// const api_key = `dHbXK0YzzXrAY59pkUeMq4bD9HMa7dOH`;
// let q = getInput(`#term`);

const res = await axios.get(`https://api.giphy.com/v1/gifs/search?api_key=dHbXK0YzzXrAY59pkUeMq4bD9HMa7dOH&q=${q}&limit=25&offset=0&rating=g&lang=en`);

addGif(res);
}

const getInput = id => {
    return document.querySelector(id).value;
};

const addGif = res => {
    const newImg = document.createElement(`img`);
    const randomIdx = Math.floor(Math.random() * 25)
    newImg.src = res.data.data[randomIdx].images.original.url;
    container.append(newImg);
}

console.log("Let's get this party started!");

form.addEventListener(`submit`, function(e) {
        e.preventDefault();
        let q = getInput(`#term`);
        getGif(q);
        // add clear input
        document.getElementById(`term`).value = ``;
        // q would not work
    });

removeBtn.addEventListener(`click`, function() {
    while(container.hasChildNodes()) {
        container.removeChild(container.firstChild)
    };
});