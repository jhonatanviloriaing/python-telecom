equipos = ["switch-chacao-01", "router-core-02", "switch-urbina-03"]
print(equipos[0])
equipos.append("router-antimano-04")
print(f"Total de equipos: {len(equipos)}")
ips = {"switch-chacao-01":"10.20.30.5", "router-core-02":"10.20.30.1", "switch-urbina-03":"10.20.30.9",}
print(ips["switch-chacao-01"])
for hostname, ip in ips.items():
    print(f"equipo: {hostname} --> ip: {ip}")