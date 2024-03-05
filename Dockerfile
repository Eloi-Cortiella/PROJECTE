FROM ubuntu:latest

# Configura el directori de treball
WORKDIR /PROJECTE

# Copia el script principal al directori de treball
COPY . .

# Instal·la les eines necesaries
RUN apt-get update && \
    apt-get install -y nmap auditd && \
    apt-get install -y python3-tk

## Dependencies
RUN apt-get install -y git python3 python3-pip smbclient && \
    pip3 install customtkinter &&

## Requeriments
RUN pip3 install --no-cache-dir -r requirements.txt -v

# Instal·lació eina Enum4linux-ng
RUN git clone https://github.com/cddmp/enum4linux-ng.git /enum4linux
RUN cd enum4linux-ng/ && pip3 install -r requirements.txt

# Instal·lació eina theHarvester
RUN git clone https://github.com/laramies/theHarvester.git /theHarvester
RUN cd theHarvester/ pip3 install -r requirements.txt

#RUN export DISPLAY=:0.0º

# Defineix l'entorn
#ENV LANG es.UTF-8

# CMD o altres instruccions per executar la aplicació
# ENTRYPOINT ["python3", "main.py"]