#__coding:utf-8__
import os
import subprocess
import sys
import time
import SocketServer
from SocketServer import StreamRequestHandler as SRH
from time import ctime

def checkping(ip):
    ubprocess.Popen([r'./ping.sh',ip],stdout=subprocess.PIPE)
    result=p.stdout.read()
    if '1\n'==result:
        return 1
    else
        return 0 

class CheckService(object):
    def __init__(self,service):
        self.service =service
    def check(self):
        return os.popen('ps -ef|grep %s|grep -v grep' %self.service).read()

host = '192.168.1.241'
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

#if run socket server cancel the #
##print 'server is running....'
#server = SocketServer.ThreadingTCPServer(addr,Servers)
#os.getpid() #get current python process ID
#server.serve_forever()


if __name__='main':
    workdir=os.popen('pwd').read().strip('\n')
    beat=os.popen("grep primarybeat %s/jakerha.cnf|awk -F= '{print $2}'" %workdir).read().strip('\n')
    host=os.popen("grep primaryhost %s/jakerha.cnf|awk -F= '{print $2}'" %workdir).read().strip('\n')
    cr=os.popen("grep crip %s/jakerha.cnf|awk -F= '{print $2}'" %workdir).read().strip('\n')
    if checkping(beat) or checkping(host) or checkping(cr):
        sys.exit()
    else:
        status=os.popen("head -1 %s/status_master.txt" %workdir).read().strip('\n')
        if status=='1':
            #服务运行主机
            os.popen("echo 0 > %s/status_master.txt" %workdir)
            os.popen("init 0")
        else:
            #备用主机
            time.sleep(5)
            os.popen("sh $s/database_master.sh")
         
        
        
    
