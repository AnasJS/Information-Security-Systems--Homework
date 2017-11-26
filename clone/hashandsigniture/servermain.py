from Server import *
from socket import *
host  = gethostname()
port = 12346
server = Server(host , port)
server.run()