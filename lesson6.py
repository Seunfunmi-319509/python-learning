count = 1

while count < 11:
    print(count)
    count+=1

secret_number = 7

guess = int(input("Guess the secret number: "))

while guess != secret_number:
    if guess > secret_number:
        print("Number too high, try again!")
    else:
        print("Number too low, try again!")
    
    guess = int(input("Guess the secret number: "))
    
print("Congratuations, you have successfully guessed the number correctly!")

