n=[2,3,4,6,7,8,8,7,9]
# o/p=[[2,3],[4,6],[7,8],[8,7]]
i=0
a=[]
while i<len(n):
    k=n[i:i+2]
    a.append(k)
    i+=2
k=a[0:4]
print(k)