import unittest

class TestTicTacToe(unittest.TestCase):
    def test_check_win(self):
        # Test winning condition for 'X'
        board = ['X', 'X', 'X', ' ', ' ', ' ', ' ', ' ', ' ']
        self.assertEqual(check_win(board), 'X')

        # Test winning condition for 'O'
        board = ['O', 'O', 'O', ' ', ' ', ' ', ' ', ' ', ' ']
        self.assertEqual(check_win(board), 'O')

        # Test tie condition
        board = ['X', 'O', 'X', 'X', 'O', 'O', 'O', 'X', 'X']
        self.assertEqual(check_win(board), 'Tie')

        # Test no win, no tie condition
        board = ['X', ' ', ' ', ' ', 'O', ' ', ' ', ' ', ' ']
        self.assertEqual(check_win(board), False)

if __name__ == '__main__':
    unittest.main()
