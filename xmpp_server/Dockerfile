FROM ubuntu:18.04

RUN apt-get update
RUN apt-get install -y \
    prosody

COPY cfgs/prosody.cfg.lua /etc/prosody/prosody.cfg.lua
COPY cfgs/conf.d/ /etc/prosody/conf.d/
COPY certs/chat.aparkinson.net.cnf /var/lib/prosody/chat.aparkinson.net.cnf
COPY certs/chat.aparkinson.net.crt /var/lib/prosody/chat.aparkinson.net.crt
COPY certs/chat.aparkinson.net.key /var/lib/prosody/chat.aparkinson.net.key

