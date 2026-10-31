class Vehicle:
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage

modelX = Vehicle(300,50)
print("Max speed of Model X:",modelX.max_speed)
print("Mileage of Model X:",modelX.mileage)        