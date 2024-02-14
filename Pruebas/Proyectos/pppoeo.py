# Este es un programa para la creacion de PPPoe sin vlan

print(str("Welcome to the automatitation Of The creation of Pppoes").title())
print(f"               By Daniel Benites\n")

# Ask the user for the Vlan

#vlan_name = input("Please type the Vlan name: ")
#vlan_id = input("Please asign a vlan Id: ")
#pppoe_server = input("Please input the name server")
pppoe_user = input("Please Input the pppoe_user: ")
pppoe_pass = input("Please input the pppoe Password: ")
client_name = input("Please input the Client Name: ")
clien_name = client_name.replace( " ", "_")
cli_name = "CPE_" +  clien_name
sabanilla_zona = ["VLAN72 - CLIENTES", "72", "N3xtS7", "Sabanilla"]



print(f"""\n \n/interface vlan
add interface=wlan1 name={vlan_name} vlan-id={vlan_id}
/interface pppoe-client
add add-default-route=yes disabled=no interface={vlan_name} name=pppoe-out1 VLANpassword={pppoe_pass} service-name={pppoe_server} user={pppoe_user}
/ip address add address=10.10.10.1/29 interface=ether1 network=10.10.10.0
/ip dhcp-server network add address=10.10.10.0/29 dns-server=8.8.8.8 gateway=10.10.10.1
/ip dns set servers=8.8.8.8
/ip firewall nat add action=masquerade chain=srcnat
/snmp set contact="{clien_name}" enabled=yes location="{clien_name}" trap-community=nextcore@red trap-generators=interfaces trap-interfaces=all trap-version=2
/system clock set time-zone-name=America/Guayaquil
/system identity set name={cli_name}


/user add name=thiago password=ranger group=full
/user add name=soporte password=c0vid group=full

""")