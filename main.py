from customtkinter import *
import tkinter as tk
from tkinter import *
from tkinter import scrolledtext 
from PIL import Image
from subprocess import PIPE, Popen
import requests
import webbrowser
import subprocess
import logging
#import time
import datetime
import re
import shodan
#from rich import print
#from rich.table import Table
#from rich.traceback import install
#install()

# Crear interficie grafica amb customtkinter
app = CTk()

# Configuracions finestra
app.title("PROJECTE E3")
app.geometry("1550x1200")
app._set_appearance_mode("dark")

# Ruta completa al script de Sherlock
SHERLOCK_SCRIPT_PATH = "/home/alumne/Escriptori/Moodle_2N/PROJECTE/sherlock/sherlock/sherlock.py"

# Constant de la API KEY
SHODAN_API_KEY = '2zHHXdcuY608POXVdGKZXb9fYngNjROO'

## Variable per al arxiu log de errors

logging.basicConfig(filename='error.log', level=logging.INFO)

temps_actual = datetime.datetime.now()

'''
print("""[bold yellow]

.______   .______        ______          __   _______   ______ .___________. _______     _______  ____   
|   _  \  |   _  \      /  __  \        |  | |   ____| /      ||           ||   ____|   |   ____||___ \  
|  |_)  | |  |_)  |    |  |  |  |       |  | |  |__   |  ,----'`---|  |----`|  |__      |  |__     __) | 
|   ___/  |      /     |  |  |  | .--.  |  | |   __|  |  |         |  |     |   __|     |   __|   |__ <  
|  |      |  |\  \----.|  `--'  | |  `--'  | |  |____ |  `----.    |  |     |  |____    |  |____  ___) |
| _|      | _| `._____| \______/   \______/  |_______| \______|    |__|     |_______|   |_______||____/
\n\n\n
""")'''

# FUNCIONS

## Funció executar botó

def exit_boto():
    app.destroy()

## Funció redirigir a pagina de github on hi ha més informació de l'eina

def dirigir_pagina_web():
    url = "https://github.com/Eloi-Cortiella/PROJECTE"
    webbrowser.open_new(url)

def dirigir_landing_page():
    url_landing_page = "https://ericgonzalez41.wixsite.com/e3security"
    webbrowser.open_new(url_landing_page)

## Funció nmap

def run_nmap():
        try:
                clear_text()
                opcion = options_nmap.get()
                if opcion == "Descobrir hosts de xarxa":
                        target = entry_nmap_ip.get()
                        cmd = ["nmap", "-sn", target]
                elif opcion == "Escaneig de ports oberts":
                        target = entry_nmap_ip.get()
                        cmd = ["nmap", "-n", "-Pn", "-p-", target]
                elif opcion == "Llistat de serveis i versions d'un, un rang o tots els ports":
                        target = entry_nmap_ip.get()
                        ports = entry__ports.get()
                        cmd = ["nmap", "-sCV", "-n", "-Pn", "-p", ports, target]
                elif opcion == "Llistat de vulnerabilitats d'un, un rang o tots els serveis":
                        target = entry_nmap_ip.get()
                        cmd = ["nmap", "--script=vuln", target]
                else:
                        resultats_text.insert(tk.END, "Opció no vàlida")
                        return
                
                executar_commanda(cmd)
        except Exception as e:
                resultats_text.insert(tk.END,"ERROR ----> Hi ha hagut un problema executant el programa... Mira l'arxiu errors.log per veure l'error.")
                logging.error(f"{temps_actual}Error en executar nmap: {e}")

## Funció OSINT

def run_osint():
        try:
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
                
                executar_commanda(cmd)
        except Exception as e:
                resultats_text.insert(tk.END,"ERROR ----> Hi ha hagut un problema executant el programa... Mira l'arxiu errors.log per veure l'error.")
                logging.error(f"{temps_actual}Error en executar OSINT: {e}")

## Funció buidar text

def clear_text():
    resultats_text.delete('1.0', tk.END)

## Funció per executar la comanda:
def executar_commanda(cmd):
    process = Popen(cmd, stdout=PIPE, stderr=PIPE, text=True)
    stdout, stderr = process.communicate()
    resultats_text.insert(tk.END, f"Comanda: {' '.join(cmd)}\n")
    resultats_text.insert(tk.END, stdout)
    resultats_text.insert(tk.END, stderr)

