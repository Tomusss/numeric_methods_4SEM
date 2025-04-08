# zad1
import numpy as np
from scipy.sparse.linalg import gmres
from numpy.linalg import norm
def zadanie1():
    A = [   [1,1,2,1], 
            [0,1,4,3],
            [4,6,8,6],
            [5,5,-5,5]]
    
    B =[    [2,1,1,2],
            [1,2,1,2],
            [2,1,2,1],
            [2,2,2,2]]

    det_a = np.linalg.det(A)
    det_b = np.linalg.det(B)

    print(det_a,det_b)

#zadanie1()

def zadanie2():
        A = np.array([
        [1, 1/2, 1/3, 1/4, 1/5],
        [1/2, 1/3, 1/4, 1/5, 1/6],
        [1/3, 1/4, 1/5, 1/6, 1/7],
        [1/4, 1/5, 1/6, 1/7, 1/8],
        [1/5, 1/6, 1/7, 1/8, 1/9]
        ])

        b = np.array([137/60, 29/20, 153/140, 743/840, 1879/2520])

        x = np.linalg.solve(A, b)
        r = np.max(np.abs(A @ x - b))
        
        print("Rozwiązanie x:", x)
        print("roznica: ", r)


zadanie2()