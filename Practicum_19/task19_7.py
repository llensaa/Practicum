class TrafficLight:
    """Класс, представляющий светофор."""
    
    permissible_values = ['зеленый', 'желтый', 'красный', 'желтый']
    
    def __init__(self):
        """Инициализация светофора. Начальный сигнал - зеленый."""
        self.current_signal = 'зеленый'
        self.current_index = 0
    
    def next_signal(self):
        """Переключает светофор на следующий сигнал."""
        self.current_index = (self.current_index + 1) % len(self.permissible_values)
        self.current_signal = self.permissible_values[self.current_index]
