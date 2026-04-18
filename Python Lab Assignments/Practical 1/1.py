# Read 5 marks
marks = []
for i in range(5):
    m = int(input(f"Enter marks for course {i+1}: "))
    marks.append(m)

# Check if all >= 40
if min(marks) < 40:
    print("Result: Fail")
else:
    total = sum(marks)
    aggregate = total / 5   # percentage

    print("Aggregate:", aggregate)

    if aggregate > 75:
        print("Grade: Distinction")
    elif aggregate >= 60:
        print("Grade: First Division")
    elif aggregate >= 50:
        print("Grade: Second Division")
    elif aggregate >= 40:
        print("Grade: Third Division")