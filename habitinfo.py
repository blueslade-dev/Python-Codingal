habit_info = ("Coding",True,4,1.5)
weekly_habits = (0,1,0,0,1,1,1)
print("Length of tuple weekly_habits:",len(weekly_habits))
print(weekly_habits[1],weekly_habits[6],weekly_habits[1:4])
a = (1,2,3)
b = (5,6,9.05)
print(a+b)
done = 0
not_done = 0
for weekly_habit in weekly_habits:
    if weekly_habit == 1:
        done += 1
    else:
        not_done += 1

print("==Weekly Habit Progress Report==")
print("Habit:",habit_info[0])
print('Is Active:',habit_info[1])
print("Days per week on average:",habit_info[2])
print(f"Average time per day spent on coding: {habit_info[3]} hours")
print("No.of days in this week Hobby done:",done)
print("No.of days in this week Hobby not done:",not_done)
print("================================")