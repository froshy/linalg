"""
A testing script for linalg modules
"""

from matrix import *


def test_is_matrix():
    """
    Testing function for is_matrix(nlist)
    """
    a = [
        
    ]
    b = [
        []
    ]
    c = [
        1 ,2 , 3
    ]
    d = [
        [1, 2, 3],
        [4, 5, 6]
    ]
    e = [
        [5 ,6 ,7 ,8],
        [1 ,2],
        [6 ,7 ,8 ,9]
    ]
    f = [
        [1, 2, 3],
        [4, 'a', 6],
        [7, 8, 9]
    ]
    g = [
        [1, 2.01235, 3],
        [4, 'a', 6],
        [7, 8, 9]
    ]

    h = [
        [1, 2.1235, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    assert not is_matrix(a)
    assert is_matrix(b)
    assert not is_matrix(c)
    assert is_matrix(d)
    assert not is_matrix(e)
    assert not is_matrix(f)
    assert not is_matrix(g)
    assert is_matrix(h)
    print(f'is_matrix passed')
    
def test_matrix_init():
    """
    Testing function for initializing matrix object
    """
    print(f'Testing matrix initialization')

    a = makemat([
        [1, 2, 3],
        [4, 5, 6]
    ])

    b = makemat([
        [1],
        [2],
        [3]
    ])

    c = makemat([
        []
    ])

    d = makemat([
        [5]
    ])

    e = makemat([
        [6.8]
    ])

    f = makemat([
        [1, 2, 3, 4, 5]
    ])

    g = makemat([
        [3, 8]
    ])

    print(f'a is {a}')
    assert a.getnCols() ==3
    assert a.getnRows() ==2
    print(f'b is {b}')
    assert b.getnCols() ==1, f'expected 1 but instead got {a.getnCols()}'
    assert b.getnRows() ==3

    print(f'c is {c}')
    assert c.getnCols() ==0
    assert c.getnRows() ==0

    print(f'd is {d}')
    assert d.getnCols() ==1
    assert d.getnRows() ==1

    print(f'e is {e}')
    assert e.getnCols() ==1
    assert e.getnRows() ==1

    print(f'f is {f}')
    assert f.getnCols() ==5
    assert f.getnRows() ==1

    print(f'g is {g}')
    assert g.getnCols() ==2
    assert g.getnRows() ==1

    try:
        h = makemat([
            [1, 2, 'a'],
            [4 ,5 ,6]
        ])
        print(f'h is broken')
        
    except AssertionError:
        pass


def test_dotprod():
    """
    Testing function for dotprod(self, m)
    """
    print(f'Testing dotprod')
    a = makemat([
        [1, 2, 3, 4, 5]
    ])
    b = makemat([
        [6 , 7, 8, 9, 10]
    ])

    c = makemat([
        [6], 
        [2],
        [3],
        [4],
        [5]
    ])

    d = makemat([
        [6],
        [7],
        [8],
        [9],
        [10]
    ])

    e = makemat([
        [5]
    ])

    f = makemat([
        [7]
    ])

    assert a.dotprod(b)==130, f'expected 130 but instead got {a.dotprod(b)}'
    assert c.dotprod(d)==160
    assert e.dotprod(f)==35
    print('Dotprod passed')

def test_transpose():
    """
    Test function for transpose()
    """
    print("Testing transpose")

    a = makemat([
        [1, 2, 3, 4, 5]
    ])

    at = makemat([
        [1],
        [2],
        [3],
        [4],
        [5]
    ])

    b = makemat([
        [1, 2, 3]
    ])

    bt = makemat([
        [1],
        [2],
        [3]
    ])

    c = makemat([
        []
    ])

    ct = makemat([
        []
    ])

    d = makemat([
        [5]
    ])

    dt = makemat([
        [5]
    ])

    e = makemat([
        [1 ,2 ,3],
        [4, 5, 6]
    ])

    et = makemat([
        [1, 4],
        [2, 5],
        [3, 6]

    ])

    assert a.transpose() == at
    assert b.transpose() == bt
    assert c.transpose() == ct
    assert d.transpose() == dt
    assert e.transpose() == et

    assert at.transpose() == a
    assert bt.transpose() == b
    assert ct.transpose() == c
    assert dt.transpose() == d
    assert et.transpose() == e
    print('transpose passed')
    
def test_equals():
    """
    Testing function for "=="
    """
    print('Testing __eq__')

    a = makemat([
        [1, 2, 3]
    ])
    b = makemat([
        [1, 2, 3]
    ])

    assert (a is not b) and (a == b)
    print("__eq__ passed")

def test_multiply():
    """
    Testing function multiply
    """
    print('Testing multiply')

    a = makemat([
        [2, 3],
        [4, 5],
        [6, 7]
    ])

    b = makemat([
        [0, 1, 2, 3],
        [2, 1, 0, 1]
    ])

    c = makemat([
        [4]
    ])

    d = makemat([
        [5]
    ])

    e = makemat([
        [3],
        [8],
        [5],
        [9],
        [1],
        [5]
    ])

    f = makemat([
        [6, 1, 2, 8, 4, 3, 8, 9, 5]
    ])

    ab = makemat([
        [6, 5, 4, 9],
        [10, 9, 8, 17],
        [14, 13, 12, 25]
    ])

    cd = makemat([
        [20]
    ])

    dc = makemat([
        [20]
    ])

    ef = makemat([
        [18, 3, 6, 24, 12, 9, 24, 27, 15],
        [48, 8, 16, 64, 32, 24, 64, 72, 40],
        [30, 5, 10, 40, 20, 15, 40, 45, 25],
        [54, 9, 18, 72, 36, 27, 72, 81, 45],
        [6, 1, 2, 8, 4, 3, 8, 9, 5],
        [30, 5, 10, 40, 20 ,15, 40, 45, 25]
    ])

    assert a.multiply(b) == ab
    assert c.multiply(d) == cd
    assert d.multiply(c) == dc
    assert e.multiply(f) == ef 
    print('multiply passed')

def test_extract_col():
    """
    Test function for extract_cols)_
    """
    print("Testing extract_col")

    a = makemat([
        [18, 3, 6, 24, 12, 9, 24, 27, 15],
        [48, 8, 16, 64, 32, 24, 64, 72, 40],
        [30, 5, 10, 40, 20, 15, 40, 45, 25],
        [54, 9, 18, 72, 36, 27, 72, 81, 45],
        [6, 1, 2, 8, 4, 3, 8, 9, 5],
        [30, 5, 10, 40, 20 ,15, 40, 45, 25]
    ])

    a1 = makemat([
        [18],
        [48],
        [30],
        [54],
        [6],
        [30]
    ])
    a2 = makemat([
        [3],
        [8],
        [5],
        [9],
        [1],
        [5]
    ])
    a3 = makemat([
        [6],
        [16],
        [10],
        [18],
        [2],
        [10]
    ])
    a4 = makemat([
        [24],
        [64],
        [40],
        [72],
        [8],
        [40]
    ])
    a5 = makemat([
        [12],
        [32],
        [20],
        [36],
        [4],
        [20]
    ])
    a6 = makemat([
        [9],
        [24],
        [15],
        [27],
        [3],
        [15]
    ])
    a7 = makemat([
        [24],
        [64],
        [40],
        [72],
        [8],
        [40]
    ])
    a8 = makemat([
        [27],
        [72],
        [45],
        [81],
        [9],
        [45]
    ])
    a9 = makemat([
        [15],
        [40],
        [25],
        [45],
        [5],
        [25]
    ])

    assert a.extract_col(1) == a1
    assert a.extract_col(2) == a2
    assert a.extract_col(3) == a3
    assert a.extract_col(4) == a4
    assert a.extract_col(5) == a5
    assert a.extract_col(6) == a6
    assert a.extract_col(7) == a7
    assert a.extract_col(8) == a8
    assert a.extract_col(9) == a9

    f = makemat([
        [6, 1, 2, 8, 4, 3, 8, 9, 5]
    ])

    f1 = makemat([
        [6]
    ])
    f2 = makemat([
        [1]
    ])
    f3 = makemat([
        [2]
    ])
    f4 = makemat([
        [8]
    ])
    f5 = makemat([
        [4]
    ])
    f6 = makemat([
        [3]
    ])
    f7 = makemat([
        [8]
    ])
    f8 = makemat([
        [9]
    ])
    f9 = makemat([
        [5]
    ])
    
    assert f.extract_col(1) == f1
    assert f.extract_col(2) == f2
    assert f.extract_col(3) == f3
    assert f.extract_col(4) == f4
    assert f.extract_col(5) == f5
    assert f.extract_col(6) == f6
    assert f.extract_col(7) == f7
    assert f.extract_col(8) == f8
    assert f.extract_col(9) == f9
    print("extract_col passed")

def test_extract_row():
    """
    Testing function extract_row()
    """
    print('Testing extract_row')

    a = makemat([
        [18, 3, 6, 24, 12, 9, 24, 27, 15],
        [48, 8, 16, 64, 32, 24, 64, 72, 40],
        [30, 5, 10, 40, 20, 15, 40, 45, 25],
        [54, 9, 18, 72, 36, 27, 72, 81, 45],
        [6, 1, 2, 8, 4, 3, 8, 9, 5],
        [30, 5, 10, 40, 20 ,15, 40, 45, 25]
    ])

    a1 = makemat([
        [18, 3, 6, 24, 12, 9, 24, 27, 15],
    ])
    a2 = makemat([
        [48, 8, 16, 64, 32, 24, 64, 72, 40],
    ])
    a3 = makemat([
        [30, 5, 10, 40, 20, 15, 40, 45, 25],
    ])
    a4 = makemat([
        [54, 9, 18, 72, 36, 27, 72, 81, 45],

    ])
    a5 = makemat([
        [6, 1, 2, 8, 4, 3, 8, 9, 5],
    ])
    a6 = makemat([
        [30, 5, 10, 40, 20 ,15, 40, 45, 25]
    ])

    assert a.extract_row(1) == a1
    assert a.extract_row(2) == a2
    assert a.extract_row(3) == a3
    assert a.extract_row(4) == a4
    assert a.extract_row(5) == a5
    assert a.extract_row(6) == a6

    f = makemat([
        [6, 1, 2, 8, 4, 3, 8, 9, 5]
    ])

    assert f.extract_row(1) == f

def test_det():
    """
    Testing function det()
    """
    print('Testing det')
    a = makemat([
        [1, 6],
        [4, 0]
    ])

    assert a.det() == -24
    print('det passed')

def test_rem_col():
    """
    Testing function for rem_col
    """
    print('Testing rem_col')
    a = makemat([
        [18, 3, 6, 24, 12, 9, 24, 27, 15],
        [48, 8, 16, 64, 32, 24, 64, 72, 40],
        [30, 5, 10, 40, 20, 15, 40, 45, 25],
        [54, 9, 18, 72, 36, 27, 72, 81, 45],
        [6, 1, 2, 8, 4, 3, 8, 9, 5],
        [30, 5, 10, 40, 20 ,15, 40, 45, 25]
    ])
    a1 = makemat([
        [3, 6, 24, 12, 9, 24, 27, 15],
        [8, 16, 64, 32, 24, 64, 72, 40],
        [5, 10, 40, 20, 15, 40, 45, 25],
        [9, 18, 72, 36, 27, 72, 81, 45],
        [1, 2, 8, 4, 3, 8, 9, 5],
        [5, 10, 40, 20 ,15, 40, 45, 25]
    ])
    a2 = makemat([
        [18, 6, 24, 12, 9, 24, 27, 15],
        [48, 16, 64, 32, 24, 64, 72, 40],
        [30, 10, 40, 20, 15, 40, 45, 25],
        [54, 18, 72, 36, 27, 72, 81, 45],
        [6, 2, 8, 4, 3, 8, 9, 5],
        [30, 10, 40, 20 ,15, 40, 45, 25]
    ])
    a3= makemat([
        [18, 3, 24, 12, 9, 24, 27, 15],
        [48, 8, 64, 32, 24, 64, 72, 40],
        [30, 5, 40, 20, 15, 40, 45, 25],
        [54, 9, 72, 36, 27, 72, 81, 45],
        [6, 1, 8, 4, 3, 8, 9, 5],
        [30, 5, 40, 20 ,15, 40, 45, 25]
    ])
    a4 = makemat([
        [18, 3, 6, 12, 9, 24, 27, 15],
        [48, 8, 16, 32, 24, 64, 72, 40],
        [30, 5, 10, 20, 15, 40, 45, 25],
        [54, 9, 18, 36, 27, 72, 81, 45],
        [6, 1, 2, 4, 3, 8, 9, 5],
        [30, 5, 10, 20 ,15, 40, 45, 25]
    ])
    a5 = makemat([
        [18, 3, 6, 24, 9, 24, 27, 15],
        [48, 8, 16, 64, 24, 64, 72, 40],
        [30, 5, 10, 40, 15, 40, 45, 25],
        [54, 9, 18, 72, 27, 72, 81, 45],
        [6, 1, 2, 8, 3, 8, 9, 5],
        [30, 5, 10, 40 ,15, 40, 45, 25]
    ])
    a6 = makemat([
        [18, 3, 6, 24, 12, 24, 27, 15],
        [48, 8, 16, 64, 32, 64, 72, 40],
        [30, 5, 10, 40, 20, 40, 45, 25],
        [54, 9, 18, 72, 36, 72, 81, 45],
        [6, 1, 2, 8, 4, 8, 9, 5],
        [30, 5, 10, 40, 20, 40, 45, 25]
    ])
    a7 = makemat([
        [18, 3, 6, 24, 12, 9, 27, 15],
        [48, 8, 16, 64, 32, 24, 72, 40],
        [30, 5, 10, 40, 20, 15, 45, 25],
        [54, 9, 18, 72, 36, 27, 81, 45],
        [6, 1, 2, 8, 4, 3, 9, 5],
        [30, 5, 10, 40, 20 ,15, 45, 25]
    ])
    a8 = makemat([
        [18, 3, 6, 24, 12, 9, 24, 15],
        [48, 8, 16, 64, 32, 24, 64, 40],
        [30, 5, 10, 40, 20, 15, 40, 25],
        [54, 9, 18, 72, 36, 27, 72, 45],
        [6, 1, 2, 8, 4, 3, 8, 5],
        [30, 5, 10, 40, 20 ,15, 40, 25]
    ])
    a9= makemat([
        [18, 3, 6, 24, 12, 9, 24, 27],
        [48, 8, 16, 64, 32, 24, 64, 72],
        [30, 5, 10, 40, 20, 15, 40, 45],
        [54, 9, 18, 72, 36, 27, 72, 81],
        [6, 1, 2, 8, 4, 3, 8, 9],
        [30, 5, 10, 40, 20 ,15, 40, 45]
    ])
    
    assert a.rem_col(1) == a1
    assert a.rem_col(2) == a2
    assert a.rem_col(3) == a3
    assert a.rem_col(4) == a4
    assert a.rem_col(5) == a5
    assert a.rem_col(6) == a6
    assert a.rem_col(7) == a7
    assert a.rem_col(8) == a8
    assert a.rem_col(9) == a9

def main():
    """
    Main method
    """
    print(f'Begin testing')
    test_is_matrix()
    test_matrix_init()
    test_dotprod()
    test_transpose()
    test_equals()
    test_multiply()
    test_extract_col()
    test_extract_row()
    test_det()
    test_rem_col()
    print(f"All tests passed")

if __name__ == '__main__':
    main()