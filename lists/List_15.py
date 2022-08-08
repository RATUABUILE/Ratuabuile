a=9119
c=str(a)
i=0
while i<len(c):
    j=0
    while j<len(c[i]):
        b=int(c[i][j])**2
        print(b,end="")
        j+=1
    i+=1