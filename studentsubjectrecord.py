student_data = {
    "id-2100":{"Name":"Riya Jaiswal","Class":"X","Subjects":['English','Maths','Chemistry']},
    "id-2101":{"Name":"Manish Das","Class":"IX","Subjects":['Maths','Computer Science','Physics']},
    "id-2102":{"Name":"Mohan Paul","Class":"IX","Subjects":['Hindi','History','Civics']},
    "id-2103":{"Name":"Manish Das","Class":"IX","Subjects":['Maths','Computer Science','Physics']}
}

print("Original Record:\n",student_data)
print("Available info on id-2101 based on original record:\n",student_data.get("id-2101","Not Found"))
print("Available info on id-2104 based on original record:\n",student_data.get("id-2105","Not Found"))
student_data["id-2102"]["Subjects:"] = ["Geography","English","Political Science"]
student_data["id-2104"] = {
    "Name":"Rima Jain",
    "Class":"XI",
    "Subjects":["Geography","History","Civics"]
}

cleaned_data = {}
seen_records = []

for student_id,details in student_data.items():
    unique_key = (details["Name"],details["Class"],details["Subjects"])
    if unique_key not in seen_records:
      seen_records.append(unique_key)
      cleaned_data[student_id] = details

student_data = cleaned_data
print("Removed student:",student_data["id-2100"]["Name"])
removed_student = student_data.pop("id-2100","Student not found.")

print(f"Length of student data dictionary: {len(student_data)}")

print("==FINAL RECORD==")
for student_id,details in student_data.items():
    print(student_id,":",details)
print("================")