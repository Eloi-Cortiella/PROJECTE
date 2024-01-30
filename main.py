from customtkinter import *
import tkinter as tk
from tkinter import *
from PIL import Image
from subprocess import PIPE, Popen


# Crear interficie grafica amb customtkinter
app = CTk()

# Configuracions finestra
app.title("PROJECTE E3")
app.geometry("1230x500")
app._set_appearance_mode("dark")

# Ruta completa al script de Sherlock
SHERLOCK_SCRIPT_PATH = "./Escaneig/sherlock/sherlock/sherlock.py"

# Variables

# FUNCIONS

## Funció executar botó

def exit_boto():
    app.destroy()

## Funció nmap

def run_nmap():
    clear_text()
    opcion = options_nmap['values']
    print(opcion)
    if opcion == "Descobrir hosts de xarxa":
        # target = variable.get()
        cmd = ["nmap", "-sn", target]
    elif opcion.get() == "Escaneig de ports oberts":
        target = entry_nmap_ip.get()
        cmd = ["nmap", "-n", "-Pn", "-p-", target]
    elif opcion == "Llistat de serveis i versions d'un, un rang o tots els ports":
        target = entry_nmap_ip.get()
        # ports = variable2.get()
        # cmd = ["nmap", "-sCV", "-n", "-Pn", "-p", ports, target]
    elif opcion == "Llistat de vulnerabilitats d'un, un rang o tots els serveis":
        target = entry_nmap_ip.get()
        cmd = ["nmap", "--script=vuln", target]
    else:
        resultats_text.insert(tk.END, "Opció no vàlida")
        return

## Funció OSINT

def run_osint():
    clear_text()
    option = options_osint.get()

    if option == "Sherlock":
        username = entry_input_username.get()
        cmd = ["python3", SHERLOCK_SCRIPT_PATH, "--print-found", username]
    elif option == "Exiftool":
        image_path = entry_input_image_path.get()
        cmd = ["exiftool", image_path]
    else:
        resultats_text.insert(tk.END, "Opció no vàlida")
        return

## Funció buidar text

def clear_text():
    resultats_text.delete('1.0', tk.END)

def update_ip_entry_state(event):
    opcion = options_nmap.get()
    entry_nmap_ip.config(state=tk.NORMAL if opcion in ["Descobrir hosts de xarxa", "Escaneig de ports oberts", "Llistat de serveis i versions d'un, un rang o tots els ports", "Llistat de vulnerabilitats d'un, un rang o tots els serveis"] else CTk.DISABLED)


## Funcions TheHarvester

'''
def the_harvester():
    logging.basicConfig(filename='error.log', level=logging.INFO)

    print("\n[bold green]The Harvester[/bold green]\n")
    time.sleep(1)

    print(table1)

    objetiu = get_user_input("\nIntrodueix l'objectiu (p.e. un domini o una adreça IP): ")

    parametres = []
    while True:
        parametre = get_user_input("Introdueix un paràmetre (p.e. '-d' o '-l', o 'stop' per finalitzar i executar la comanda): ")
        if parametre == "stop":
            break
        elif parametre_valid(parametre):
            valor = get_user_input(f"Introdueix el valor per al paràmetre {parametre}: ")
            parametres.append(f"{parametre} {valor}")
        else:
            print("Paràmetre no vàlid. Torna-ho a intentar o escriu 'stop' per finalitzar.")

    subprocess_command = ["./Fase_reconeixement/theHarvester/theHarvester.py", "-d", objetiu] + parametres

    try:
        output = subprocess.check_output(subprocess_command, text=True)
        with open("resultats_theharvester.txt", "w") as arxiu:
            arxiu.write(output)
        print("\n[bold cyan]Resultats guardats a 'resultats_theharvester.txt'[bold cyan]\n")
        time.sleep(2)
    except subprocess.CalledProcessError as e:
        print(f"S'ha produït un error en executar TheHarvester: {e}")
        logging.error(f"Error en executar TheHarvester: {e}")'''

def parametre_valid(parametre):
    valid_params = ["-d", "--domain", "-b", "--source", "-l", "--limit", "-S", "--start", "-p", "--proxies", "-s", "--shodan", "--screenshot", "-v", "--virtual-host", "-e", "--dns-server", "-t", "--take-over", "-r", "--dns-revolve", "-n", "--dns-lookup", "-c", "--dns-brute", "-f", "--filename"]
    return parametre in valid_params

def get_user_input(prompt, validation_func=None):
    while True:
        user_input = input(prompt)
        if validation_func is None or validation_func(user_input):
            return user_input
        else:
            print("Entrada no vàlida. Torna-ho a intentar.")

# Imatges

logo = CTkImage(dark_image=Image.open("./img/Logo_empresa.png"),
                size=(60,60)
                )

# Frames

# Frame principal

framepr = CTkFrame(app,
    height=400,
    width=600
    )
framepr.grid(column=1, row=1, pady=10, padx=10, sticky="n")

## Frame eines amb les seves configuracions i opcions

frame2 = CTkFrame(app,
    height=50,
    width=570
    )
frame2.grid(column=0, row=1, pady=10, padx=10, sticky="n")

# Labels

## Label Titol

labelpr = CTkLabel(app, 
    text="PROJECTE E3", 
    font=("Arial", 40), 
    text_color="white",
)
labelpr.grid(column=0, row=0, pady=5, sticky="s")

## Label resultats

laberesult = CTkLabel(framepr, 
    text="Resultats", 
    font=("Arial Bold", 25), 
)
laberesult.place(x=250, y=5)

