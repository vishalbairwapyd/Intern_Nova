def square(number):
    return number * number

def average(a, b, c):
    return (a + b + c) / 3

num = float(input("Enter a number to find its square: "))
print("Square:", square(num))

n1 = float(input("Enter first number: "))
n2 = float(input("Enter second number: "))
n3 = float(input("Enter third number: "))
print("Average:", average(n1, n2, n3))
