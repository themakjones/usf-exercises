// Quick question 1
[1, 2, 3, 4]

// Quick question 2
[`r`,`e`,`f`]

// Quick question 3
[[1,2,3], false]

// hasDuplicate
const hasDuplicate = arr => {
    let arrSet = Set(arr);
     return arrSet.size !== arr.length ? true : false;
}

// vowelCount
const vowelCount = str => {
    let strSet = new Set(str);
    let countMap = new Map();
    for (letter of str) {
        if (strSet.has(letter)) {
            if (countMap.get(letter) === 1) {
                countMap.set(letter, += 1)
            } else {
                countMap.set(letter, 1)};
        };
    return countMap
    };
}