def lastDigit(num1, num2):
    square = num1 ** num2
    onesPlace = square % 10
    return onesPlace
y = lastDigit(7,5)
print(y)