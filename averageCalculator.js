function average(set){
    var sum = 0;
    for(var i = 0; i < set.length; i++){
        sum += set[i];
    }
    return sum / set.length;
}
console.log(average([12,44,-55,10,65,-44]));