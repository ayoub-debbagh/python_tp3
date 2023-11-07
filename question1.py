
def somme(m, n):
    l = []
    if m > n:
        c = m
        m = n
        n = c
    for i in range(m, n+1):
        l.append(i)

    return sum(l)

m = int(input("Entrer le debut : "))
n = int(input("Entrer la fin : "))



print(f"La somme des entiers entre {m} et {n} est : {somme(m, n)}")


