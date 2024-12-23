class UserAccount:
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password

    def set_password(self, new_password):
        self.password = new_password

    def check_password(self, password):
        return self.password == password


user = UserAccount("user1", "user1@gmail.com", "qwerty123")
user.set_password("password")
print(user.check_password("qwerty123"))
print(user.check_password("password"))