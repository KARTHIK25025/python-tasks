def infinite_even_numbers():
    n = 2
    while True:
        yield n
        n += 2
N = 10
even_gen = infinite_even_numbers()
print(f"First {N} even numbers:")
for _ in range(N):
    print(next(even_gen), end=" ")
