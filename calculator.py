print("Choose an option below:")
print("1 for addition \n2 for subtraction \n3 for multiplication \n4 for division.")
#take user input
operator = input("your choice?? ")
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

#declare all functions we need
#sum fuction
def sum():
    print(num1 + num2)

#subtraction function
def subtract():
    print(num1 - num2)

#multiplication function
def multiply():
    print(num1 * num2)

#division function
def divide():
    print(num1 / num2)

#conditional statements to check user inputs.
if operator == "1":
    sum()
elif operator == "2":
    subtract()
elif operator == "3":
    multiply()
elif operator == "4":
    divide()
else:
    print("wrong input choice")