def manual_sum(numbers):
    total = 0
    for num in numbers:
        total += num
    return total

my_nums = [1, 2, 3, 4, 5]
print(f"The total sum is: {manual_sum(my_nums)}")
