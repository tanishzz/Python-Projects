persons = int(input("Total number of persons : "))
rent = int (input("House rent : "))
unit = int(input("Total units spends : "))
per_unit = int(input("Per unit rate : "))
groceries = int(input("Grocries bill : "))

electricitybill = unit * per_unit

total = (rent + electricitybill + groceries)/persons

print("Each person to pay : ", total)