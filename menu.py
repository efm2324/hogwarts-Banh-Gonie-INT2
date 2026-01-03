
def display_main_menu():
    print("1. Start Chapter 1 - Arrival in the magic world")
    choice =int(input("2. Exit Game"))
    if choice == 2:
        print("Exiting the game.)
        exit(0)
    if choice == 1:
        from chapters.chapter_1 import start_chater_1
        character = start_chater_1()
        return character


