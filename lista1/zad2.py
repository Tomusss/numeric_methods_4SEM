#zad2 a)
def rek(n):
    x = [1,1/5]
    for i in range(1,n):
        x.append(26/5*x[i]-x[i-1] )
    return x

def rev_rek(n,obliczone_x):
    x = [obliczone_x[n-1],obliczone_x[n-2]]
    for i in range(1,n):
        #x_i = 26/5x_i+1 - x_i+2
        x.append(26/5*x[i]-x[i-1])
    return x
x = rek(30)
x_rev = rev_rek(30,x)
print(f'oryginalnie 1,0.2, po wykonaniu: {x_rev[28]},{x_rev[29]}')

#zad2 b)
def rek2(n):
    x = [1,1/2]
    for i in range(1,n):
        x.append(5/2*x[i]-x[i-1] )
    return x

def rev_rek2(n,obliczone_x):
    x = [obliczone_x[n-1],obliczone_x[n-2]]
    for i in range(1,n):
        #x_i = 5/2x_i+1 - x_i+2
        x.append(5/2*x[i]-x[i-1])
    return x
x2 = rek2(30)
#print(x)
x_rev2 = rev_rek2(30,x2)
#print(x_rev2)
print(f'oryginalnie 1,0.5, po wykonaniu:{x_rev2[28]},{x_rev2[29]}')

#bledy wynikaja z zapisu w systemie 2jkowym, 0.2 jest ulamkiem okresowym przez co komputer uzywa przyblizen
#a 0.5 da sie zapisac jako skonczona liczbe
#wzmacnianie bledu o 5.2 za kazdym razem
