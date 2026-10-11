weather = (1,0,0,1,1,0)
sunny = 0
rainy = 0
for i in range(0,len(weather) - 1):
    if weather[i] == 1:
        sunny+=1
    else:
        rainy+=1

print("Good weather probability: ",round((sunny/len(weather) * 100),2),"%")
print("Bad weather probability: ",round(((rainy/len(weather)) * 100),2),"%")    