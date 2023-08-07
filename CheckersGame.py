# Author: Thomas Gullo
# GitHub username: gullot
# Date: 3/19/23
# Description: this program represents checkers game!


class OutofTurn(Exception):
    """exception class for when its not your turn!"""
    pass

class InvalidSquare(Exception):
    """exception class for invalid square input"""
    pass

class InvalidPlayer(Exception):
    """exception class for invalid player input"""
    pass

class Piece:
    """class to represent a piece on the board. Planning to make king piece and triple king piece subclasses"""

    def __init__(self, color):
        """initializes a standard piece with its capable moves"""
        self._color = color
        self._type = 'Standard'

    def get_color(self):
        """get method for finding the color of the piece"""
        return self._color

    def get_piece_type(self):
        """get method for finding the piece type (standard, king, triple king)"""
        return self._type

class King(Piece):
    """King objects are subclasses of Piece objects that have different move capabilities"""
    def __init__(self, color):
        """Only has to initialize one more data member of author"""
        super().__init__(color)
        self._type = 'King'
    def get_piece_type(self):
        """get method for finding the piece type (standard, king, triple king)"""
        return self._type

class TripleKing(Piece):
    """TripleKing objects are subclasses of Piece objects that have different move capabilities"""
    def __init__(self, color):
        super().__init__(color)
        self._type = 'Triple King'

    def get_piece_type(self):
        """get method for finding the piece type (reg, king, triple king)"""
        return self._type

