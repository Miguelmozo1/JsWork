var prizeList = ["3 Points:Glow Stick","6 Points:Beer Hat","9 Points: A fish, all or nothing","10 Points: Jumbo Animal of your choosing"];
console.log(prizeList);
console.log("Your GO!");
for(var score = 0; score <= 10; score++){
    console.log(score);
    if(score == 10){
        console.log("WINNER WINNER");
    }
    if(score == 3){
        console.log("Way to go");
    }
    else if(score == 6){
        console.log("My favorite prize of 'em all");
    }
    else if(score == 9){
        console.log("You know you want to take this fish home, you don't want this last point");
    }
}
