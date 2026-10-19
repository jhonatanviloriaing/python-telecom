print("+++++++BUSCADOR DE IPS DE LOS EQUIPOS+++++")
ips = {"Router-chacao":"192.168.104.1", "Switch-artigas":"192.168.104.2", "Router-Antimano":"192.168.104.3"}
hostname = input("Escribe el hostname: ")
print(ips[hostname])