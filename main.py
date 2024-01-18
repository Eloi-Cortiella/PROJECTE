import tkinter as tk
from tkinter import messagebox
import time
from Auditoria_de_serveis.Enum4linux.enumeracio import executar_enum4linux
from Fase_reconeixement.TheHarvester import lanzar_the_harvester
from rich.console import Console
from rich import print
from rich.table import Table
from rich.traceback import install
install()

class AplicacionTkinterRich:
    def __init__(self, master):
        self.master = master
        master.title("Tkinter con Rich")
        master.geometry("800x600")  # Tamaño de la ventana principal

        self.crear_interfaz()

    def crear_interfaz(self):
        # Configurar el esquema de colores
        self.master.configure(bg='#2c3e50')  # Color de fondo de la ventana principal
        boton_color = '#3498db'  # Color de fondo de los botones
        texto_color = 'white'  # Color del texto de los botones

        # Crear una tabla con Rich
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

        # Crear botones para cada opción con colores personalizados
        for i in range(1, 9):
            btn = tk.Button(self.master, text=f"Opció {i}", command=lambda i=i: self.ejecutar_opcion(i),
                            bg=boton_color, fg=texto_color)
            btn.pack(pady=10)

    def ejecutar_opcion(self, opcion):
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
            elif opcion == 7:
                time.sleep(3)
                print("Iniciant: theHarvester")
                time.sleep(3)
                lanzar_the_harvester()
            elif opcion == 8:
                time.sleep(1.5)
                print("Iniciant: Enum4linux")
                time.sleep(1.5)
                executar_enum4linux()
        except Exception as e:
            print(e)

if __name__ == "__main__":
    ventana_principal = tk.Tk()
    app = AplicacionTkinterRich(ventana_principal)
    ventana_principal.mainloop()
