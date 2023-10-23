function statsRange(set){
    var lowest = set[0];
    var highest = set[0];
    for(let i = 1; i < set.length; i++) {
        if(set[i] > highest) {
            highest = set[i];
        }
        else if(set[i] < lowest) {
            lowest = set[i];
        }
    }
    return highest - lowest;
}
console.log(statsRange([68, 77,83,94,73,80,79,84,90]));