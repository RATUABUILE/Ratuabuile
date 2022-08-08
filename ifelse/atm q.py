print("welcome to atm machine")
language=input("enter the language") 
if language=="enlish" or "hindi":
    print("welcome to canara bank\swipe your card")
    balance=20000
    print("transaction:\n1.balance inquiry:\n2.withdrawal:\n3.deposit:\n4.transfer_money:\n5.exit")
    transaction=int(input("enter the transaction:")) 
    if transaction==1 or transaction==2 or transaction==3 or transaction==4:
        atm_pin=int(input("enter the pin"))
        if atm_pin==5656:
            if transaction==1:
               print("balance is",balance)  
            elif transaction==2:
               withdrawal_amount=int(input("enter the withdrawal_amount"))
               if withdrawal_amount<=balance:
                  total=balance-withdrawal_amount
                  print(total)   
                  print("collect your cash\.thank you") 
            elif transaction==3:
                deposit=int(input("enter the deposit_amount"))
                if deposit>0:
                    total=balance+deposit
                    print(total)  
                    print("your deposit successful\.thank you")
                else:
                    print("no deposit")
            elif transaction==4:
                transfer_money=int(input("enter the transfer_money")) 
                if transfer_money>0:
                    total=balance-transfer_money
                    print(total) 
                    print("your money has been transfer\.thank you")  
                else:
                    print("transfer failed") 
    elif transaction==5:
        exit=input("do you want to exit?:") 
        if exit=="yes":
            print("thank you for visiting")
        else:
            print("choose your transaction")
else:
    print("language does not exit")