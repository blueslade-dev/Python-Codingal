class Parrot:
    species = "bird"
    def __init__(self,name,age,color):
        self.name = name
        self.age = age
        self.color = color

Mitu = Parrot("Mitu",8,"Red")
Tweetie = Parrot("Tweetie",11,"Green")

print(f"Mitu's name:{Mitu.name}\nMitu's age:{Mitu.age}\nMitu's color:{Mitu.color}\n\n")
print(f"Tweetie's name:{Tweetie.name}\nTweetie's age:{Tweetie.age}\nTweetie's color:{Tweetie.color}")