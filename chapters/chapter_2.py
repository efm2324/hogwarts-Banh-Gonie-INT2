
def meet_friends():
    print(
        "Hi! I'm Ron Weasley. Mind if I sit with you? \n\nHow do you respond?"
    )
    while True:
        try:
            answer = int(input("1. Yes \n2. No ").strip())
        except ValueError:
            print("Invalid input. Please enter the number 1 or 2.")
            continue

        print("Your choice : ", answer)
        if answer == 1:
            print("Hagrid takes you to Diagon Alley, where you buy your wand, books, and robes.")
            break
        elif answer == 2:
            print("Hagrid gently insists and takes you along anyway!")
            break
        else:
            print("Invalid choice. Please choose 1 or 2.")
        