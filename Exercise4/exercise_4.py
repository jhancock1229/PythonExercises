print "EXERCISE 4 - MENU " \
      "1. Write input to file " \
      "2. Write input to screen " \
      "3. Quit"
user_input = raw_input("Enter your choice [1-3]: ")

if user_input == '1':
    user_input = raw_input("Please write input to screen: ")
    with open(r'test2.txt', 'r+') as f:
        user_input_string = str(user_input)
        write_data = f.write(user_input_string)
        f.seek(0)
        for line in f:
            print line
        back_to_menu = raw_input("Choose from the Menu, MENU 1. Write input to file 2. Write input to screen 3. Quit: ")
if user_input == '2':
    user_input = raw_input("Please write an input to the screen: ")
    print user_input

if user_input == "3":
    print "You have quit the program!"




# with open(r"test.txt", 'r') as f:
#     data = f.read()
#     print(data)