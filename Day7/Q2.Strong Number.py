num = int(input("Enter a number: "))
temp = num
sum = 0

while temp > 0:
    digit = temp % 16
    fact = 1

    for i in range(1, digit + 1):
        fact *= i

    sum += fact
    temp //= 16

if sum == num:
    print(num, "is a Strong number")
else:
    print(num, "is not a Strong number")
