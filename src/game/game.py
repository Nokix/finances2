from typing import Dict

from List_Tools import flatten
from functools import reduce
from itertools import chain


class WaveSolver:
    def __init__(self, coordinates, possibility_room, rule):
        self.wave: Dict = {coordinate: possibility_room for coordinate in coordinates}
        self.collapsed = dict()
        self.rule = rule

    def single_step_remove_rule(self, coordinate, inserted):
        self.collapsed[coordinate] = inserted
        try:
            del self.wave[coordinate]
        except KeyError:
            pass
        for c, to_remove in self.rule(coordinate, inserted).items():
            for item in to_remove:
                try:
                    self.wave[c].remove(item)
                except ValueError:
                    pass
                except KeyError:
                    continue
                if not self.wave[c]:
                    del self.wave[c]

    def get_next_collapse_position(self, chooser=(lambda ls: ls[0])):
        while True:
            self.wave = dict(sorted(self.wave.items(), key=(lambda item: len(item[1])), reverse=True))
            try:
                coordinate, possibilities = self.wave.popitem()
            except KeyError:
                break
            if len(possibilities):
                if len(possibilities) == 1:
                    yield coordinate, possibilities[0]
                else:
                    yield coordinate, chooser(possibilities)
            else:
                break

    def solve(self):
        for coordinate, chosen in self.get_next_collapse_position():
            self.single_step_remove_rule(coordinate, chosen)


class Game(object):
    pass


class Sudoku(Game):
    def __init__(self, size_x: int = 9, size_y: int = 9, quadrant_size_x: int = 3, quadrant_size_y: int = 3):
        self.size_x = size_x
        self.size_y = size_y
        self.quardrant_size_x = quadrant_size_x
        self.quardrant_size_y = quadrant_size_y
        self.board = [[0 for i in range(self.size_y)] for j in range(self.size_x)]
        self.all_possibilities = list(range(1, 1 + self.size_x))

        def remove_rule(coordinate, inserted):
            to_remove = {coordinate: self.all_possibilities}
            for c in chain(self.row_coordinates(coordinate),
                           self.column_coordinates(coordinate),
                           self.quadrant_coordinates(coordinate)):
                to_remove[c] = [inserted]
            return to_remove

        self.rule = remove_rule

    def row_coordinates(self, coordinate):
        i, j = coordinate
        for r in range(self.size_y):
            yield i, r

    def column_coordinates(self, coordinate):
        i, j = coordinate
        for r in range(self.size_x):
            yield r, j

    def quadrant_coordinates(self, coordinate):
        """
        Liefert einen Iterator, der alle Coordinaten zurückgibt, die coordinate enthält.
        :param coordinate: Coodrdinate, dessen Quadrant gesucht wird.
        :return: Iterator durch den Quadranten, die coordinate enthält
        """
        i, j = coordinate
        i_quadrant = i // self.quardrant_size_x
        j_quadrant = i // self.quardrant_size_y
        start_x = i_quadrant * self.quardrant_size_x
        start_y = j_quadrant * self.quardrant_size_y
        for k in range(start_x, start_x + self.quardrant_size_x):
            for j in range(start_y, start_y + self.quardrant_size_y):
                yield k, j

    def coordinates(self):
        for i in range(self.size_x):
            for j in range(self.size_y):
                yield i, j

    def solve(self):
        solver = WaveSolver(coordinates=self.coordinates(),
                            possibility_room=self.all_possibilities,
                            rule=self.rule)
        for i, j in self.coordinates():
            if self.board[i][j]:
                solver.single_step_remove_rule((i, j), self.board[i][j])
        solver.solve()
        return solver.collapsed

    def __str__(self):
        vertical_line_seperator = " | "
        result = ""
        for i in range(self.size_x):
            for j in range(self.size_y):
                result += str(self.board[i][j])
                if j % self.quardrant_size_y == self.quardrant_size_y - 1 and not j == self.size_y - 1:
                    result += vertical_line_seperator
                if j % self.size_y == self.size_y - 1:
                    result += "\n"
                    if i % self.quardrant_size_x == self.quardrant_size_x - 1 and not i == self.size_x - 1:
                        result += "-" * (self.size_y + len(vertical_line_seperator) * (int(
                            self.size_y / self.quardrant_size_y) - 1))
                        result += "\n"
        return result


class Str8t(Game):
    pass
