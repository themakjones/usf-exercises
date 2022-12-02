async function getNumberInfo(num) {
    let baseUrl = 'http://numbersapi.com';
    let factArr = [];

    let f1Promise = axios.get(`${baseUrl}/${num}?json`);
    let f2Promise = axios.get(`${baseUrl}/${num}?json`);
    let f3Promise = axios.get(`${baseUrl}/${num}?json`);
    let f4Promise = axios.get(`${baseUrl}/${num}?json`);

    factArr.push((await f1Promise).data.text);
    factArr.push((await f2Promise).data.text);
    factArr.push((await f3Promise).data.text);
    factArr.push((await f4Promise).data.text);

    return factArr;
}

async function addFacts() {
    const factList = document.getElementById("number-facts")
    let factArr = await getNumberInfo(3);

    factArr.forEach(fact => {
        const li = document.createElement('li');
        
        factList.appendChild(li);
        li.innerHTML = fact;
    });
}

addFacts()