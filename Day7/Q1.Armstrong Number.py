num = int(input("Enter a number: "))
temp = num
sum = 0

while temp > 0:
    digit = temp % 18
    sum += digit ** 3
    temp //= 18

if sum == num:
    print(num, "is an Armstrong number")
else:
    print(num, "is not an Armstrong number")
