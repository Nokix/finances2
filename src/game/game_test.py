import unittest

from src.game.game import Sudoku


class MyTestCase(unittest.TestCase):
    def test_str_1(self):
        sud = Sudoku()
        result = "000 | 000 | 000\n" \
                 "000 | 000 | 000\n" \
                 "000 | 000 | 000\n" \
                 "---------------\n" \
                 "000 | 000 | 000\n" \
                 "000 | 000 | 000\n" \
                 "000 | 000 | 000\n" \
                 "---------------\n" \
                 "000 | 000 | 000\n" \
                 "000 | 000 | 000\n" \
                 "000 | 000 | 000\n"
        self.assertEqual(result, str(sud))

    def test_row_coordinates_1(self):
        sud = Sudoku()
        row = list(sud.row_coordinates((0, 7)))
        self.assertListEqual(row,
                             [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7), (0, 8)])

    def test_column_coordinates_1(self):
        sud = Sudoku()
        row = list(sud.column_coordinates((3, 7)))
        self.assertListEqual(row,
                             [(0, 7), (1, 7), (2, 7), (3, 7), (4, 7), (5, 7), (6, 7), (7, 7), (8, 7)])

    def test_quadrant_coordinates_1(self):
        sud = Sudoku(size_x=6, size_y=6, quadrant_size_x=2, quadrant_size_y=3)
        print(sud)
        quadrant = list(sud.quadrant_coordinates((3, 3)))
        self.assertListEqual(quadrant,
                             [(2, 3), (2, 4), (2, 5), (3, 3), (3, 4), (3, 5)])

    def test_WaveSolver_1(self):
        sud = Sudoku()
        sud.board = [
            [7, 8, 0, 4, 0, 0, 1, 2, 0],
            [6, 0, 0, 0, 7, 5, 0, 0, 9],
            [0, 0, 0, 6, 0, 1, 0, 7, 8],
            [0, 0, 7, 0, 4, 0, 2, 6, 0],
            [0, 0, 1, 0, 5, 0, 9, 3, 0],
            [9, 0, 4, 0, 6, 0, 0, 0, 5],
            [0, 7, 0, 3, 0, 0, 0, 1, 2],
            [1, 2, 0, 0, 0, 7, 4, 0, 0],
            [0, 4, 9, 2, 0, 6, 0, 0, 7]
        ]
        print(sud.solve())
        pass

if __name__ == '__main__':
    unittest.main()
