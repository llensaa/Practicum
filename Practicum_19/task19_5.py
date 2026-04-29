class Game:
    
    def __init__(self, teams):
        self.command1_name = teams['command1']
        self.command2_name = teams['command2']
        self.command1_score = 0
        self.command2_score = 0
    
    def ball_thrown(self, command, points):
        if command == 1:
            self.command1_score += points
        elif command == 2:
            self.command2_score += points
    
    def get_score(self):
        return (self.command1_score, self.command2_score)
    
    def get_winner(self):
        if self.command1_score > self.command2_score:
            return self.command1_name
        elif self.command2_score > self.command1_score:
            return self.command2_name
        else:
            return 'Ничья'