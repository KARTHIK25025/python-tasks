branch_a = [
    [10, 20],
    [30, 40]
]

branch_b = [
    [5, 15],
    [25, 35]
]

combined = [
    [branch_a[i][j] + branch_b[i][j] for j in range(len(branch_a[0]))]
    for i in range(len(branch_a))
]

total_employees = sum(sum(row) for row in combined)

print("Combined Matrix:")
for row in combined:
    print(row)

print("Total Employees:", total_employees)