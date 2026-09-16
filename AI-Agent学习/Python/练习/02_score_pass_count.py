scores = []
for i in range(5):
    scores.append(int(input("")))
count = 0
for score in scores:
    if score >= 60:
        count+=1

print(f"及格的人数为：{count}")