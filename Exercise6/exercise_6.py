def function_one(file_name):
    with open(file_name, 'r') as f:
        return f

def function_two(file_name):
    try:
        function_one(file_name)
    except IOError:
        print "Error: can't find file or read data."
    else:
        print "Written content in the file successfully!"


print function_two('list.txt')




