# control flow

# if-else statement 

# if
a = 10
b = 5
if a > b:
    print(f"{a} is greater than {b}")
print("\n")

# if-else
a = 8
b = 20
if a > b:
    print(f"{a} is greater than {b}")
else:
    print(f"{b} is greater than {a}")
print("\n")

# if-elif-else
score = 61
if score > 80:
    print("A")
elif score > 70:
    print("B")
elif score > 60:
    print("D")
else:
    print("E")
print("\n")

# looping

# for loop

# for-each
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for num in numbers:
    print(num)
print("\n")

# accessing list value with index for loop
for i in range(len(numbers)):
    print(numbers[i])
print("\n")

# for loop range
for i in range(5, 10):
    print(i)
print("\n")

# nested for loop
separator = "#"
for i in range(3):
    for j in range(3):
        print(numbers[j])
    print(separator)
print("\n")

# while loop
i = 0
while i < len(numbers):
    print(numbers[i])
    i += 1
print("\n")

# continue statement
for i in range(1, 11):
    if i % 2 == 0:
        continue
    print(i)
print("\n")

# break statement
for i in range(1, 11):
    if i == 4:
        break
    print(i)
print("\n")