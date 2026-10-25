grade_book = {
    "Yash":56,
    "Rahul":48,
    "Rammohan":94,
    "Mohan": 83,
    "Rita":62
}
total = 0
lst = []
for i in grade_book:
    grade = grade_book.get(i)
    total += grade
    lst.append(grade)
   

avg = total/len(grade_book)
print("Average marks:",avg)

print("Lowest marks:", max(lst))
print("Highest marks:",min(lst))

search = input("Enter student name:").capitalize().strip()
answer = grade_book.get(search,f"{search} Not Found")
if answer == f"{search} Not Found":
    print(f"Sorry,{search} Not Found.")
else:
    print(f"{search} got {answer}.")