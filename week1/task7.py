text = "Python Programming"
print("Original:", text)
print("Upper Case:", text.upper())
print("Lower Case:", text.lower())
print("Replace:", text.replace("Python", "Java"))
print("Find 'Programming':", text.find("Programming"))

fruits = ["Apple", "Banana", "Mango"]
print("\nOriginal List:", fruits)
fruits.append("Orange")
print("After Append:", fruits)
fruits.remove("Banana")
print("After Remove:", fruits)
fruits.sort()
print("After Sort:", fruits)

colors = ("Red", "Green", "Blue")
print("\nTuple:", colors)
print("First Element:", colors[0])
print("Last Element:", colors[-1])

student = {"name": "Vishal", "age": 25, "branch": "MCA"}
print("\nStudent Dictionary:", student)
print("Name:", student["name"])

numbers = {1, 2, 3, 4}
print("\nOriginal Set:", numbers)
numbers.add(5)
print("After Add:", numbers)
numbers.remove(2)
print("After Remove:", numbers)
