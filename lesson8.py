student = {
    "name": "Oluwaseun",
    "age": 20,
    "state": "Ogun",
    "favorite_food": "Amala",
    "favorite_language": "Python"
}

print(student["name"])
student["age"] += 1
student["hobby"] = "Reading"
del(student["state"])

for key, value in student.items():
    print(f"{key} : {value}")