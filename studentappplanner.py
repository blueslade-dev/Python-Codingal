CAMERA = 1 #0001
MICROPHONE = 2 #0010
STORAGE = 4 #0100
LOCATION = 8 #1000
approved_apps = ("YouTube","Google Classroom","Duolingo")
restricted_apps = ("Facebook","Google Play","Instagram")
std_name = input("Enter your name:").capitalize()
requested_app = input("Enter your requested app, if none type'No'").capitalize()
if std_name is str:
    print("Student name is a string datatype")
else:
    print("Student name is not a string datatype")

if requested_app is not int:
    print("The requested app is'nt an integer datatype")
else:
    print("The requested app is an integer datatype")

if requested_app in approved_apps:
    print(f"Your app, {requested_app} in approved! You can use it in the system.")
elif requested_app not in approved_apps and restricted_apps:
    print(f"App, {requested_app} not recognised by the system seek human approval")
elif requested_app in restricted_apps:
    print(f"App Approval Denied for {requested_app}")

student_permissions = CAMERA|STORAGE|MICROPHONE
print(f"Permission number: {bin(student_permissions)}")

if student_permissions & CAMERA:
    print("Camera permission: Enabled")

if student_permissions & MICROPHONE:
    print("Microphone permission: Enabled") 

if student_permissions & STORAGE:
    print("Storage permission: Enabled")

if student_permissions & LOCATION:
    print("Location permission: Enabled")
else:
    print("Location permission: Disabled")

next_permission = CAMERA << 1
print(f"Camera bit:{CAMERA}")
print(f"Camera bit shifted to left: {next_permission}")

prev_permission = STORAGE >> 1
print(f"Storage bit:{STORAGE}")
print(f"Storage but after right shift: {STORAGE}")