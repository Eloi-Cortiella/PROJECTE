from main import menu_tipus
from rich.table import Table
import subprocess
from subprocess import PIPE, Popen
import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext

def executar_nmap():

    if menu_tipus == "term":

        def escaneig():

            taula1 = Table(title="Opcions nmap")

            taula1.add_column("Num.", style="bold yellow")
            taula1.add_column("Nom", style="bold green")
            taula1.add_row("1", "Descobrir hosts de xarxa.")
            taula1.add_row("2", "Escaneig de ports oberts.")
            taula1.add_row("3", "Llistat de serveis i versions d'un, un rang o tots els ports.")
            taula1.add_row("4", "Llistat de vulnerabilitats d'un, un rang o tots els serveis.")
            
            opcio = input("\nEscull la opció que desitjis usar: ")

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

    elif menu_tipus == "graf":

        def run_nmap():

            clear_text()
            opcion = nmap_options.get()
            
            if opcion == "Descobrir hosts de xarxa":
                target = input_ip.get()
                cmd = ["nmap", "-sn", target]
            elif opcion == "Escaneig de ports oberts":
                target = input_ip.get()
                cmd = ["nmap", "-n", "-Pn", "-p-", target]
            elif opcion == "Llistat de serveis i versions d'un, un rang o tots els ports":
                target = input_ip.get()
                ports = input_ports.get()
                cmd = ["nmap", "-sCV", "-n", "-Pn", "-p", ports, target]
            elif opcion == "Llistat de vulnerabilitats d'un, un rang o tots els serveis":
                target = input_ip.get()
                cmd = ["nmap", "--script=vuln", target]
            else:
                result_text.insert(tk.END, "Opció no vàlida")
                return

            run_command(cmd)

        def run_command(cmd):

            process = Popen(cmd, stdout=PIPE, stderr=PIPE, text=True)
            stdout, stderr = process.communicate()
            result_text.insert(tk.END, f"Comanda: {' '.join(cmd)}\n")
            result_text.insert(tk.END, stdout)
            result_text.insert(tk.END, stderr)

        def clear_text():

            result_text.delete('1.0', tk.END)

        def update_ip_entry_state(event):

            opcion = nmap_options.get()
            input_ip.config(state=tk.NORMAL if opcion in ["Descobrir hosts de xarxa", "Escaneig de ports oberts", "Llistat de serveis i versions d'un, un rang o tots els ports", "Llistat de vulnerabilitats d'un, un rang o tots els serveis"] else tk.DISABLED)

        root = tk.Tk()
        root.title("Menú NMAP")

        frame = tk.Frame(root)
        frame.pack(padx=20, pady=20)

        # Sección de NMAP a la izquierda
        frame_nmap = tk.Frame(frame)
        frame_nmap.pack(side=tk.LEFT, padx=20, pady=20)

        label_nmap = tk.Label(frame_nmap, text="Selecciona una opció d'NMAP:")
        label_nmap.pack()

        nmap_options = ttk.Combobox(frame_nmap, values=["Descobrir hosts de xarxa", "Escaneig de ports oberts", "Llistat de serveis i versions d'un, un rang o tots els ports", "Llistat de vulnerabilitats d'un, un rang o tots els serveis"], state="readonly")
        nmap_options.current(0)
        nmap_options.pack(pady=5)

        label_ip = tk.Label(frame_nmap, text="Introdueix la IP o xarxa:")
        label_ip.pack()

        input_ip = tk.Entry(frame_nmap, state=tk.DISABLED)
        input_ip.pack(pady=5)

        # Agrega una entrada para el rango de puertos
        label_ports = tk.Label(frame_nmap, text="Introdueix el port o rang de ports (p.e, 80 o 20-100):")
        label_ports.pack()

        input_ports = tk.Entry(frame_nmap)
        input_ports.pack(pady=5)

        # Configura la actualización del estado de la entrada de IP según la opción seleccionada
        nmap_options.bind("<<ComboboxSelected>>", update_ip_entry_state)

        run_nmap_button = tk.Button(frame_nmap, text="Executar NMAP", command=run_nmap)
        run_nmap_button.pack(pady=5)

        # Cuadro de texto para mostrar resultados
        result_label = tk.Label(frame, text="Resultats:")
        result_label.pack(pady=10)

        result_text = scrolledtext.ScrolledText(frame, height=20, width=70)
        result_text.pack(pady=5)

        root.mainloop()