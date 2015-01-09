# Function which displays the menu options for the user
def menu():
    with open(r"menu.txt", "r") as x:
        for choices in x:
            print choices


# Global confirmation message so the user knows what they did was successful
success_prompt = "Input Successful! PLease make another choice:"


# Function which runs the program
def back_to_menu():
    user_input = raw_input("Enter your choice: 1, 2 or 3: ")  # Prompts the user to enter value 1, 2, or 3
    if user_input == '1':
            user_input_one = raw_input("Please write your input to the file: ")  # Prompt for choice 1
            with open(r'test1.txt', 'w+') as f:  # Opens a writable file and names it f
                user_input_string = str(user_input_one)  # Converts the user input to a string
                f.write(user_input_string)  # This writes the user input to the file called previously
                f.seek(0)  # This resets the cursor to the beginning of the user input within the text file
                for line in f:  # Calls for the text written within the file f
                    print line  # Prints text from the file f
                print success_prompt  # Lets the user know that their input was successful
                menu()  # Displays the menu for the user
                back_to_menu()  # Runs the function, again.
    elif user_input == '2':
        user_input = raw_input("Please write your input to the screen: ")  # Prompt for choice 2
        print user_input
        print success_prompt  # Tells the user that their input was successful
        menu()  # Displays the menu for the user
        back_to_menu()  # Runs the function, again.

    elif user_input == "3":
        print "You have quit the program!"  # Exits the program
    else:
        back_to_menu()  # Puts the user back to the beginning.


menu()
back_to_menu()

