import numpy as np
import matplotlib.pyplot as plt


def matrix_mul(A, B):
    return np.matmul (A, B)

def display_plot (mx, num, nrows=2, ncolns=3):
    plt.subplot(nrows, ncolns, num)
    plt.plot(mx[0], mx[1], "xk", linestyle='-')


A = [[1, 0.5], [0, 1]]
B = [[1, 1, 1.5, 1.5, 2, 2], [2, 4, 4, 2.5, 2.5, 2]]

C = B
C[0].append(B[0][0])
C[1].append(B[1][0])

display_plot (C, 1)

rt_mx = matrix_mul(A,B)
display_plot(rt_mx, 2)


A1 = [[1, -0.5], [0, 1]]
lt_mx =  matrix_mul(A1,B)
display_plot(lt_mx, 3)


A2 = [[1, 0], [0.5, 1]]
C3 = matrix_mul(A2,B)
display_plot(C3, 4)

A3 = [[1, 0], [-0.5, 1]]
C3 = matrix_mul(A3,B)
display_plot(C3, 5)

A3 = [[-1, 0.5], [0, 1]]
C3 = matrix_mul(A3,B)
display_plot(C3, 6)

plt.show()
