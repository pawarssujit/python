#if,else ,elif ladder in python
M1=int(input("Enter your marks 1="))
M2=int(input("Enter your marks 2="))
M3=int(input("Enter your marks 3="))
total= M1+M2+M3
per= total/3
print("total=",per)
if per>70:
    print("DISTINCTION")
elif per>60:
    print("first class")
elif per>50:
    print("2nd class")
elif per>40:
    print("pass class")
else:
    print("FAIL")


#multiple if statements
a= 8
if a<3:
    print("The value of a is greater than 3")
if a>13:
    print("The value of a is greater than 13")
if a>7:
    print("The value of a is greater than 7")
if a>17:
    print("The value of a is greater than 17")
else:
    print("The value is not greater than 3 or 7")


