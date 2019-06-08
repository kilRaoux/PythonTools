class Grid:
    """
    Grid of Cell sized width*height.
    """
    def __init__(self, width, height, zero_value = 0):
        self.width = width
        self.height = height
        self.grid = [[zero_value for i in range(height)] for j in range(width)]

    def __getitem__(self, pos):
        """
        Get one item at <col>/<line> position.
        :param pos: the id of the column and line where the cell is.
        :return: the cell.
        """
        col, line = pos
        if not(0 < col < self.height and 0 < line < self.width):
            return False
        return self.grid[col][line]

    def __setitem__(self, key, value):
        """
        Set one item at <col>/<line> position.
        :param key: the id of the column and line where the cell is.
        :param value: the value to set.
        :return: the cell.
        """
        col, line = key
        if not(0 < col < self.height and 0 < line < self.width):
            print("Warning: indeces out of bounds")
            return
        self.grid[col][line] = value

    def getline(self, line: int):
        """
        Get the line n°<line>.
        :param line: the id of the line.
        :return: the line in list
        """
        if not(0 < line < self.width):
            return []
        res = []
        for col in self.grid:
            res.append(col[line])
        return res

    def getcolumn(self, col: int):
        """
        Get the column n°<col>
        :param col: the id of the column.
        :return:
        """
        if not(0 < col < self.height):
            return []
        return self.grid[col]

    def get_adjacent_cells_4(self, col, line):
        """
        Get 4 adjacents cells.
        :param col: column index.
        :param line: line index.
        :return: list of adjacent cells.
        """
        res = []
        res.append(self[col+1,line])
        res.append(self[col-1,line])
        res.append(self[col,line+1])
        res.append(self[col,line-1])
        return res

    def get_adjacent_cells_8(self, col, line):
        """
        Get 8 adjacents cells.
        :param col: column index.
        :param line: line index.
        :return: list of adjacent cells.
        """
        res = self.get_adjacent_cells_4(col, line)
        res.append(self[col+1,line+1])
        res.append(self[col+1,line-1])
        res.append(self[col-1,line-1])
        res.append(self[col-1,line+1])
        return res

    def print(self):
        """
        Function to print the grid.
        """
        for col in self.grid:
            print(col)


class Cell:
    """
    Represents a cell of a grid. It is best to use a cell to wrap values ​​and handles with a pointer instead of a value.
    """
    def __init__(self):
        pass


class TorGrid(Grid):
    """
    Grid in the form of tor. Requesting a value exceeding the bounds returns the value of the side opose.
    Prevents errors at the edge of the grid.
    Example:
        - If the gride is 10 by 10 cells, when you want to get the 11th element you get the first.
            grid = TorGrid(10,10)
            grid[10,1] <=> grid[0,1]

    """
    def __init__(self, width, height, zero_value = 0):
        Grid.__init__(self, width, height, zero_value)

    def __getitem__(self, pos):
        """
        Get one item at <col>/<line> position.
        :param pos: the id of the column and line where the cell is.
        :return: the cell.
        :example:
            grid[10,1] to get the 11th column and 2th line cell.
        """
        col, line = pos
        if not(0 < line < self.width):
            return []
        return self.grid[col % self.height][line % self.width]

    def __setitem__(self, key, value):
        """
        Set one item at <col>/<line> position.
        :param key: the id of the column and line where the cell is.
        :param value: the value to set.
        :return: the cell.
        """
        col, line = key
        self.grid[col % self.height][line % self.width] = value

    def getline(self, line: int):
        """
        Get the line n°<line>.
        :param line: the id of the line.
        :return: the line in list
        """
        if not(0 < line < self.width):
            return []
        res = []
        for col in self.grid:
            res.append(col[line%self.width])
        return res

    def getcolumn(self, col: int):
        """
        Get the column n°<col>
        :param col: the id of the column.
        :return:
        """
        return self.grid[col % self.height]


class PipeGrid(Grid):
    def __init__(self, width, height, zero_value = 0):
        Grid.__init__(self, width, height, zero_value)

    def __getitem__(self, pos):
        """
        Get one item at <col>/<line> position.
        :param pos: the id of the column and line where the cell is.
        :return: the cell.
        :example:
            grid[10,1] to get the 11th column and 2th line cell.
        """
        col, line = pos
        return self.grid[col][line % self.width]

    def __setitem__(self, key, value):
        """
        Set one item at <col>/<line> position.
        :param key: the id of the column and line where the cell is.
        :param value: the value to set.
        :return: the cell.
        """
        col, line = key
        self.grid[col][line % self.width] = value

    def getline(self, line: int):
        """
        Get the line n°<line>.
        :param line: the id of the line.
        :return: the line in list
        """
        res = []
        for col in self.grid:
            res.append(col[line%self.width])
        return res

    def getcolumn(self, col: int):
        """
        Get the column n°<col>
        :param col: the id of the column.
        :return: the column n°<col>
        """
        return self.grid[col]


if __name__ == "__main__":
    grid_test = Grid(10,10)

    # __getitem__ call test.
    print("Test 1.1a: __getitem__")
    print(grid_test[1,1])

    # __setitem__ call test.
    print("Test 1.1b: __setitem__")
    grid_test[1,1] = 1

    # getline call test.
    print("Test 1.2: getline")
    print(grid_test.getline(1))

    # getcolumn call test.
    print("Test 1.3: getcolumn")
    print(grid_test.getcolumn(1))

    # print call test
    print("Test 1.4: print")
    grid_test.print()

    # get adjacent 4
    print("Test 1.5a: adjacent 4")
    print(grid_test.get_adjacent_cells_4(2,2))

    # get adjacent 8
    print("Test 1.5b: adjacent 8")
    print(grid_test.get_adjacent_cells_8(2,2))

    # TorGrid test
    print("TorGrid test 2:")
    torgrid_test = TorGrid(5,5)

    # Test 2.1a: getitem out of bound.
    print("Test 2.1a: getitem out of bound.")
    print(torgrid_test[146,548])

    # Test 2.1b: setitem out of bound.
    print("Test 2.1b: setitem out of bound")
    torgrid_test[5465,156] = 5
    torgrid_test.print()

    # Test 2.1c: few test.
    print("Test 2.1c: few test for getitem")
    for i in range(12):
        print(torgrid_test[i,0], end= ",")
    print()


