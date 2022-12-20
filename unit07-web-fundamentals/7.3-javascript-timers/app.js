const countdown = num => {
    let time = num * 1000;

    setInterval(() => {
        console.log(num);
        num -= 1;
    }, 1000)

    setTimeout(() => {
        console.log('Done!');
        clearInterval(1);
    }, time);
}


const randomGame = () => {
    let counter = 0;
    let randomNum;

    let interval = setInterval(() => {
        randomNum = Math.random();
        counter ++;
        console.log(randomNum)

        if (randomNum > .75) {
            console.log(`It took ${counter} tries`);
            clearInterval(interval);
        }

    }, 1000)
}