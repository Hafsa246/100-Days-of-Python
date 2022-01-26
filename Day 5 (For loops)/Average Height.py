student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
print(student_heights)

sum = 0
for height in student_heights:
    sum += height

leng = 0
for i in student_heights:
    leng += 1

ans = sum/leng
print(round(ans))