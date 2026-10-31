class Pet:
    def __init__(self,animal,name,age):
        self.animal = animal
        self.name = name
        self.age = age
  
def petprofilemaker(name,age,animal): 
          
    pet_identity = Pet(name,age,animal)
    print("\n==Pet Profile Maker==")
    print(f"Name: {pet_identity.name}\nAge: {pet_identity.age}\nAnimal: {pet_identity.animal}")
    print("=====================\n")

while True:
  animal = input("Which animal is your pet?: ")
  name = input("Enter your pet's name:")
  age = int(input("Enter your pet's age:"))
  petprofilemaker(name,age,animal)
  repeat = input("Do you wanna make another pet profile?(Yes/No)").capitalize()
  if repeat == "Yes":
      continue
  else:
      print("Hope you liked the Pet Profile maker service!")
      break   