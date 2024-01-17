import subprocess
import os


def sherlock_search(username):
    command = f'python3 sherlock --print-found {username}'
    
    try:
        output = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT, text=True)
        
        print(output)
    except subprocess.CalledProcessError as e:
        print(f"Error: {e.output}")
    except Exception as e:
        print(f"S'ha produït un error: {e}")

def exiftool_search(image_path):
    command = f'exiftool {image_path}'

    try:
        output = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT, text=True)
        print(output)
    except subprocess.CalledProcessError as e:
        print(f"Error: {e.output}")
    except Exception as e:
        print(f"S'ha produït un error: {e}")

def osint_submenu():
    while True:
        print("\n--- { Submenú OSINT }  ---\n")
        print("1. Sherlock")
        print("2. Exiftool")
        print("3. Tornar al menú principal\n")

        choice = input("Seleccioneu una opció: ")

        os.system('clear')
        if choice == "1":
            username = input("\nIntroduïu el nom d'usuari a investigar: ")
            sherlock_search(username)
        elif choice == "2":
            image_path = input("\nIntroduïu el nom de la imatge: ")
            exiftool_search(image_path)
        elif choice == "3":
            break
        else:
            print("Opció no vàlida. Torneu-ho a provar.")

def main_menu():
    while True:
        print("\n--- { Menú Principal } ---\n")
        print("1. Més OSINT")
        print("2. Sortir\n")
        
        choice = input("Seleccioneu una opció: ") 

        if choice == "1":
            osint_submenu()
        elif choice == "2":
            print("Adéu!")
            break
        else:
            print("Opció no vàlida. Torneu-ho a provar.")

if __name__ == "__main__":
    main_menu()