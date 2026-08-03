name = input("Enter your name: ")

with open("students.txt", "a") as file:
    file.write(f"{name}\n")
print("Student saved successfully!")

with open("students.txt", "r") as file:
    content = file.read()
    print(f"Current Students:\n{content}\n")