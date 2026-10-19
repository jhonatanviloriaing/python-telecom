print("+++++++BUSCADOR DE IPS DE LOS EQUIPOS+++++")
ips = {"Router-chacao":"192.168.104.1", "Switch-artigas":"192.168.104.2", "Router-Antimano":"192.168.104.3"}
hostname = input("Escribe el hostname: ")
print(ips[hostname])
while True:
    nombre = input("dame el hostname que buscas o ~ salir ~: ")
    if nombre == "Router-chacao":
        print(ips["Router-chacao"])
    elif nombre == "Switch-artigas":
        print(ips["Switch-artigas"])
    elif nombre == "Router-Antimano":
        print(ips["Router-Antimano"])
    elif nombre == "salir":
        break
    else:
        print("Equipo no encontrado")
print("chauuu")