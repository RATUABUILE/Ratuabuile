element=[23,14,56,12,19,9,15,25,31,42,43]
i=0
sum=0
avg=0
while i<len(element):
    a=element[i]
    sum=sum+a
    avg=sum/a
    i+=1
print(sum)
print("avg=",avg)