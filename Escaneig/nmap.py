import subprocess

def escaneig():
    print("Selecciona una opció:\n")
    print("1. Descobrir hosts de xarxa.")
    print("2. Escaneig de ports oberts.")
    print("3. Llistat de serveis i versions d'un, un rang o tots els ports.")
    print("4. Llistat de vulnerabilitats d'un, un rang o tots els serveis.")
    
    opcio = input("\nOpció: ")

    if opcio == "1":
        target = input("Introdueix la xarxa a escanejar (p. ex., 192.168.1.0/24): ")
        subprocess.run(["nmap", "-sn", target])

    elif opcio == "2":
        target = input("Introdueix l'adreça IP a escanejar: ")
        subprocess.run(["nmap", "-n", "-Pn", "-p-", target])

    elif opcio == "3":
        target = input("Introdueix l'adreça IP a escanejar: ")
        ports = input("Introdueix el port o rang de ports (p. ex., 80 o 20-100): ")
        subprocess.run(["nmap", "-sCV", "-n", "-Pn", "-p", ports, target])

    elif opcio == "4":
        target = input("Introdueix l'adreça IP a escanejar: ")
        subprocess.run(["nmap", "--script=vuln", target])

    else:
        print("Opció no vàlida")

if __name__ == "__main__":
    escaneig()