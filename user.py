class User:
    def __init__(self,login,password):
        self.login = login
        self.password = password

    def user_exists(self,password):
        if self.password == password:
            return True
        return False


