# num=[30,74,99,45,49,54,67]
# i=0
# a=0
# b=0
# while i<len(num):
#     if num[i]>b:
#         b=num[i]
#     if num[i]>a and num[i]!=b:
#         a=num[i]
#     i+=1
# print(b)

a=[[2,5,8,],[4,8,6],[59,2,46]]
b=[]
i=0
while i<len(a):
    if type(a[i])==type([]):
        j=0
        while j<len(a[i]):
            if type(a[i][j])==([]):
                b.append(a[i][j])
            else:
                b.append(a[i][j])
            j=j+1
    else:
        b.append(a[i])
    i=i+1
print(b)
