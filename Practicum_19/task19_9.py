class StrandsDNA:
    """Класс, хранящий цепочки ДНК."""
    
    def __init__(self):
        """Инициализация пустого списка цепочек."""
        self.all_strands = []
    
    def add_strands(self, strands):
        """
        Добавляет цепочки ДНК.
        
        Параметры:
        strands - строка с цепочками через пробел
        """
        new_strands = strands.split()
        for s in new_strands:
            self.all_strands.append(s)
    
    def get_max_strands(self):
        """
        Возвращает строку с уникальными цепочками максимальной длины.
        Цепочки отсортированы в алфавитном порядке.
        """
        if not self.all_strands:
            return ''
        
        # Находим максимальную длину
        max_len = max(len(s) for s in self.all_strands)
        
        # Отбираем цепочки максимальной длины
        max_strands = [s for s in self.all_strands if len(s) == max_len]
        
        # Убираем дубликаты и сортируем
        unique_strands = sorted(set(max_strands))
        
        # Возвращаем строку
        return ' '.join(unique_strands)
    
    def __str__(self):
        """Строковое представление объекта."""
        return f"StrandsDNA({self.all_strands})"
