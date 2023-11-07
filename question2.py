from math import sqrt

# d ==> delta

def delta(a,b,c):
    return (pow(b,2) - 4*a*c)

def NombreRacine(a, b, c):
    if a == 0:
        return 1
    d = delta(a, b, c)
    return 0 if d < 0 else ( 1 if d == 0 else 2 )


def AfficheNombreRacine(a, b, c):
    d = delta(a,b,c)
    print(f"Le nombre des solutions est : {NombreRacine(a, b, c)}")


def Racines(a, b, c):
    d = delta(a, b, c)
    racine1, racine2 = -1, -1

    if a == 0 and b!=0:
        racine1 = -c/b 
    elif a == 0 and b == 0:
            print("!!!!!!!!!!!!")
    elif NombreRacine(a, b, c) != 0:
        if d == 0:
            racine1 = -b/2*a
        elif d > 0:
            racine1 = (-b + sqrt(d))/2*a
            racine2 = (-b - sqrt(d))/2*a
    else:
        print("Il n'y a pas de solution dans |R")

    return racine1, racine2


def main() :
    print("Une equation de deuxieme degre s'ecrit sous la forme : ax^2 + bx + c")
    a = float(input("Entrer la valeur de a : "))
    b = float(input("Entrer la valeur de b : "))
    c = float(input("Entrer la valeur de c : "))

    AfficheNombreRacine(a, b, c)

    racine1, racine2 = Racines(a, b, c)
    racines = [racine1, racine2]
    print("Les solutions : ", end=" ")
    [print("{:.2f}".format(racine), end=", ") if racine != -1 else "" for racine in racines]



if __name__ == "__main__":
    main()