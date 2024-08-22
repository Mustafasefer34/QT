# -*- coding: utf-8 -*-
"""
Created on Tue Aug 20 09:46:29 2024

@author: casper
#TCP CLIENT SOCKET
"""

import socket

client_socket =socket.socket()

client_socket.connect(('localhost',50000))

mesaj="client 3 den selamlar"

cikis_mesaji="exit"

client_socket.send(bytes(cikis_mesaji,'utf-8'))

client_socket.close()

