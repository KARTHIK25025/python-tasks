def number_generator(n):
    """Generates numbers from 1 to N"""
    for i in range(1, n + 1):
        yield i
N = 5
print(f"Generating numbers up to {N}:")
for num in number_generator(N):
    print(num)
