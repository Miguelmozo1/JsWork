def countdown(num):
    list = []
    for i in range(num, -1, -1):
        list.append(i)
    return f"Countdown list: {list}"            # if you don't add return and use print, you'll get "none" after what you needed to be printed

x = countdown(10)
print(x)