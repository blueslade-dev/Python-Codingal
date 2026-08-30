string = input("Enter a string of your choice:")
string2 = ("")
for i in string:
    string2 = i + string2
print(f"\nOrignal string:{string}")
print(f"\nReversed string:{string2}")