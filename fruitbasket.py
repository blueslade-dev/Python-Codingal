import array as a
basket1 = {'Apple','Orange','Blackberry','Watermelon'}
basket2 = {'Banana','Apple','Blueberry','Blackberry','Pomegranate'}
basket1.add('Lemon')
b = basket1.intersection(basket2)


c = a.array("i",[2,7,3,2])
fruit_count = c.count(2)
print(fruit_count)
print(c[1:3])
c.insert(3,3)
print(c)
c.append(2)
print(c)

print("========================")
print("Fruits in Basket 1: ",basket1)
print("Fruits in Basket 2: ",basket2)
print("Common fruits:",b)
print("Fruit Count: ",fruit_count)
print('========================')