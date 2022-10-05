from player import HumanPlayer, RandomComputerPlayer
class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)] #a single list to represent 3 x 3 board
        self.current_winner = None # keep track of the winner

    def print_board(self):
        # getting the rows
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')

    @staticmethod
    def print_board_nums():
        # 0 | 1 | 2 | What number corresbond to what box
        number_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        for row in number_board:
            print('| ' + ' | '.join(row) + ' |')

    def available_moves(self):
        # returns a list of the empty spots
        return [i for i, spot in enumerate(self.board) if spot == ' ']

    def empty_squares(self):
        return ' ' in self.board

    def num_empty_squares(self):
        return self.board.count(' ')

    def make_move(self, square, letter):
        # if valid move, assing the letter to the square
        # then return true if invalid return false
        if self.board[square] == ' ':
            self.board[square] = letter
            # Checking for the winner
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        else:
            return False

    def winner(self, square, letter):
        # check the rows
        row_ind = square // 3
        row = self.board[row_ind*3 : (row_ind + 1)*3]
        if all([spot == letter for spot in row]):
            return True

        # check column
        col_ind = square % 3
        column = [self.board[col_ind + i*3] for i in range(3)]
        if all([spot == letter for spot in column]):
            return True

        # check diagonals
        # if the square is even number 
        if square % 2 ==0:

            diagonal1 = [self.board[i] for i in [0, 4, 8]] #left to right diagnoal
            if all([spot == letter for spot in diagonal1]):
                return True

            diagonal2 = [self.board[i] for i in [2, 4, 6]] #right to left diagnoal
            if all([spot == letter for spot in diagonal2]):
                return True

        # return false if there is no winner
        return False


def play(game, x_player, o_player, print_game = True):
    # returns the winner(letter) of the game or None for a tie

    if print_game:
        game.print_board_nums()
    
    letter = 'X' #starting letter
    # iterate while there are empty squares
    while game.empty_squares():
        # get the move from the appropriate player
        if letter == 'O':
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)
        # call the function that makes the move
        if game.make_move(square, letter):

            if print_game:
                print(letter + f' make a move to square {square}')
                game.print_board() # the board after the move
                print('') # an empty line

            if game.current_winner:
                if print_game:
                    print(letter + ' wins!')
                return letter

            # alternate letters after making a move
            if letter == 'X':
                letter = 'O'
            else:
                letter = 'X'
    
    # In case there is no winner
    if print_game:
        print('It\'s a tie')

if __name__ == '__main__':
    x_player = HumanPlayer('X')
    o_player = RandomComputerPlayer('O')
    t = TicTacToe()
    play(t, x_player, o_player, print_game=True)