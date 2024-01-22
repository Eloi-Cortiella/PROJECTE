from subprocess import PIPE, Popen
import tkinter as tk
from tkinter import messagebox
import time
from Auditoria_de_serveis.Enum4linux.enumeracio import executar_enum4linux
from Fase_reconeixement.TheHarvester import the_harvester
from Escaneig.nmap import executar_nmap
from rich import print
from rich.table import Table
from rich.traceback import install
install()

subprocess_command = f"/ScriptsINterficieGràfica/app.y"

print("""[bold yellow]
.______   .______        ______          __   _______   ______ .___________. _______     _______  ____   
|   _  \  |   _  \      /  __  \        |  | |   ____| /      ||           ||   ____|   |   ____||___ \  
|  |_)  | |  |_)  |    |  |  |  |       |  | |  |__   |  ,----'`---|  |----`|  |__      |  |__     __) | 
|   ___/  |      /     |  |  |  | .--.  |  | |   __|  |  |         |  |     |   __|     |   __|   |__ <  
|  |      |  |\  \----.|  `--'  | |  `--'  | |  |____ |  `----.    |  |     |  |____    |  |____  ___) | 
| _|      | _| `._____| \______/   \______/  |_______| \______|    |__|     |_______|   |_______||____/
""")

time.sleep(2)

tipus = Table(title="\nTipus menu")
tipus.add_column("Opció menu", style="bold green")
tipus.add_column("Nom", style="bold cyan")
tipus.add_column("Descripció", style="bold white")
tipus.add_row("term","Menú en terminal","Les eines s'executaràn en terminal")
tipus.add_row("graf","Menú gràfic","Les eines s'executen gràficament amb la llibreria Tkinter")

print(tipus)

menu_tipus = str(input("\nEscull el tipus de menú en el que vulguis treballar: "))

time.sleep(1.5)

print("Has escollit:", menu_tipus+". Iniciant menu...")

time.sleep(2)

if menu_tipus == "term":
    def executar_opcio_terminal():
        global menu_tipus

        # Crear una taual amb Rich
        table = Table(title="Eines disponibles")
        table.add_column("Num", style="bold magenta")
        table.add_column("Eina", justify="center", style="bold")
        table.add_column("Descripció", justify="left", style="bold cyan")
        table.add_row("1", "[green]Més Osint", "Una eina d'Open Source Intelligence (OSINT) que amplia la recopilació d'informació oberta per a anàlisi i investigació.")
        table.add_row("2", "[blue]Api Shodan", "Una interfície de programació d'aplicacions que ofereix accés a la base de dades de Shodan, permetent la cerca d'equips i dispositius connectats a Internet.")
        table.add_row("3", "[yellow]Enumeració", "Recopilació i llistat de detalls o informació relativa a sistemes informàtics, com ara noms d'usuari o recursos accessibles.")
        table.add_row("4", "[red]Bot Telegram", "Programa automatitzat a la plataforma de missatgeria Telegram que pot realitzar diverses funcions o proporcionar informació mitjançant comandes.")
        table.add_row("5", "[violet]Auditoria SSH", "Conjunt de procediments per avaluació de la seguretat del protocol SSH (Secure Shell) per assegurar que les connexions siguin segures i protegides contra vulnerabilitats.")
        table.add_row("6", "[black]Escaneig", "Pràctica de revisar una xarxa informàtica per identificar actius, obertures de seguretat o altres elements rellevants, generalment mitjançant eines automatitzades.")
        table.add_row("7", "[cyan]The Harvester", "Eina de recopilació d'informació que permet la cerca i extracció de dades sobre dominis, correus electrònics i altres elements relacionats amb la seguretat informàtica.")
        table.add_row("8", "[brown]Enumeració", "Eina específica per a sistemes basats en Linux que es fa servir per a la enumeració i recopilació d'informació en entorns Windows amb el protocol SMB (Server Message Block).")
        
        print(table)

        opcion = int(input("\nEscull l'eina a executar: "))

        try:
            if opcion == 1:
                time.sleep(3)
                print("Iniciant: Més Osint")
                time.sleep(3)
            elif opcion == 2:
                time.sleep(3)
                print("Iniciant: ApiShodan")
                time.sleep(3)
            elif opcion == 3:
                time.sleep(3)
                print("Iniciant: Telegram")
                time.sleep(3)
            elif opcion == 4:
                time.sleep(3)
                print("Iniciant: Auditoria SSH")
                time.sleep(3)
            elif opcion == 5:
                print("Iniciant:")
            elif opcion == 6:
                time.sleep(3)
                print("Iniciant: Escaneig")
                time.sleep(3)
                executar_nmap() 
            elif opcion == 7:
                time.sleep(3)
                print("Iniciant: theHarvester")
                time.sleep(3)
                the_harvester()
            elif opcion == 8:
                time.sleep(1.5)
                print("Iniciant: Enum4linux")
                time.sleep(1.5)
                executar_enum4linux()
        except Exception as e:
            print(e)
    
    executar_opcio_terminal()

elif menu_tipus == "graf":

    class AplicacionTkinterRich:

        global menu_tipus

        def __init__(self, master):
            self.master = master
            master.title("PROJECTE ASIX")
            master.geometry("800x300")  # Tamaño de la ventana principal

            self.crear_interfaz()

        def crear_interfaz(self):
            # Configurar el esquema de colores
            self.master.configure(bg='#2c3e50')  # Color de fondo de la ventana principal

            # Lista de nombres de botones
            nombres_botones = [
                "Api Shodan",
                "The Harvester",
                "Més OSINT",
                "Escaneig",
                "Auditoria SSH",
                "Enumeració",
                "Bot de Telegram"
            ]

            # Crear y colocar los botones en la ventana con comandos incorporados
            for nombre in nombres_botones:
                boton = tk.Button(ventana_principal, text=nombre, command=lambda n=nombre: print(f"Presionaste el botón: {n}"))
                boton.pack(pady=5)

        

    if __name__ == "__main__":
        ventana_principal = tk.Tk()
        app = AplicacionTkinterRich(ventana_principal)
        ventana_principal.mainloop()
