myfavoritefood = ["Rice", "Yam", "Amala", "Bread", "Fufu"]
print(myfavoritefood[0])
print(myfavoritefood[-1])
myfavoritefood.append("Jollof Rice")
print(myfavoritefood)
myfavoritefood.insert(1, "Pounded-yam")
print(myfavoritefood)
myfavoritefood.remove("Bread")
print(myfavoritefood)

for food in myfavoritefood:
    print(food)