from customtkinter import *
import tkinter as tk
from tkinter import *
from tkinter import scrolledtext 
from PIL import Image
from subprocess import PIPE, Popen
import requests
import subprocess
import logging
import time
import datetime
import re
import shodan
from rich import print
from rich.table import Table
from rich.traceback import install
install()

# Crear interficie grafica amb customtkinter
app = CTk()

# Configuracions finestra
app.title("PROJECTE E3")
app.geometry("1550x600")
app._set_appearance_mode("dark")

# Ruta completa al script de Sherlock
SHERLOCK_SCRIPT_PATH = "./sherlock/sherlock/sherlock.py"

# Constant de la API KEY
SHODAN_API_KEY = '2zHHXdcuY608POXVdGKZXb9fYngNjROO'

## Variable per al arxiu log de errors

logging.basicConfig(filename='error.log', level=logging.INFO)

temps_actual = datetime.datetime.now()

print("""[bold yellow]

.______   .______        ______          __   _______   ______ .___________. _______     _______  ____   
|   _  \  |   _  \      /  __  \        |  | |   ____| /      ||           ||   ____|   |   ____||___ \  
|  |_)  | |  |_)  |    |  |  |  |       |  | |  |__   |  ,----'`---|  |----`|  |__      |  |__     __) | 
|   ___/  |      /     |  |  |  | .--.  |  | |   __|  |  |         |  |     |   __|     |   __|   |__ <  
|  |      |  |\  \----.|  `--'  | |  `--'  | |  |____ |  `----.    |  |     |  |____    |  |____  ___) |
| _|      | _| `._____| \______/   \______/  |_______| \______|    |__|     |_______|   |_______||____/
\n\n\n
""")


time.sleep(2)

# Taules

## Taula The Harvester

table1 = Table(title="Paràmetres principals")

table1.add_column("Opcions", style="Bold yellow")
table1.add_column("Descripció", style="Bold")

table1.add_row("-h, --help","Show help message and exit.")
table1.add_row("-d DOMAIN, --domain DOMAIN","Company name or domain to search.")
table1.add_row("-l LIMIT, --limit LIMIT","Limit the number of search results, default=500.")
table1.add_row("-S START, --start START","Start with result number X, default=0.")
table1.add_row("-p, --proxies","Use proxies for requests, enter proxies in proxies.yaml.")
table1.add_row("-s, --shodan","Use Shodan to query discovered hosts.")
table1.add_row("--screenshot SCREENSHOT","Take screenshots of resolved domains specify output directory: --screenshot output_directory")
table1.add_row("-v, --virtual-host","Verify host name via DNS resolution and search for virtual hosts.")
table1.add_row("-e NDS_SERVER, --dns-server DNS_SERVER"," DNS server to use for lookup.")
table1.add_row("-t, --take-over","Check for takeovers.")
table1.add_row("-r [DNS_RESOLVE], --dns-resolve [DNS_RESOLVE]","Perform DNS resolution on subdomains with a resolver list or passed inresolvers, default False.")
table1.add_row("-n, --dns-lookup","Enable DNS server lookup, default False.")
table1.add_row("-c, --dns-brute","Perform a DNS brute force on the domain.")
table1.add_row("-f FILENAME, --filename FILENAME","Save the results to an XML and JSON file.")
table1.add_row("-b SOURCE, --source SOURCE","anubis, baidu, bevigil, binaryedge, bing, bingapi, bufferoverun, brave, censys, certspotter, criminalip, crtsh, dnsdumpster, duckduckgo, fullhunt, github-code, hackertarget, hunter, hunterhow, intelx, netlas, onyphe, otx, pentesttools, projectdiscovery, rapiddns, rocketreach, securityTrails, sitedossier, subdomaincenter, subdomainfinderc99, threatminer, tomba, urlscan, virustotal, yahoo, zoomeye")

print(table1)

time.sleep(1.5)

## Taules TheHarvester

table2 = Table(title="\nParàmetres prinicpals Enum4linux-ng")

table2.add_column("Opcions", style="Bold yellow")
table2.add_column("Descripció", style="Bold")

