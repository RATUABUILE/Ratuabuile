elements=[23,14,56,12,19,9,15,25,31,42,43]
sum=0
sum1=0
i=0
while i<len(elements):
    if elements[i]%2==0:
        sum=elements[i]+sum
    else:
        sum1=elements[i]+sum1
    i+=1
print("even sum =",sum)
print("odd sum =",sum1)