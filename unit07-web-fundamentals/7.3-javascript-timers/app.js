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

countdown(4);