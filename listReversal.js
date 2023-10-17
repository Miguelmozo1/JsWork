function reversal(list) {
    var left = 0;
    var right = list.length - 1;
    while(left < right) {
        var temp = list[left];
        list[left] = list[right];
        list[right] = temp;
        left++;
        right--;
    }
    return list;
}

console.log(reversal([1,2,3,4,5]));