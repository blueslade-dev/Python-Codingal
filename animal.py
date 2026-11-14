from abc import ABC,abstractmethod

class Animal(ABC):
    @abstractmethod
    def move(self):
        print("I can move")
class Human(Animal):
    def move(self):
        print("I can walk")
class Dog(Animal):
    def move(self):
        print("I can run")
class Snake(Animal):
    def move(self):
        print("I can crawl")
class Fish(Animal):
    def move(self):
        print("I can swim")


human = Human()
dog = Dog()
snake = Snake()
fish = Fish()

human.move()
dog.move()
snake.move()
fish.move()        