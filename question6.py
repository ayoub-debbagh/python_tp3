from question3 import conversion_temps
from question5 import conversion_distance

# les parametres doivent etre passe sous forme d'un tuple
# dist et temps se sont des tuples
def vitesse(dist, temps):
    d = conversion_distance(dist[0], dist[1], dist[2])
    t = conversion_temps(temps[0], temps[1], temps[2])
    return d/t



def main():
    h   = int(input("nombre des heures : "))
    mn  = int(input("nombre des minutes : "))
    s   = int(input("nombre de secondes : "))
    km  = int(input("combien de Km : "))
    mtr = int(input("combien de metre : "))
    cm  = int(input("combien de cm : "))
    print("La vitesse moyenne c'est : {} (m/s)".format(vitesse((km, mtr, cm), (h,mn,s))))

if __name__ == "__main__":
    main()