## Funció per actualitzar l'estat del entry_nmap_ip_config

def update_ip_entry_state(event):
    opcion = options_nmap.get()
    entry_nmap_ip.config(state=tk.NORMAL if opcion in ["Descobrir hosts de xarxa", "Escaneig de ports oberts", "Llistat de serveis i versions d'un, un rang o tots els ports", "Llistat de vulnerabilitats d'un, un rang o tots els serveis"] else CTk.DISABLED)

## Funció que demana a l'usuari el fitxer de la imatge amb la seva ruta

def ask_image_path(): 
    file_path = filedialog.askopenfilename()
    entry_input_image_path.delete(0, tk.END)
    entry_input_image_path.insert(tk.END, file_path)

## Funcions TheHarvester

### Funció executar the Harvester

def the_harvester():
    clear_text()
    objectiu = the_harvester_entry_target.get()
    parametres = the_harvester_entry_options.get()
    comanda_the_harvester = ["./theHarvester/theHarvester.py", "-d", objectiu, parametres]

    try:
        resultats_text.insert(tk.END,"Resultats guardats a 'resultats_theharvester.txt'\n")

        ## Per a l'arxiu txt
        output = subprocess.check_output(comanda_the_harvester, text=True)
        output_sense_colors = re.sub(r'\x1b\[[0-9;]*m', '', output)
        with open("resultats_theharvester.txt", "w") as arxiu:
            arxiu.write(output_sense_colors)
        
        ## Per a la interfície gràfica
        executar_commanda(comanda_the_harvester)

    except Exception as e:
        resultats_text.insert(tk.END,"S'ha produït un error en executar TheHarvester Mira l'arxiu errors.log per veure l'error.")
        logging.error(f"{temps_actual}Error en executar TheHarvester: {e}")

## Funcions enum4linux

def executar_enum4linux():
    clear_text()
    objectiu = enum4linux_entry_target.get()
    parametres = enum4linux_entry_options.get()
    comanda_enumeracio = ["./enum4linux-ng/enum4linux-ng.py",parametres,objectiu]

    try:
        resultats_text.insert(tk.END,"Resultats guardats a 'resultats_theharvester.txt'\n")
        ## Per a l'arxiu txt
        output = subprocess.check_output(comanda_enumeracio, text=True)
        output_sense_colors = re.sub(r'\x1b\[[0-9;]*m', '', output)
        with open("resultats_enumeracio.txt", "w") as arxiu:
            arxiu.write(output_sense_colors)

        ## Interfície gràfica
        executar_commanda(comanda_enumeracio)
    
    except Exception as e:
        resultats_text.insert(tk.END,"ERROR ----> Hi ha hagut un problema executant el programa... Mira l'arxiu errors.log per veure l'error.")
        logging.error(f"{temps_actual}Error en executar Enum4linux: {e}")

## Funcions API Shodan

def obtenir_informacio_ip(ip):
    api = shodan.Shodan(SHODAN_API_KEY)
    try:
        resultat = api.host(ip)
        return resultat
    except shodan.APIError as e:
        resultats_text.insert(tk.END,f"Error de Shodan: {e}")
        logging.error(f"{temps_actual}|Error en executar ApiShodan: {e}")
        return None

def mostrar_info_general(info):
    if info:
        resultats_text.insert(tk.END,f"IP: {info['ip_str']}\n")
        resultats_text.insert(tk.END,f"País: {info['country_name']}\n")
        resultats_text.insert(tk.END,f"Organització: {info.get('org', 'No disponible')}\n")
        resultats_text.insert(tk.END,f"Sistema Operatiu: {info.get('os', 'No disponible')}\n")
        resultats_text.insert(tk.END,f"Ports oberts: {', '.join(map(str, info['ports']))}\n")
        resultats_text.insert(tk.END,"\nNoms de domini associats:\n")
        for dominio in info['hostnames']:
            resultats_text.insert(tk.END,f"  - {dominio}\n")
    else:
        resultats_text.insert(tk.END,"No s'ha trobat informació per a aquesta IP.")

def obtenir_info_servei(port):
    return port.get('name', 'No disponible')

def mostrar_serveis_ports(ip, ports):
    resultats_text.insert(tk.END,f"\nServei amb els ports oberts de {ip}:")
    for port in ports:
        info_servei = obtenir_info_servei(port)
        resultats_text.insert(tk.END,f"\n   Port {port['port']} ({port['transport']}): {info_servei}")

