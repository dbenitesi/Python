#Program that configures a CPE with VLAN - WIRELESS - PPPOE
import os
import pyperclip


def addToClipBoard(text):
    command = 'echo ' + text.strip() + '| clip'
    os.system(command)

print("Por favor seleccione la zona deseada")
print("Para PC Zona 241 - Digite el 1")
print("Para PC Zona 242 - Digite el 2")
print("Para PC Zona 243 - Digite el 3")
print("Para PC Zona 244 - Digite el 4")
print("Para PC Zona 246 - Digite el 5")



zone_value = input("Digite la opcion que desea: ")
vlan_id= 0
service_name = ""
vlan_name = ""
commands_vlan_service = f'interface vlan add name={vlan_name} vlan-id={vlan_id} interface=wlan1\n \\ninterface pppoe-client add service-name={service_name} interface{vlan_name}\ninterface pppoe-client enable 0'



if zone_value == "1":
    print("Ud. ha elegido PC Zona 241")
    vlan_id = 241
    service_name = "N3xtSPC1"
    vlan_name= "VLAN241-CLIENTES"
    resultado =  f"Su vlan es {vlan_id} y su service name es {service_name}"
    commands_vlan_service = f'\interface vlan add name={vlan_name} vlan-id={vlan_id} interface=wlan1 \n\interface pppoe-client add service-name={service_name} interface{vlan_name} \n\interface pppoe-client enable 0'
    pyperclip.copy(commands_vlan_service)
    print(commands_vlan_service)

else:
    print("No ha escogido una zona valida")

