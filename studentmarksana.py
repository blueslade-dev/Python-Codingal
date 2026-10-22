l = []
marks_list = [85,91,77,82,66]
sample_list = [55,81,98] 
triple = sample_list * 3
print("Length of the list of marks: ",len(marks_list))
print(f"First mark: {marks_list[0]} & Last mark: {marks_list[-1]}")
print("First three marks: ",marks_list[0:3])
print("Reversed marks list: ",marks_list[::-1])

def marks_checker():
    for mark in marks_list:
        if str(mark)[-1] ==str(mark)[0]:
            print(f"{mark} has first and last character same")  
total = 0
for element in marks_list:
    total += element

print(marks_checker())
print("Total marks scored by the students: ",total)
print("Average score: ",total/len(marks_list))
marks_list.sort()
print("Marks in ascending order: ",marks_list)
print(f"Smallest Marks:{marks_list[0]}\nGreatest Marks:{marks_list[-1]}")