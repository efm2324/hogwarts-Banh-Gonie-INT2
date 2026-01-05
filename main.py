from menu import display_main_menu

def main():

    try:
        display_main_menu()
    except Exception as e:
        print(f"\n[SYSTEM ERROR]: The game encountered a problem: {e}")
    
    print("       THANK YOU FOR PLAYING!       ")
    input("Press Enter to exit...")

if __name__ == "__main__":
    main()