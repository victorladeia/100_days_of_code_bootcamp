student_scores = input( "Input a list of students scores " ).split()
for score_index in range( 0, len( student_scores ) ):
    student_scores[score_index] = int( student_scores[score_index] )
print( student_scores )

highest_score = student_scores[0]

for score in student_scores:
    if score > highest_score:
        highest_score = score

print( f"The highest score in the class is: {highest_score}" )