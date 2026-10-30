n = int(input())
rows = []
for _ in range(n):
    name, score = input().split()
    rows.append((name, int(score)))
print("{:<10} | {:^6}".format("Name", "Grade").rstrip())
print("-" * 10 + "+" + "-" * 6)
for name, score in rows:
    if score >= 90:
        grade = "A"
    elif score >= 80:
        grade = "B"
    elif score >= 70:
        grade = "C"
    elif score >= 60:
        grade = "D"
    else:
        grade = "F"
    print("{:<10} | {:^6}".format(name,grade).rstrip())