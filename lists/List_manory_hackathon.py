# l=["Python","Java","java","C","c","c++"]
# print(max(l))
# print(min(l)) 

a=[('a',1),('b',4),('z',7),('y',2),('i',5),('j',3),('o',6)]
i=0
while i<len(a):
    j=0
    while j<len(a):
        if a[i]<a[j]:
            a[i],a[j]=a[j],a[i]
        j+=1
    i+=1
print(a)