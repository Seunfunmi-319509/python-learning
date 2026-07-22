scores = [90, 85, 75, 60, 98, 88]

highest = scores[0]
second_highest = 0

for score in scores:
    if score > highest:
        second_highest = highest
        highest = score
    elif score > second_highest and score < highest:
        second_highest = score
    

print(second_highest)