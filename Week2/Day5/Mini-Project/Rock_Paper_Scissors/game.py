'''
game.py – this will contain a Game class which will have functions to play 
a single game of rock-paper-scissors against the computer, determine the game’s result, and return the result.

'''

class Game:
    def __init__(self) -> None:
        pass

    @staticmethod
    def det_winner(m_pc, m_player):
        if m_pc == 'rock':
            if m_player == 'rock':
                return 'Tie'
            elif m_player == 'paper':
                return 'Player'
            elif m_player == 'scissors':
                return 'PC'
        elif m_pc == 'paper':
            if m_player == 'rock':
                return 'PC'
            elif m_player == 'paper':
                return 'Tie'
            elif m_player == 'scissors':
                return 'Player'
        elif m_pc == 'scissors':
            if m_player == 'rock':
                return 'Player'
            elif m_player == 'paper':
                return 'PC'
            elif m_player == 'scissors':
                return 'Tie'

    @staticmethod        
    def input_handler(prompt, desired_type, allowed_values=None):
        while True:
            inp = input(prompt)
            try:
                # Attempt to convert the input to the desired type
                inp = desired_type(inp)
                
                # If allowed_values is provided, check if the input is in the allowed values
                if allowed_values and inp not in allowed_values:
                    print(f"Input must be one of the following: {allowed_values}")
                    continue
                
                # If the input is valid, return it
                return inp
            
            except ValueError:
                print(f"Input must be of type {desired_type.__name__}")
