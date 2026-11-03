def main():
    while True:
        print("Welcome to my Student Record Manager where you can:")
        print("1. Add a Student")
        print("2. View all Students")
        print("3. Search for Student")
        print("4. Check student Grade")
        print("5. Exit")

        choice = int(input("What would you like to do? "))

        if choice == 1:
            add_student()
        elif choice == 2:
            view_students()
        elif choice == 3:
            search_students()
        elif choice == 4:
            check_grade()
        elif choice == 5:
            break
        else:
            print("Sorry, enter one of the options above")



studentLists = []

def add_student():
    name = input("Enter the name of the student you would like to add: ")
    score = int(input("Enter the score of the student: "))

    student = {
        "name": name,
        "score": score
    }
    studentLists.append(student)
    print("Student saved successfully!")

def view_students():
    print("Current Students:")
    for student in studentLists:
        print(f"Name: {student['name']}")
        print(f"Score: {student['score']}")


def search_students():
    student_search = input("Kindly enter the name of the student you are looking for:")
    for student in studentLists:
        if student_search in student:
            print("Student found!")
            return
    print("Oops!!! Seems this student has not been registered")

def check_grade():
    name = input("Kindly enter the name of the student to check the grade")
    for student in studentLists:
        if student["name"].lower() == name.lower():
            score = student["score"]

        if score >= 50:
            print("Student Grade: Passed")
        else:
            print("Student Grade: Failed")

        return
    print("Oops! This student has not been registered.")

main()

