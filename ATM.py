Bank_Accs={
    40101 : [21203,3223,"chandu@gmail.com","Chandu"],
    40120 : [202100,None,"wasim@gmail.com","Wasim"],
    40341 : [671901,7854,"amy@gmaiul.com","Amy"]
    }
print(Bank_Accs)
while True:
    print("Choose One Option: ")
    print("1. Withdraw")
    print("2. Deposit")
    print("3. Pin Genertaion")
    print("4. Mini Statement")
    print("5. Exit")
    n=int(input("Enter Your Choice: "))
    if n == 1:
        acc_num=int(input("Enter Your Account Number: "))
        if acc_num not in Bank_Accs:
            print("Invalid Account Number!")
        else:
            pin = int(input("Enter Your Pin: "))
            if pin != Bank_Accs[acc_num][1]:
                print("Invalid Pin!")
            else:
                amt = int(input("Enter Amount: "))
                if amt > Bank_Accs[acc_num][0]:
                    print("Insuffiecent Amount!")
                else:
                    Bank_Accs[acc_num][0] = Bank_Accs[acc_num][0] - amt
                    print("Withdraw Successfull!")
        
    elif n == 2:
        acc_num = int(input("Enter Your Account Number: "))
        if acc_num not in Bank_Accs:
            print("Invalid Account Number!")
        else:
            pin = int(input("Enter Your Pin: "))
            if pin != Bank_Accs[acc_num][1]:
                print("Invalid Pin!")
            else:
                amt = int(input("Enter Your Amount: "))
                Bank_Accs[acc_num][0] = Bank_Accs[acc_num][0] + amt
                print("Deposit Successfull!")
                      
    elif n == 3:
        acc_num=int(input("Enter Your Account Number: "))
        if acc_num not in Bank_Accs:
            print("Invalid Account Number!")
        else:
            if Bank_Accs[acc_num][1] is not None:
                print("Pin Already Generated")
            else:
                pin = int(input("Enter Pin:"))
                Bank_Accs[acc_num][1] = pin
                print("Pin Generated Successfully!")
    elif n == 4:
        acc_num = int(input("Enter Your Account Number: "))
        if acc_num not in Bank_Accs:
            print("Invalid Account Number!")
        else:
            pin = int(input("Enter Your Pin:"))
            if pin != Bank_Accs[acc_num][1]:
                print("Invalid Pin")
            else:
                print(f"Name : {Bank_Accs[acc_num][-1]}")
                print(f"Mail : {Bank_Accs[acc_num][-2]}")
                print(f"Balance : {Bank_Accs[acc_num][0]}")
                print("Thank You")
    elif n == 5:
        print("Thank You!")
        print("Visit again!")
          
