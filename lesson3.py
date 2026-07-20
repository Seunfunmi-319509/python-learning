name = input("What is your name? ")
subject_one_score = int(input("What's your score in Mathematics? "))
subject_two_score = int(input("What's your score in English? "))
subject_three_score = int(input("What's your score in Physics? "))
average_score = (subject_one_score + subject_two_score + subject_three_score) / 3
print(f"Hello, {name}!\n")
print(f"Average Score: {average_score:.2f}")

if average_score >= 70:
    print(f"""
Grade: A\n
Congratuations! You qualify for an academic award          
""")
elif average_score >= 60:
    print("Grade: B")
elif average_score >= 50 :
    print("Grade: C")
else:
    print("Grade: F")