# Matrix addition (add same dataset to itself)
A = marks
B = marks + 10   # shifted version

print("\nMatrix addition (A + B):")
print(A + B)

print("\nMatrix multiplication (element‑wise):")
print(A * B)

print("\nDot product (students × subjects inner products):")
result_dot = np.dot(A, B.T)   # 10×10: student‑vs‑student similarity
print(result_dot)

print("\nTranspose (now 5×10, subjects × students):")
T = A.T
print(T)
