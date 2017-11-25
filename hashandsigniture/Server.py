from ClientThread import *
from socket import *

class Server:
    def __init__(self,host ,port):
        self.host = host
        self.port = port
        #socket.AF_INET, socket.SOCK_STREAM
        self.socket = socket()
        self.socket.bind((self.host , self.port))
        self.socket.listen(10)

    def print_info(self):
        pass
    def run(self):
        threads = []
        while True:
            print("Multithreaded Python server : Waiting for connections from TCP clients...")
            (conn1, (ip, port)) = self.socket.accept()
            newthread = ClientThread(ip, port, conn1)
            print(ip)
            newthread.start()
            # newthread.join()
            threads.append(newthread)
            newthread.join()
            # MESSAGE = input("tcpClientA: Enter message to continue/ Enter exit:")
            # if MESSAGE == 'exit':
            #     for t in threads:
            #         t.clossing_connect()
            #     self.clossing()
            #     break
        for t in threads:
            t.join()
    def clossing(self):
        self.socket.close()