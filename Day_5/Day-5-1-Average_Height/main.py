student_heights = input( "Input a list of student heights " ).split()
for student_heights_index in range( 0, len( student_heights ) ):
    student_heights[ student_heights_index ] = int( student_heights[ student_heights_index ] )
print( student_heights )

sum_of_height = 0
number_of_students = 0

for height in student_heights:
    sum_of_height += height
    number_of_students += 1

heigths_average = sum_of_height / number_of_students
heigths_average = round( heigths_average )

print( heigths_average )