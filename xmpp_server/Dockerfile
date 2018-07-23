FROM ubuntu:18.04

COPY cfgs/prosody.cfg.lua /etc/prosody/prosody.cfg.lua
COPY cfgs/conf.avail/ /etc/prosody/conf.avail/

RUN apt-get update
RUN apt-get install -y \
    prosody

