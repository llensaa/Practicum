class TrafficLight:
    
    permissible_values = ['зеленый', 'желтый', 'красный', 'желтый']
    
    def __init__(self):
        self.current_signal = 'зеленый'
        self.current_index = 0
    
    def next_signal(self):
        self.current_index = (self.current_index + 1) % len(self.permissible_values)
        self.current_signal = self.permissible_values[self.current_index]