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

Aqui està el script en python que hem creat per a que cridi a l'eina theHarvester i que esculli les opcions necessaries:

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

# 🔉 Escaneig 🔉

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

# 📊 Auditoria SSH 📊

# 📃 Enumeració 📃

# 📂 Funcionalitats afegides 📂

# 🤖 Bot de telegram amb Python 🤖

### Contingut script

![bot_telegram_script](/img/Selecció_1170.png)


### Prova
- Prova amb una imatge al grup de telegram per si funciona l’enviament desde el bot amb python, i veiem que s’envia correctament

![proves_bot_telegram](/img/Selecció_1171.png)

# 🐳 Contenidor de Docker per a Auditories Automatitzades 🐳

- **EN PROCÉS**

# 🔧 Pla de Millora 🔧

- **EN PROCÉS**

# 📄 Landing Page 📄

- **EN PROCÉS**