def prova_boto():
    clear_text()
    entry_ip = api_shodan_entry_ip.get()
    info_ip = obtenir_informacio_ip(entry_ip)

    mostrar_info_general(info_ip)

    if info_ip:
        mostrar_serveis_ports(entry_ip, info_ip['data'])

## Funcions Bot de Telegram

def enviar_missatge_telegram():
        try:
                # TOKEN: '6730938053:AAGjxzquj5-M1XMSDibw_JNIzCneTwk3AXc' ID_GRUP: -4093496817 
                missatge = telegram_entry_missatge.get()
                idBot = telegram_entry_token.get()
                idGrupo = telegram_entry_grup.get()

                requests.post('https://api.telegram.org/bot' + idBot + '/sendMessage',
                data={'chat_id': idGrupo, 'text': missatge, 'parse_mode': 'HTML'})
                clear_text()
                resultats_text.insert(tk.END,"Missatge enviat correctament al bot de Telegram, comprova el teu missatge.")
        except Exception as e:
                clear_text()
                resultats_text.insert(tk.END,"ERROR ----> Hi ha hagut un problema executant el programa... Mira l'arxiu errors.log per veure l'error.")
                logging.error(f"{temps_actual}Error en executar el Bot de Telegram: {e}")

def enviar_document_telegram():
        try:
                ruta = telegram_entry_document.get()
                idGrupo = telegram_entry_grup.get()
                idBot = telegram_entry_token.get()
                
                requests.post('https://api.telegram.org/bot' + idBot + '/sendDocument',
                files={'document': (ruta, open(ruta, 'rb'))},
                data={'chat_id': idGrupo, 'caption': 'imagen caption'})
                clear_text()
                resultats_text.insert(tk.END,"Document/Imatge enviat correctament al bot de Telegram, comprova el teu document.")

        except Exception as e:
                clear_text()
                resultats_text.insert(tk.END,"ERROR ----> Hi ha hagut un problema executant el programa... Mira l'arxiu errors.log per veure l'error.")
                logging.error(f"{temps_actual}Error en executar el Bot de Telegram: {e}")

def ask_document_path(): 
    file_path = filedialog.askopenfilename()
    telegram_entry_document.delete(0, tk.END)
    telegram_entry_document.insert(tk.END, file_path)

# Imatges

## Imatge logo Empresa

logo = CTkImage(dark_image=Image.open("./img/Logo_empresa.png"),
                size=(60,60)
                )

# Frames

# Frame principal

framepr = CTkFrame(app,
    height=500,
    width=900
    )
framepr.grid(column=1, row=1, pady=10, padx=10, sticky="n")

## Frame eines amb les seves configuracions i opcions

frame2 = CTkFrame(app,
    height=480,
    width=615
    )
frame2.grid(column=0, row=1, pady=10, padx=20, sticky="n")

## Frame per a mostrar a l'usuari els diferents paràmetres de les respectives eines

framepara = CTkFrame(app, 
    height=400,
    width=1550
    )
framepara.place(x=20, y=600)

# Labels

## Label Titol

labelpr = CTkLabel(app, 
    text="E3 SECURITY", 
    font=("Arial", 40), 
    text_color="yellow",
)
labelpr.place(x=800, y=15)

## Label resultats

laberesult = CTkLabel(framepr, 
    text="Resultats", 
    text_color="green",
    font=("Arial Bold", 25), 
)
laberesult.place(x=400, y=10)

## Label checkbox

labelcheckbox = CTkLabel(frame2, 
    text="Eines",
    text_color="orange", 
    font=("Arial Bold", 25) 
)
labelcheckbox.place(x=280, y=10)

## Label del titol de frame parametres

labelpara = CTkLabel(framepara,
    text="Funcionament/Paràmetres - Eines",
    text_color="brown",
    font=("Arial", 25)
    )
labelpara.place(x=620, y=15)

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
    fg_color="black", 
    height=100,
    width=150      
    )
sortir_boto.place(x=1650, y=400)

## Botó per redirigir a pàgina de github al navegador

repositori_boto = CTkButton(app,
    text="Més informació",
    command=dirigir_pagina_web,
    font=("Arial Bold", 20),
    fg_color="red", 
    height=100,
    width=210      
    )
