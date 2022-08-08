q=["what is the capital of india?"]
s=["1.Chandigarh","2.Bhopat","3.Chennai","4.Delhi"]
solution=[4]
i=0
j=0
while i<len(q) and j<len(s):
    print(q[i])
    k=0
    while k<(len(s)):
        print(s[k])
        k+=1
    sol=int(input("enter the number:"))
    if sol==solution[i]:
        print("congratulation! correct answer")
    else:
        print("better luck next time")
    print()
    i+=1
    j+=1