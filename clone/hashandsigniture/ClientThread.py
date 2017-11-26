from threading import Thread
from TCP import *
import _pickle as pickle
# Multithreaded Python server : TCP Server Socket Thread Pool
clients = {}
publics ={}
client = [1 , 2]
class ClientThread(Thread):
    def __init__(self, ip, port, conn):
        Thread.__init__(self)
        self.ip = ip
        self.port = port
        self.conn = conn
        print( "[+] New server socket thread started for " + ip + ":" + str(port))

    def run(self):
        tag = self.conn.recv(1)
        if tag == b'0':
            id = self.conn.recv(1024)
            self.conn.send("accept".encode('utf-8'))
            public_key = self.conn.recv(1024)
            clients.update({int.from_bytes(id,'big'):self.conn})
            publics.update({int.from_bytes(id,'big'):public_key})
        elif tag == b'1':
            print("in transpose state")
            # 0
            destination_id = int.from_bytes(recv_one_message(self.conn),'big')
            sender_id      = int.from_bytes(recv_one_message(self.conn), 'big')
            print("sender_id      {sender_id}     ".format(sender_id=sender_id))
            print("destination_id {destination_id}".format(destination_id=destination_id))
            # 00
            send_one_message(self.conn,publics[destination_id])
            send_one_message(clients[destination_id],publics[sender_id])
            print("sender_public_key {p}".format(p=publics[sender_id]))
            print("distenation_public_key {p}".format(p=publics[destination_id]))

            # 3
            send_one_message(clients[destination_id], (recv_one_message(self.conn)))
            print("packet lhhlhlhlhlhlh")
            # 1
            d1=recv_one_message(self.conn)
            send_one_message(clients[destination_id],d1)
            print("len cipher data")
            # 2
            send_one_message(clients[destination_id],recv_one_message(self.conn))
            print("len cipher session key" )
            #4
            send_one_message(clients[destination_id],recv_one_message(self.conn))
            print("len sign")
            self.conn.close()
            # clients[destination_id].send(self.conn.recv(1024))
            # 1 size of cipher key
            # clients[destination_id].send(self.conn.recv(1024))
            # print("after 1 ")
            # self.conn.send("accept".encode())
            # # msg = clients[destination_id].recv(1024)
            #
            # # 2 size of cipher data
            # clients[destination_id].send(self.conn.recv(1024))
            # self.conn.send("accept".encode())
            # # msg = clients[destination_id].recv(1024)
            # # 3 packet
            # clients[destination_id].send(self.conn.recv(1024))
            #
            # # data = self.conn.recv(1024)
            #
            # # print(data)
            # # clients[destination_id].send(data)
            # print("ending transpose state")

        else:
            print('error tagging message')




    def clossing_connect(self):
        # print("client {i} is leaving".format(self.conn.listening_socket.id))
        self.conn.close()