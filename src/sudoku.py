from typing import List, Iterator


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

    def check_quadrant(self, quadrant: List[List[int]]) -> bool:
        return self.check_line(sum(quadrant, []))

    def check_line(self, line: List[int]) -> bool:
        return sorted(line) == list(range(1, self.board_length + 1))

    def is_correct(self):
        return all(self.check_line(r) for r in self.rows()) \
               and all(self.check_line(c) for c in self.columns()) \
               and all(self.check_quadrant(q) for q in self.quadrants())

