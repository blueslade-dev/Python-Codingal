class DailyMessage:
    def __init__(self):
        self.msg = "Hello! Good day User!"
        print(self.msg)
    def get_message(self,user_input):
        self.user_input = user_input
    def print_message(self):
        print(str(self.user_input).upper())

daily_text = DailyMessage()
daily_text.get_message("hello hello.")
daily_text.print_message()

class HelperSession:
    def __init__(self):        
        print("Hi!")
    def __del__(self):
        print("Destroyed")
def create_session():
    print("Starting Session")
    ob = HelperSession()
    print("End of Session")
    del ob

create_session()

class PairFinder:
    def find_pair(self,target,nums):
        a = set()        
        for num in nums:
            x = target - num
            if target - num in nums:
                if x not in a and target-x not in a and x != target-x:
                  print(x,"+",target-x,"=",target)
                  a.add(x)
                  a.add(target-x)

numbers = (10,20,30,50)
target = 60
Finder = PairFinder()
Finder.find_pair(target,numbers)