repositori_boto.place(x=1650, y=530)

## Botó que redirigeix a la landing page de la nostra empresa

landingpage_boto = CTkButton(app,
    text="La nostra pàgina",
    command=dirigir_landing_page,
    font=("Arial Bold", 20),
    #fg_color="blue", 
    height=100,
    width=210      
    )
landingpage_boto.place(x=1650, y=650)

# Textbox

## Textbox dels resultats

resultats_text = scrolledtext.ScrolledText(framepr,
    height=23,
    width=98,
    font=("Times New Roman",13)
    )
resultats_text.place(x=0, y=50)

# Tabview

## Tabview de les opcions de les diferents eines

tabviewpr = CTkTabview(frame2,
    height=400,
    width=500
    )
tabviewpr.place(x=10, y=40)

## Tabview dels paràmetres de les eines

tabviewpar = CTkTabview(framepara,
    height=350,
    width=1500
    )
tabviewpar.place(x=25, y=40)


## Tabs de les diferents eines amb les opcions 

# Api Shodan

## Tabview parametres explicats

tab_shodan_par = tabviewpar.add("Api Shodan")

label_shodan_titol = CTkLabel(tab_shodan_par,
        text="Motor de recerca de Metadades",
        text_color="yellow",
        font=("Arial", 23)
        ).pack(pady=5)

label_shodan_par1 = CTkLabel(tab_shodan_par,
        text="Shodan és un motor de recerca de metadades el qual ens ofereix informació segons diversos filtres dels diferents dispositius que es troben a la xarxa. ",
        font=("Arial", 18)
        ).pack(pady=5)

label_shodan_par2 = CTkLabel(tab_shodan_par,
        text="Funcionament",
        text_color="orange",
        font=("Arial", 23)
        ).pack(pady=5)

label_shodan_par3 = CTkLabel(tab_shodan_par,
        text="Introdueix la IP que vulguis buscar i fes click al botó d'executar shodan, és mostrarà el resultat al cap d'uns segons",
        font=("Arial", 18)
        ).pack(pady=5)

## Tabview opcions

tab_shodan = tabviewpr.add("Api Shodan")

api_shodan_label_ip = CTkLabel(tab_shodan,
        text="Introdueix la IP a consultar:",
        font=("Arial", 15)
        ).pack(pady=5)

api_shodan_entry_ip = Entry(tab_shodan
        )
api_shodan_entry_ip.pack(pady=5)

run_api_shodan_boto = CTkButton(tab_shodan,
    text="Executar Api Shodan",
    command=prova_boto
    ).pack(pady=5)


# Més OSINT

## Tabview explicació eina OSINT

tab_osint_par = tabviewpar.add("Més OSINT")

label_OSINT_titol = CTkLabel(tab_osint_par,
        text="Recopilar i analitzar informació de fonts d'accés públic",
        text_color="yellow",
        font=("Arial", 23)
        ).pack(pady=5)

label_osint_par1 = CTkLabel(tab_osint_par,
        text="La finalitat de l'OSINT és obtenir dades rellevants i útils per comprendre millor una situació, entitat o individu.\n\nLa informació recopilada mitjançant l'OSINT es pot utilitzar en diverses àrees (Seguretat, investigació, intel·ligència...)",
        font=("Arial", 18)
        ).pack(pady=5)

label_osint_par2 = CTkLabel(tab_osint_par,
        text="Funcionament",
        text_color="orange",
        font=("Arial", 23)
        ).pack(pady=5)

label_osint_par3 = CTkLabel(tab_osint_par,
        text="La finalitat de l'OSINT és obtenir dades rellevants i útils per comprendre millor una situació, entitat o individu.\n\nLa informació recopilada mitjançant l'OSINT es pot utilitzar en diverses àrees (Seguretat, investigació, intel·ligència...)",
        font=("Arial", 18)
        ).pack(pady=5)

## Tabview opcions eina OSINT

tab_osint = tabviewpr.add("Més OSINT")

label_osint = CTkLabel(tab_osint,
        text="Selecciona una de les opcions de OSINT:",
        font=("Arial", 15)
        ).pack()

options_osint = CTkComboBox(tab_osint,
        #variable=variable2,
        values=[
            "Sherlock", 
            "Exiftool",
            ""
            ], 
        state="readonly"
        )
options_osint.pack(pady=5)

