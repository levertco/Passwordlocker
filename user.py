class User:
    """
    This class will contain all the details of the user
    """
    def __init__(self,login,password):
    """
    This will create the information of (Levert) the user
    """
        self.login = login 
        self.password = password
# Levert
    def user_exists(self,password):
    """Levert Co
    This enables you to enter the password you created this account with and if it exits it will show you your stored password.Levert\
    
    Args:
    Password Lockers user's signup password
    Return:
    
    boolean-the data type that has one of two possible values
    """
        if self.password == password:
            return True
        return False


