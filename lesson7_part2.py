scores = [85, 70, 92, 60, 78]

highest = scores[0]

for score in scores:
    if score > highest:
        highest = score

lowest = scores[0]

for score in scores:
    if score < lowest:
        lowest = score

total = 0
for score in scores:
    total+=score

average = total / len(scores)


print(f"""
{highest}
{lowest}
{total}
{average}
""")