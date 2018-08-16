#!/usr/bin/env python

import logging, uuid, sys
from sleekxmpp import ClientXMPP, Message
from sleekxmpp.exceptions import IqError, IqTimeout


class EchoBot(ClientXMPP):
    def __init__(self, jid, password, room, nick):
        ClientXMPP.__init__(self, jid, password)
        self.room = room
        self.nick = nick

        self.add_event_handler("session_start", self.session_start)
        self.add_event_handler('groupchat_message', self.groupchat_message)

    def session_start(self, event):
        self.send_presence()
        roster = self.get_roster(block=True)
        self.plugin['xep_0045'].joinMUC(self.room, self.nick)

    def groupchat_message(self, msg):
        if msg['mucnick'] != self.nick:
            self.send_message(mto=msg['from'].bare, mbody='Hi! You sent me this: {}'.format(msg['body']), mtype='groupchat')


jid = "woodhouse@aparkinson.net"
password = "password"
room = sys.argv[1]
nick = sys.argv[2]

logging.basicConfig(level=logging.DEBUG, format='%(levelname)-8s %(message)s')
xmpp = EchoBot(jid, password, room, nick)
xmpp.register_plugin('xep_0030')
xmpp.register_plugin('xep_0045')
xmpp.register_plugin('xep_0199')
xmpp.connect(address=('localhost', '5222'))
xmpp.process(block=True)
