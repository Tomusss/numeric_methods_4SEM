def epsilon():
    e = 1 
    while e + 1>1:
        e=e/2
    return e*2
ep = epsilon()

def epsilon_a(a):
    e = 1
    while a + e >a:
        e = e/2
    return e*2
l = [10**x for x in range(1,5)]
l.insert(0,1)
for el in l:
    print(f'Dla a = {el}: epsilon = {epsilon_a(el)}')
