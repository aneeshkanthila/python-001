a=int(input("enter num1:"))
b=int(input("enter num2:"))
c=int(input("enter num3:"))

if(a>=b and a<=c):
    print("second greatest is :",a)
elif(b>=a and b<=c):
    print("second greatest is :",b)
else:
    print("second greatest is :",c)