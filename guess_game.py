import random

secret_number = random.randint(1, 10)

count = 0


while True:
    guess = int(input("Guess the secret number: "))
    count += 1

    if guess == secret_number:
        break

    if guess > secret_number:
        print("Number too high, try again!")

    else:
        print("Number too low, try again!")

print(f"Congratulations! You got it in {count} attempts!")

    