## Label checkbox

labelcheckbox = CTkLabel(frame2, 
    text="Eines", 
    font=("Arial Bold", 25), 
)
labelcheckbox.place(x=250, y=5)

# Botons

## Boto logo

logo_boto = CTkButton(app,
    image=logo,
    text="",
    font=("Arial Bold", 20), 
    fg_color="transparent",
    height=50,
    width=40           
    )
logo_boto.grid(column=0, row=0, pady=(5,0), padx=10, sticky="w")

## Boto per exit/sortir programa

sortir_boto = CTkButton(app,
    text="Exit/Sortir programa",
    command=exit_boto,
    font=("Arial Bold", 20), 
    height=50,
    width=40      
    )
sortir_boto.grid(column=0, row=1, sticky="s")

# Textbox

## Textbox dels resultats

resultats_text = CTkTextbox(framepr,
    height=350,
    width=600,
    fg_color="silver",
    text_color="black",
    scrollbar_button_color="#FFCC70", 
    corner_radius=16,
    border_color="#FFCC70", 
    border_width=2)
resultats_text.place(x=0, y=50)

# Tabview

## Tabview de les opcions de les diferents eines

tabviewpr = CTkTabview(app,
    height=300,
    width=500
    )
tabviewpr.grid(column=0,row=1, padx=5)

## Tabs de les diferents eines amb les opcions 

# Api Shodan

tab_shodan = tabviewpr.add("Api Shodan")

botoprova = CTkButton(tab_shodan,
    text="Prova"
    ).pack(pady=5)

# Més OSINT

tab_osint = tabviewpr.add("Més OSINT")

label_osint = CTkLabel(tab_osint,
        text="Selecciona una de les opcions de OSINT:",
        ).pack()

options_osint = CTkComboBox(tab_osint,
        #variable=variable2,
        values=[
            "Sherlock", 
            "Exiftool",
            ""
            ], 
        state="readonly"
        ).pack(pady=5)

label_osint_username = CTkLabel(tab_osint,
        text="Introdueix el nom d'usuari:"
        ).pack()

entry_input_username = Entry(tab_osint,
        ).pack(pady=5)

label_osint_image_path = CTkLabel(tab_osint,
        text="Selecciona la ruta de l'imatge"
        ).pack()

entry_input_image_path = Entry(tab_osint,
        ).pack(pady=5)


select_image_button = CTkButton(tab_osint, 
        text="Seleccionar imatge", 
        command=""
        ).pack(pady=5)

run_osint_boto = CTkButton(tab_osint, 
        text="Executar OSINT", 
        command=run_osint
        ).place(x=20, y=100)


# TheHarvester

tab_the_harvester = tabviewpr.add("The Harvester")

the_harvester_label_target = CTkLabel(tab_the_harvester,
        text="Introdueix l'objectiu (domini, adreça IP...)",
        font=("Arial", 15)
        ).pack(pady=5)

the_harvester_entry_target = Entry(tab_the_harvester,
        ).pack(pady=5)

the_harvester_label_options = CTkLabel(tab_the_harvester,
        text="Introdueix els paràmetres amb els seus valors respectius",
        font=("Arial", 15)
        ).pack(pady=5)

the_harvester_entry_options = Entry(tab_the_harvester,
        ).pack(pady=5)

# Auditoria SSH

tab_auditoria = tabviewpr.add("Auditoria SSH")

# Enumeració(Enum4linux)

tab_enumeracio = tabviewpr.add("Enumeracio")

# Bot Telegram

tab_telegram = tabviewpr.add("Bot Telegram")

telgram_label_token = CTkLabel(tab_telegram, 
        text = "Coloca aqui el token del teu bot:",
        font=("Arial", 20)
        ).pack(pady=5)

telegram_entry_token = Entry(tab_telegram,
        ).pack(pady=5)

telgram_label_grup = CTkLabel(tab_telegram,
        text="Coloca aqui el ID del grup on vols publicar",
        font=("Arial", 20)
        ).pack(pady=5)

telegram_entry_grup = Entry(tab_telegram,
        ).pack(pady=5)

# Escaneig NMAP

tab_escaneig = tabviewpr.add("Escaneig")

label_nmap = CTkLabel(tab_escaneig, 
    text="Selecciona una opció de NMAP",
    font=("Arial", 20)
    ).pack()

options_nmap = CTkComboBox(tab_escaneig, 
        width=360,
        # variable_opcio=variable,
        values=[
                "Descobrir hosts de xarxa", 
                "Escaneig de ports oberts", 
                "Llistat de serveis i versions d'un, un rang o tots els ports", 
                "Llistat de vulnerabilitats d'un, un rang o tots els serveis",
                ""
                ],
        state="readonly").pack(pady=5)

label_nmap_ip = CTkLabel(tab_escaneig,
        text="Introdueix la IP o xarxa:"
        ).pack()

entry_nmap_ip = Entry(tab_escaneig,
        ).pack(pady=5)

label_ports_nmap = CTkLabel(tab_escaneig, 
        text="Introdueix el port o rang de ports (p.e, 80 o 20-100)"
        ).pack()

entry__ports = Entry(tab_escaneig,
        ).pack(pady=5)

run_nmap_boto = CTkButton(tab_escaneig, text="Executar NMAP",
        command=run_nmap    
        ).pack(pady=5)

## options_nmap.bind("<<ComboxSelected", update_ip_entry_state)

# Obrir interficie gràfica
app.mainloop()