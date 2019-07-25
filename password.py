from random import randint
#class Levert
class Password:
   """
    This is the (Levert) class which we will use to create the passwords
   """
    passwords = []
    # This stores all the user's passwords
    def __init__(self,account,username,password):
        self.account = account
        self.username = username
        self.password = password
    def save_pass(self):
      """
        This is a function that will add the Levert password locker user's password into the passwords array
      """
        Password.passwords.append(self)
    def generate_pass(length):
      """
        This function generates Levert password locker app passwords
      """
        items = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","1","2","4","5","7","8","9","0","_","-",]
        new_pass = ""
        while(len(new_pass) < length):
            item = items[randint(0,len(items) -1)]
            new_pass += item
        return new_pass
    @classmethod#levert
      """
        This function shows all the passwords stored
      """
    def display_passwords(cls):
        return cls.passwords    
    @classmethod
      """
        This function will withdraw all the passwords stored
      """
    def delete_password(cls,account):
        for password in cls.passwords:
            if password.account.lower() == account.lower():
                cls.passwords.remove(password)    
    @classmethod
      """
        This function will check whether theres such a password stored Levert
      """
    def password_exist(cls,acc):
        for password in cls.passwords:
            if password.account.lower() == acc.lower():
                return True
        return False

