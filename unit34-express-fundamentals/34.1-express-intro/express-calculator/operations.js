function findMean(nums) {
  let numsTotal = 0;

  nums.forEach((num) => {
    numsTotal += num;
  });

  return numsTotal / nums.length;
}

function findMode(nums) {
  let uniqueNums = Array.from(new Set(nums));

  let currMode = [];
  let highestOccurance = 0;

  uniqueNums.forEach((uniqueNum) => {
    let occurance = 0;

    nums.forEach((num) => {
      if (uniqueNum == num) occurance++;
    });

    if (occurance == highestOccurance) {
      currMode.push(uniqueNum);
      occurance = 0;
    } else if (occurance > highestOccurance) {
      currMode = [uniqueNum];
      highestOccurance = occurance;
      occurance = 0;
    } else {
      occurance = 0;
    }
  });
  return currMode;
}

function findMedian(nums) {
  let sortedNums = nums.sort((a, b) => {
    return a - b;
  });

  if (sortedNums.length % 2 == 0) {
    let middle1 = sortedNums[sortedNums.length / 2 - 1];
    let middle2 = sortedNums[sortedNums.length / 2];
    let sum = middle1 + middle2;
    return sum / 2;
  } else {
    return sortedNums[Math.floor(sortedNums.length / 2)];
  }
}

console.log(findMode([1, 2, 1, 3, 4, 2, 3, 3]));
