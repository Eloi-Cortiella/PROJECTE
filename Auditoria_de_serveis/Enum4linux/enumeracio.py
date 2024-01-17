import subprocess
import time
import random
from rich import print
from rich.table import Table
from rich.progress import Progress
from rich.console import Console
from rich.progress import track
from rich.traceback import install
install()

# Aquesta tasca va relacionada amb la fase d'enumeració, només cal que invoqueu l'script enum4linux, el configureu i li doneu un objectiu.

## Taules
table1 = Table(title="Paràmetres prinicpals")

table1.add_column("Opcions", style="Bold yellow")
table1.add_column("Descripció", style="Bold")

table1.add_row("-U","get userlist")
table1.add_row("-M","get machine list*")
table1.add_row("-S","get sharelist")
table1.add_row("-P","get password policy information")
table1.add_row("-G","get group and member list")
table1.add_row("-d","be detailed, applies to -U and -S")
table1.add_row("-u user","specify username to use (default "")")
table1.add_row("-p pass","specify password to use (default "")")
    

table2 = Table(title="\nParàmetres addicionals")

table2.add_column("Opcions", style="Bold yellow")
table2.add_column("Descripció", style="Bold")

table2.add_row("-a","Do all simple enumeration (-U -S -G -P -r -o -n -i).")
table2.add_row("-h","Display this help message and exit")
table2.add_row("-r","enumerate users via RID cycling")
table2.add_row("-R range","RID ranges to enumerate (default: 500-550,1000-1050, implies -r)")
table2.add_row("-K n","Keep searching RIDs until n consective RIDs don't correspond to a username.  Impies RID range ends at 999999. Useful against DCs.")
table2.add_row("-l","Get some (limited) info via LDAP 389/TCP (for DCs only)")
table2.add_row("-s file","brute force guessing for share names")
table2.add_row("-k user","User(s) that exists on remote system (default: administrator,guest,krbtgt,domain admins,root,bin,none)")
table2.add_row("-o","Get OS information")
table2.add_row("-i","Get printer information")
table2.add_row("-w wrkg","Specify workgroup manually (usually found automatically)")
table2.add_row("-n","Do an nmblookup (similar to nbtstat)")
table2.add_row("-v","Verbose.  Shows full commands being run (net, rpcclient, etc.)")
table2.add_row("-A","Aggressive. Do write checks on shares etc")
table2.add_row("stop","Parar d'introduïr paràmetres")

stop = "stop"

progress = Progress()
console = Console()

Prova = "enum4linux -h"

def executar_enum4linux():

    print("""
        [bold yellow]
        ######## ##    ## ##     ## ##     ## ######## ########     ###     ######  ####  #######  
        ##       ###   ## ##     ## ###   ### ##       ##     ##   ## ##   ##    ##  ##  ##     ## 
        ##       ####  ## ##     ## #### #### ##       ##     ##  ##   ##  ##        ##  ##     ## 
        ######   ## ## ## ##     ## ## ### ## ######   ########  ##     ## ##        ##  ##     ## 
        ##       ##  #### ##     ## ##     ## ##       ##   ##   ######### ##        ##  ##     ## 
        ##       ##   ### ##     ## ##     ## ##       ##    ##  ##     ## ##    ##  ##  ##     ## 
        ######## ##    ##  #######  ##     ## ######## ##     ## ##     ##  ######  ####  #######  
        [/bold yellow]
          
        [bold cyan]Fet per Eloi Cortiella Fortuño
    """)

    print(table1)
    print(table2)

    while True:
        try:
            
            objectiu = input("\nIntrodueix la ip de l'objectiu: ")
            opcions = []
            opcions_input = input("Escull els paràmetres (p.e -U, -M...) amb el ordre correcte: ")
            comanda_enumeracio = "enum4linux"+' '+objectiu
            print(comanda_enumeracio)

            while opcions_input != stop:
                opcions.append(opcions_input)
                print(opcions)
                opcions_input = input("Afegeix més paràmetres (si no vols introduïr-ne més, escriu 'stop'): ")
            else:
                print("\n[bold green]Iniciant enumeració...[/bold green]\n")
                time.sleep(0.3)
                comanda = subprocess.call(comanda_enumeracio, shell=True)
                    
                
                '''with open('./resultats.txt', "w") as f:
                    for line in resultat:
                        f.write(line + "\n")'''

        except Exception as e:
            print("[bold red]ERROR ----> Hi ha hagut un problema executant el programa...")
            print("    ",e)

            with open('./errors.log',"w") as a:
                a.write(str(e))

            break