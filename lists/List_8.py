number=30
list =[13,17,15,15,12,11]
i=1
b=[]
while i<len(list):
    j=0
    a=[]
    while j<i:
        if list[j]+list[i]==number:
            b.append(list[i])
            b.append(list[j])
        j+=1
    i+=1
print(b)