table2.add_row("-h, --help","show this help message and exit")
table2.add_row("-A","Do all simple enumeration including nmblookup (-U -G -S -P -O -N -I -L). ")
table2.add_row("-As","Do all simple short enumeration without NetBIOS names lookup (-U -G -S -P -O -I -L)")
table2.add_row("-U","Get users via RPC")
table2.add_row("-G","Get groups via RPC")
table2.add_row("-Gm","Get groups with group members via RPC")
table2.add_row("-S","Get shares via RPC")
table2.add_row("-C","Get services via RPC")
table2.add_row("-P","Get password policy information via RPC")
table2.add_row("-O","Get OS information via RPC")
table2.add_row("-L","Get additional domain info via LDAP/LDAPS (for DCs only)")
table2.add_row("-I","Get printer information via RPC")
table2.add_row("-R [BULK_SIZE]","Enumerate users via RID cycling. Optionally, specifies lookup request size.")
table2.add_row("-N","Do an NetBIOS names lookup (similar to nbtstat) and try to retrieve workgroup from output")
table2.add_row("-w DOMAIN","Specify workgroup/domain manually (usually found automatically)")
table2.add_row("-u USER","Specify username to use (default "")")
table2.add_row("-p PW","Specify password to use (default "")")
table2.add_row("-K TICKET_FILE","Try to authenticate with Kerberos, only useful in Active Directory environment")
table2.add_row("-H NTHASH","Try to authenticate with hash")
table2.add_row("--local-auth","Authenticate locally to target")
table2.add_row("-d","Get detailed information for users and groups, applies to -U, -G and -R")
table2.add_row("-k USERS","User(s) that exists on remote system (default: administrator,guest,krbtgt,domain admins,root,bin,none). Used to get sid with 'lookupsids'")
table2.add_row("-r RANGES","RID ranges to enumerate (default: 500-550,1000-1050)")
table2.add_row("-s SHARES_FILE","Brute force guessing for shares")
table2.add_row("-t TIMEOUT","Sets connection timeout in seconds (default: 5s)")
table2.add_row("-v","Verbose, show full samba tools commands being run (net, rpcclient, etc.)")
table2.add_row("--keep","Don't delete the Samba configuration file created during tool run after enumeration (useful with -v)")
table2.add_row("-oJ OUT_JSON_FILE","Writes output to JSON file (extension is added automatically)")
table2.add_row("-oY OUT_YAML_FILE","Writes output to YAML file (extension is added automatically)")
table2.add_row("-oA OUT_FILE","Writes output to YAML and JSON file (extensions are added automatically)")

print(table2)

time.sleep(3)

print("\n[bold blue] Els resultats de les eines es mostraràn a la finestra un cop hagi finalitzat la execució d'aquest. Si us plau, tingueu paciència\n")

time.sleep(3)

# FUNCIONS

## Funció executar botó

def exit_boto():
    app.destroy()

## Funció nmap

def run_nmap():
    clear_text()
    opcion = options_nmap.get()
    print(opcion)
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
    
    executar_commanda(cmd)

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
        print("[bold red]\nERROR ----> Hi ha hagut un problema executant el programa... Mira l'arxiu errors.log per veure l'error.")
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
laberesult.place(x=400, y=5)

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
    font=("Arial Bold", 10), 
    height=50,
    width=40      
    )
sortir_boto.grid(column=0, row=1, sticky="s")

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

tabviewpr = CTkTabview(app,
    height=400,
    width=500
    )
tabviewpr.grid(column=0,row=1, rowspan=1, padx=5)

## Tabs de les diferents eines amb les opcions 

# Api Shodan

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

# Enumeració(Enum4linux)

tab_enumeracio = tabviewpr.add("Enumeracio")

eum4linux_label_target = CTkLabel(tab_enumeracio, 
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

tab_telegram = tabviewpr.add("Bot Telegram")

telgram_label_token = CTkLabel(tab_telegram, 
        text = "Coloca aqui el token del teu bot:",
        font=("Arial", 15)
        ).pack(pady=5)

telegram_entry_token = Entry(tab_telegram,
        )
telegram_entry_token.pack(pady=5)

telgram_label_grup = CTkLabel(tab_telegram,
        text="Coloca aqui el ID del grup on vols publicar",
        font=("Arial", 15)
        ).pack(pady=5)

telegram_entry_grup = Entry(tab_telegram,
        )

telegram_entry_grup.pack(pady=5)

run_telegram_boto = CTkButton(tab_telegram,
    text="Executar Bot Telegram"
    ).pack(pady=5)

# Escaneig NMAP

tab_escaneig = tabviewpr.add("Escaneig")

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