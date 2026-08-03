scores = [90, 85, 75, 60, 98, 88]

highest = scores[0]
second_highest = scores[1]
third_highest = scores[2]

for score in scores:
    if score > highest:
        third_highest = second_highest
        second_highest = highest
        highest = score
    elif score > second_highest and score < highest:
        third_highest = second_highest
        second_highest = score
    elif score > third_highest and score < second_highest:
        third_highest = score
    

print(third_highest)