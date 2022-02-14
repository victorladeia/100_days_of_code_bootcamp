students_heights = input("Input a list of students heights ").split()

for n in range(0, len(students_heights)):
    students_heights[n] = int(students_heights[n])
print(students_heights)

counter = 0
sum = 0
for height in students_heights:
    sum += height
    counter += 1

print(round(sum / counter))