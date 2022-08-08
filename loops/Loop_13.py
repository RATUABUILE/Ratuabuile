guess=5
i=1
while i<=5:
    n=int(input("enter number"))
    if guess==n:
        print("right")
        break
    i=i+1
else:
    print("your chance is finished")