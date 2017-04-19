from numpy import array, zeros, round

def frobenius(matrix):
    matrix = array(matrix, dtype='f8', copy=True)
    assert matrix.ndim == 2 and matrix.shape[0] == matrix.shape[1]
    print('A:')
    print(matrix)
    m3 = zeros((4,4), dtype='f8')
    m3[0,0] = 1
    m3[1,1] = 1
    m3[3,3] = 1
    m3[2,0] = matrix[3,0]
    m3[2,1] = matrix[3,1]
    m3[2,2] = matrix[3,2]
    m3[2,3] = matrix[3,3]
    print('M3^-1:')
    print(m3)
    M3 = m3.copy()
    M3[2,0] = -m3[2,0] / matrix[3,2]
    M3[2,1] = -m3[2,1] / matrix[3,2]
    M3[2,2] = 1 / matrix[3,2]
    M3[2,3] = -m3[2,3] / matrix[3,2]
    print('M3:')
    print(M3)
    m3AM3 = m3.dot(matrix.dot(M3))
    print('M3^-1 AM3:')
    print(m3AM3)

    m2 = zeros((4,4), dtype='f8')
    m2[0,0] = 1
    m2[2,2] = 1
    m2[3,3] = 1
    m2[1,0] = m3AM3[2,0]
    m2[1,1] = m3AM3[2,1]
    m2[1,2] = m3AM3[2,2]
    m2[1,3] = m3AM3[2,3]
    print('M2^-1:')
    print(m2)
    M2 = m2.copy()
    M2[1,0] = -m2[1,0] / m3AM3[2,1]
    M2[1,1] = 1 / m3AM3[2,1]
    M2[1,2] = -m2[1,2] / m3AM3[2,1]
    M2[1,3] = -m2[1,3] / m3AM3[2,1]
    print('M2:')
    print(M2)
    m2m3AM3M2 = round(m2.dot(m3AM3.dot(M2)), 15)
    print('M2^-1 M3^-1 AM3M2:')
    print(m2m3AM3M2)

    m1 = zeros((4,4), dtype='f8')
    m1[1,1] = 1
    m1[2,2] = 1
    m1[3,3] = 1
    m1[0,0] = m2m3AM3M2[1,0]
    m1[0,1] = m2m3AM3M2[1,1]
    m1[0,2] = m2m3AM3M2[1,2]
    m1[0,3] = m2m3AM3M2[1,3]
    print('M1^-1:')
    print(m1)
    M1 = m1.copy()
    M1[0,0] = 1 / m2m3AM3M2[1,0]
    M1[0,1] = - m1[0,1] / m2m3AM3M2[1,0]
    M1[0,2] = - m1[0,2] / m2m3AM3M2[1,0]
    M1[0,3] = - m1[0,3] / m2m3AM3M2[1,0]
    print('M1:')
    print(M1)
    P = round(m1.dot(m2m3AM3M2.dot(M1)), 8)
    print('M1^-1 M2^-1 M3^-1 AM3M2M1:')
    print(P)

    return P
