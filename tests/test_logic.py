import unittest
from game.logic import game_round, coupon_values, highest_value_coupon, board, board_size, move_pointees

class TestGameLogic(unittest.TestCase):
    def test_initial_board(self):
        self.assertEqual(board[0][0], 1)
    
    def test_move_pointees(self):
        global board
        board = [[1 for _ in range(board_size)] for _ in range(board_size)]
        new_board = move_pointees()
        self.assertNotEqual(board, new_board)

    def test_coupon_values(self):
        self.assertTrue(isinstance(coupon_values(), list))
    
    def test_highest_value_coupon(self):
        self.assertTrue(isinstance(highest_value_coupon(), list))

if __name__ == '__main__':
    unittest.main()
