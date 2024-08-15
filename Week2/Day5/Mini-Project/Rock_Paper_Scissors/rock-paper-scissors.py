'''
rock-paper-scissors.py – this will contain functions to show the main menu, 
handle user’s input, and show the game summary before exiting.
'''

import random
from game import Game

class Main:

    def __init__(self) -> None:
        print('Welcome to the game!')
        self.l_count = 0
        self.w_count = 0
    
    def menu(self):
        choice = Game.input_handler(
            prompt="""
1. Play a new game.
2. Show scores and exit.
                
Choose your option: """,
            desired_type=int,
            allowed_values=[1, 2]
        )
        return choice

    def game_ui(self):
        print('''
You are the first to make a move
Write one option: rock, paper, scissors''')

    def scores_ui(self):
        print(f"You've won {self.w_count} times and lost {self.l_count} times")
    
    def run(self):
        while True:
            choice = self.menu()
            if choice == 1:
                self.game_ui()
                m_player = Game.input_handler(
                    prompt='Write your move: ', 
                    desired_type=str,
                    allowed_values=['rock', 'paper', 'scissors']
                )
                m_pc = random.choice(['rock', 'paper', 'scissors'])
                print(f"Computer's move was {m_pc}")
                winner = Game.det_winner(m_pc, m_player)
                if winner == 'PC':
                    self.l_count += 1
                    print("You'd be better next time")
                elif winner == 'Player':
                    self.w_count += 1
                    print("Congratulations!")
                else:
                    print("It's a tie!")
            elif choice == 2:
                self.scores_ui()
                quit()

if __name__ == "__main__":
    game1 = Main()
    game1.run()
