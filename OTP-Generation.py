#OTP GENERATION.


import random

def random_four():
    name=input("Enter your name: ")
    random_four = random.randint(999, 9999)
    f=open("OTP4-6.txt","w")
    f.write(name)
    f.write(str(random_four))
    print("4 digit OTP:", random_four)

def random_six():
    name=input("Enter your name: ")
    random_six=random.randint(99999,999999)
    f=open("OTP4-6.txt","w")
    f.write(name)
    f.write(str(random_six))
    print("6 digit OTP: ",random_six)

def main():
    while True:
        print("Welcome to OTP Generating Machine.")
        print("1. 4 digit Otp.")
        print("2. 6 digit Otp.")
        print("3. Exit.")
        
        choice= input("Enter your choice: ")
        
        if choice == '1':
            random_four()
        elif choice == '2':
            random_six()
        elif choice == '3':
            print("Thankyou for using OTP Generating Machine.Goodbye!")
            break 
        else:
            print("Invalid choice. Please enter a valid number.")
main() 