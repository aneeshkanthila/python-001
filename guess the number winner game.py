import random
name1=input("enter player 1 :")
name2=input("enter player 2 :")
print("computer has fixed 5 nums in range of 1 to 10")
print("u guys guess it ....Ready??")

nums=[]
while(len(nums)!=5):
    d=random.randint(1,10)
    if(d not in nums):
        nums.append(d)
print("-------------------")

s1=0
s2=0
player1=[]
player2=[]

for i in range(3):
    print("-------ROUND {}--------".format(i-1))
    print("Dear {} guess your cahoice ".format(name1))
    ch=int(input())
    while(ch in player1 or ch in player2):
        ch=int(input("oops the number is already taken so take another number"))
    player1.append(ch)
    if(ch in nums):
        print("------>DEHMMMM CORECT :)")
        s1=s1+1
    else:
        print("---___WRONG___---")


    print("-------ROUND {}--------".format(i-1))
    print("Dear {} guess your cahoice ".format(name2))
    ch=int(input())
    while(ch in player1 or ch in player2):
        ch=int(input("oops the number is already taken so take another number"))
    player2.append(ch)
    if(ch in nums):
        print("------>DEHMMMM CORECT :)")
        s2=s2+1
    else:
        print("---___WRONG___---")

print("-------------------")
print("***LETS HAVE SUMMARY***")
print("COMPUTER HAS FIXED:",nums)

print("*********************")
print("{} has chosen {}".format(name1,player1))
print("{} score: {}".format(name1,s1))

print("*********************")

print("{} has chosen {}".format(name2,player2))
print("{} score: {}".format(name2,s2))

print("*********************")
if(s1>s2):
    print("{} is the winner".format(name1))
else:
    print("{} is the winner".format(name2))

        
        
        