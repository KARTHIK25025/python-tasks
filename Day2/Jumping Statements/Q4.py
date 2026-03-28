numbers = [10, 25, 42, 7, 99, 15]
target = 7

for num in numbers:
    if num == target:
        print(f"Found {target}!")
        break
    print(f"Checking {num}...")
