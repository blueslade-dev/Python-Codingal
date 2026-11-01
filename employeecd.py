class Employee:
    def __init__(self):
        self.msg = "Employee Assigned"
        print(self.msg)
        
    def __del__(self):
        self.msg = "Employee Fired"
        print(self.msg)

def create_Obj():
    print("Program starting......")
    obj = Employee()    
    print("Program ending.....")
    
    return obj

print("Calling function create_Obj()....")   
obj = create_Obj()

print("==END OF PROGRAM==")
del obj