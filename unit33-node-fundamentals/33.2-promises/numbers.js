let url = "http://numbersapi.com/2?json";

let firstPromise = axios.get(url);

let promiseArr = [];
const factList = document.getElementById("number-facts")

firstPromise.then(res1 => {
    promiseArr.push(res1.data.text);
    return axios.get(url);
})
.then(res2 => {
    promiseArr.push(res2.data.text);
    return axios.get(url);
})
.then(res3 => {
    promiseArr.push(res3.data.text);
    return axios.get(url);
})
.then(res4 => {
    promiseArr.push(res4.data.text);
    for (const fact of promiseArr) {
        const li = document.createElement('li');

        factList.appendChild(li);
        li.innerHTML = fact;
    };
    return axios.get(url);
})
.catch(err => {
    console.log(err);
});


