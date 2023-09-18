#name must be 3 char or more and not more than 50 char
name = input("Enter your name: ")
if len(name) <  3:
    print("must be more than 3 char")
elif len(name) > 50:
    print("Name should not exceed a max of 50 char")
else:
    print("Name Looks good")