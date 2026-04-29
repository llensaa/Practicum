class User:
    
    def __init__(self, id, nick_name, first_name, last_name='', middle_name='', gender=''):
        self.id = id
        self.nick_name = nick_name
        self.first_name = first_name
        self.last_name = last_name
        self.middle_name = middle_name
        self.gender = gender
    
    def update(self, id=None, nick_name=None, first_name=None, last_name=None, middle_name=None, gender=None):
        if id is not None:
            self.id = id
        if nick_name is not None:
            self.nick_name = nick_name
        if first_name is not None:
            self.first_name = first_name
        if last_name is not None:
            self.last_name = last_name
        if middle_name is not None:
            self.middle_name = middle_name
        if gender is not None:
            self.gender = gender
    
    def __str__(self):
        return f"User(id={self.id}, nick_name='{self.nick_name}', first_name='{self.first_name}')"