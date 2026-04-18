import numpy as np

# Real‑life dataset: 10 students × 5 subjects (marks out of 100)
# Each row = 1 student; each column = 1 subject
marks = np.array([
    [85, 78, 92, 88, 90],  # student 0
    [72, 65, 70, 68, 75],  # student 1
    [90, 89, 93, 91, 95],  # student 2
    [60, 55, 62, 58, 65],  # student 3
    [78, 82, 79, 80, 81],  # student 4
    [95, 98, 97, 96, 99],  # student 5
    [50, 45, 52, 48, 55],  # student 6
    [88, 85, 90, 89, 92],  # student 7
    [65, 70, 68, 72, 70],  # student 8
    [77, 75, 78, 76, 79],  # student 9
])

print("Dataset (10 students × 5 subjects):")
print(marks)