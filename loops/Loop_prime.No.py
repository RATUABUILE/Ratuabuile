n=int(input("enter the number"))
i=2
while i<=n:
    j=1
    count=0
    while j<=n:
        if i%j==0:
            count=count+1
        j=j+1
    if count==2:
        print(i,"prime")
    i=i+1