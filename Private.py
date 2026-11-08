class myClass:
    __privateVar = 38
    def __privMeth():
        print("Hi")
    def greet(self):
        print("Hello!")
xyz = myClass()
xyz.greet()
xyz.__privateVar
xyz.__privMeth()