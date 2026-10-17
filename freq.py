d = {"Codingal":2,"best":2,"sea":2,"halloween":1}

print("Original Dictionary:" + str(d))


K = 2

i = 0
for key in d:
    
    if d.get(key) == K:
        print()
        i+=1

print("Frequency of K:",i)
    