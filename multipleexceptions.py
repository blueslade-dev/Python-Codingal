try:
    num1, num2 = eval(input("Enter two numbers seperated by a comma(,): "))
    div = num1/num2
    print(div)
except TypeError as x:
    print("Exception: ",x)
except ZeroDivisionError as y:
    print("Exception: ",y)
except SyntaxError as z:
    print("Exception(you most probably skipped the commas): ", z)
except:
    print("You have done something wrong in the input try again")
else:
    print("No Exceptions. Everything correct")
finally:
    print("\n==Code Execution Successful==")