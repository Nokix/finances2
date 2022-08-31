import unittest

from src.sudoku import Sudoku


class MyTestCase(unittest.TestCase):
    def test_check_line_1(self):
        sudoku = Sudoku()
        self.assertTrue(sudoku.check_line([1, 2, 3, 4, 5, 6, 7, 8, 9]))

    def test_check_line_2(self):
        sudoku = Sudoku()
        self.assertTrue(sudoku.check_line([9, 8, 5, 3, 2, 1, 4, 7, 6]))

    def test_check_line_3(self):
        sudoku = Sudoku()
        self.assertFalse(sudoku.check_line([9, 8, 5, 3, 2, 2, 0, 1, 3]))

    def test_check_line_4(self):
        sudoku = Sudoku(quadrant_size=2)
        self.assertTrue(sudoku.check_line([1, 2, 4, 3]))

    def test_quadrants_1(self):
        sudoku = Sudoku(quadrant_size=2)
        sudoku.board = [[1, 2, 3, 4], [3, 4, 1, 2], [2, 1, 4, 3], [4, 3, 2, 1]]
        quadrants = sudoku.quadrants()
        self.assertListEqual([[1, 2], [3, 4]], next(quadrants))
        self.assertListEqual([[3, 4], [1, 2]], next(quadrants))
        self.assertListEqual([[2, 1], [4, 3]], next(quadrants))
        self.assertListEqual([[4, 3], [2, 1]], next(quadrants))

    def test_check_quadrant_1(self):
        sudoku = Sudoku()
        self.assertTrue(sudoku.check_quadrant([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))

    def test_check_quadrant_2(self):
        sudoku = Sudoku()
        self.assertTrue(sudoku.check_quadrant([[1, 9, 7], [4, 5, 6], [3, 8, 2]]))

    def test_rows_1(self):
        sudoku = Sudoku(quadrant_size=2)
        sudoku.board = [[1, 2, 3, 4], [3, 4, 1, 2], [2, 1, 4, 3], [4, 3, 2, 1]]
        rows = sudoku.rows()
        self.assertListEqual([1, 2, 3, 4], next(rows))
        self.assertListEqual([3, 4, 1, 2], next(rows))
        self.assertListEqual([2, 1, 4, 3], next(rows))
        self.assertListEqual([4, 3, 2, 1], next(rows))

    def test_columns_1(self):
        sudoku = Sudoku(quadrant_size=2)
        sudoku.board = [[1, 2, 3, 4], [3, 4, 1, 2], [2, 1, 4, 3], [4, 3, 2, 1]]
        rows = sudoku.columns()
        self.assertListEqual([1, 3, 2, 4], next(rows))
        self.assertListEqual([2, 4, 1, 3], next(rows))
        self.assertListEqual([3, 1, 4, 2], next(rows))
        self.assertListEqual([4, 2, 3, 1], next(rows))

    def test_is_correct_1(self):
        sudoku = Sudoku(quadrant_size=2)
        sudoku.board = [[1, 2, 3, 4], [3, 4, 1, 2], [2, 1, 4, 3], [4, 3, 2, 1]]
        self.assertTrue(sudoku.is_correct())

    def test_is_correct_2(self):
        sudoku = Sudoku()
        sudoku.board = [
            [5, 3, 4, 6, 7, 8, 9, 1, 2],
            [6, 7, 2, 1, 9, 5, 3, 4, 8],
            [1, 9, 8, 3, 4, 2, 5, 6, 7],
            [8, 5, 9, 7, 6, 1, 4, 2, 3],
            [4, 2, 6, 8, 5, 3, 7, 9, 1],
            [7, 1, 3, 9, 2, 4, 8, 5, 6],
            [9, 6, 1, 5, 3, 7, 2, 8, 4],
            [2, 8, 7, 4, 1, 9, 6, 3, 5],
            [3, 4, 5, 2, 8, 6, 1, 7, 9]
        ]
        self.assertTrue(sudoku.is_correct())

    def test_is_correct_3(self):
        sudoku = Sudoku(quadrant_size=2)
        sudoku.board = [[1, 2, 3, 0], [3, 4, 1, 2], [2, 1, 4, 3], [4, 3, 2, 1]]
        self.assertFalse(sudoku.is_correct())


if __name__ == '__main__':
    unittest.main()
