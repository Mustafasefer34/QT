# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
TCP SERVER SOCKET
"""
import socket

server_socket=socket.socket()

server_socket.bind(('localhost',50000)) #port numarasını verdik 

server_socket.listen(5)#client sayımız 5
print("Soket oluşturuldu bağlantı bekleniyor...")

while True:
    client_socket, adres=server_socket.accept()
    print(adres," isimli bilgisayar ile bağlantı kuruldu")
    
    #client dan gelen mesajı ekrana yazdırıyoruz
    gelen_mesaj=client_socket.recv(1024).decode()
    print(gelen_mesaj)
    
    client_socket.close()
    
    #While döngüsünde takılı kalmamak için exit mesajını yollamamız gerekiyor.
    
    if(gelen_mesaj=='exit'):
        break
    
print("Hoşçakalın")
      
    
    
    