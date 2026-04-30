class User:
    """Класс, представляющий пользователя сайта."""
    
    def __init__(self, id, nick_name, first_name, last_name='', middle_name='', gender=''):
        """
        Инициализация пользователя.
        
        Параметры:
        id - уникальный номер пользователя (обязательный)
        nick_name - псевдоним пользователя (обязательный)
        first_name - имя пользователя (обязательный)
        last_name - фамилия (необязательный)
        middle_name - отчество (необязательный)
        gender - пол (необязательный)
        """
        self.id = id
        self.nick_name = nick_name
        self.first_name = first_name
        self.last_name = last_name
        self.middle_name = middle_name
        self.gender = gender
    
    def update(self, id=None, nick_name=None, first_name=None, last_name=None, middle_name=None, gender=None):
        """
        Обновляет атрибуты пользователя.
        Если параметр не передан, атрибут не изменяется.
        """
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
        """Строковое представление пользователя."""
        return f"User(id={self.id}, nick_name='{self.nick_name}', first_name='{self.first_name}')"
