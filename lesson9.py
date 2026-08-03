backend = {"Python", "Go", "Java"}
frontend = {"JavaScript", "HTML", "CSS", "Python"}

print(backend | frontend)
print(backend & frontend)
print(backend - frontend)
backend.add("Rust")
backend.remove("Java")
print(backend)