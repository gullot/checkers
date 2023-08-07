# Author: Thomas Gullo
# GitHub username: gullot
# Date: 3/19/23
# Description: this test file tests CheckersGame.py for multiple test cases

import unittest
from CheckersGame import Checkers
from CheckersGame import Player
from CheckersGame import OutofTurn
from CheckersGame import InvalidPlayer
from CheckersGame import InvalidSquare
from CheckersGame import Piece
from CheckersGame import King
from CheckersGame import TripleKing

class TestCheckers(unittest.TestCase):
    """
    Contains unit tests for the Checkers class
    """

    def test_1(self):
        """Test for simple moves"""
        game = Checkers()
        game.create_player('thomas', 'Black')
        game.create_player('cheyenne', 'White')
        game.play_game('thomas', (5,0), (4,1))
        self.assertEqual(game.get_checker_details((4,1)), 'Black')
        self.assertEqual(game.game_winner(), 'Game has not ended')

    def test_2(self):
        """Test for simple moves and a capture"""
        game2 = Checkers()
        game2.create_player('thomas', 'Black')
        game2.create_player('cheyenne', 'White')
        game2.play_game('thomas', (5, 0), (4, 1))
        game2.print_board()
        game2.play_game('cheyenne', (2, 1), (3, 2))
        game2.print_board()
        game2.play_game('thomas', (5, 6), (4, 5))
        game2.print_board()
        game2.play_game('cheyenne', (3, 2), (5, 0))
        game2.print_board()
        self.assertIs(game2.get_checker_details((4, 1)), None)
        self.assertEqual(game2.get_player('cheyenne').get_captured_pieces_count(), 1)


    def test_3(self):
        """Test a bunch of exceptions!"""
        game3 = Checkers()
        game3.create_player('thomas', 'Black')
        game3.create_player('cheyenne', 'White')
        #not White's turn
        self.assertRaises(OutofTurn, lambda: game3.play_game('cheyenne', (2, 7), (3, 6)))
        #moving off the board
        self.assertRaises(InvalidSquare, lambda: game3.play_game('thomas', (5, 0), (4, -1)))
        #invalid player name
        self.assertRaises(InvalidPlayer, lambda: game3.play_game('georgio', (5, 0), (4, -1)))
        #moving piece on top of other piece
        self.assertRaises(InvalidSquare, lambda: game3.play_game('thomas', (5, 0), (2, 1)))
        #moving wrong piece
        self.assertRaises(InvalidSquare, lambda: game3.play_game('thomas', (2, 1), (3, 0)))
        #moving non diagonal
        self.assertRaises(InvalidSquare, lambda: game3.play_game('thomas', (5, 0), (5, 1)))


    def test_4(self):
        """tests for getting to kings"""
        game4 = Checkers()
        game4.create_player('thomas', 'Black')
        game4.create_player('cheyenne', 'White')
        game4.play_game('thomas', (5, 0), (4, 1))
        game4.print_board()
        game4.play_game('cheyenne', (2, 1), (3, 2))
        game4.print_board()
        game4.play_game('thomas', (5, 6), (4, 5))
        game4.print_board()
        game4.play_game('cheyenne', (3, 2), (5, 0))
        game4.print_board()
        game4.play_game('thomas', (5, 2), (4, 1))
        game4.print_board()
        game4.play_game('cheyenne', (2, 3), (3, 2))
        game4.print_board()
        game4.play_game('thomas', (6, 1), (5, 2))
        game4.print_board()
        game4.play_game('cheyenne', (5, 0), (6, 1))
        game4.print_board()
        game4.play_game('thomas', (5, 2), (4, 3))
        game4.print_board()
        game4.play_game('cheyenne', (3, 2), (5, 0))
        game4.print_board()
        game4.play_game('thomas', (6, 3), (5, 2))
        game4.print_board()
        game4.play_game('cheyenne', (2, 5), (3, 4))
        game4.print_board()
        game4.play_game('thomas', (7, 2), (6, 3))
        game4.print_board()
        game4.play_game('cheyenne', (6, 1), (7, 2))
        game4.print_board()
        self.assertEqual(game4.get_checker_details((7, 2)), 'White King')

    def test_5(self):
        """test for more moves and triple kings, as well as the count of kings/triple kings"""
        game5 = Checkers()
        game5.create_player('thomas', 'Black')
        game5.create_player('cheyenne', 'White')
        game5.print_board()
        print('\n')
        game5.play_game('thomas', (5, 0), (4, 1))
        game5.print_board()
        print('\n')
        game5.play_game('cheyenne', (2, 1), (3, 2))
        game5.print_board()
        print('\n')
        game5.play_game('thomas', (5, 6), (4, 5))
        game5.print_board()
        print('\n')
        game5.play_game('cheyenne', (3, 2), (5, 0))
        game5.print_board()
        print('\n')
        game5.play_game('thomas', (5, 2), (4, 1))
        game5.print_board()
        print('\n')
        game5.play_game('cheyenne', (2, 3), (3, 2))
        game5.print_board()
        print('\n')
        game5.play_game('thomas', (6, 1), (5, 2))
        game5.print_board()
        print('\n')
        game5.play_game('cheyenne', (5, 0), (6, 1))
        game5.print_board()
        print('\n')
        game5.play_game('thomas', (5, 2), (4, 3))
        game5.print_board()
        print('\n')
        game5.play_game('cheyenne', (3, 2), (5, 0))
        game5.print_board()
        print('\n')
        game5.play_game('thomas', (6, 3), (5, 2))
        game5.print_board()
        print('\n')
        game5.play_game('cheyenne', (2, 5), (3, 4))
        game5.print_board()
        print('\n')
        game5.play_game('thomas', (7, 2), (6, 3))
        game5.print_board()
        print('\n')
        game5.play_game('cheyenne', (6, 1), (7, 2))
        game5.print_board()
        print('\n')
        game5.play_game('thomas', (4, 5), (2, 3))
        game5.print_board()
        print('\n')
        game5.play_game('cheyenne', (7, 2), (6, 1))
        game5.print_board()
        print('\n')
        game5.play_game('thomas', (5, 4), (4, 5))
        game5.print_board()
        print('\n')
        game5.play_game('cheyenne', (3, 4), (5, 6))
        game5.print_board()
        print('\n')
        game5.play_game('thomas', (4, 3), (3, 4))
        game5.print_board()
        print('\n')
        game5.play_game('cheyenne', (6, 1), (2, 5))  #double jump
        game5.print_board()
        print('\n')
        game5.play_game('thomas', (6, 7), (4, 5))
        game5.print_board()
        print('\n')
        game5.play_game('cheyenne', (5, 0), (6, 1))
        game5.print_board()
        print('\n')
        game5.play_game('thomas', (7, 6), (6, 7))
        game5.print_board()
        print('\n')
        game5.play_game('cheyenne', (1, 4), (3, 2))
        game5.print_board()
        print('\n')
        game5.play_game('thomas', (5, 2), (4, 1))
        game5.print_board()
        print('\n')
        game5.play_game('cheyenne', (0, 5), (2, 3))
        game5.print_board()
        print('\n')
        game5.play_game('thomas', (6, 3), (5, 4))
        game5.print_board()
        print('\n')
        game5.play_game('cheyenne', (2, 5), (1, 4))
        game5.print_board()
        print('\n')
        game5.play_game('thomas', (5, 4), (4, 3))
        game5.print_board()
        print('\n')
        game5.play_game('cheyenne', (1, 4), (0, 5))  #triple king
        game5.print_board()
        print('\n')
        self.assertEqual(game5.get_checker_details((0,5)), 'White Triple King')
        self.assertEqual(game5.get_player('cheyenne').get_triple_king_count(), 1)
        self.assertEqual(game5.get_player('cheyenne').get_king_count(), 0)
        self.assertEqual(game5.get_player('cheyenne').get_captured_pieces_count(), 4)