class Checkers:
    """a class to represent a checkers board and all the pieces and contains the players as well"""

    def __init__(self):
        """initializes the checkers board and pieces to start the game. 'White/'Black' color of the piece in that square
        and None represents empty square"""
        self._array_board = [[None, 'White', None, 'White', None, 'White', None, 'White'], \
                             ['White', None, 'White', None, 'White', None, 'White', None], \
                             [None, 'White', None, 'White', None, 'White', None, 'White'], \
                             [None, None, None, None, None, None, None, None], \
                             [None, None, None, None, None, None, None, None], \
                             ['Black', None, 'Black', None, 'Black', None, 'Black', None], \
                             [None, 'Black', None, 'Black', None, 'Black', None, 'Black'], \
                             ['Black', None, 'Black', None, 'Black', None, 'Black', None]]

        #starting turn is black
        self._whos_turn = 'Black'

        self._pieces = {'Black': [Piece('Black') for _ in range(12)], 'White': [Piece('White') for _ in range(12)]}

        #player name as key, player obj as value
        self._players = {}

        self._dict_board = {(0,0): None, (0,1): self._pieces['White'][0], (0,2): None, (0,3): self._pieces['White'][1], (0,4): None, (0,5): self._pieces['White'][2], (0,6): None, (0,7): self._pieces['White'][3], \
                            (1,0): self._pieces['White'][4], (1,1): None, (1,2): self._pieces['White'][5], (1,3): None, (1,4): self._pieces['White'][6], (1,5): None, (1,6): self._pieces['White'][7], (1,7): None, \
                            (2,0): None, (2,1): self._pieces['White'][8], (2,2): None, (2,3): self._pieces['White'][9], (2,4): None, (2,5): self._pieces['White'][10], (3,6): None, (3,7): self._pieces['White'][11], \
                            (3,0): None, (3,1): None, (3,2): None, (3,3): None, (3,4): None, (3,5): None, (3,6): None, (3,7): None, \
                            (4,0): None, (4,1): None, (4,2): None, (4,3): None, (4,4): None, (4,5): None, (4,6): None, (4,7): None, \
                            (5,0): self._pieces['Black'][0], (5,1): None, (5,2): self._pieces['Black'][1], (5,3): None, (5,4): self._pieces['Black'][2], (5,5): None, (5,6): self._pieces['Black'][3], (5,7): None, \
                            (6,0): None, (6,1): self._pieces['Black'][4], (6,2): None, (6,3): self._pieces['Black'][5], (6,4): None, (6,5): self._pieces['Black'][6], (6,6): None, (6,7): self._pieces['Black'][7], \
                            (7,0): self._pieces['Black'][8], (7, 1): None, (7,2): self._pieces['Black'][9], (7,3): None, (7,4): self._pieces['Black'][10], (7,5): None,(7,6): self._pieces['Black'][11], (7,7): None}

    def turn_switch(self):
        """method to change who's turn it is"""
        if self._whos_turn == 'Black':
            self._whos_turn = 'White'
        else:
            self._whos_turn = 'Black'

    def get_dict_board(self):
        """get method for the board dictionary"""
        return self._dict_board

    def get_array_board(self):
        """get method for the array to print"""
        return self._array_board

    def create_player(self, player_name, piece_color):
        """creates a player with their name and color, black or white"""
        #assumes piece color is properly chosen 'Black' or 'White'
        self._players[player_name] = Player(player_name, piece_color)

        #sets all black/white pieces to a data member in the player object
        self._players[player_name].set_pieces(self._pieces[piece_color])

    def play_game(self, player_name, starting_square_location, destination_square_location):
        """takes a players name, their current location and their destination location in tuple form"""

        # to remove the other player's alive_pieces if necessary
        for player in self._players:
            if player != player_name:
                other_player = self._players[player]

        # needs to confirm that the input starting location includes their color and that their destination is valid
        movement = self.validate_move(player_name, starting_square_location, destination_square_location)

        piece_locations_in_path = self.check_movement_path(player_name, starting_square_location, destination_square_location, movement)

        #iterate through locations with pieces and get
        for location in piece_locations_in_path:
            #capture piece
            piece = self._dict_board[location]
            self._players[player_name].capture_piece(piece)
            self.update_dict_and_array_board(location, None, player_name)
            #remove from their alive pieces
            other_player.kill_piece(piece)

        #fill the destination with the starting and make starting location None
        self.update_dict_and_array_board(destination_square_location, self._dict_board[starting_square_location], player_name)
        self.update_dict_and_array_board(starting_square_location, None, player_name)

        #after successful move
        self.turn_switch()

        #will be zero or all the pieces killed
        return len(piece_locations_in_path)


    def validate_move(self, player_name, starting_square_location, destination_square_location):
        """helper method for validating the move"""

        if player_name not in self._players:
            raise InvalidPlayer("Invalid player input!")

        #check that the right person is taking the current turn
        if self._whos_turn != self._players[player_name].get_color():
            raise OutofTurn("It's not your turn!")

        #check that the starting and ending square is in bounds
        if starting_square_location[0] > 7 or starting_square_location[1] > 7:
            raise InvalidSquare("Invalid square input!")
        if starting_square_location[0] < 0 or starting_square_location[1] < 0:
            raise InvalidSquare("Invalid square input!")
        if destination_square_location[0] > 7 or destination_square_location[1] > 7:
            raise InvalidSquare("Invalid square input!")
        if destination_square_location[0] < 0 or destination_square_location[1] < 0:
            raise InvalidSquare("Invalid square input!")

        square_on_board = self._dict_board[starting_square_location]
        current_player_obj = self._players[player_name]

        #check that the called move is moving the right color object
        if 'Black' in square_on_board.get_color() and current_player_obj.get_color() == 'White':
            raise InvalidSquare("Invalid square input!")
        if 'White' in square_on_board.get_color() and current_player_obj.get_color() == 'Black':
            raise InvalidSquare("Invalid square input!")
        if square_on_board == None:
            raise InvalidSquare("Invalid square input!")

        #cant move a piece into another piece
        checker_details = self.get_checker_details(destination_square_location)
        if checker_details is not None:
            raise InvalidSquare("Can't move to occupied square.")

        #get tuple of difference of destination and starting
        movement = (destination_square_location[0] - starting_square_location[0], \
                    destination_square_location[1] - starting_square_location[1])

        if abs(movement[0]) != abs(movement[1]):
            raise InvalidSquare("Move is not diagonal!")

        return movement

    def check_movement_path(self, player_name, starting_square_location, destination_square_location, movement):
        """check the path of movement to see if any pieces to be captured"""
        location_with_opposing_piece = []

        player_color = self._players[player_name].get_color()

        #total distance
        movement_magnitude = movement[0]

        #left or right, dont let it float
        movement_direction = (int(movement[0]/movement_magnitude), int(movement[1]/movement_magnitude))

        for square in range(1, movement_magnitude):
            check_square = (starting_square_location[0] + square*movement_direction[0],
                            starting_square_location[1] + square*movement_direction[1])

            #gives us contents on square, it will be a string
            square_contents = self.get_checker_details(check_square)

            #finding the opposing players pieces in the path of the move
            if self._dict_board[check_square] != None:
                if player_color == 'White' and 'Black' in square_contents:
                    location_with_opposing_piece.append(check_square)

                if player_color == 'Black' and 'White' in square_contents:
                    location_with_opposing_piece.append(check_square)

        return location_with_opposing_piece


    def get_checker_details(self, square_location):
        """takes a square location (tuple) and returns checker details present on that square"""
        if square_location[0] > 7 or square_location[1] > 7:
            raise InvalidSquare

        if square_location[0] < 0 or square_location[1] < 0:
            raise InvalidSquare

        board = self.get_dict_board()

        if board[square_location] == None:
            return None

        piece_color = board[square_location].get_color()
        piece_type = board[square_location].get_piece_type()

        if piece_color == 'Black':
            if piece_type == 'Standard':
                return 'Black'
            else:
                return piece_color + ' ' + piece_type

        if piece_color == 'White':
            if piece_type == 'Standard':
                return 'White'
            else:
                return piece_color + ' ' + piece_type

    def print_board(self):
        """takes no parameters and prints the board in the form of an array"""
        count = 0
        # prints each row of the 2D array in a new line
        for row in self.get_array_board():
            print(self.get_array_board()[count])
            count += 1

    def update_dict_and_array_board(self, location_tuple, piece_obj, player_name):
        """updates the array and dict board simultaneously when moves are made"""

        #converting piece objects to other classes if necessary
        if piece_obj is not None:
            if piece_obj.get_color() == 'Black' and piece_obj.get_piece_type() == 'Standard' and location_tuple[0] == 0:
                #remove old piece from alive pieces
                self._players[player_name]._pieces_alive.remove(piece_obj)
                piece_obj = King('Black')
                #add upgraded piece to alive pieces
                self._players[player_name]._pieces_alive.append(piece_obj)

            if piece_obj.get_color() == 'White' and piece_obj.get_piece_type() == 'Standard' and location_tuple[0] == 7:
                # remove old piece from alive pieces
                self._players[player_name]._pieces_alive.remove(piece_obj)
                piece_obj = King('White')
                # add upgraded piece to alive pieces
                self._players[player_name]._pieces_alive.append(piece_obj)

            if piece_obj.get_color() == 'Black' and piece_obj.get_piece_type() == 'King' and location_tuple[0] == 7:
                # remove old piece from alive pieces
                self._players[player_name]._pieces_alive.remove(piece_obj)
                piece_obj = TripleKing('Black')
                # add upgraded piece to alive pieces
                self._players[player_name]._pieces_alive.append(piece_obj)

            if piece_obj.get_color() == 'White' and piece_obj.get_piece_type() == 'King' and location_tuple[0] == 0:
                # remove old piece from alive pieces
                self._players[player_name]._pieces_alive.remove(piece_obj)
                piece_obj = TripleKing('White')
                # add upgraded piece to alive pieces
                self._players[player_name]._pieces_alive.append(piece_obj)


        #updating array board to reflect change in piece
        self._dict_board[location_tuple] = piece_obj
        if piece_obj is not None:
            if piece_obj.get_piece_type() != 'Standard':
                self._array_board[location_tuple[0]][location_tuple[1]] = piece_obj.get_color() + ' ' + piece_obj.get_piece_type()
            else:
                self._array_board[location_tuple[0]][location_tuple[1]] = piece_obj.get_color()
        else:
            self._array_board[location_tuple[0]][location_tuple[1]] = None

    def game_winner(self):
        """takes no parameters and tells you the name of the player who won the game"""
        #this method should take no parameters and return
        #iterate through each key/value pair (player name string/player object)
        for player in self._players:
            #if player object has 12 pieces
            if self._players[player].get_captured_pieces_count() == 12:
                #should be player name string
                return player
            else:
                return 'Game has not ended'

    def get_pieces(self, piece_color):
        """get method for all the pieces of one color"""
        #this will return a list of all the pieces of that color 1-12
        return self._pieces[piece_color]

    def get_player(self, player_name):
        """get method that returns the player object for a given name"""
        return self._players[player_name]