label_osint_username = CTkLabel(tab_osint,
        text="Introdueix el nom d'usuari:",
        font=("Arial", 15)
        ).pack()

entry_input_username = Entry(tab_osint,
        )
entry_input_username.pack(pady=5)

label_osint_image_path = CTkLabel(tab_osint,
        text="Selecciona la ruta de l'imatge",
        font=("Arial", 15)
        ).pack()

entry_input_image_path = Entry(tab_osint,
        )
entry_input_image_path.pack(pady=5)

select_image_button = CTkButton(tab_osint, 
        text="Seleccionar imatge", 
        command=ask_image_path
        ).pack(pady=5)

run_osint_boto = CTkButton(tab_osint, 
        text="Executar OSINT", 
        command=run_osint
        ).pack(pady=5)

# TheHarvester

tab_the_harvester_par = tabviewpar.add("The Harvester")

label_harvester_par_titol = CTkLabel(tab_the_harvester_par,
        text="Paràmetres principals",
        text_color="yellow",
        font=("Arial", 24)
        ).pack(pady=5)

text_parametres_harvester = """· -h, --help --> Show help message and exit.                                                                                     ·-c, --dns-brute --> Perform a DNS brute force on the domain. 
· -d DOMAIN, --domain DOMAIN --> Company name or domain to search.                                        ·-f FILENAME, --filename FILENAME --> Save the results to an XML and JSON file.
· -l LIMIT, --limit LIMIT --> Limit the number of search results, default=500.                                       ·-b SOURCE, --source SOURCE --> Fonts d'origen.
· -S START, --start START --> Start with result number X, default=0.
· -p, --proxies --> Use proxies for requests, enter proxies in proxies.yaml.
· -s, --shodan --> Use Shodan to query discovered hosts.
· --screenshot SCREENSHOT --> Take screenshots of resolved domains specify output directory.
· -v, --virtual-host --> Verify host name via DNS resolution and search for virtual hosts.
· -e NDS_SERVER, --dns-server DNS_SERVER --> DNS server to use for lookup.
· -t, --take-over --> Check for takeovers.
· -r [DNS_RESOLVE] --> Perform DNS resolution on subdomains with a resolver list.
· -n, --dns-lookup --> Enable DNS server lookup, default False."""

label_harvester_par1 = CTkLabel(tab_the_harvester_par,
        text=text_parametres_harvester,
        font=("Arial", 17),
        justify="left"
        ).pack(pady=5, anchor="w")

## Tabview opcions 

tab_the_harvester = tabviewpr.add("The Harvester")

the_harvester_label_target = CTkLabel(tab_the_harvester,
        text="Introdueix l'objectiu (domini, adreça IP...)",
        font=("Arial", 15)
        ).pack(pady=5)

the_harvester_entry_target = Entry(tab_the_harvester,
        )
the_harvester_entry_target.pack(pady=5)

the_harvester_label_options = CTkLabel(tab_the_harvester,
        text="Introdueix els paràmetres amb els seus valors respectius",
        font=("Arial", 15)
        ).pack(pady=5)

the_harvester_entry_options = Entry(tab_the_harvester,
        )
the_harvester_entry_options.pack(pady=5)

run_the_harvester_boto = CTkButton(tab_the_harvester, text="Executar The Harvester",
        command=the_harvester    
        ).pack(pady=5)

# Auditoria SSH

tab_auditoria = tabviewpr.add("Auditoria SSH")

tab_auditoria_par = tabviewpar.add("Auditoria SSH")

# Enumeració(Enum4linux)

## Tabview explicació paràmetres enum4linux 

tab_enumeracio_par = tabviewpar.add("Enumeracio")

tabview_enumeracio_par = CTkTabview(tab_enumeracio_par,
    height=310,
    width=1500
    )
tabview_enumeracio_par.place(x=0, y=0)

tab_enumeracio_par1 = tabview_enumeracio_par.add("1")

enum4linux_label_par1 = CTkLabel(tab_enumeracio_par1, 
        text="""· -h, --help","show this help message and exit")
· -A --> Do all simple enumeration including nmblookup (-U -G -S -P -O -N -I -L). ")
· -As --> Do all simple short enumeration without NetBIOS names lookup (-U -G -S -P -O -I -L)")
· -U --> Get users via RPC")
· -G --> Get groups via RPC")
· -Gm --> Get groups with group members via RPC")
· -S --> Get shares via RPC")
· -C --> Get services via RPC")
· -P --> Get password policy information via RPC")
· -O --> Get OS information via RPC")
· -L --> Get additional domain info via LDAP/LDAPS (for DCs only)")
· -I --> Get printer information via RPC")
· -R [BULK_SIZE] --> Enumerate users via RID cycling. Optionally, specifies lookup request size.")""",
        font=("Arial", 17),
        justify="left"
        ).pack()

