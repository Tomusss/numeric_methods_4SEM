import numpy as np
from scipy.integrate import quad

def iloczyn(x0, lista):
    wynik = 1
    for x in lista:
        wynik*=(x0-x)
    return wynik

def interpolacje(x,y,x0):
    n = len(x)-1
    w = 0
    for i in range(0,len(x)):
        przedzial= np.concatenate([x[:i],x[i+1:]])
        w += y[i] * iloczyn(x0,przedzial)/iloczyn(x[i],przedzial)
    return w 

def metoda_trapezow(a,b,f):
    calka = (b - a) * (f(a) + f(b)) / 2
    return calka

def zad1():
    a,b = 0,1
    wielomiany = [(lambda x: 1, 1.0),
        (lambda x: x, 0.5),
        (lambda x: x**2, 1/3),
        (lambda x: x**3, 0.25)]
    for f, wynik in wielomiany:
        trapezy = metoda_trapezow(a,b,f)
        blad = abs(wynik-trapezy)
        print(f'dokladny wynik: {wynik}, metoda trapezów: {trapezy}, blad: {blad}')

#zad1()

def metoda_parabol(a,b,f):
    h = (b - a)/2
    ab = a+h
    calka = h * (f(a) + f(b)+ 4*f(ab)) / 3
    return calka

def zad2():
    a,b = 0,1
    wielomiany = [(lambda x: 1, 1.0),
        (lambda x: x, 0.5),
        (lambda x: x**2, 1/3),
        (lambda x: x**3, 0.25),
        (lambda x: x**4, 0.2)]
    for f, wynik in wielomiany:
        trapezy = metoda_parabol(a,b,f)
        blad = abs(wynik-trapezy)
        print(f'dokladny wynik: {wynik}, metoda trapezów: {trapezy}, blad: {blad}')

#zad2()

def metoda_romberga(f, a, b, max_iter=10):
    R = np.zeros((max_iter, max_iter))
    h=b-a
    R[0, 0] = (f(a) + f(b)) * h / 2.0

    """for i in range(max_iter):
        n =2**i
        h =(b-a)/n
        fik = 0
        for k in range(0,2**i):
            xik = a+k*h
            fik += f(xik)
        T0i= h*(fik - 0.5 * (f(a) + f(b)))
        R[0, i] = T0i

    for m in range(1, max_iter):
        for i in range(max_iter - m):
            R[m, i] = R[m - 1, i + 1] + (R[m - 1, i + 1] - R[m - 1, i]) / (4**m - 1)"""

    for i in range(1, max_iter):
        h /= 2
        sum_f = sum(f(a+(2*k-1)*h) for k in range(1,2**i // 2 +1))
        R[i,0]= 0.5*R[i-1,0] + h * sum_f

        for k in range(1,i+1):
            R[i,k] = R[i, k-1] + (R[i,k-1] -R[i-1,k-1])/(4**k-1)
    return R

def zad3():
    a,b = 0,1
    wielomiany = [(lambda x: 1, 1.0),
        (lambda x: x, 0.5),
        (lambda x: x**2, 1/3),
        (lambda x: x**3, 0.25),
        (lambda x: x**4, 0.2)]
    for f, wynik in wielomiany:
        rom = metoda_romberga(f,a,b)
        print(rom)
        #blad = abs(wynik-rom)
        #print(f'dokladny wynik: {wynik}, metoda romberga: {rom}, blad: {blad}')

#zad3()
def zad4():
    a,b = 0,1
    wielomiany = [('1',lambda x: 1, 1.0),
        ('x',lambda x: x, 0.5),
        ('x^2',lambda x: x**2, 1/3),
        ('x^3',lambda x: x**3, 0.25),
        ('x^4',lambda x: x**4, 0.2),
        ("sin(x)", np.sin, 1 - np.cos(1)),
        ("exp(x)", np.exp, np.exp(1) - 1)]
    for wzor,f, wynik in wielomiany:
        rom = metoda_romberga(f,a,b)[-1,-1]
        blad = abs(wynik-rom)
        print(f'funkcja: {wzor}, dokladny wynik: {wynik}, metoda romberga: {rom}, blad: {blad}')

#zad4()

def metoda_rombergaMOD(f, a, b, max_iter=10, epsilon = 1e-8):
    R = np.zeros((max_iter, max_iter))
    h=b-a
    R[0, 0] = (f(a) + f(b)) * h / 2.0

    """for i in range(max_iter):
        n =2**i
        h =(b-a)/n
        fik = 0
        for k in range(0,2**i):
            xik = a+k*h
            fik += f(xik)
        T0i= h*(fik - 0.5 * (f(a) + f(b)))
        R[0, i] = T0i

    for m in range(1, max_iter):
        for i in range(max_iter - m):
            R[m, i] = R[m - 1, i + 1] + (R[m - 1, i + 1] - R[m - 1, i]) / (4**m - 1)
"""
    for i in range(1, max_iter):
        h /= 2
        sum_f = sum(f(a+(2*k-1)*h) for k in range(1,2**i // 2 +1))
        R[i,0]= 0.5*R[i-1,0] + h * sum_f

        for k in range(1,i+1):
            R[i,k] = R[i, k-1] + (R[i,k-1] -R[i-1,k-1])/(4**k-1)
        if abs(R[i,i]-R[i-1,i-1]) < epsilon:
            return (R[i,i])

def zad5():
    a,b = 0,1
    wielomiany = [('1',lambda x: 1, 1.0),
        ('x',lambda x: x, 0.5),
        ('x^2',lambda x: x**2, 1/3),
        ('x^3',lambda x: x**3, 0.25),
        ('x^4',lambda x: x**4, 0.2),
        ("sin(x)", np.sin, 1 - np.cos(1)),
        ("exp(x)", np.exp, np.exp(1) - 1)]
    for wzor,f, wynik in wielomiany:
        rom = metoda_rombergaMOD(f,a,b)
        quad_wynik = quad(f, a, b)[0]
        blad = abs(wynik-rom)
        bladq = abs(quad_wynik-wynik)
        print(f'funkcja: {wzor}, dokladny wynik: {wynik}, metoda romberga blad: {blad}, wbudowana blad:{bladq}')

#zad5()
