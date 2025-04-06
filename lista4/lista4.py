# zad1
import numpy as np

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

zadanie1()

def zadanie2():
    a = 0