class Player:
    """represents a player in the game that has a name and a color"""

    def __init__(self, player_name, piece_color):
        """init method that takes input for their name and chosen color"""

        self._player_name = player_name
        self._piece_color = piece_color

        #will be a list of piece objects captured
        self._captured_pieces = []
        #initialized here but filled out in the create_player method of Checkers
        self._pieces_alive = []

    def set_pieces(self, list_of_pieces):
        """set method for use in checkers class to set the player's pieces to themselves"""
        self._pieces_alive = list_of_pieces

    def get_name(self):
        """get method for the players name"""
        return self._player_name

    def kill_piece(self, piece_obj):
        """to remove a piece from alive_pieces data member"""
        if piece_obj in self._pieces_alive:
            self._pieces_alive.remove(piece_obj)
        else:
            print("trying to remove a piece that ain't there!!")

    def get_color(self):
        """get method for the color of pieces"""
        return self._piece_color

    def get_king_count(self):
        """takes no parameters and returns the number of kings that player has"""
        king_count = 0
        for element in self._pieces_alive:
            if element.get_piece_type() == 'King':   #this is a method in the Piece object
                king_count += 1
        return king_count

    def get_triple_king_count(self):
        """takes no parameters and returns the number of triple kings that player has"""
        triple_king_count = 0
        for element in self._pieces_alive:
            if element.get_piece_type() == 'Triple King':
                triple_king_count += 1
        return triple_king_count

    def get_captured_pieces_count(self):
        """takes no parameters and returns the number of pieces that player has captured"""
        return len(self._captured_pieces)

    def capture_piece(self, captured_piece):
        """appends the captured piece object to the captured piece list"""
        self._captured_pieces.append(captured_piece)


