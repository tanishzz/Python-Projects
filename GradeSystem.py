Maths = int(input("Enter your marks in maths : "))
Science = int(input("Enter your marks in science : "))
English = int(input("Enter your marks in english : "))
Hindi = int(input("Enter your marks in hindi : "))

TotalMarks = Maths + Science + English + Hindi
print("Your total makrs is : ", TotalMarks)
Percentage = TotalMarks/4
print("Your percentage is : ", Percentage, "%")

if Percentage >= 70:
    print("Wow, A grade")

elif (Percentage < 70) & (Percentage > 33):
    print("Improve yourself, B grade")

elif (Percentage < 33):
    print("Fail, with C grade")