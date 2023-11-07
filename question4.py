import question3

h = int(input("Entrer le nombre des heures : "))
m = int(input("Entrer le nombre des minutes : "))
s = int(input("Nombre des secondes : "))

print("{}h {}m {}s en secondes est : {}s".format(h, m, s, question3.conversion_temps(h, m, s)))