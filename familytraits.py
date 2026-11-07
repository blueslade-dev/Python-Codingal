class FamilyMember:
    def __init__(self,height_cm,eye_colour):
        self.height_cm = height_cm
        self.eye_colour = eye_colour

    def showTraits(self):
        print("Height(in cm): ",self.height_cm)
        print("Eye Colour: ",self.eye_colour)

class Kid(FamilyMember):
    def __init__(self,name,age,height_cm,eye_colour,hobby):
        self.name = name
        self.age = age
        self.hobby = hobby
        super().__init__(height_cm,eye_colour)

    def showTraits(self):
        print("Name: ",self.name)
        print("Age: ",self.age)        
        super().showTraits()
        print("Hobby: ",self.hobby) 

    def grade(self,grade):
        print(f"{self.name} studies in grade {grade}.")   

child = Kid("Chintu",8,105,"Black","Watching TV")
child.showTraits()
child.grade(2)

print("Is Kid a subclass of Family Member?",issubclass(Kid,FamilyMember))