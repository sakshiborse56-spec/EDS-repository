# Horizontal stacking (more columns, i.e., more subjects avg, etc.)
avg_per_student = np.mean(A, axis=1, keepdims=True)   # 10×1
stacked_horiz = np.hstack((A, avg_per_student))
print("\nHorizontal stacking (original + avg per student):")
print(stacked_horiz)

# Vertical stacking (more rows, i.e., more students)
extra_students = np.array([
    [80, 85, 82, 83, 84],
    [65, 68, 70, 67, 69]
])
stacked_vert = np.vstack((A, extra_students))
print("\nVertical stacking (original + 2 extra students):")
print(stacked_vert)
