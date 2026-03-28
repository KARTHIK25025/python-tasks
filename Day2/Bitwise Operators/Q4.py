num = int(input("Enter a number: "))
shift = int(input("Enter shift count: "))

left_shift = num << shift
right_shift = num >> shift

print(f"{num} << {shift} is: {left_shift}")
print(f"{num} >> {shift} is: {right_shift}")
