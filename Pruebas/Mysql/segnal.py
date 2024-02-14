from RouterOS_api import RouterOS_api as ROS

# Conectarse al router
connection = ROS.RouterOS_api()
connection.connect('10.31.0.2', 'thiago', 'ranger')

# Lista de direcciones IP
ip_list = ["192.168.1.2", "192.168.1.3", "192.168.1.4"]

# Enviar comando "interface wireless reg-table print" para cada dirección IP
for ip in ip_list:
    connection.talk(f"/ip/hotspot/user/profile/print address={ip}")
    result = connection.talk("interface wireless reg-table print")
    print(f"Resultados para {ip}:")
    print(result)
