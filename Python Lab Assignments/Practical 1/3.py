n = int(input("Enter n: "))

# Pattern 1: Left‑aligned triangle
print("Pattern 1:")
for i in range(1, n+1):
    print("*" * i)

# Pattern 2: Right‑aligned triangle
print("\nPattern 2:")
for i in range(1, n+1):
    print(" "*(n-i) + "*"*i)

# Pattern 3: Pyramid
print("\nPattern 3:")
for i in range(1, n+1):
    print(" "*(n-i) + "* "*(i))