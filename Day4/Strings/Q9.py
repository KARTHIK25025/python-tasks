text = "Python"
frequency = {}

for char in text:
    frequency[char] = frequency.get(char, 0) + 1

print("Character frequencies:", frequency)
