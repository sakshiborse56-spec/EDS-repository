def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i   # return index if found
    return -1          # not found

# Input
n = int(input("Enter number of elements: "))
lst = []
for i in range(n):
    lst.append(int(input(f"Enter element {i+1}: ")))

key = int(input("Enter number to search: "))

pos = linear_search(lst, key)

if pos == -1:
    print("Number not found in the list.")
else:
    print("Number found at position:", pos)