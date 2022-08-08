n=[50,40,23,70,56,12,5,10,7]
i=0
while i<len(n):
    j=i+1
    while j<len(n):
        if n[i]>n[j]:
          n[i],n[j]=n[j],n[i]
        j+=1
    i+=1
print(n)