# Arithmetic
print("\nArithmetic operations (add 5, multiply by 0.9):")
print("A + 5 =")
print(A + 5)
print("A * 0.9 =")
print(A * 0.9)

# Statistical operations
print("\nStatistical operations:")
print("Sum of all marks                 =", np.sum(A))
print("Average of all marks             =", np.mean(A))
print("Max mark                         =", np.max(A))
print("Min mark                         =", np.min(A))
print("Standard deviation               =", np.std(A))
print("Average per student (axis=1)   =", np.mean(A, axis=1))
print("Average per subject (axis=0)   =", np.mean(A, axis=0))
