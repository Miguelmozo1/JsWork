local_val = "magical unicorns"
def square(n):
    return n * n
class User:
    def __init__(self, name):
        self.name = name
    def say_hello(self):
        return "hello"
    if __name__ == "__main__":
        print("the file is being executed directly")
        print(square(6))
    else:
        print("file is being executed because it is imported by another file. The file is called;", __name__)

# print(square(6)) this will not be ran in the child file if it is called upon to run since it must be ran from the __main__ file that it was constructed on
#   or the file known as "parent"
user1 = User("Bertha")
print(user1.name)
print(user1.say_hello())
print(__name__)