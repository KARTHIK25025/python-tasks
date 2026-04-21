import random
numbers = []
for _ in range(10):
    num = random.randint(1, 100)
    numbers.append(num)
print("Generated Numbers:", numbers)
even_count = 0
odd_count = 0
for num in numbers:
    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1
print("Even Numbers Count:", even_count)
print("Odd Numbers Count:", odd_count)
unique_numbers = set(numbers)
print("Unique Numbers:", unique_numbers)