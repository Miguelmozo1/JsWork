function findLargestNumber(list){
    var largest = "";
    for(var i = 0; i < list.length; i++){
        if(list[i] > list[0]){
            largest = list[i];
        }
    }
    return largest;
}
console.log(findLargestNumber([33,14,-4,43,-67,12]));