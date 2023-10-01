function howMuchLeftOverCake(numberOfPieces, numberOfPeople) { // function to store equation for our problem so that we can recall/manipulate it later
    var slices = numberOfPieces % numberOfPeople;               // equation that is stored in function
    return numberOfPieces % numberOfPeople;                     // what the function will specifically display once it is recalled
}

var result = howMuchLeftOverCake(71,11);        // variable holding function and given parameters to have plugged in

console.log(result);                     // prints out outcome from parameters plugged into function

if (result == 0){
    console.log("No leftovers for you!");
}
else if (result <= 2){
    console.log("You have some leftovers");
}
else if (result <= 5){
    console.log("You have leftovers to share");
}
else if (result > 5){
    console.log("Hold another party!");
}
