import shodan

SHODAN_API_KEY = '2zHHXdcuY608POXVdGKZXb9fYngNjROO'

def obtenir_informacio_ip(ip):
    api = shodan.Shodan(SHODAN_API_KEY)
    try:
        resultat = api.host(ip)
        return resultat
    except shodan.APIError as e:
        print(f"Error de Shodan: {e}")
        return None

def mostrar_info_general(info):
    if info:
        print(f"IP: {info['ip_str']}")
        print(f"País: {info['country_name']}")
        print(f"Organització: {info.get('org', 'No disponible')}")
        print(f"Sistema Operatiu: {info.get('os', 'No disponible')}")
        print(f"Ports oberts: {', '.join(map(str, info['ports']))}")
        print("\nNoms de domini associats:")
        for dominio in info['hostnames']:
            print(f"  - {dominio}")
    else:
        print("No s'ha trobat informació per a aquesta IP.")

def obtenir_info_servei(port):
    return port.get('name', 'No disponible')

def mostrar_serveis_ports(ip, ports):
    print(f"\nServei amb els ports obertss de {ip}:")
    for port in ports:
        info_servei = obtenir_info_servei(port)
        print(f"Port {port['port']} ({port['transport']}): {info_servei}")

if __name__ == "__main__":
    ip = input("Introdueix la IP a consultar: ")
    info_ip = obtenir_informacio_ip(ip)

    mostrar_info_general(info_ip)

    if info_ip:
        mostrar_serveis_ports(ip, info_ip['data'])
