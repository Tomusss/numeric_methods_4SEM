import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline

def f1(x):
    return np.abs(x)

def f2(x):
    return 1 / (1 + 25 * x**2)

def zadanie1():
    stopnie = [1,2,5,10,20]
    x = np.linspace(-1, 1, 100)
    y = [f1(y) for y in x]
    
    plt.figure(figsize=(10, 6))
    plt.plot(x, y, label='y = |x|', color='black', linewidth=2)
    
    for degree in stopnie:
        c = np.polyfit(x, y, degree)
        p = np.poly1d(c)
        plt.plot(x, p(x), label=f'Stopień {degree}', alpha=0.7)
    
    plt.title('Aproksymacja wielomianowa funkcji y = |x|')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.grid()
    plt.show()

#zadanie1()

def zadanie2():
    stopnie = [1,2,5,10,20]
    x = np.linspace(-1, 1, 100)
    y = [f2(y) for y in x]
    
    plt.figure(figsize=(10, 6))
    plt.plot(x, y, label='y = |x|', color='black', linewidth=2)
    
    for degree in stopnie:
        c = np.polyfit(x, y, degree)
        p = np.poly1d(c)
        plt.plot(x, p(x), label=f'Stopień {degree}', alpha=0.7)
    
    plt.title('Aproksymacja wielomianowa funkcji y = 1 /(1+25)*x^2')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.grid()
    plt.show()

#zadanie2()

def zadanie3():
    odcinki = [2,5,10,20]
    x = np.linspace(-1, 1, 100)
    y = f1(x)
    
    plt.figure(figsize=(10, 6))
    plt.plot(x, y, label='y = |x|', color='black', linewidth=2)
    
    for n in odcinki:
        xx = np.linspace(-1,1,n)
        yy = f1(xx)
        cs = CubicSpline(xx, yy, bc_type='natural')
        plt.plot(x, cs(x), label=f'{n} punktów', alpha=0.6)
    
    plt.title('Interpolacja sklejana funkcji y = |x|')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.grid()
    plt.show()

#zadanie3()

def zadanie4():
    odcinki = [2,5,10,20]
    x = np.linspace(-1, 1, 100)
    y = f2(x)
    
    plt.figure(figsize=(10, 6))
    plt.plot(x, y, label='y = 1 /(1+25)*x^2', color='black', linewidth=2)
    
    for n in odcinki:
        xx = np.linspace(-1,1,n)
        yy = f2(xx)
        cs = CubicSpline(xx, yy, bc_type='natural')
        plt.plot(x, cs(x), label=f'{n} punktów', alpha=0.6)
    
    plt.title('Interpolacja sklejana funkcji y = 1 /(1+25)*x^2')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.grid()
    plt.show()

#zadanie4()

def zadanie5():
    def f3(x):
        return 40 + 10*x + 5*x**2 + 3*x**3 + 2*x**4 + x**5 + x**6
    xk = np.array([1,2,3,4,5,6,7])
    yk = f3(xk)  
    x = np.linspace(-1, 8, 200)  
    coeffs = np.polyfit(xk, yk, 6)
    poly_approx = np.polyval(coeffs, x)
    ya = np.polyval(coeffs, xk)


    plt.figure()
    plt.plot(x, f3(x), label='Oryginalna funkcja', color='black', linewidth=2)
    plt.plot(x, poly_approx, label='Aproksymacja stopnia 6')
    plt.scatter(xk,yk,color='red', label='Punkty aproksymacji')
    plt.legend()
    plt.title('Aproksymacja wielomianem stopnia 6')
    plt.show()
    print(coeffs)
    print('-------')
    print(yk)
    print('-------')
    print(ya)
    print('-------')

zadanie5()