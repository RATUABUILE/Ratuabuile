# numbers=[50,40,23,70,56,12,5,10,7]
# for i in numbers:
#     if i>=20 and i<=40:
#         print(i)

# between 20 and 40:
numbers=[50,40,23,70,56,12,5,10,7]
i=0
count=0
while i<len(numbers):
    if numbers[i]>=20 and numbers[i]<=40:
        count=count+1
    i+=1
print(count)