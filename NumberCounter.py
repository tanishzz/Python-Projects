pos = 0
neg = 0
zero = 0

num = int(input("How many numbers do you want to count : "))

for n in range(num):
    number = int(input("Enter your number : "))

    if number > 0:
        pos += 1
        
    elif number < 0:
        neg += 1
    
    elif number == 0:
        zero += 1

print(f"Positive number : {pos}")
print (f"Negative number : {neg}")
print(f"Zero : {zero}")