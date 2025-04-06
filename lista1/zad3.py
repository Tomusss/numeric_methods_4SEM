import matplotlib.pyplot as plt 
X = [10**x for x in range(4,11)]

def funkcja1(x):
    y = x - (1+x**2)**0.5
    return y

def funkcja2(x):
    y = -1/(x + (1+x**2)**0.5)
    return y

y1 = [funkcja1(x) for x in X]
y2 = [funkcja2(x) for x in X]
y = [funkcja1(x) - funkcja2(x) for x in X]
for x in range(0,len(X)):
    print(f'x={x}, f1: {y1[x]}, f2: {y2[x]}')

plt.plot(X,y1)
plt.xscale("log")
plt.xlabel("x")
plt.ylabel("Funkcja1 - funkcja2")
plt.show()

#mniejsza dokladnosc dla funkcji 1