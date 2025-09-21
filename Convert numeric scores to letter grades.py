import numpy as np


def convert_to_grades(scores):
    # Create a NumPy array from the input list
    score_array = np.array(scores)

    # Create an empty string array of the same shape as score_array
    grade_array = np.empty_like(score_array, dtype='U1')

    # Fill grade_array with letter grades
    grade_array[score_array >= 90] = 'A'
    grade_array[(score_array >= 80) & (score_array < 90)] = 'B'
    grade_array[(score_array >= 70) & (score_array < 80)] = 'C'
    grade_array[(score_array >= 60) & (score_array < 70)] = 'D'
    grade_array[score_array < 60] = 'F'

    return grade_array


# Get input from user
scores = list(map(int, input().split()))

# Call the function and print the result
result = convert_to_grades(scores)
print(result)
