user=int(input("enter the number:"))
i=1
x="0"
while user>0:
    r1=user%10
    user//=10
    r2=user%10
    user//=10
    r3=user%10
    user//=10
    i+=1
print(str(r3)+x*3,"+",str(r2)+x*2,"+",str(r1))