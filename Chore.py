total_chores = 4
chore_num = 0
while chore_num <= 4:
    
    if chore_num == 0: print("Go and wash dishes")
    elif chore_num == 1: print("Feed the pet")
    elif chore_num == 2: print("Water the plants")
    elif chore_num == 3: print("Cook dinner")
    elif chore_num == 4: print("All Chores completed")


    answer = input("Have you finished all chores? (Yes/No)").strip().capitalize()
    if answer == "Yes":
        
        print(f"\nYou have completed all {chore_num} chores! Have a break!")
    else:
        print(f"\nComplete the {total_chores - chore_num} remaining chores")
    chore_num += 1
    

test_value = 0
safety_counter = 0
while safety_counter <= test_value:
    test_value += 1
    safety_counter += 1
    if safety_counter == 3: print("The cycle is stopped")
    break
print("\n== Chore Checklist ==")
print(f"\nNumber of chores done: {chore_num - 1}")
print(f"\nNumber of chores remaining: {(total_chores - chore_num) + 1}")