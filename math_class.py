class MathClass:
    def __init__(self):
        self.result = 0
    def add(self, num, *nums):
        sum = num
        for n in nums:
            sum += n
        self.result = sum
        return self
    def subtract(self, num, *nums):
        sum = num
        for n in nums:
            sum -= n
        self.result = sum
        return self
mc = MathClass()
x = mc.add(4,5,6).subtract(2,5,1).result
print(x)