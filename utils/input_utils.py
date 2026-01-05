import json

def ask_text(message):
    while True:
        user_input = input(message).strip()
        if user_input:
            return user_input
        else:
            print("Input cannot be empty. Please try again.")

def ask_number(message, min_value=None, max_value=None):
    while True:
        try:    
            value = int(input(message))
            if min_value is not None and value < min_value:
                print(f"Please enter a number greater than or equal to {min_value}.")
                continue
            if max_value is not None and value > max_value:
                print(f"Please enter a number less than or equal to {max_value}.")
                continue
                
            return value
        except ValueError:
            print("Invalid input. Please enter a valid whole number.")

def ask_choice(message, options_list):
    print(message)
    for i, opt in enumerate(options_list, 1):
        print(f"{i}. {opt}")

    choice = ask_number("Your choice: ", 1, len(options_list))
    return options_list[choice - 1]

def load_file(file_path):
    try:
        with open(file_path, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"The file was not found: {file_path}")
    except json.JSONDecodeError as e:
        print(f"Invalid JSON in {file_path}: {e}")
    except Exception as e:
        print(f"There was an error loading the file {file_path}: {e}")
    return None