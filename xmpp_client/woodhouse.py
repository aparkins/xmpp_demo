#!/usr/bin/env python

import logging, uuid, sys
from sleekxmpp import ClientXMPP, Message
from sleekxmpp.exceptions import IqError, IqTimeout


class Woodhouse(ClientXMPP):
    def __init__(self, jid, password):
        ClientXMPP.__init__(self, jid, password)
        self.rooms = []
        self.muc_host = 'chat-muc.aparkinson.net'
        self.nick = 'woody'

        self.add_event_handler("session_start", self.session_start)
        self.add_event_handler('message', self.message)

    def invite_to_room(self, requester, room_name):
        print('ASKED TO INVITE {} TO {}!'.format(requester, room_name))
        room_jid = '{}@{}'.format(room_name, self.muc_host)
        if room_jid not in self.plugin['xep_0045'].getJoinedRooms():
            print('JOINED {}!'.format(room_jid))
            self.plugin['xep_0045'].joinMUC(room_jid, self.nick)
        self.plugin['xep_0249'].send_invitation(requester, room_jid, reason="Beacuse you asked me to!")

    def session_start(self, event):
        print('SESSION STARTED!')
        self.send_presence()
        roster = self.get_roster(block=True)

    def message(self, msg):
        print('RECEIVED MESSAGE!')

        # Group chat messages shouldn't ACTUALLY be handled by this function
        if msg['type'] == 'groupchat':
            return

        if msg['body'].startswith('join-room'):
            args = msg['body'].split(' ')[1:]
            self.invite_to_room(msg['from'].bare, *args)

        else:
            self.send_message(mto=msg['from'].bare, mbody='You sent me an invalid message: {}'.format(msg['body']))


jid = "woodhouse@aparkinson.net"
password = "password"

logging.basicConfig(level=logging.INFO, format='%(levelname)-8s %(message)s')
xmpp = Woodhouse(jid, password)
xmpp.register_plugin('xep_0030')
xmpp.register_plugin('xep_0045')
xmpp.register_plugin('xep_0199')
xmpp.register_plugin('xep_0249')
xmpp.connect(address=('localhost', '5222'))
xmpp.process(block=True)
