from Client import *
from Server import *
from socket import gethostname
from rc4 import *

host  = gethostname()
port = 12345
# server = Server(host , port)

c1 = Client(host,port,5)
c2 = Client(host,port,8)



c1.sender("data",8)
c2.recive()
# server.clossing()
# for c in Client:
#     c.clossing_connect()
# for i in range(10):
#     name = "s{t}".format(t=i)
#     vars() [name]= socket()
#     client.append("s{t}".format(t = i))

