from typing import List, Iterator, Iterable


class Sudoku(object):
    def __init__(self, quadrant_size: int = 3):
        self.quadrant_size = quadrant_size
        self.board_length = quadrant_size ** 2
        self.board = [[0 for _ in range(0, self.board_length)]
                      for _ in range(0, self.board_length)]

    def quadrants(self) -> Iterator[List[List[int]]]:
        count_of_quadrants = int(self.board_length / self.quadrant_size)
        for i in range(count_of_quadrants):
            for j in range(count_of_quadrants):
                yield [self.board[i * self.quadrant_size + k]
                       [j * self.quadrant_size:(j + 1) * self.quadrant_size]
                       for k in range(self.quadrant_size)]

    def rows(self) -> Iterator[List[int]]:
        for i in range(self.board_length):
            yield self.board[i]

    def columns(self) -> Iterator[List[int]]:
        for j in range(self.board_length):
            yield [self.board[i][j] for i in range(self.board_length)]

    def fields(self) -> Iterator[Iterable[int]]:
        for i in range(self.board_length):
            for j in range(self.board_length):
                yield i, j, self.board[i][j]

    def check_quadrant(self, quadrant: List[List[int]]) -> bool:
        return self.check_line(sum(quadrant, []))

    def check_line(self, line: List[int]) -> bool:
        return sorted(line) == list(range(1, self.board_length + 1))

    def is_correct(self) -> bool:
        return all(self.check_line(r) for r in self.rows()) \
               and all(self.check_line(c) for c in self.columns()) \
               and all(self.check_quadrant(q) for q in self.quadrants())


class SudokuSolver(object):
    def solve(self) -> bool:
        pass


class SudokuSolverWave(SudokuSolver):
    def __init__(self, sudoku: Sudoku):
        self.sudoku = sudoku
        self.wave: List[List[List[int]]] = [[list(range(1, 1 + self.sudoku.board_length))
                                             for i in range(self.sudoku.board_length)]
                                            for j in range(self.sudoku.board_length)]
        self.solved = Sudoku(quadrant_size=self.sudoku.quadrant_size)

    def collapse_positions(self, i: int, j: int) -> Iterator[Iterable[int]]:
        # rows
        for col in range(self.sudoku.board_length):
            yield i, col

        # columns
        for row in range(self.sudoku.board_length):
            yield row, j

        # quadrant
        q_size = self.sudoku.quadrant_size
        q_i = int(i / q_size)
        q_j = int(j / q_size)
        for r in range(q_size * q_i, q_size * (q_i + 1)):
            for c in range(q_size * q_j, q_size * (q_j + 1)):
                yield r, c

    def collapse(self, i: int, j: int, n: int) -> None:
        for k, l in self.collapse_positions(i, j):
            try:
                self.wave[k][l].remove(n)
            except ValueError:
                pass
        self.wave[i][j] = []

    def get_next_best_collapse_position(self, chooser=(lambda ls: ls[0])):
        while True:
            min_i, min_j, min_count = 0, 0, self.sudoku.board_length + 1
            for i, j, n in self.solved.fields():
                count = len(self.wave[i][j])
                if count == 0:
                    continue
                if count == 1:
                    min_count = 1
                    yield i, j, self.wave[i][j][0]
                    break
                if count < min_count:
                    min_i, min_j, min_count = i, j, count
                    continue
            if min_count == self.sudoku.board_length + 1:
                break
            if min_count > 1:
                yield min_i, min_j, chooser(self.wave[min_i][min_j])

    def solve(self):
        for i, j, n in self.sudoku.fields():
            if n != 0:
                self.wave[i][j] = [n]

        for i, j, n in self.get_next_best_collapse_position():
            self.collapse(i, j, n)
            self.solved.board[i][j] = n
