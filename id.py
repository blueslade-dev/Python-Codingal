student_data = {
    "id1":{"name":"John","class":"IX","subjects":"English, Maths, Science Group"},
    "id2":{"name":"Rohan","class":"X","subjects":"English, History, Geography"},
    "id3":{"name":"Priya","class":"XII","subjects":"Philosophy, Sociology, History"},
    "id4":{"name":"Mohan","class":"VIII","subjects":"English, Computer Science, History"}
}

lst = []
detail_lst = []
i = -1
j = -1

for student_id,details in student_data.items():
    if student_id not in lst and details not in lst:
        lst.append(student_id) 
        detail_lst.append(details)
        i += 1
        j += 1
        k = lst[i]
        v = detail_lst[j]
        print(k,":",v)     


