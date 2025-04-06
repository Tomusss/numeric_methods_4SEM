import matplotlib.pyplot as plt 
import numpy as np

X = np.linspace(1 - 1e-3, 1 + 1e-3, 100)

def f1(x):
    y = (x-1)**4
    return y

def f2(x):
    y = x**4 - 4*x**3 + 6*x**2 - 4*x + 1
    return y

y1 = [f1(x) for x in X]
y2 = [f2(x) for x in X]
y = [f1(x) - f2(x) for x in X]
for x in range(0,len(X)):
    print(f'x={X[x]}, f1: {y1[x]}, f2: {y2[x]}')

plt.plot(X,y1)
plt.xlabel("x")
plt.ylabel("Funkcja1 - funkcja2")
plt.show()

#mniejsza dokladnosc dla funkcji2 okolicach 1, kolejne dzialania zmniejszaja dokladnosc i sprawiaja ze komputer zaokragla do 0  