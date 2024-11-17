class users:
    def __init__(self, name, surname, birthday, age, username, right, password):
        self.name = name
        self.surname = surname
        self.birthday = birthday
        self.age = age
        self.username = username 
        self.reght = right
        self.password = password
    
    def introduce(self):
        return f"I'm {self.name}, {self.age} years old."
