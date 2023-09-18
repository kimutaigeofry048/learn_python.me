numbers = [1,2,3,4,1,5,7,9,2,5,1,7,6,3] #removing duplicates
unique = []
for number in numbers:
    if number not in unique:
        unique.append(number)
print(unique)