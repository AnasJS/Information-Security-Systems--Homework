from builtins import set
from socket import *
from TCP import *
import _pickle as pickle
import rsa as rsa
from rc4 import *
import hashlib
class Client:
   def __init__(self,server_host,server_port,id):
       print("i am new client my id is : {i}".format(i=id))
       self.server_host = server_host
       self.server_port = server_port
       self.listening_socket = socket()#socket.AF_INET, socket.SOCK_STREAM
       self.id = id
       self.listening_socket.connect((server_host,server_port))
       self.public_key, self.private_key = rsa.newkeys(1024)
       n_public = pickle.dumps(self.public_key)
       self.listening_socket.send(b'0')
       self.listening_socket.send(bytes([id]))
       msg = self.listening_socket.recv(1024)
       self.listening_socket.send(n_public)

   def sender(self,data,client_id):
       print('in sender')

       sender_socket = socket()
       sender_socket.connect((self.server_host,self.server_port))
       sender_socket.send(b'1')
       # 0
       send_one_message(sender_socket,bytes([client_id]))
       send_one_message(sender_socket,bytes([self.id]))
       # print("distenation client : {df}".format(df =  bytes([client_id])))
       # 00
       n_public = recv_one_message(sender_socket)
       print("n_public {n_public}".format(n_public=n_public))
       public_key =pickle.loads(n_public)

       # sender_socket.send(cipher_data)
       session_key  = "session_key"
       cipher_session_key = rsa.encrypt(session_key.encode('utf-8'),public_key)
       cipher_data =encrypt(data,session_key)

       packet = bytearray()
       packet += cipher_session_key
       packet += cipher_data
       hashedData = hashlib.sha1()
       hashedData.update(packet)
       sign = rsa.sign(hashedData.digest(),self.private_key,'SHA-1')
       packet +=sign
       # 3
       print("end send len(packet){h}".format(h = len(packet)))
       send_one_message(sender_socket, packet)

       # 1
       send_one_message(sender_socket, bytes([len(cipher_data)]))
       print("end send len cipher_data {len_cipher_data}".format(len_cipher_data = len(cipher_data)))
       # 2
       send_one_message(sender_socket , bytes([len(cipher_session_key)]))
       print("end send len cipher_session_key {len_cipher_session_key}".format(len_cipher_session_key = len(cipher_session_key)))
       # 4
       print("end send len sign {len_sign}".format(len_sign=len(sign)))
       send_one_message(sender_socket, bytes([len(sign)]))
       print("cipher data {sd}".format(sd=cipher_data))

       sender_socket.close()
       # sender_socket.close()
   def recive(self):
       print("in reciver")
       sender_n_public_key = recv_one_message(self.listening_socket)
       sender_public_key = pickle.loads(sender_n_public_key)
       # 3
       packet = recv_one_message(self.listening_socket)
       print("size packet {o}".format(o = len(packet)))
       # 1
       size_cipher_data = int.from_bytes(recv_one_message(self.listening_socket),'big')
       print("size_cipher_data {size_cipher_data}".format(size_cipher_data=size_cipher_data))
       # 2
       size_cipher_key =int.from_bytes(recv_one_message(self.listening_socket),'big')
       print("size_cipher_key {size_cipher_key}".format(size_cipher_key =size_cipher_key))
       # 4
       size_sign = int.from_bytes(recv_one_message(self.listening_socket), 'big')
       print("size_sign {size_sign}".format(size_sign=size_sign))

       packet1 = packet[:-size_sign]
       sign = packet[-size_sign:]

       # recived_hash = rsa.verify(sign,sender_public_key)
       hashed_packet1 = hashlib.sha1()
       hashed_packet1.update(packet1)
       if rsa.verify(hashed_packet1.digest(),sign,sender_public_key):
           cipher_session_key = packet1[:size_cipher_key]
           cipher_data= packet1[size_cipher_key:size_cipher_key+size_cipher_data]
           print("i   a m   h e r e ")
           session_key = rsa.decrypt(cipher_session_key, self.private_key)
           print(session_key)
           print("type(cipher_data){g}".format(g = type(cipher_data)))

           print("type(session_key){g}".format(g=type(session_key)))
           print("cipher_data {cipher_data}".format(cipher_data=cipher_data))

           data = decrypt(cipher_data,session_key.decode('utf-8'))
           print(data)
           return data
       return None
   def clossing_connect(self):
       print("client {i} is leaving".format(self.id))
       self.listening_socket.close()

