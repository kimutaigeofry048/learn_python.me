#handling errors in python

try:
    age = int(input("Age: ")) #if user entered correct numerical value the try part will be executed correctly
    print(age)
    income = 40000
    risk = income / age
    print(risk)
except ValueError:          #will accept the value error for invalid inputs and not crush the program. 
    print("Invalid input")
except ZeroDivisionError:
    print("age cannot be zero.")