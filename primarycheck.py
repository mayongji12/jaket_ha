#__coding:utf-8__
import os
import subprocess
beat=os.popen("grep primarybeat /source/socket/jakerha.cnf|awk -F= '{print $2}'").read().strip('\n')
def checkping(ip):
    ubprocess.Popen([r'./ping.sh',ip],stdout=subprocess.PIPE)
    result=p.stdout.read()
    if '1\n'==result:
        return 1 #网络畅通
    else
        return 0 #网络阻塞

