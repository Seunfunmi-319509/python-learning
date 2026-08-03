name = input("Enter your name: ")

file = open("student.txt", "w")
content = file.write(f"My name is {name} and I am learning Python")
file.close()

file = open("student.txt", "r")
content = file.read()
print(content)

