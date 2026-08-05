print("Numbers from 1 to 20:")
for i in range(1, 21):
    print(i, end=" ")

print("\n\nMultiplication Table")
num = int(input("Enter a number: "))
for i in range(1, 11):
    print(num, "x", i, "=", num * i)

print("\nEven numbers from 1 to 50:")
i = 1
while i <= 50:
    if i % 2 == 0:
        print(i, end=" ")
    i += 1
