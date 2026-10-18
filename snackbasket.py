#In this assignment, you will build a School Snack Counter using Python. You will create snack boxes with sets, add new snacks, find shared snacks, create an array of snack counts, add values to the array, and use count() and reverse() to explore the final result.
box1 = {'Chips','Biscuits','Cold drink'}
box2 = {'Biscuits','Soft Drink','Fries'}
box1.add('Chicken Wings')
shared = box1.intersection(box2)

import array
a = array.array("i",[2,4,1,8])
a.insert(4,1)
a.append(1)

print("=================")
print(f"Snacks in Box 1: {box1}\nSnacks in Box 2: {box2}")
print("Shared Fruits: ",shared)
a.reverse()
print("Reversed form of array a:",a)
print('=================')