import socket
from ssh2.session import Session

host = '137.221.149.141'
user = 'zanserver'
password = ''

sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.connect((host,22))

session = Session()
session.handshake(sock)
session.userauth_password(user, password)

channel = session.open_session()
channel.execute('cd ~/innovationProject/frec/facrec && ls && python identify_face_image.py')
size, data = channel.read()
while size > 0:
    print(data.decode())
    size, data = channel.read()
channel.close()
print("Exit status: {}".format(channel.get_exit_status))

