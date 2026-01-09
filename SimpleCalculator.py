a = int(input("Enter first number : "))
b = int(input("Enter second number : "))

print("1. Add")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

choice = int(input("Enter your choise : "))

if choice == 1:
    print("result", a+b)

if choice == 2:
    print("result", a-b)

if choice == 3:
    print("result", a*b)

if choice == 4:
    print("result", a/b)