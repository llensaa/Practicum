class Dog:
    
    def __init__(self, name):
        self.name = name
    
    def say(self):
        print("Гав!")
    
    def __str__(self):
        return f"Собака по кличке {self.name}"
