class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)] #a single list to represent 3 x 3 board
        self.current_winner = None # keep track of the winner

    def print_board(self):
        # getting the rows
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')

game1 = TicTacToe()

print(game1.print_board())