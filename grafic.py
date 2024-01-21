import tkinter as tk
from rich import print
import time

class AplicacionTkinterRich:
    def __init__(self, master):
        self.master = master
        master.title("PROJECTE ASIX")
        master.geometry("800x330")
        self.crear_interfaz()

    def crear_interfaz(self):
        nombres_botones = [
            "Api Shodan",
            "The Harvester",
            "Més OSINT",
            "Escaneig",
            "Auditoria SSH",
            "Enumeració",
            "Bot de Telegram",
            "Sortir"
        ]

        for nombre in nombres_botones:
            boton = tk.Button(self.master, text=nombre, command=lambda n=nombre: self.ejecutar_opcion(n))
            boton.pack(pady=5)

    def ejecutar_opcion(self, opcion):
        try:
            opciones = {
                "Api Shodan": 1,
                "The Harvester": 2,
                "Més OSINT": 3,
                "Escaneig": 4,
                "Auditoria SSH": 5,
                "Enumeració": 6,
                "Bot de Telegram": 7,
            }
            opcion_seleccionada = opciones.get(opcion)
            if opcion_seleccionada is not None:
                time.sleep(3)
                print(f"Iniciant: {opcion}")
                time.sleep(3)
                # Llama a la función correspondiente según la opción seleccionada
                self.ejecutar_opcion_terminal(opcion_seleccionada)
            else:
                print(f"Opción no válida: {opcion}")
        except Exception as e:
            print(e)

    def ejecutar_opcion_terminal(self, opcion):
        # Función para ejecutar la opción en la versión terminal
        pass

if __name__ == "__main__":
    ventana_principal = tk.Tk()
    app = AplicacionTkinterRich(ventana_principal)
    ventana_principal.mainloop()
