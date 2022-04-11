import random

class RockPaperScissor():
    MAX_POINTS = 5
    is_inprogress = False
    def __init__(self, playerName: str, max_points: int = MAX_POINTS):
        self.is_inprogress = True
        self.MAX_POINTS = max_points
        self.playerName = playerName
        self.score = 0
        self.computerScore = 0

    def print_user_question(self):
        return '''Choose one from below(1-3):
    1) Rock
    2) Paper
    3) Scissor
    '''

    def play_computer(self):
        random_value = random.randint(0,3)
        return self.get_entity_by_number(random_value)

    def get_entity_by_number(self, val: int):
        if val == 0:
            return 'Rock'
        elif val == 1:
            return 'Paper'
        else:
            return 'Scissor'
    
    def calculate(self, userIp: str, computerIp: str):
        if (userIp == 'Rock' and computerIp == 'Paper' 
            or userIp == 'Paper' and computerIp == 'Scissor' 
            or userIp == 'Scissor' and computerIp == 'Rock'):
            self.computerScore += 1
        elif (userIp == 'Rock' and computerIp == 'Scissor' 
              or userIp == 'Paper' and computerIp == 'Rock'
              or userIp == 'Scissor' and computerIp == 'Paper'):
            self.score += 1
        if self.computerScore == self.MAX_POINTS or self.score == self.MAX_POINTS:
            self.is_inprogress = False
    
    @classmethod
    def initialize(cls, name: str, max_points: int):
        return RockPaperScissor(name, max_points)


game = RockPaperScissor.initialize('Navadeep', 3)
print(game.print_user_question())
while game.is_inprogress:
    print(f"Player Score: {game.score}, Computer Score: {game.computerScore}")
    try:
        selected = int(input("Enter your selecting: "))
        if selected > 0 and selected < 4:
            user_opt = game.get_entity_by_number(selected - 1)
            comp_opt = game.play_computer()
            print(f"User Turn: {user_opt}")
            print(f"Computer Turn: {comp_opt}")
            game.calculate(user_opt, comp_opt)
        else:
            raise Exception("Invalid Input, value should be between (1-3)")
    except Exception as e:
        print(e)

if game.score > game.computerScore:
    print('Player is the winner')
else:
    print('Better luck next time')
