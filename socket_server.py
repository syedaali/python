__author__ = 'syedaali'

'''
Sample program to demonstrate a socket based server in Python
Once you run this program, you can telnet to port 9000 and type in
random characters.
The basic process of socket connection is:
- Create socket
- Bind
- Listen
- Accept
- Receive data
- Send reply if needed
- Close connection
'''

import socket
import sys
from thread import  *
import signal

def sig_handler(signum, stack):
    print '\nReceived signal, quitting'
    sys.exit(0)

signal.signal(signal.SIGINT,sig_handler)

#function that is called once you listen to a port
def clientthreads(conn):
    conn.send('Hello, say something\n')
    while True:
        data = conn.recv(2048)
        reply = 'Got -> {}'.format(data)
        if not data:
            break
        conn.sendall(reply)
    conn.close()

def main():
    #listening to all interfaces on port 9000
    HOST = ''
    PORT = 9000

    #create a socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print 'Socket created'

    #try to bind to port
    try:
        s.bind((HOST,PORT))
    except socket.error as msg:
        print 'Unable to bind {0} with message {1}'.format(str(msg[0]),msg[1])
        sys.exit(1)
    else:
        print 'Socket bind complete'

    #after binding to port, start to  listen
    s.listen(10)
    print 'Socket now listening'

#now that we are listening, we are ready to accept
#we call our function clientthreads once we connnect
    while 1:
        #this is a blocking call
        conn, addr = s.accept()
        print 'Connected with {0} : {1}'.format(addr[0],str(addr[1]))
        #here is where we multi-thread
        start_new_thread(clientthreads ,(conn,))

    s.close()

if __name__=='__main__':
    main()