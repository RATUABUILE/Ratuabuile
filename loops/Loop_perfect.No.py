num=int(input("enter the number"))
i=1
sum=0
while i<num:
    if(num%i==0):
        sum=sum+i
    i+=1
if(sum==num):
    print("%d perfect no"%num)
else:
    print("%d not a perfect no"%num)