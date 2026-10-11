def palind(a):
    x = len(a) - 1
    y = 0
    while y < x:
        if a[x] == a[y]:
            return True
        x-=1
        y+=1
        return False

a = (1,2,3,4,3,2)        
if palind(a):
    print("The tuple is a flip flop")
else:
    print("The tuple is not a flip flop")