n=[19,17,12,17,17,18,10,17,14,12,19,17,12,13]
i=0
a=[]
b=[]
count=0
while i<len(n):
    if n[i] not in a:
        a.append(n[i])
    else:
        if n[i] not in b:
            b.append(n[i])
    i=i+1
print(b)