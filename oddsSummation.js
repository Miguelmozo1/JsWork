function sumOdds(){
    var sum = 0;
    for(var counter = 1; counter < 156; counter++){
        if(counter %2 ==1){
            sum += counter
        }
    }
    return sum;
}
console.log(sumOdds());