function higherThanAvrg(set) {
    var sum = 0;
    var count = 0;
    for(let i = 0; i < set.length; i++) {
        sum += set[i];
    }
    var avrg = sum / set.length;                // orders matters when defining later in loop process
    for(let u = 0; u < set.length; u++) {       // had placed this loop above avrg decleration
        if(set[u] > avrg) {
            count++;
        }
    }
    return count;
}

var numOf = higherThanAvrg([10,-3,3,1,4]);
console.log(numOf);
