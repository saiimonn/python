n = int(input())
student_marks = {}
for _ in range(n):
    name, *line = input().split()
    scores = list(map(float, line))
    student_marks[name] = scores
query_name = input()

if query_name in student_marks:
    print(f"{sum(student_marks[query_name]) / len(student_marks[query_name]):.2f}")
else:
    print("No name in the database")