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

def main():
    """
    Main method
    """
    print(f'Begin testing')
    test_is_matrix()
    test_matrix_init()
    test_dotprod()
    print(f"All tests passed")

if __name__ == '__main__':
    main()