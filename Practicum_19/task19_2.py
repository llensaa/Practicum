class NotSleeping:
    
    def __init__(self, name, count_sheeps=0):
        self.name = name
        self.count_sheeps = count_sheeps
    
    def add_sheep(self):
        self.count_sheeps += 1