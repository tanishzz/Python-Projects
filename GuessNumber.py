import random
number = random.randint(1,10)

ans = int(input("Guess the number between 1 to 10 : "))

if ans == number:
    print("YES!!, the number is ", number)
else:
    print("NOO, you guessed wrong")



