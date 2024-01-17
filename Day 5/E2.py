student_heights = input().split()
for n in range (0, len(student_heights)):
    student_heights[n] = int(student_heights[n])

sum = 0
for n in student_heights:
    sum += n

sum2 = round(sum/len(student_heights),0)
print(f"Total height = {sum}\nNumber of students = {len(student_heights)}\nAverage Height = {sum2}")