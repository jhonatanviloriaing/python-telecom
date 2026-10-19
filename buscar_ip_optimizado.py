print("+++++++BUSCADOR DE IPS DE LOS EQUIPOS+++++")
ips = {"Router-chacao":"192.168.104.1", "Switch-artigas":"192.168.104.2", "Router-Antimano":"192.168.104.3"}

while True:
    nombre = input("dame el hostname que buscas o ~ salir ~: ")
    if nombre == "salir":
        break
    elif nombre in ips:
        print(ips[nombre])
    else:
        print("Equipo no encontrado")

print("chauuu")
