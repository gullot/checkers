# Author: Thomas Gullo
# GitHub username: gullot
# Date: 3/4/23
# Description: this program represents checkers game


#**Checkers:**

#The Checkers object represents the game as played.

#The class should contain information about the board and the players. The board is initialized when the Checkers object is created.

#It must contain these methods (but may have more if you want):
#* create_player - takes as parameter the player_name and piece_color that the player wants to play with and creates the player object. The parameter piece_color is a string of value "Black" or "White" representing
# Black or White checkers pieces respectively. This function returns the player object that has been created.

#* play_game - takes as parameter player_name, starting_square_location and destination_square_location of the piece that the player wants to move. The square_location is a tuple in format (x,y).
# If a player wants to move a piece from third square in the second row to fourth square in the fifth row, the starting and destination square locations will be (1,2) to (4,3). Following the rules of the game move this piece.

#    * If a player attempts to move a piece out of turn, raise an OutofTurn exception (you'll need to define this exception class).
#    * If a player does not own the checker present in the square_location or if the square_location does not exist on the baord; raise an InvalidSquare exception (you'll need to define this exception class).
#    * If the player_name is not valid, raise an InvalidPlayer exception (you'll need to define this exception class).
#    * This method returns the number of captured pieces, if any, otherwise return 0.
#    * If the destination piece reaches the end of opponent's side it is promoted as a king on the board. If the piece crosses back to its original side it becomes a triple king.
#    * If the piece being moved is a king or a triple king assess the move according to the rules of the game.

#* get_checker_details - takes as parameter a square_location on the board and returns the checker details present in the square_location
#    * Returns None, if no piece is present in the location
#    * If the square_location does not exist on the board, raise an InvalidSquare exception (use the same exception class that was created for play_game function).
#    * If black piece is present return "Black"
#    * If white piece is present return "White"
#    * If black king piece is present return "Black_king"
#    * If white king piece is present return "White_king"
#    * If black triple king piece is present return "Black_Triple_King"
#    * If white triple king piece is present return "White_Triple_King"

class OutofTurn(Exception):
    """exception class for when its not your turn!"""
    pass

class InvalidSquare(Exception):
    """exception class for invalid square input"""
    pass

class Piece:
    """class to represent a piece on the board. Planning to make king piece and triple king piece subclasses
    This will need to have an init method with color as a parameter and a type initialized to Standard.
    This will need a get method for the color of the piece for the Checkers and Player class to access.
    This will also need a get method for the type of piece for the Checkers class"""

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
    """a class to represent a checkers board and all the pieces and contains the players as well.

    This will also initialize the 'Black' player as who's turn it is.

    I plan on initializing all the Piece objects as well here so that I can place them on the board."""

    def __init__(self):
        """initializes the checkers board and pieces to start the game. This must initialize the board, and I plan to
         have the information in a dictionary for ease of access. The key will be the tuple coordinate, and the value
        will be what is on the square (either None or a Piece object)
        This will also need to initialize an empty list or dict for the player objects to reside in"""
        pass


    def turn_switch(self):
        """method to change who's turn it is. This will be called at the end of every valid move.
        This will also be called when a piece gets made to King or triple king
        if no captures are made, the turn switches"""
        pass

    def get_board(self):
        """get method for the board dictionary for use of the print_board method."""
        return self._board

    def create_player(self, player_name, piece_color):
        """creates a player with their name and color, black or white. This will need to validate Black or White is
        input ok, and will take any string name. This will create Player objects and store them in the player dict in
        Checkers class"""
        pass

    def play_game(self, player_name, starting_square_location, destination_square_location):
        """takes a players name, their current location and their destination location in tuple form
        - once the move is validated via the helper method below, this will need to update the piece information as required
        - this will require set methods on the Player object to set the captured pieces and its own alive pieces
        - will update the board dictionary directly
        - will need a way to update the board that is printed for clarity in addition to the dictionary

        - will need to keep track of whos turn it is. Perhaps having a toggle on the play_game method at the end of method
        - should send the captured pieces to the Player object to keep track of captured pieces

        - should check piece type by get_checker_details to determine possible moves based on the Piece object type, as
        well as check all diagonals for Nones and Pieces (black and white) to determine move capabilities and to determine
        if a capture is made

        - for any piece of opposite color reaching the opposite side, the Piece object must be removed and the appropriate
        subclass of Piece should be swapped in.
        """
        #
    def validate_move(self, starting_square_location, destination_square_location):
        """
        - needs to confirm that the input starting location includes their color and that their destination is valid
        - will need to access the board dictionary via get_board
        - will need to validate move is valid by the rules of the game
        - will need to confirm if a piece or more shall be removed from the game following the move
        """


    def get_checker_details(self, square_location):
        """takes a square location and returns checker details present on that square.
        This will need to validate the tuple is actually on the board and raise the InvalidSquare as required.
        We will also check for None and need to check the color of the Piece object and the type of the Piece object"""
        pass

    def print_board(self):
        """takes no parameters and prints the board in the form of an array. Since I have a dictionary representing the
        board, I will need to iterate through the dictionary and extract the value at each key and print them, with a
        new line being at every 8 entries"""
        pass

    def game_winner(self):
        """takes no parameters and tells you the name of the player who won the game.
        this method should take no parameters and return the name of the player that has all 12 pieces
        (get_captured_pieces to come in handy here) and return an error or a No Winner message if neither has 12."""
        pass

    def get_pieces(self, piece_color):
        """get method for all the pieces of one color. This will be used in populating the Player object with
        all of its Pieces of the color needed"""
        return self._pieces[piece_color]

class Player:
    """represents a player in the game that has a name and a color"""

    def __init__(self, player_name, piece_color):
        """init method that takes input for their name and chosen color, and will also initialize a captured pieces
        data member to None and also ASSIGN all the white/black pieces to that data member based on the color chosen"""

        pass

    def get_king_count(self):
        """takes no parameters and returns the number of kings that player has.
        this will need to iterate through the pieces alive data member"""
        pass

    def get_triple_king_count(self):
        """takes no parameters and returns the number of triple kings that player has.
        this will need to iterate through the pieces alive data member"""
        pass

    def get_captured_pieces_count(self):
        """takes no parameters and returns the number of pieces that player has captured.
        This will need to iterate through the captured pieces data member"""
        pass

    def set_captured_pieces(self, pieces_object):
        """This will update the captured pieces data member to keep track of the captured pieces"""
        pass

    def set_pieces_alive(self, pieces_object):
        """this will update the players pieces that have been taken from them in the other playes move"""
        pass

