markone = int(input("Mark1:"))
marktwo = int(input("Mark2:"))
markthree = int(input("Mark3:"))
markfour = int(input("Mark4:"))
markfive = int(input("Mark5:"))


tot = markone + marktwo + markthree + markfour + markfive
avg = tot/5
if avg in range(91,101):
    print(" Grade: A1")
elif avg in range(81,91):
    print("Grade:A2")
elif avg in range(71,81):
    print("Grade:B1")
elif avg in range(61,71):
    print("Grade:B2")
elif avg in range(51,61):
    print("Grade:C1")
elif avg in range(41,51):
    print("Grade: C2")
elif avg in range(31,41):
    print("Grade: D1")
elif avg in range(21,31):
    print("Grade: D2")
elif avg in range(11,21):
    print("Grade: E1")
elif avg in range(0,11):
    print("Grade: E2")
elif avg not in range (0,101):
    print("Invalid marks")
else:
    print("Invalid")