tab_enumeracio_par2 = tabview_enumeracio_par.add("2")

enum4linux_label_par2 = CTkLabel(tab_enumeracio_par2, 
        text="""· -N --> Do an NetBIOS names lookup (similar to nbtstat) and try to retrieve workgroup from output")
· -w DOMAIN --> Specify workgroup/domain manually (usually found automatically)")
· -u USER --> Specify username to use (default "")")
· -p PW --> Specify password to use (default "")")
· -K TICKET_FILE --> Try to authenticate with Kerberos, only useful in Active Directory environment")
· -H NTHASH --> Try to authenticate with hash")
· --local-auth --> Authenticate locally to target")
· -d --> Get detailed information for users and groups, applies to -U, -G and -R")
· -k USERS --> User(s) that exists on remote system (default: administrator,guest,krbtgt,domain admins,root,bin,none). Used to get sid with 'lookupsids'")
· -r RANGES --> RID ranges to enumerate (default: 500-550,1000-1050)")
· -s SHARES_FILE --> Brute force guessing for shares")
· -t TIMEOUT --> Sets connection timeout in seconds (default: 5s)")""",
        font=("Arial", 17),
        justify="left"
        ).pack(pady=5)

tab_enumeracio_par3 = tabview_enumeracio_par.add("3")

enum4linux_label_par3 = CTkLabel(tab_enumeracio_par3, 
        text="""· -v --> Verbose, show full samba tools commands being run (net, rpcclient, etc.)")
· --keep --> Don't delete the Samba configuration file created during tool run after enumeration (useful with -v)")
· -oJ OUT_JSON_FILE --> Writes output to JSON file (extension is added automatically)")
· -oY OUT_YAML_FILE --> Writes output to YAML file (extension is added automatically)")
· -oA OUT_FILE --> Writes output to YAML and JSON file (extensions are added automatically)")""",
        font=("Arial", 17),
        justify="left"
        ).pack(pady=5)


## Tabview enumeració 

tab_enumeracio = tabviewpr.add("Enumeracio")

enum4linux_label_target = CTkLabel(tab_enumeracio, 
        text="Introdueix la ip del objectiu:",
        font=("Arial", 15)
        ).pack(pady=5)

enum4linux_entry_target = Entry(tab_enumeracio,
        )
enum4linux_entry_target.pack(pady=5)

enum4linux_label_options = CTkLabel(tab_enumeracio,
        text="Escull els paràmetres (p.e -U, -M...) amb el ordre correcte:",
        font=("Arial", 15)
        ).pack(pady=5)

enum4linux_entry_options = Entry(tab_enumeracio,
        )
enum4linux_entry_options.pack(pady=5)

run_enum4linux_boto = CTkButton(tab_enumeracio, text="Executar Enum4linux",
        command=executar_enum4linux    
        ).pack(pady=5)

# Bot Telegram

## Tabview parametres eines bot telegram

tab_telegram_par = tabviewpar.add("Bot Telegram")

telgram_label__par = CTkLabel(tab_telegram_par, 
        text = "Amb l'eina del bot de Telegram, pots enviar missatges, imatges i qualsevol altre tipus de document a qualsevol grup de telegram.\nPer poder connectar-te amb el bot, hauràs d'introduir el Token del bot i el id de grup del Telegram.\n\n Respecte el enviament de documents i imatges, pots usar un botó el qual s'encarrega de buscar, amb l'explorador d'arxius, la ruta completa del objecte,\nsense la necessitat d'introduïr manualment la ruta.\n\nPer últim, els dos botons restants, s'encarreguen d'enviar els missatges i els documents/imatges, respectivament.",
        justify="left",
        font=("Arial", 18)
        ).pack(pady=5)

## Tabview opcions eines bot telegram

tab_telegram = tabviewpr.add("Bot Telegram")

