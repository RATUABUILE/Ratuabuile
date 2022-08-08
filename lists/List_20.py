n=[1,2,3,4,5,6,7,8,9,10]
i=0
even=0
odd=0
while i<len(n):
    if n[i]%2==0:
        even+=1
    else:
        odd+=1
    i+=1
print("the count of even is=",even)
print("the count of odd is=",odd)