def main():
    game = Checkers()
    game.print_board()
    game.create_player('thom', 'Black')
    game.create_player('chey', 'White')
    # print(game.get_checker_details((0,0)))
    # print(game.get_checker_details((0,1)))
    # print(game.get_checker_details((5,0)))
    #game.play_game('chey', (1,0), (1,1))    #out of turn
#   print(game.get_checker_details((0,12))) #invalid square
    #print('hi')
    print(game.get_player('thom').get_captured_pieces_count())  #zero
    print(game.get_player('thom').get_captured_pieces_count())  #zero
    print(game.game_winner())                                   #no winner yet
    print(game.get_player('thom').get_king_count())             #zero

    #game.play_game('thom', (0,1), (0,2))                        #not my piece (invalid square)
    #game.play_game('george',(0,1), (0,2))                       #invalid name (invalid player)
    #game.play_game('thom', (-1,0), (1,0))                        #out of bounds (invalid square)

    print(game.get_checker_details((4,1)))                         #should be None
    print(game.get_checker_details((5,0)))                          #should be Black
    print('move thom from (5,0 ) to (3,2)')
    game.play_game('thom', (5,0), (3,2))
    game.play_game('chey', (2, 3), (4,1))
    game.print_board()
    game.play_game('thom', (5,2), (3,0))
    game.print_board()
    print(game.get_checker_details((4,1)))                          #should be Black instead of none

    print(game.get_checker_details((5,0)))                         #should be None

    print()
    #game.play_game('thom', (4,1), (3,2))        #should raise not your turn

if __name__ == '__main__':
    main()