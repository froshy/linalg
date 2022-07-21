"""
Module for class Matrix
"""

def is_matrix(m) -> bool:
    """
    Checks if m (array) is a valid matrix of NUMBERS ONLY

    Parameters:
    m: a list

    Returns:
    True of m is a valid matrix, False otherwise
    """
    if m == []:
        return False
    assert type(m) is list
    length = -1
    for y in m:
        if not isinstance(y, list):
            return False
        if length == -1:
            length = len(y)
        if len(y) != length:
            return False
        for x in y:
            if not isinstance(x, (int, float)):
                return False
        
    return True

def makemat(nlist):
    """
    Used for making a matrix object. Should be the
    only funtion called to instantiate a matrix object
    Checks for valid matrix format and creates matrix object

    Parameters:
    nlist: a list of nested list(s) in valid matrix format
    Returns:
    A matrix object
    """

    assert is_matrix(nlist), "Not a valid matrix format"
    return matrix(nlist)

class matrix():
    """
    Class to represent a matrix made up of NUMBERS ONLY 
    in the format:
    [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    
    Class atrributes:
    
    self.content: A list of nested lists of nums in a valid matrix format
    self.ncols: number of columns in a matrix
    self.nrows: number of rows in a matrix

    """

    def __init__(self, nlist):
        """
        Initializes object attributes

        Parameters:
        nlist: a list of nested lists in a valid
        matrix format
        """
        self.content = nlist
        self.ncols = len(nlist[0])

        if nlist[0] ==[]:
            self.nrows =0
        else:
            self.nrows= len(nlist)

    def getnRows(self) -> int:
        """
        Returns the number of rows in matrix object

        Parameters:
        self: a matrix object

        Returns:
        Integer representation of number of rows in a matrix
        """

        return self.nrows

    def getnCols(self) -> int:
        """
        Returns the number of columns in matrix object

        Parameters:
        self: a matrix object

        Returns:
        Integer representation of number of columns in a matrix
        """

        return self.ncols

    def dotprod(self, m) -> int or float:
        """ 
        Calculates the dot product of non-empty VECTORS m and self

        Parameters:
        m: A vector (single dimension matrix)
        self: A vector (single dimension matrix) of same size as m
        """
        
        assert isinstance(m, matrix)
        assert (m.ncols ==self.ncols) and (m.nrows == self.nrows)
        assert (m.ncols == 1 or m.nrows == 1)
        prod = 0

        for x in range(m.nrows):
            for y in range(m.ncols):
                prod = prod + m.content[x][y] * self.content[x][y]
        return prod

    def multiply(self, m):
        """
        Calculates the matrix product of self and m.
        self.ncols must equal m.nrows.
        Note: x.multiply(y) may not equal y.multipl(x)


        Parameters:
        self: A matrix object size n x m
        m: A matrix object size m x p
        where n, m, p are ints
        (n x m) X (m x p) => (n x p)
        Returns:
        New matrix object
        """

        assert self.ncols == m.nrows 
        result = []

        n = m.transpose()
        for y in range(self.nrows):
            result.append([])
            for ny in range(n.nrows):
                entry = 0
                for nx in range(n.ncols):
                    entry += self.content[y][nx] * n.content[ny][nx]
                result[y].append(entry)
        return makemat(result)
    
    def transpose(self):
        """
        Creates a new matrix that is the transposed matrix of self
        and returns is

        Parameters:
        self: a matrix object

        Returns:
        A new matrix object
        """
        if self.content == [[]]:
            return makemat([[]])
        result = []
        for y in range(self.ncols):
            result.append([])
            for x in range(self.nrows):
                result[y].append(self.content[x][y])
        return makemat(result)

    def extract_col(self, ncol):
        """
        Extract a single column out of non-empty matrix object
        NOTE: 1-INDEXED

        Parameters:
        self: a matrix object
        ncol: column number(1-indexed)

        Returns:
        a new matrix index with dimension n x 1
        """

        assert ncol <= self.ncols
        result = []
        for x in range(self.nrows):
            result.append([self.content[x][ncol-1]])

        return makemat(result)

    def extract_row(self, nrow):
        """
        Extract a single row out of non-empty matrix object
        NOTE: 1-INDEXED

        Parameters:
        self: a matrix object
        nrow: row number(1-indexed)

        Returns:
        a new matrix index with dimension 1 x n
        """

        assert nrow <= self.nrows
        return makemat([self.content[nrow-1]])
    
    def invert(self):
        """
        Creates inverse matrix, if it exists
        Raises error otherwise

        Parameters: 
        self: a matrix object

        Returns:
        a matrix object
        """
        pass

    def det(self):
        """
        Calculates determinant of matrix
        Matrix must be square

        Parameters:
        self: a square matrix object

        Returns:
        an integer or float
        """
        if self.nrows == 2:
            return self.content[0][0]*self.content[1][1] - self.content[0][1]*self.content[1][0]

    def rem_col(self, ncol, inplace = False):
        """
        Remove column at specified ncol (1-indexed)
        
        Parameters:
        self: a matrix object
        ncol: 1-indexed column indice to remove
        inplace: if True, modifies self object, otherwise return new matrix object

        Returns:
        a new matrix object if inplace = False,
        nothing otherwise
        """
        if not inplace:
            result = []
            for y in range(self.nrows):
                result.append([])
                for x in range(self.ncols):
                    if x+1 != ncol:
                        result[y].append(self.content[y][x])
            return makemat(result)

        for x in range(self.nrows):
            self.content[y].pop(ncol-1)

    def rem_row(self, nrow, inplace = False):
        """
        Remove row at specified ncol

        Parameters:
        self: a matrix object
        nrow: 1-indexed row indice to remove
        inplace: if True, modifies self object, otherwise return new matrix object

        Returns:
        a new amtrix object if inplace = True,
        nothing otherwise
        """
        pass

    def __str__(self) -> str:
        """
        Returns a string representation of a matrix object to view

        Parameters:
        self: a matrix object

        Returns:
        String representation of matrix object to view
        """
        result = ''
        for x in self.content:
            result = result + '\n' +repr(x)
        return result

    def __repr__(self) -> str:
        """
        Returns a string representation of a matrix object

        Parameters:
        self: a matrix object
        
        Returns:
        String representation of matrix object
        """
        return self.contents
    
    def __eq__(self, ob):
        """
        Checks equality between two objects
        Equal if theya re both amtric objects and 
        attribute .contents are also equal

        Parameters:
        self: a matrix object
        ob: an object

        Returns:
        True if equal, otherwise False
        """
        if ob is None or not isinstance(ob, matrix):
            return False
        return self.content == ob.content

