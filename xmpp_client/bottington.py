#!/usr/bin/env python

import logging, uuid, sys
from sleekxmpp import ClientXMPP, Message
from sleekxmpp.exceptions import IqError, IqTimeout


class Bottington(ClientXMPP):
    def __init__(self, jid, password):
        ClientXMPP.__init__(self, jid, password)
        self.rooms = []
        self.muc_host = 'chat-muc.aparkinson.net'
        self.nick = 'bttngtn'

        self.add_event_handler("session_start", self.session_start)
        self.add_event_handler("groupchat_direct_invite", self.invite)
        self.add_event_handler('groupchat_message', self.groupchat_message)

    def invite(self, inv):
        self.plugin['xep_0045'].joinMUC(inv['groupchat_invite']['jid'], self.nick)

    def session_start(self, event):
        self.send_presence()
        roster = self.get_roster(block=True)
        self.request_join_room()

    def request_join_room(self):
        self.send_message(mto='woodhouse@aparkinson.net', mbody='join-room our-test-room')

    def groupchat_message(self, msg):
        if msg['mucnick'] != self.nick:
            self.send_message(mto=msg['from'].bare, mbody='Hi! You sent me this: {}'.format(msg['body']), mtype='groupchat')


jid = "bottington@aparkinson.net"
password = "password"

logging.basicConfig(level=logging.INFO, format='%(levelname)-8s %(message)s')
xmpp = Bottington(jid, password)
xmpp.register_plugin('xep_0030')
xmpp.register_plugin('xep_0045')
xmpp.register_plugin('xep_0199')
xmpp.register_plugin('xep_0249')
xmpp.connect(address=('localhost', '5222'))
xmpp.process(block=True)
