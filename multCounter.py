low_Num = 3
high_Num = 48
mult = 2
count = 0
for i in range(low_Num, high_Num):
    if i % mult == 0:
        count += 1
        print(i)
    else:
        i += mult
print("Number of times your multiple shows in given range is: " , count)