import hashlib
import getpass

password_manager = {}

def create_account():
    account_name = input("\nEnter the account name or account type: ")
    username = input("Enter your desired username: ")
    password = getpass.getpass("Enter your desired password: ")
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    password_manager[username] = hashed_password
    print("Account created successfully!")


def login():
    account_name = input("Enter the account name or type which the credentials belong to: ")
    username = input("Enter your username: ")
    password = getpass.getpass("Enter your password: ")
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    if username in password_manager.keys() and password_manager[username] == hashed_password:
        print("Login Successful!")   
    else:
        print("Invalid Password or Username.")

def main():
    while True:
        choice = input("Press 1 to create account, Press 2 to login to the account, Press 0 to exit: ")
        if choice == "1":
            create_account()
        elif choice == "2":
                login()
        elif choice == "0":
             break
        else:
             print("Invalid Choice. ")

if __name__ == "__main__":
     main()
