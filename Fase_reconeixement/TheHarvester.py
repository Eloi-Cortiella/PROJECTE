import subprocess
import time
from rich import print
from rich.table import Table
from rich.progress import Progress
from rich.console import Console
from rich.progress import track
from rich.traceback import install
install()

## Taules
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

def lanzar_the_harvester():
    
    print("\n[bold green]The Harvester[/bold green]\n")
    time.sleep(1)

    print(table1)

    objetiu = get_user_input("\nIntrodueix l'objectiu (p.e. un domini o una adreça IP): ")

    parametres = []
    while True:
        parametre = input("Introdueix un paràmetre (p.e. '-d' o '-l', o 'stop' per finalitzar i executar theHarvester): ")
        if parametre == "stop":
            break
        elif parametre in ("-d", "--domain", "-b", "--source", "-l", "--limit", "-S", "--start", "-p", "--proxies", "-s", "--shodan", "--screenshot", "-v", "--virtual-host", "-e", "--dns-server", "-t", "--take-over", "-r", "--dns-revolve", "-n", "--dns-lookup", "-c", "--dns-brute", "-f", "--filename", ):
            valor = get_user_input(f"Introdueix el valor per al paràmetre {parametre}: ")
            parametres.append(f"{parametre} {valor}")
        else:
            print("Paràmetre no vàlid. Torna-ho a intentar o utilitza 'fin' per finalitzar.")

    subprocess_command = f"./Fase_reconeixement/theHarvester/theHarvester.py -d {objetiu} {' '.join(parametres)}"

    try:
        output = subprocess.check_output(subprocess_command, shell=True, text=True)
        with open("resultats_theharvester.txt", "w") as arxiu:
            arxiu.write(output)
        print("\n[bold cyan]Resultats guardats a 'resultats_theharvester.txt'[bold cyan]\n")
        time.sleep(2)
    except Exception as e:
        print(f"S'ha produït un error en executar TheHarvester: {e}")
    
    try:
        subprocess.call(subprocess_command, shell=True)
    except Exception as e:
        print(f"S'ha produït un error en executar TheHarvester: {e}")
        with open('./errors.log',"a") as a:
            a.write(str(e))

def get_user_input(prompt, validation_func=None):
    while True:
        user_input = input(prompt)
        if validation_func is None or validation_func(user_input):
            return user_input
        else:
            print("Entrada no vàlida. Torna-ho a intentar.")