telgram_label_token = CTkLabel(tab_telegram, 
        text = "Coloca aqui el token del teu bot:",
        font=("Arial", 15)
        ).pack(pady=5)

telegram_entry_token = Entry(tab_telegram,
        width=50   
        )
telegram_entry_token.pack(pady=5)

telgram_label_grup = CTkLabel(tab_telegram,
        text="Coloca aqui el ID del grup on vols publicar",
        font=("Arial", 15)
        ).pack(pady=5)

telegram_entry_grup = Entry(tab_telegram,
        width=40
        )
telegram_entry_grup.pack(pady=5)

telgram_label_missatge = CTkLabel(tab_telegram,
        text="Coloca aqui el missatge que vols enviar",
        font=("Arial", 15)
        ).pack(pady=5)

telegram_entry_missatge = Entry(tab_telegram,
        width=50
        )
telegram_entry_missatge.pack(pady=5)

telgram_label_document = CTkLabel(tab_telegram,
        text="Coloca aqui el document que vols enviar",
        font=("Arial", 15)
        ).pack(pady=5)

telegram_entry_document = Entry(tab_telegram,
        width=50
        )
telegram_entry_document.pack(pady=5)

run_telegram_missatge_boto = CTkButton(tab_telegram,
    text="Selecciona el document/imatge",
    command=ask_document_path
    ).pack(pady=5)

run_telegram_missatge_boto = CTkButton(tab_telegram,
    text="Enviar missatge a bot telegram",
    command=enviar_missatge_telegram
    ).pack(pady=5)

run_telegram_document_boto = CTkButton(tab_telegram,
    text="Enviar document a bot telegram",
    command=enviar_document_telegram
    ).pack(pady=5)

# Escaneig NMAP

tab_escaneig = tabviewpr.add("Escaneig")

## Parametres escaneig al TabView

tab_escaneig_par = tabviewpar.add("Escaneig")

label_nmap_par_titol = CTkLabel(tab_escaneig_par,
        text="Eina de seguretat informàtica i exploració de xarxes",
        text_color="yellow", 
        font=("Arial", 22)
        ).pack(pady=10, padx=5)

label_nmap_par = CTkLabel(tab_escaneig_par,
        text="Permet als usuaris descobrir i analitzar dispositius a una xarxa, identificar els serveis\nque estan en execució en aquests dispositius i determinar les vulnerabilitats potencials.",
        font=("Arial", 18)
        ).pack(pady=10, padx=5)

label_nmap_par2 = CTkLabel(tab_escaneig_par,
        text="\nOpcions disponibles",
        text_color="orange",
        font=("Arial", 25)
        ).pack(padx=10)

label_nmap_par3 = CTkLabel(tab_escaneig_par,
        text="1. Descobrir hosts de xarxa: permet descobrir els hosts actius en una xarxa sense realitzar un escaneig de ports.\n 2. Escaneig de ports oberts: escaneja els ports d'un host o d'una xarxa per determinar quins ports estan oberts i disponibles.\n 3. Llistat de serveis i versions d'un, un rang o tots els ports: realitza un escaneig de versions per identificar els serveis que s'estan executant als ports oberts.\n 4. Llistat de vulnerabilitats d'un, un rang o tots els ports: utilitza scripts de Nmap per identificar possibles vulnerabilitats als serveis detectats.",
        font=("Arial", 18),
        ).pack(padx=10)

## Opcions escaneig

label_nmap = CTkLabel(tab_escaneig, 
    text="Selecciona una opció de NMAP",
    font=("Arial", 15)
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
        state="readonly")

options_nmap.bind("<<ComboboxSelected>>", update_ip_entry_state)

options_nmap.pack(pady=5)

label_nmap_ip = CTkLabel(tab_escaneig,
        text="Introdueix la IP o xarxa:",
        font=("Arial", 15)
        ).pack()

entry_nmap_ip = Entry(tab_escaneig,
        )
entry_nmap_ip.pack(pady=5)

label_ports_nmap = CTkLabel(tab_escaneig, 
        text="Introdueix el port o rang de ports (p.e, 80 o 20-100)",
        font=("Arial", 15)
        ).pack()

entry__ports = Entry(tab_escaneig,
        )
entry__ports.pack(pady=5)

run_nmap_boto = CTkButton(tab_escaneig, text="Executar NMAP",
        command=run_nmap    
        ).pack(pady=5)

# Obrir interficie gràfica
app.mainloop()