number=30
n = [10, 11, 12, 13, 14, 17, 18, 19]
i=1
b=[]
while i<len(n):
    j=0
    while j<i:
        if n[j]+n[i]==number:
            c=n[j],n[i]
            b.append(c)
            b.sort()
        j+=1
    i+=1
print(b)