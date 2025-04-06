from sympy import Sum
from sympy.abc import n as sympy_n
import matplotlib.pyplot as plt
import numpy as np
import heapq
#zad1

def wbudowana_suma():
    return Sum(1/sympy_n**2, (sympy_n,1,10**6)).evalf()
def zliczanie_najw():
    suma = 0 
    for n in range(1,10**6+1):
        suma+=1/n**2
    return suma
def zliczanie_najmn():
    suma = 0
    for n in range(10**6,0,-1):
        suma+=1/n**2
    return suma
def sumowanie_najmn():
    h = [1/n**2 for n in range(10**6,0,-1)]
    heapq.heapify(h)
    while len(h)>2:
        elm = heapq.heappop(h)
        elm2 = heapq.heappop(h)
        heapq.heappush(h,elm + elm2)
    return sum(h)

print(f'Wbudowana:\t\t\t\t{wbudowana_suma()}\nZliczanie najmniejsze:\t\t\t{zliczanie_najmn()}\nZliczanie najwieksze:\t\t\t{zliczanie_najw()}\nSumowanie najmniejszych elemetow:\t{sumowanie_najmn()}\n')

#najdokladniejsze sumowanie dwoch najmniejszych elementow, poniewaz dokladnosc dodawania mniejszych elementow jest wieksza
#gdy sumujemy wieksze elementy mamy mniej cyfr znaczacych
print('-------------zad2---------------')
#---------zad2------------
# szereg geom, a1 = 1, q = 1/2
# S = 2(1 - 1/(2^n+1))

def suma():
    return 2*(1- 1/(2**31))
print(f'Skonczona suma: {suma()}')

def wbudowana_suma2():
    return Sum(1/2**sympy_n, (sympy_n,0,30)).evalf()
def zliczanie_najw2():
    suma = 0 
    for n in range(0,30):
        suma+=1/2**n
    return suma
def zliczanie_najmn2():
    suma = 0
    for n in range(30,-1,-1):
        suma+=1/2**n
    return suma
def sumowanie_najmn2():
    h = [1/2**n for n in range(30,-1,-1)]
    heapq.heapify(h)
    while len(h)>2:
        elm = heapq.heappop(h)
        elm2 = heapq.heappop(h)
        heapq.heappush(h,elm + elm2)
    return sum(h)

print(f'Wbudowana:\t\t\t\t{wbudowana_suma2()}\nZliczanie najmniejsze:\t\t\t{zliczanie_najmn2()}\nZliczanie najwieksze:\t\t\t{zliczanie_najw2()}\nSumowanie najmniejszych elemetow:\t{sumowanie_najmn2()}')

#------------zad3-------------
print('---------zad3-----------')

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

def funkcja_zad3(x):
    return np.abs(x)

stopnie = [1,2,5,10,15,20]
def zad3():
    x_plot = np.linspace(-1,1,1000)
    plt.plot(x_plot, funkcja_zad3(x_plot), label='Funkcja y = |x|',linewidth=2)

    for n in stopnie:
        x_wezly = np.linspace(-1,1,n+1)
        y_wezly = funkcja_zad3(x_wezly)
        y_interp = [interpolacje(x_wezly, y_wezly, x) for x in x_plot]
        
        plt.plot(x_plot,y_interp,label=f'Stopień {n}', alpha=0.5)

    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.ylim(-1,2)
    plt.tight_layout()
    plt.show()

#zad3()

#------------zad4-------------

def funkcja_zad4(x):
    return 1/(1+25*(x**2))

def zad4():
    x_plot = np.linspace(-1,1,1000)
    plt.plot(x_plot, funkcja_zad4(x_plot), label='Funkcja y = 1/1+25x^2',linewidth=2)

    for n in stopnie:
        x_wezly = np.linspace(-1,1,n+1)
        y_wezly = funkcja_zad4(x_wezly)
        y_interp = [interpolacje(x_wezly, y_wezly, x) for x in x_plot]
        
        plt.plot(x_plot,y_interp,label=f'Stopień {n}', alpha=0.5)

    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.ylim(-1,2)
    plt.tight_layout()
    plt.show()

    #zad4()