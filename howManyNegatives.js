function howManyNegatives(arr){
var count = 0;
for(var i = 0; i<arr.length; i++){
    if(arr[i]<0){ 
        count += 1;
    }
}
    return count;
}
console.log(howManyNegatives([1,34,-55,23,1,-67,-11,2]));