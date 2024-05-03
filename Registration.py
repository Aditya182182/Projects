#CADD REGISTRATION
#f=open("registration.txt","x")
print("File is created")
def main():
    print("1.Registration.")
    print("2.Login.")
main()

def registration():
    choice=int(input("Enter your choice(1-2): "))
    if(choice==1):
        name=(input("Enter User Name: "))
        password=input("Enter Password: ")
        cpassword=input("Confirm Password: ")
        if(cpassword==password):
            f = open("registration.txt","w")
            f.write(name)
            f.write(password)
            print("Successfully Registered.")
            print("Please Login")
            f.close()
    else:
        print("Invalid Choice")
        print("Invalid Password")
registration()

def login():
    choice=int(input("Enter your choice(1-2): "))
    if(choice==2):
        name=(input("Enter User Name: "))
        password=(input("Enter Password: "))
        f=open("registration.txt","r")
        
        a=f.read()
        if (name)and(password)in a:
            print("Successfully Login.")
            print(a)
        else:
            print("Invalid Choice")
            print("Login Failed")
login()  