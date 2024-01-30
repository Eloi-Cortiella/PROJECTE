from subprocess import PIPE, Popen
import tkinter as tk
from tkinter import PhotoImage
import time

subprocess_command = f"/ScriptsINterficieGràfica/app.y"

'''print("""
.______   .______        ______          __   _______   ______ .___________. _______     _______  ____   
|   _  \  |   _  \      /  __  \        |  | |   ____| /      ||           ||   ____|   |   ____||___ \  
|  |_)  | |  |_)  |    |  |  |  |       |  | |  |__   |  ,----'`---|  |----`|  |__      |  |__     __) | 
|   ___/  |      /     |  |  |  | .--.  |  | |   __|  |  |         |  |     |   __|     |   __|   |__ <  
|  |      |  |\  \----.|  `--'  | |  `--'  | |  |____ |  `----.    |  |     |  |____    |  |____  ___) |
| _|      | _| `._____| \______/   \______/  |_______| \______|    |__|     |_______|   |_______||____/
""")'''

time.sleep(2)

def crear_interfaz(master):
        # Configurar el esquema de colores
        master.configure(bg='#2c3e50')  # Color de fondo de la ventana principal
        
        logo = PhotoImage(file="/home/alumne/Escriptori/Moodle_2N/PROJECTE/img/Logo_empresa.png")

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
            boton = tk.Button(master, text=nombre, command=lambda n=nombre: presionar_boton(n))
            boton.pack(pady=5)

        label_imatge = tk.Label(master, image=logo, bg='#2c3e50')
        label_imatge.pack(anchor='nw')

def presionar_boton(nombre):
    print(f"Presionaste el botón: {nombre}")
    
if __name__ == "__main__":
    ventana_principal = tk.Tk()
    ventana_principal.title("PROJECTE ASIX")
    ventana_principal.geometry("800x300")  # Tamaño de la ventana principal

    crear_interfaz(ventana_principal)

    ventana_principal.mainloop()