print("==Holiday Planner==")
print("Enter 1 for Vacation")
print("Enter 2 for staying at Home")
choice = input("Enter 1 or 2 for your holiday choice")
if choice == "1":
    print("You are going for a vacation")
    print("Enter 1 for Beach Vacation")
    print("Enter 2 for Mountain Vacation")
    print("Enter 3 for Countryside Vacation")
    vacation_choice = input("Enter your vacation choice:").strip()
    if vacation_choice == "1":
        print("Vacation planned to go: Beach vacation")
        print("You experience the the sun, and the waves of the sea, swimming peacefully with the cool waves.")
        print("Beaches in India you can explore are: Digha, Puri, Vhaijak, Thiruvanathapuram, Goa, Mumbai,etc.")
    elif vacation_choice == "2":
        print("You are planning to visit the cold and serene mountains")
        print("You get to experience the beauty of nature and without pollution you can breath peacefully")
        print("In India you can visit the Himalyan Ranges, Nilgiri Ranges, In Foreign see the Alps and the Andes.")
    elif vacation_choice == "3":
        print("You choose to go to the country and have ur vacation")
        print("The places are peaceful, without city noise, just the sound of the wind and the leaves you get a soothing experience.")
        print("In India you can visit the villages to get such calmness")

elif choice == "2":
    print("So you have planned to be at home")
    print("Enter 1 if you wish to go outside and play")
    print("Enter 2 if you wish to play video games and watch videos on screen")
    print("Enter 3 if you wish to study hard and read story books")
    print("Enter 4 if you want the balance between the above choices")
    home_choice = input("Enter 1,2,3,4 for your choice")
    if home_choice == "1":
        print("Go outside and play, play football, cricket, basketball, etc with your friends increase your physical health + have fun")
    elif home_choice == "2":
        print("Get your phone, Laptop, PC or Ipad, play games with your friends, have fun , play worrilessly throughout the vacation but at a limit (4-5 hrs per day max)")
    elif home_choice == "3":
        print("You wish to study hard, well it would actually be really good for you as it would increase your knowledge, and help you in ur exams. Reading books will also help u imagine things increasung your creativity")
    elif home_choice == "4":
        print("So you wish to manage a balance between the above choices, well it would be the best combination possible! You would get to have fun while increasing your physical strength, you would be able to have screen time and have fun plus it would help in your exams and creativity too")
    else:
        print("Invalid Choice")

else:
    print("Invalid Choice")