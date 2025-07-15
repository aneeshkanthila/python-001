p=input("enter the password:")
lw=0
up=0
dig=0
sp=0
if(len(p)>7):
    for i in p:
        if(i.isupper()):
            up=up+1
        elif(i.islower()):
            lw=lw+1
        elif(i.isdigit()):
            dig=dig+1
        else:
            sp=sp+1
    if(up>0 and lw>0 and dig>0 and sp>0):
        print("good passs")
    else:
        print("bad pass")
else:
    print("bad pass bcz of less char")