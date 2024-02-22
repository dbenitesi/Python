from librouteros import connect

# Configura tus credenciales y la dirección IP de tu equipo MikroTik
host = '10.185.1.2'
username = 'thiago'
password = 'ranger'

try:
    # Crea una conexión con el equipo MikroTik
    connection = connect(host=host, username=username, password=password)

    # Envía el comando y obtén la respuesta
    response = connection(cmd='/ip/address/print')

    # Imprime la respuesta
    for item in response:
        print(item)

except Exception as e:
    print("Error:", e)

finally:
    # Cierra la conexión
    if 'connection' in locals():
        connection.close()
