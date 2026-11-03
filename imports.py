import random

foods = ["Amala", "Rice", "Yam", "Fufu", "Pounded Yam"]
food = random.choice(foods)
print(f"Today's food recommendation: {food}")

from datetime import datetime
now = datetime.now()

print(f"Today is {now.day}/{now.month}/{now.year}")
print(now.second)