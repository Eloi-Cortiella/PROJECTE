<h1 align="center">PROJECTE ASIX MP14 - 2023/2024</h1>
<p align="center">
<strong>Projecte ASIX del mòdul MP14, format per Èric González, Èric Peréz i Eloi Cortiella.</strong>
</p>

<p align="center">
<img src="https://img.shields.io/badge/python-%3E=_3.10.12-blue"/>
</p>

<p align="center">
<img src="/img/Logo_empresa.png">
</p>

## ÍNDEX

1. **Fase de Reconeixement**
   1.1 [Api Shodan en Python](#api-shodan-en-python)
   1.2 [The Harvester en Python](#theharvester-en-python)
   1.3 [Més OSINT](#més-osint)

2. **Auditoria de Serveis**
   2.1 [Escaneig](#escaneig)
   2.2 [Auditoria SSH](#auditoria-ssh)
   2.3 [Enumeració](#enumeració)

3. **Funcionalitats Afegides**
   3.1 [Bot de Telegram en Python](#bot-de-telegram-amb-python)
   3.2 [Contenidor de Docker per a Auditories Automatitzades](#contenidor-de-docker-per-a-auditories-automatitzades)

4. [Pla de Millora](#pla-de-millora)

5. [Landing Page](#landing-page)

# 💡 Introducció 💡

ch## CUSTOM TKINTER

La llibreria **CustomTkinter** és una extensió de Tkinter que proporciona nous widgets moderns i personalitzables. Aquests widgets es poden utilitzar de la mateixa manera que els widgets Tkinter estàndard i també es poden utilitzar en combinació amb elements Tkinter normals.

**CustomTkinter** proporciona les següents característiques principals:

- **Widgets moderns i personalitzables:** CustomTkinter proporciona una àmplia gamma de widgets moderns i personalitzables, com ara botons, etiquetes, caixes de text, etc. Aquests widgets es poden utilitzar per crear interfícies d'usuari més modernes i atractius.
- **Ajustament automàtic al tema del sistema:** CustomTkinter permet ajustar automàticament els colors i les formes dels widgets al tema del sistema operatiu. Això facilita la creació d'interfícies d'usuari que s'integrin bé amb l'entorn d'usuari.
- **Suport per a la escala de DPI alta:** CustomTkinter suporta la escala de DPI alta per a Windows i macOS. Això permet que les interfícies d'usuari es mostrin clarament en monitors amb una resolució alta.

Per utilitzar **CustomTkinter**, simplement cal importar el mòdul `customtkinter`. A continuació, es poden crear widgets **CustomTkinter** de la mateixa manera que es creen widgets Tkinter estàndard.

## Menú Gràfic  

Quan executem el script main.py ens apareixerà el següent:

![Interficie_grafica](/img/Interficie_grafica.png)

Això es la interfície gràfica que hem creat de moment, al ser provisional per comprovar el funcionament de les eines, encara està en desenvolupament, però tot funciona correctament.

El menú gràfic s'ha pogut crear gràcies als paquets tkinter (s'encarga de crear interficíes gràfiques) i customtkinter (personalitza més i millora l'aparença del menú gràfic.)

## Descripció detallada del menú gràfic

### Títol: E3 - Eines d'OSINT

**Objectiu:** El menú gràfic del projecte E3 proporciona una interfície d'usuari fàcil d'utilitzar per a executar diverses eines (OSINT, TheHarvester...)

### Components:

1. **Barra de títol:**
   - Mostra el nom del projecte (E3)

2. **Panell d'eines:**
   - Conté botons per a cada una de les eines disponibles, cadascun amb una icona i un nom descriptiu:
      - Apt Shodan: Cerca informació sobre servidors web i dispositius connectats a Internet que utilitzen el gestor de paquets APT.
      - Més OSINT: Enllaça a una pàgina web amb una llista extensa d'eines d'OSINT.
      - The Harvester: Recull informació d'usuaris i correus electrònics a partir de noms de domini i subdominis.
      - Auditoria SSH: Realitza una auditoria de seguretat en servidors SSH per a identificar vulnerabilitats.
      - Enumeració: Mostra informació sobre un objectiu específic, com ara noms d'usuaris, grups, carpetes i fitxers.
      - Bot Telegram: Envia missatges a un canal de Telegram mitjançant un bot.
      - Escaneig: Realitza escaneigs de ports, xarxes i hosts amb nmap.

3. **Panell d'opcions:**
   - Mostra opcions específiques per a l'eina seleccionada al panell d'eines. El contingut d'aquest panell varia segons l'eina:
      - Selecciona una de les opcions de OSINT: Mostra un menú desplegable amb les opcions disponibles per a cada eina.
      - Introdueix el nom d'usuari: Mostra un camp de text per a introduir un nom d'usuari a buscar (p.ex. per a The Harvester).
      - Selecciona la ruta de l'imatge: Mostra un camp de text per a seleccionar la ruta d'una imatge a analitzar (p.ex. per a l'enumeració d'imatges).
      - Introduir la IP/URL: Mostra un camp de text per a introduir l'adreça IP o URL de l'objectiu a analitzar (p.ex. per a l'escaneig de ports).
      - Introduir el token de Telegram: Mostra un camp de text per a introduir el token d'autorització del canal de Telegram (p.ex. per al bot de Telegram).

4. **Àrea de resultats:**
   - Mostra els resultats de l'eina seleccionada en format text.
   - Els resultats poden incloure informació com ara:
      - Llista de servidors web i dispositius trobats (Apt Shodan)
      - Llista d'usuaris i correus electrònics trobats (The Harvester)
      - Llista de vulnerabilitats trobades (Auditoria SSH)
      - Informació sobre l'objectiu (Enumeració)
      - Missatges enviats al canal de Telegram (Bot Telegram)
      - Llista de ports oberts (Escaneig)


# 📡 Fase de Reconeixement 📡

# Api Shodan en Python

# TheHarvester en Python
![theHarvester](/img/theHarvester-logo.webp)

TheHarvester és una eina de codi obert dissenyada per recopilar informació de fonts públiques en línia amb l'objectiu de realitzar anàlisis d'intel·ligència i proves de penetració. Desenvolupada en Python, TheHarvester és particularment útil per recopilar informació sobre dominis, subdominis, adreces de correu electrònic, noms d'amfitrions, xarxes i altres detalls relacionats amb una entitat en línia.

Algunes de les característiques clau de TheHarvester són:

1. Recerca de Dominis i Subdominis: TheHarvester permet buscar informació sobre un domini específic, inclosos els subdominis associats. Pots realitzar cerques en motors de cerca, motors de cerca de certificats SSL, servidors DNS i altres recursos públics per recopilar una llista exhaustiva de dominis i subdominis relacionats.

2. Adreces de Correu Electrònic: L'eina pot buscar adreces de correu electrònic associades amb un domini o una entitat específica. Això és útil per identificar contactes clau i possibles punts d'entrada en una organització.

3. Recerca de Noms d'Amfitrions i Xarxes: TheHarvester també pot recopilar informació sobre noms d'amfitrions i xarxes associades amb un domini. Això proporciona una visió més completa de la infraestructura tecnològica d'una entitat.

4. Integració amb APIs Públiques: L'eina pot utilitzar APIs públiques de serveis com Shodan, servidors de claus PGP i altres per recopilar informació addicional sobre una entitat.

5. Suport per a Múltiples Fonts: TheHarvester és capaç de consultar i combinar informació de diverses fonts, el que permet obtenir resultats més complets i precisos.

6. Personalització de Cerques: Els usuaris poden personalitzar les seves cerques mitjançant l'especificació de paràmetres com el motor de cerca a utilitzar, la font d'informació, el tipus d'informació a cercar i més.


### Instal·lació

Per a la instal·lació de l'eina TheHarvester per tal d'executar el seu script, seguirem l'opció 4 (source) de la instal·lació de theHarvester de la pagina oficial de Github (Link: https://github.com/laramies/theHarvester).

1. Primer de tot usarem la comanda ```git clone https://github.com/laramies/theHarvester ``` per clonar el contingut del repositori en una carpeta.

![Clonar](/img/Selecció_4387.png)

2. A continuació entrem a la carpeta creada amb ```cd theHarvester```

![Entrar_carpeta](/img/Selecció_4388.png)

3. Per últim, realitzarem la instal·lació amb la comanda ```python3 -m pip install -r requirements/base.txt```, la qual instal·larà els requeriments que necessita l'eina TheHarvester

![Instal·lació](/img/Selecció_4389.png)

4. Comprovem que l'instal·lació s'ha realitzat correctament executant l'script que es troba a la carpeta clonada. Farem la comanda ```python3 theHarvester -h```

![Comprovació_TheHarvester](/img/Selecció_4391.png)

### Contingut Script

Aqui està el script en python de la funció que hem creat per a que cridi a l'eina theHarvester i que esculli les opcions necessaries:


**POSAR FOTO DE L'SCRIPT**

**CAL EXPLICACIÓ AMB DETALL DE L'SCRIPT**

### Execució Script

**POSAR GIF CONFORME FUNCIONA L'SCRIPT**

# Més OSINT

Per aquesta tasca tenim que investigar sobre eines, scripts o altres recursos que ens poden semblar útils i interessants per posar el nostre script de python

Ens van posar la següent web per investigar sobre moltes eines de scripts, pero vam optar per seleccionar 2 de les que considerem més útils:

### 1. **Sherlock**

Sherlock és una eina de codi obert utilitzada per a la recopilació d'informació de fonts públiques en línia

- **Cerca de perfils de xarxes socials:** Sherlock pot cercar perfils a múltiples plataformas de xarxes socials com Facebook, Twitter, Instagram, LinkedIn, Reddit, TikTok i altres. Això pot ser útil per trobar informació sobre una persona o una entitat específica en línia.
- **Recopilació d'informació pública:** L'eina recopila informació que és pública i que els usuaris han compartit als seus perfils online. Això inclou noms d'usuari, fotos de perfil, descripcions de perfils i altra informació visible públicament.
- **Automatització:** Sherlock automatitza la tasca de prop de perfils a diverses plataformas, el que ahorra temps i esforç en la recerca d'aquesta informació de manera manual.

#### Contingut del Script
![Captura_script_mesOSINT_Sherlock](/img/Selecció_1153.png)

#### Captures de demostració de l'script
![Captura_demostracio_mesOSINT_Sherlock_1](/img/Selecció_1155.png)
![Captura_demostracio_mesOSINT_Sherlock_2](/img/Selecció_1157.png)

### 2. **Exiftool**
ExifTool és una eina de línia de comandes molt potent i versàtil dissenyada per gestionar i editar metadades en arxius d'imatge, vídeo i altres tipus de fitxers mitjançant metadades. Aquesta eina és àmpliament utilitzada per professionals de la fotografia, investigadors forenses digitals, i altres persones que necessiten accedir i gestionar la informació incrustada als arxius.

#### Contingut de l'script

![Captura_script_mesOSINT_Exitfool_1](/img/Selecció_4125.png)

#### Captures de demostració de l'script

![Captura_demostracio_mesOSINT_Exitfool_1](/img/Selecció_1158.png)
![Captura_demostracio_mesOSINT_Exitfool_2](/img/Selecció_1159.png)

# 💻 Auditoria de serveis 💻

# Escaneig

- **Menú**

![menu_script_escaneig](/img/Selecció_1160.png)

- **Descobrir hosts de xarxa.**

![hosts_xarxa_escaneig](/img/Selecció_1161.png)

- **Funcionament**

![funcionament_hosts_xarxa_escaneig](/img/Selecció_1162.png)

- **Escaneig de ports oberts**

![ports_oberts_escaneig](/img/Selecció_1163.png)

- **Funcionament**

![funcionament_ports_oberts_escaneig](/img/Selecció_1164.png)

- **Llistat de serveis i versions d'un, un rang o tots els ports**

![serveis_i_versions_escaneig](/img/Selecció_1165.png)

- **Funcionament**

![funcionament_serveis_i_versions_escaneig](/img/Selecció_1166.png)

- **Llistat de vulnerabilitats d'un, un rang o tots els serveis**

![vulnerabilitats_serveis_escaneig](/img/Selecció_1167.png)

- **Funcionament**

![funcionament_vulnerabilitats_serveis_escaneig](/img/Selecció_1168.png)

# Auditoria SSH

# Enumeració

# 📂 Funcionalitats afegides 📂

# Bot de telegram amb Python

### Contingut script

![bot_telegram_script](/img/Selecció_1170.png)


### Prova
- Prova amb una imatge al grup de telegram per si funciona l’enviament desde el bot amb python, i veiem que s’envia correctament

![proves_bot_telegram](/img/Selecció_1171.png)

# Contenidor de Docker per a Auditories Automatitzades

- **EN PROCÉS**

# Pla de Millora

- **EN PROCÉS**

# Landing Page

- **EN PROCÉS**