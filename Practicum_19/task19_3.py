class NotSleeping:
    """Класс, представляющий засыпающего человека, который считает овец."""
    
    def __init__(self, name, count_sheeps=0):
        """
        Инициализация человека.
        
        Параметры:
        name - имя человека
        count_sheeps - начальное количество овец (по умолчанию 0)
        """
        self.name = name
        self.count_sheeps = count_sheeps
    
    def add_sheep(self):
        """Добавляет одну овцу к счету."""
        self.count_sheeps += 1
    
    def lost(self):
        """Сбрасывает счет овец (человек сбился со счета)."""
        self.count_sheeps = 0
    
    def get_count_sheeps(self):
        """Возвращает текущее количество овец."""
        return self.count_sheeps
