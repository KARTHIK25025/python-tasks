import copy
classes = [["Math", [30, 35]], ["Science", [25, 28]]]
classes_copy = copy.deepcopy(classes)
classes[0][1][0] = 999   # change Math first value
print("Original classes:", classes)
print("Deep Copy:", classes_copy)