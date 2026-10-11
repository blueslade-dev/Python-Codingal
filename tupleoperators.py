t = (17,"Donald",8.01,True,8.01)

print(t)
print("No.of elements in Tuple t: ",len(t))
print(f"No.of {t[2]}s in Tuple t: ",t.count(8.01))

t = t + ("Trump",)
print(t)

print(f"First element of tuple t: {t[0]}")
print(t[1])
print(t[-1],"\n",t[-2])
print(t[2:4])
print(t[:3])
print(t[1:])