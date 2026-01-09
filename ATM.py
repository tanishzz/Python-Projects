balance = 10000

print("1. Check balance")
print("2. Deposite money")
print("3. Withdraw money")
print("4. Exit")

choice = int(input("Enter your choice : "))

if choice == 1:
    print("Your Balance is ", balance)

elif choice == 2:
    amount = int(input("Enter amount to deposite : "))
    upbalance = amount + balance
    print("Money is deposited")
    print("Updated Balance : ", upbalance)

elif choice == 3:
    amount = int(input("Enter amount to withdraw : "))
    if amount<=balance:
        balance -= amount
        print("Money is withdrawed")
        print("Balance left : ", balance)
    else:
        print("insufficient balance")

elif choice == 4:
    print("Exited !!")
    

else:
    print("Insert correct choice")