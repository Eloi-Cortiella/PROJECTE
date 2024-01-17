import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from tkinter import scrolledtext
from subprocess import PIPE, Popen

# Ruta completa al script de Sherlock
SHERLOCK_SCRIPT_PATH = "/home/alumne/Escriptori/PROJECTE/sherlock/sherlock/sherlock.py"

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

def run_osint():
    clear_text()
    option = osint_options.get()

    if option == "Sherlock":
        username = input_username.get()
        cmd = ["python3", SHERLOCK_SCRIPT_PATH, "--print-found", username]
    elif option == "Exiftool":
        image_path = input_image_path.get()
        cmd = ["exiftool", image_path]
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

def ask_image_path():
    file_path = filedialog.askopenfilename()
    input_image_path.delete(0, tk.END)
    input_image_path.insert(tk.END, file_path)

root = tk.Tk()
root.title("Menú de Auditoría de Seguridad")

frame = tk.Frame(root)
frame.pack(padx=20, pady=20)

# Sección de NMAP a la izquierda
frame_nmap = tk.Frame(frame)
frame_nmap.pack(side=tk.LEFT, padx=20, pady=20)

label_nmap = tk.Label(frame_nmap, text="Selecciona una opción de NMAP:")
label_nmap.pack()

nmap_options = ttk.Combobox(frame_nmap, values=["Descobrir hosts de xarxa", "Escaneig de ports oberts", "Llistat de serveis i versions d'un, un rang o tots els ports", "Llistat de vulnerabilitats d'un, un rang o tots els serveis"], state="readonly")
nmap_options.current(0)
nmap_options.pack(pady=5)

label_ip = tk.Label(frame_nmap, text="Introduce la IP o red:")
label_ip.pack()

input_ip = tk.Entry(frame_nmap, state=tk.DISABLED)
input_ip.pack(pady=5)

# Agrega una entrada para el rango de puertos
label_ports = tk.Label(frame_nmap, text="Introduce el puerto o rango de puertos (por ejemplo, 80 o 20-100):")
label_ports.pack()

input_ports = tk.Entry(frame_nmap)
input_ports.pack(pady=5)

# Configura la actualización del estado de la entrada de IP según la opción seleccionada
nmap_options.bind("<<ComboboxSelected>>", update_ip_entry_state)

run_nmap_button = tk.Button(frame_nmap, text="Ejecutar NMAP", command=run_nmap)
run_nmap_button.pack(pady=5)

# Sección de OSINT a la derecha
frame_osint = tk.Frame(frame)
frame_osint.pack(side=tk.RIGHT, padx=20, pady=20)

label_osint = tk.Label(frame_osint, text="Selecciona una opción de OSINT:")
label_osint.pack()

osint_options = ttk.Combobox(frame_osint, values=["Sherlock", "Exiftool"], state="readonly")
osint_options.current(0)
osint_options.pack(pady=5)

# Cuadro de entrada para el nombre de usuario
label_username = tk.Label(frame_osint, text="Introduce el nombre de usuario:")
label_username.pack()

input_username = tk.Entry(frame_osint)
input_username.pack(pady=5)

# Cuadro de entrada para la ruta de la imagen
label_image_path = tk.Label(frame_osint, text="Selecciona la ruta de la imagen:")
label_image_path.pack()

input_image_path = tk.Entry(frame_osint)
input_image_path.pack(pady=5)

# Botón para seleccionar la imagen
select_image_button = tk.Button(frame_osint, text="Seleccionar Imagen", command=ask_image_path)
select_image_button.pack(pady=5)

run_osint_button = tk.Button(frame_osint, text="Ejecutar OSINT", command=run_osint)
run_osint_button.pack(pady=5)

# Cuadro de texto para mostrar resultados
result_label = tk.Label(frame, text="Resultado:")
result_label.pack(pady=10)

result_text = scrolledtext.ScrolledText(frame, height=20, width=70)
result_text.pack(pady=5)

root.mainloop()
