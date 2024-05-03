#CADD FAST FOOD
qnt=()
bill=()
while True:
    print("Welcome to CADD FAST FOOD")
    print("1.IDLY    $80 rupees.")
    print("2.DOSA    $120 rupees.")
    print("3.SAMBAR  $50 rupees.")
    print("4.VADA    $80 rupees.")
    print("5.APPAM   $80 rupees.")
    print("6.PURI    $50 rupees.")
    print("7.PONGAL  $80 rupees.")
    print("8 EXIT")
    choice=int(input("ENTER YOUR CHOICE(1-8):"))
    
    if (choice == 1):
        
        qnt=int(input("ENTER THE QUANTITY: "))
        if (choice == 1):
          bill=80*qnt
          print("Your total bill is: ",bill)
        else:
          print("INVALID CHOICE")
    elif (choice == 2):
         qnt=int(input("ENTER THE QUANTITY: "))
         if (choice == 2):
             bill=120*qnt
             print("Your total bill is: ",bill)
         else:
            print("INVALID CHOICE")
    elif (choice == 3):
        qnt=int(input("ENTER THE QUANTITY: "))
        if (choice == 3):
          bill=50*qnt
          print("Your total bill is: ",bill)
        else:
          print("INALID CHOICE")
    elif (choice == 4):
        qnt=int(input("ENTER THE QUANTITY: "))
        if (choice == 4):
          bill=80*qnt
          print("Your total bill is: ",bill)
        else:
          print("INVALID CHOICE")
    elif (choice == 5):
        qnt=int(input("ENTER THE QUANTITY: "))
        if (choice == 5):
          bill=80*qnt
          print("Your total bill is: ",bill)
        else:
          print("INVALID CHOICE")
    elif (choice == 6):
        qnt=int(input("ENTER THE QUANTITY: "))
        if (choice == 6):
          bill=50*qnt
          print("Your total bill is: ",bill)
        else:
          print("INVALID CHOICE")
    elif (choice == 7):
         qnt=int(input("ENTER THE QUANTITY: "))
         if (choice == 7):
             bill=80*qnt
             print("Your total bill is: ",bill)
         else:
           print("INVALID CHOICE")
    elif (choice == 8):
        print("Thankyou for using CADD FAST FOOD. GOODBYE!!!")
        break