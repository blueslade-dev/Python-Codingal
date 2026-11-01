class IOString:
    def __init__(self):
        self.str1 = ""
    def get_string(self):
        self.str1 = input("Enter String: ")
    def print_string(self):
        self.str1 = print("Printed String: ",self.str1.upper())

o = IOString()
o.get_string()
o.print_string()