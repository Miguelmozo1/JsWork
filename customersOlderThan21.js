function olderThan21(list){
    var count = 0;
    for(var i = 0; i < list.length; i++){
        if(list[i]>=21){
            count += 1;
        }
    }
    return count;
}
console.log(olderThan21([15,32,22,52,17,12,8,54,33,21]));