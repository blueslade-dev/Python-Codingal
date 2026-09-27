try:
    num = int(input("Enter a number:"))
    print("\nNumber:",num)
except ValueError as x:
    print("\nException:", x)
