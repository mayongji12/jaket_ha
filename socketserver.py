#__coding:utf-8__
#Create SocketServerTCP service 
#Create by myj
#create at 2015-09-06 
import SocketServer
from SocketServer import StreamRequestHandler as SRH
from time import ctime
import os
host = '192.168.1.239'
port = 9999
addr = (host,port)

class Servers(SRH):
    def handle(self):
#        print 'got connection from ',self.client_address  
#        self.wfile.write('connection %s:%s at %s succeed!' % (host,port,ctime()))  
        while True:
            data = self.request.recv(2048)
            if not data:
                break
#            print data
#            print "RECV from ", self.client_address[0]  
            result = os.popen(data).read()
#            result = str(eval(data))
#            print result
            self.request.send(result)

#print 'server is running....'  
server = SocketServer.ThreadingTCPServer(addr,Servers)
os.getpid() #get current python process ID
server.serve_forever()
