FROM ubuntu:18.04

RUN apt-get update
RUN apt-get install -y \
    prosody

COPY cfgs/prosody.cfg.lua /etc/prosody/prosody.cfg.lua
COPY cfgs/conf.d/ /etc/prosody/conf.d/

COPY certs/aparkinson.net.cnf /var/lib/prosody/aparkinson.net.cnf
COPY certs/aparkinson.net.crt /var/lib/prosody/aparkinson.net.crt
COPY certs/aparkinson.net.key /var/lib/prosody/aparkinson.net.key
RUN prosodyctl --root cert import aparkinson.net /var/lib/prosody/

RUN prosodyctl register woodhouse aparkinson.net password
RUN prosodyctl register bottington aparkinson.net password
