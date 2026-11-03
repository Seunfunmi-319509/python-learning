def add_student():
      name = input("Enter the name of the student you will like to add: ")

      with open("students.txt", "a") as file:
            file.write(f"{name}\n")

      print("Student saved successfully!")

def view_students():
      with open("students.txt", "r") as file:
            student_list = file.read().splitlines()

      print("Current Students:")

      for student in student_list:
          print(student)

def search_students():
      with open("students.txt", "r") as file:
            student_list = file.read().splitlines()

      student_search = input("Kindly enter the name of the student you are looking for: ")

      if student_search in student_list:
            print("Student found!")
      else:
            print("Oops!!! Seems this student has not been registered")


while True:
    print("--------------------------------------------")
    print("Welcome to my Student Record Manager!!!")
    print("What would you like to do?")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Exit")
    print()
    
    choice = input("Enter your choice (1-4): ")
    
    if choice == "1":
            add_student()
    
    elif choice == "2":
           view_students()

    elif choice == "3":
          search_students()
    
    elif choice == "4":
            print("Goodbye!\n")
            break
    
    else:
          print("Invalid Input\n")
      
        

