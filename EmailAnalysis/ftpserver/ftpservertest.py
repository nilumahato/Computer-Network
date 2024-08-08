from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer

# Create an authorizer object to handle authentication
authorizer = DummyAuthorizer()

# Add a user with full permissions
authorizer.add_user("user", "password", ".", perm="elradfmwMT")

# Create an FTP handler object
handler = FTPHandler
handler.authorizer = authorizer

# Define the server address and port
server_address = ('', 21)  # Use port 21 for standard FTP

# Create and start the FTP server
server = FTPServer(server_address, handler)
print("Simple FTP server running on port 21.")
server.serve_forever()
