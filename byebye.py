valid = False
while not valid:
    num = int(input("Enter a number:"))
    try:
        while num%2 == 0:
           
           print("bye")
           break
        valid = True  
    except ValueError as a:
        print("Exception:", a)
    finally:
        print("==Code Execution Successful==")
   