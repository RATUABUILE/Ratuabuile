# Q_6.count of positive/sum of negative:
a=[0,2,3,0,5,6,7,8,9,10,-11,-12,-13,-14]
i=0
pos=0
neg=0
sum=0
count=0
b=[]
while i<len(a):
    if a[i]>0:
        pos+=1
        count=count+1
    elif a[i]<0:
        neg+=1
        sum=sum+a[i]
    else:
        pass
    i+=1
b.append(pos)
b.append(sum)
print(b)