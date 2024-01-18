# PROJECTE ASIX MP14 - 2023/2024

**Projecte ASIX del mòdul MP14, format per Èric González, Èric Peréz i Eloi Cortiella.**

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

# Fase de Reconeixement

## Api Shodan en Python

## TheHarvester en Python

### Instal·lació

### Contingut Script

```

```

## Més OSINT

Per aquesta tasca tenim que investigar sobre eines, scripts o altres recursos que ens poden semblar útils i interessants per posar el nostre script de python

Ens van posar la següent web per investigar sobre moltes eines de scripts, pero vam optar per seleccionar 2 de les que considerem més útils:

### 1. **Sherlock**

Sherlock és una eina de codi obert utilitzada per a la recopilació d'informació de fonts públiques en línia

- **Cerca de perfils de xarxes socials:** Sherlock pot cercar perfils a múltiples plataformas de xarxes socials com Facebook, Twitter, Instagram, LinkedIn, Reddit, TikTok i altres. Això pot ser útil per trobar informació sobre una persona o una entitat específica en línia.
- **Recopilació d'informació pública:** L'eina recopila informació que és pública i que els usuaris han compartit als seus perfils online. Això inclou noms d'usuari, fotos de perfil, descripcions de perfils i altra informació visible públicament.
- **Automatització:** Sherlock automatitza la tasca de prop de perfils a diverses plataformas, el que ahorra temps i esforç en la recerca d'aquesta informació de manera manual.

#### Contingut del Script
![Captura_script_mesOSINT_Sherlock](/Documentacio/img/Selecció_1153.png)

#### Captures de demostració de l'script
![Captura_demostracio_mesOSINT_Sherlock_1](/Documentacio/img/Selecció_1155.png)
![Captura_demostracio_mesOSINT_Sherlock_2](/Documentacio/img/Selecció_1157.png)

### 2. **Exiftool**
ExifTool és una eina de línia de comandes molt potent i versàtil dissenyada per gestionar i editar metadades en arxius d'imatge, vídeo i altres tipus de fitxers mitjançant metadades. Aquesta eina és àmpliament utilitzada per professionals de la fotografia, investigadors forenses digitals, i altres persones que necessiten accedir i gestionar la informació incrustada als arxius.

#### Contingut de l'script

![Captura_script_mesOSINT_Exitfool_1](/Documentacio/img/Selecció_4125.png)

#### Captures de demostració de l'script

![Captura_demostracio_mesOSINT_Exitfool_1](/Documentacio/img/Selecció_1158.png)
![Captura_demostracio_mesOSINT_Exitfool_2](/Documentacio/img/Selecció_1159.png)

## Tasca - Escaneig

- **Menú**

![menu_script_escaneig](/Documentacio/img/Selecció_1160.png)

- **Descobrir hosts de xarxa.**

![hosts_xarxa_escaneig](/Documentacio/img/Selecció_1161.png)

- **Funcionament**

![funcionament_hosts_xarxa_escaneig](/Documentacio/img/Selecció_1162.png)

- **Escaneig de ports oberts**

![ports_oberts_escaneig](/Documentacio/img/Selecció_1163.png)

- **Funcionament**

![funcionament_ports_oberts_escaneig](/Documentacio/img/Selecció_1164.png)

- **Llistat de serveis i versions d'un, un rang o tots els ports**

![serveis_i_versions_escaneig](/Documentacio/img/Selecció_1165.png)

- **Funcionament**

![funcionament_serveis_i_versions_escaneig](/Documentacio/img/Selecció_1166.png)

- **Llistat de vulnerabilitats d'un, un rang o tots els serveis**

![vulnerabilitats_serveis_escaneig](/Documentacio/img/Selecció_1167.png)

- **Funcionament**

![funcionament_vulnerabilitats_serveis_escaneig](/Documentacio/img/Selecció_1168.png)


# Auditoria de serveis

## Escaneig

## Auditoria SSH

## Enumeració

# Funcionalitats afegides

## Bot de telegram amb Python

### Contingut script

![bot_telegram_script](/Documentacio/img/Selecció_1170.png)


### Prova
- Prova amb una imatge al grup de telegram per si funciona l’enviament desde el bot amb python, i veiem que s’envia correctament

![proves_bot_telegram](/Documentacio/img/Selecció_1171.png)

## Contenidor de Docker per a Auditories Automatitzades

## Pla de Millora

## Landing Page