from abc import ABC,abstractmethod

class AbstractClass(ABC):
    def Print(self,content):
        print("Printed thing:",content)
    @abstractmethod
    def task(self):
        print("This function is part of class AbstractClass")

class TaskClass(AbstractClass):
    def task(self):
        print("Hello World!")
        super().task()

t = TaskClass()
t.Print("Hello!")
t.task()
a = AbstractClass()
a.task()