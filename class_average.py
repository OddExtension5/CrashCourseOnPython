# class_average.py
"""Class average program with sequence-controlled iteration."""

# initialization phase
total = 0  # sum of grades
grade_counter = 0
grades = [98, 76, 71, 87, 83, 90, 57, 79, 82, 94]  # list of 10 grades

# processing phase
for grade in grades:  
    total += grade  # add current grade to the running total
    grade_counter += 1  # indicate that one more grade was processed

# termination phase
average = total / grade_counter
print(f'Class average is {average}')