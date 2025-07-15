a=int(input("num1:"))
b=int(input("num2:"))
if(a>b):
    big=a
else:
    big=b
step=big
while True:
    if(big%a==0 and big%b==0):
        print("lcm is:",big)
        break
    else:
        big=big+step