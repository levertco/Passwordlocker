
from password import Password
# import levert
from user import User
# import Levert
import getpass
  
def new_user(login,password):
    """
    This will create a new user everytime they login
    """
    return User(login,password)
def add_password(account,username,password):
    """
    This function add's a new password to the passwords list
    """
    new_pass = Password(account,username,password)
    new_pass.save_pass()   
def generate_password(length):# genarate Levert
    """
    This will create a random password for the user
    Args:
        length - user's preferred length for the password
    Return:
        It will return a random password containing the specified preferred length
    """
    return Password.generate_pass(length)
def view_passwords():
    """
    This function enables the user(Levert) to view all the passwords
    """
    return Password.display_passwords()
def delete_password(acc):#levert
    """
    This function delete's the password
    Args:
        acc - the password of the account the user wants to delete
    """
    Password.delete_password(acc)
def password_exists(acc):
    return Password.password_exist(acc)
def main():                                                                                   
    print("WELCOME TO LEVERT'S PASSWORD LOCKER\n")
    print("Sign up/create your new password locker account.","\n")
    print("NB:Dont froget your password locker account credentials cause it will be needed to help you retreive passwords from your password locker app.","\n")
    user_name = input("User Name\n")
    user_pass = getpass.getpass('Password:\n')
    new_user(user_name,user_pass)
    print(f"Welcome {user_name}\n")
    print("What would you like to do?\n")
#Levert
    while True:
        command = input("Input 'generate' to  generate a password, 'add' to add an existing password, 'del' to delete a password, 'view' to view all your passwords, 'exit' to leave :( \n")
        if command == "add":
            print("Key in your new passwords\n")
            acc = input("The password is to be used on which platform?\n")
            u_name = input("What is your username?\n")
            password = getpass.getpass("What is your password?\n")

            add_password(acc,u_name,password)

            print(f"New password for {acc} added\n")
        elif command == "generate":
            print("I will help you genearate a password for your account.")
            acc = input("What is the name of the platform on which the password wil be used?\n")
            u_name = input("What is your account username?\n")
            length = input("Input the length of the password to be generated\n")
            try:     
                add_password(acc,u_name,generate_password(int(length)))
                print(f"Password for {acc} generated\n")
            except ValueError:
                print("Use numbers only\n")
        elif command == "del":
            print("Oh no!:(\n")
            pass_word = getpass.getpass("Enter your password?\n")
            if pass_word == user_pass:
                acc= input("Which account would you like to delete its password?\n")
                if password_exists(acc):
                    delete_password(acc)
                    print(f"{acc} password deleted\n")
                else:
                    print("Password does not exist\n")
            else:
                print("\nWrong password.Please try Again\n")
        elif command == "view":
            pass_word = getpass.getpass("Enter your password?\n")
            if pass_word == user_pass:
                if view_passwords():#levert
                    for password in view_passwords():
                        print("-"*6,view_passwords().index(password)+1,"-"*6,"\n")
                        print(f"Account --> {password.account}\n")
                        print(f"Username --> {password.username}\n")
                        print(f"Password --> {password.password}\n")
                else:
                    print("No passwords stored\n")
            else:
                print("Access denied!! Wrong password. You cannot view your saved passwords.Please try again\n")
if __name__ == "__main__":
    main()
    
 