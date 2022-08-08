list1=[1,[2],4,[3,9],[8],5,8,[2,[1]]]
i=0
while i<len(list1):
    if type(list1[i])==list:
        j=0
        while j<len(list1[i]):
            print(i,j,list1[i][j]) 
            j+=1
        i+=1
    else:
        print(i,list1[i])    
        i+=1   