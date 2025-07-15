l1=input("Enter1:")
l2=input("Enter2:")
a=l1.lower()
b=l2.lower()
a1="".join(i for i in a if i!=" ")
b1="".join(i for i in b if i!=" ")
a2=sorted(a1)
b2=sorted(b1)
if(a2==b2):
    print("anagram")
else:
    print("not anagram")
