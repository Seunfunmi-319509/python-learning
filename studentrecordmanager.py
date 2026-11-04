def main():
    while True:
        print("Welcome to my Student Record Manager where you can:")
        print("1. Add a Student")
        print("2. View all Students")
        print("3. Search for Student")
        print("4. Check student Grade")
        print("5. Exit")

        choice = int(input("What would you like to do? "))

        match choice:
            case 1: 
                add_student()
            case 2:
                view_students()
            case 3:
                search_students()
            case 4:
                check_grade()
            case 5:
                break
            case _:
                print("Sorry, enter one of the options above")

def validateName(name):
    if name.replace(" ", "").isalpha():
        return True

    return False

def validateScore(score):
    if score.isdigit():
        return True

    return False 

studentLists = []

def add_student():
    name = input("Enter the name of the student you would like to add: ")
    
    if not validateName(name):
        print("Invalid student name!")
        return

    score = int(input("Enter the score of the student: "))

    if not validateScore(score):
        print("Invalid Student Score!")
        return

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

    if not validateName(student_search):
        print("Invalid student name!")
        return
    
    for student in studentLists:
        if student_search in student:
            print("Student found!")
            return
    print("Oops!!! Seems this student has not been registered")

def check_grade():
    name = input("Kindly enter the name of the student to check the grade: ")

    if not validateName(name):
            print("Invalid student name!")
            return

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

