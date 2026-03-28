numbers = [10, 45, 45, 20, 30, 4]
unique_nums = list(set(numbers))
unique_nums.sort()

if len(unique_nums) < 2:
    print("List is too short.")
else:
    print("The second largest number is:", unique_nums[-2])
