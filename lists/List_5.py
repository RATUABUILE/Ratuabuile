list=[3,"humpty",4,3,5,3]
i=0
count=0
while i<len(list):
    count+=1
    i+=1
list.pop(1)
j=0
s=0
while j<len(list):
    s=s+list[j]
    j+=1
print(count)
print(s)