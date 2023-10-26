function fiboList(n) {
    var fibArr = [0,1];
    var sum = 1;                    // keeps sum of previous two values in list and starts summation process
    for(let i = 0; i < n; i++) {
        sum += fibArr[i];
        fibArr.push(sum);
    }
    return fibArr;
}

var result = fiboList(10);
console.log(result);