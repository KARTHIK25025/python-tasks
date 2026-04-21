def sum_digits(n):
    if n < 10:
        return n
    else:
        last_digit = n % 10
        remaining_digits = n // 10
        return last_digit + sum_digits(remaining_digits)
print(sum_digits(123))
print(sum_digits(4567))
