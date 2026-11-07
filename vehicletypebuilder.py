class ParentModel:
    def __init__(self,sitting_capacity,engine_model):
        self.sitting_capacity = sitting_capacity
        self.engine_model = engine_model

    def showDetails(self):
        print("Sitting Capacity: ",self.sitting_capacity)
        print("Engine Model: ",self.engine_model)

class ChildModel(ParentModel):
    def __init__(self,sitting_capacity,engine_model,color,isSelfDriving):
        self.color = color
        self.isSelfDriving = isSelfDriving
        super().__init__(sitting_capacity,engine_model)
    def showDetails(self):
        print("Car Colour:",self.color)
        print("Car is Self Driving?:",self.isSelfDriving)
        super().showDetails()

modelX = ChildModel(5,"X1","Red",True)
modelY = ChildModel(5,"X1","Blue",False)
modelX.showDetails()
modelY.showDetails()