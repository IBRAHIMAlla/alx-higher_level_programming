#!/usr/bin/python3
"""
Includes the matrix_mul function
"""


def matrix_mul(m_a, m_b):
    """Perform matrix multiplication on two matrices(lists of lists of integers/floats)"""
    if type(m_a) is not list:
        raise TypeError("m_a must be a list")
    m1 = len(m_a)
    if m1 == 0:
        raise ValueError("m_a can't be empty")
    m2 = None
    for m in m_a:
        if type(m) is not list:
            raise TypeError("m_a must be a list of lists")
        if m2 is None:
            m2 = len(m)
            if m2 == 0:
                raise ValueError("m_a can't be empty")
        if m2 != len(m):
            raise TypeError("each row of m_a must should be of the same size")
        for y in m:
            if type(y) is not int and type(y) is not float:
                raise TypeError("m_a should contain only integers or floats")
    if type(m_b) is not list:
        raise TypeError("m_b must be a list")
    if len(m_b) == 0:
        raise ValueError("m_b can't be empty")
    m3 = None
    for m in m_b:
        if type(m) is not list:
            raise TypeError("m_b must be a list of lists")
        if m3 is None:
            m3 = len(m)
            if m3 == 0:
                raise ValueError("m_b can't be empty")
        if m3 != len(m):
            raise TypeError("each row of m_b must should be of the same size")
        for y in m:
            if type(y) is not int and type(y) is not float:
                raise TypeError("m_b should contain only integers or floats")
    if m2 != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")
    mat = []
    for m in range(m1):
        o = []
        for y in range(m3):
            n = 0
            for j in range(m2):
                n += m_a[m][j] * m_b[j][y]
            o.append(n)
        mat.append(o)
    return mat
