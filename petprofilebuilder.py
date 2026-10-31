class Pet:
    def __init__(self,animal,name,age):
        self.animal = animal
        self.name = name
        self.age = age
  
def petprofilemaker(animal,name,age): 
          
    pet_identity = Pet(animal,name,age)
    print("\n==Pet Profile Maker==")
    print(f"Name: {pet_identity.name}\nAge: {pet_identity.age}\nAnimal: {pet_identity.animal}")
    print("=====================\n")

while True:
  animal = input("Which animal is your pet?: ")
  name = input("Enter your pet's name:")
  age = int(input("Enter your pet's age:"))
  petprofilemaker(animal,name,age)
  repeat = input("Do you wanna make another pet profile?(Yes/No)").capitalize()
  if repeat == "Yes":
      continue
  else:
      print("Hope you liked the Pet Profile maker service!")
      break   
