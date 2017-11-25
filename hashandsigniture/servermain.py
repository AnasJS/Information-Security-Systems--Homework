from Server import *
from socket import *
host  = gethostname()
port = 12345
server = Server(host , port)
server.run()