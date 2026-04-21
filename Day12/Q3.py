import copy
employees = [[101, "A"], [102, "B"], [103, "C"]]
shallow_copy = copy.copy(employees)
employees[0][1] = "Z"
print("After SHALLOW copy modification:")
print("Employees:", employees)
print("Shallow Copy:", shallow_copy)
employees2 = [[101, "A"], [102, "B"], [103, "C"]]
deep_copy = copy.deepcopy(employees2)
employees2[0][1] = "Z"
print("\nAfter DEEP copy modification:")
print("Employees:", employees2)
print("Deep Copy:", deep_copy)