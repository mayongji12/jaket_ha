#__coding:utf-8__
import os
class CheckService(object):
    def __init__(self,service):
        self.service =service
    def check(self):
        return os.popen('ps -ef|grep %s|grep -v grep' %self.service).read()
            
if __name__='main':
    import checkservice
    a=checkservice.CheckService('httpd')
    a.check()
