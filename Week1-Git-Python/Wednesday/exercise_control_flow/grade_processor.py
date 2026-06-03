scores = [88, 92, 75, -1, 63, 95, 81, 70, -5, 55, 100, 78, -999, 90, 85]
valid_scores = []

a_count = 0
b_count = 0
c_count = 0
d_count = 0
f_count = 0

for index, score in enumerate(scores):
    if score == -999:
        break
    
    if score < 0:
        continue
    
    if score >= 90:
        grade = "A"
        a_count += 1
        valid_scores.append(score)
    elif score >= 80:
        grade = "B"
        b_count += 1
        valid_scores.append(score)
    elif score >= 70:
        grade = "C"
        c_count += 1
        valid_scores.append(score)
    elif score >= 60:
        grade = "D"
        d_count += 1
        valid_scores.append(score)
    else:
        grade = "F"
        f_count += 1
        valid_scores.append(score)

average_score = sum(valid_scores) / len(valid_scores)


print(f"Student Grades: {valid_scores}")
print (f"\nClass Average: {average_score}")
print (f"\nHighest Grade: {max(valid_scores)}")
print (f"\nLowest Grade : {min(valid_scores)}\n")

print("═" * 40)
print(" Distribution Count")
print("═" * 40)

print(f"\nA: {a_count}")
print(f"\nB: {b_count}")
print(f"\nC: {c_count}")
print(f"\nD: {d_count}")
print(f"\nF: {f_count}")


