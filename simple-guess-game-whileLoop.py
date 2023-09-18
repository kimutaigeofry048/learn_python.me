# three times to guess the right number,
#can be applied to user auth systems


secreat_number = 9
guess_limit = 3
guess_count = 0
while guess_count < guess_limit:
    guessed_number = int(input("Guess: "))
    guess_count += 1
    if guessed_number == secreat_number:
        print("You won")
        break
else:
    print("You failed.")
    

