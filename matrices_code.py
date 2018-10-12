class BaseMatrix(object):

    def __init__(self, type1, rows, columns):
        self.n = rows
        self.m = columns
        self.t = type1
        self.data = []
        types = [int, complex, float]
        if type1 in types:
            for a in range(columns):
                row = []
                for b in range(rows):
                    row.append(self.t(0))
                self.data.append(row)
        else:
            raise TypeError("Please enter a valid type")

    def __str__(self):
        s = self.__class__.__name__ + "({})". format((self.n, self.m))+"\n"
        for i in range(0, self.n):
            for j in range(0, self.m):
                s += str(self.get(i, j)) + " "
            s += "\n"
        result = "{} x {} matrix of type {}: ".format(self.n, self.m, self.t)
        return result + s

    def get(self, row, column):
        if row <= (self.n - 1) and column <= (self.m - 1):
            val = self.data[row][column]
            return val
        else:
            raise IndexError("the position you are looking for was not found")

    def set(self, row, column, value):
        if row <= (self.n - 1) and column <= (self.m - 1):
            self.data[row][column] = value
        else:
            raise IndexError("the index you are looking for is out of range")

    def __add__(self, other):
        if self.n == other.n and self.m == other.m and self.t == other.t:
            m = BaseMatrix(self.t, self.n, self.m)
            for i in range(0, self.n):
                for j in range(0, self.m):
                    s = self.get(i, j) + other.get(i, j)
                    m.set(i, j, s)
            return m
        else:
            print("the matrices' dimensions / type do not match")

    def __eq__(self, other):
        condition = True
        if self.n == other.n and self.m == other.m and self.t == other.t:
            for i in range(0, self.n):
                for j in range(0, self.m):
                    if not self.get(i, j) == other.get(i, j):
                        condition = False
                        return condition
            return condition
        else:
            condition = False
            return condition


class MySparseMatrix(BaseMatrix):

    def __init__(self, t, n, m):
        types = [int, complex, float]
        if t in types:
            self.n = n
            self.m = m
            self.t = t

            self.data = {}
        else:
            raise TypeError("Please enter a valid type")

    def set(self, i, j, v):
        if i <= (self.n - 1) and j <= (self.m - 1):
            key = (i, j)
            self.data[key] = v
        else:
            raise IndexError("the index you are looking for is out of range")

    def get(self, i, j):
        if i <= (self.n - 1) and j <= (self.m - 1):
            key = (i, j)
            return self.data.get(key, self.t())
        else:
            raise IndexError("the position you are looking for was not found")
