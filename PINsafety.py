class Account:
    def __init__(self,owner,pin):

        self.owner = owner
        if str(pin).isnumeric() and len(str(pin)) in [4,6]:
            self.__pin = pin
        else:
            print("Invalid Pin")
            exit()

    def AccountStatus(self):
        print("==Account status==")
        print(f"Owner: {self.owner}")
        print("PIN Code: Can't be shown. Stored safely inside the account.")
        print("==================")
    
    def check_PIN(self,entered_pin):
        if self.__pin == entered_pin:
            print("Correct Pin!")
        else:
            print("Incorrect Pin!")

    def change_PIN(self,old_pin,new_pin):
        if self.__pin == old_pin:
            if len(str(new_pin)) in [4,6] and str(new_pin).isnumeric():
                print("New PIN: ",new_pin)
            else:
                print("Invalid PIN.")                 
        else:
            print("Incorrect PIN")

Acc1 = Account("Krithik",458812)
Acc1.AccountStatus()
Acc1.change_PIN(458812,8834)
Acc1.AccountStatus()
Acc1.check_PIN(8182112)