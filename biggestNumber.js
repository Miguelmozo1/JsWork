function largestNumber(array){
    var largest = [0];
    for(var i = 0; i < array.length; i++){
        if(array[i] > array[0]){
            largest = array[i];
        }
    }
    return largest;
}
console.log(largestNumber([3,5,-99,78,56,9999]));