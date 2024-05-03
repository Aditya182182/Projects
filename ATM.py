pin = 1212
balance = 100000
amount = 0

def check_balance(balance):
    pin_input = int(input("Enter your Pin:"))
    if pin_input == pin:
        print("Your Balance is:", balance)
    else:
        print("Invalid pin")

def withdraw_money(balance, amount):
    pin_input = int(input("Enter your Pin:"))
    if pin_input == pin:
        if amount <= balance:
            print("Withdrawal successful:", amount)
            balance -= amount
        else:
            print("Insufficient funds!")
    else:
        print("Invalid pin")
    return balance

def deposit_money(balance, amount):
    pin_input = int(input("Enter your pin:"))
    if pin_input == pin:
        balance += amount
        print("Deposit successful.")
    else:
        print("Invalid pin.")
    return balance

while True:
    print("Welcome to CADD ATM!")
    print("1. Check Balance")
    print("2. Withdraw Money")
    print("3. Deposit Money")
    print("4. Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        check_balance(balance)
    elif choice == '2':
        amount = float(input("Enter the amount to withdraw: $"))
        balance = withdraw_money(balance, amount)
    elif choice == '3':
        amount = float(input("Enter the amount to deposit: $"))
        balance = deposit_money(balance, amount)
    elif choice == '4':
        print("Thank you for using CADD ATM.")
        break
    else:
        print("Invalid choice.")

print("Final balance:", balance)