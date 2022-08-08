question= [
"How many continents are there?","What is the capital of India?","NG mei kaun se course padhaya jaata hai?"
]
option = [
["Four", "Nine", "Seven", "Eight"], 
["Chandigarh", "Bhopal", "Chennai", "Delhi"],
["Software Engineering", "Counseling", "Tourism", "Agriculture"]
]
solution= [3, 4, 1]
i=0
while i<len(question):
    print("Q",i+1,question[i])
    j=0
    while j<(len(option)+1):
        print(j+1,option[i][j])
        j+=1
    k=0
    sol=int(input("choose your choice:"))
    if sol==solution[i]:
        print("yes, you have choose the right answer:",sol)
    else:
        print("wrong")
        print("sorry, you are out of the game. restart the game.")
        break
    print()
    i+=1
    k+=1