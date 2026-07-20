def greet(name):
    print(f"""
Hello, {name}!
Welcome to Python          
""")


def square(number):
    return number * number



def calculate_average(a,b,c):
    return (a+b+c)/3

greet("Oluwaseun")
print(square(11))
print(f"Average Score: {calculate_average(56, 44, 43):.2f}")
    