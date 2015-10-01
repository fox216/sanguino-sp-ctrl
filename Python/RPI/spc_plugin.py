# Sprinkler control plugin 
# example -> http://www.defuze.org/archives/222-integrating-sqlalchemy-into-a-cherrypy-application.html

import cherrypy
import socket, sys, os
class WiflyControl(cherrypy.process.plugins.SimplePlugin):
    # Web plugin for wifly controller
    """ 
    def __init__(self):
        # Initial control 
        cherrypy.log('Initializing Wifly Controller Plugin ')
        wifly01_ip = '10.42.8.61'
        try: 
            rc = os.system('ping -c 1 -w 2 %s' %(wifly01_ip))
        except:
            print "Could not ping system"

        if (rc != 0):
            cherrypy.log('Remote system %s is no available ' %(wifly01_ip))
        else:
            cherrypy.log('Remote system %s is on-line ' %(wifly01_ip))
    """

    def start(self):
        cherrypy.log('Start called ')
        # Initial control 
        cherrypy.log('Initializing Wifly Controller Plugin ')
        wifly01_ip = '10.42.8.61'
        try: 
            rc = os.system('ping -c 1 -w 2 %s' %(wifly01_ip))
        except:
            print "Could not ping system"

        if (rc != 0):
            cherrypy.log('Remote system %s is no available ' %(wifly01_ip))
        else:
            cherrypy.log('Remote system %s is on-line ' %(wifly01_ip))
    def stop(self):
        cherrypy.log('Stop called ')

    def callme(self):
        cherrypy.log('Call me Called by calling program ')



'''
Register plugin with cherrypy engine sub-system
'''
cherrypy.engine.wiflycontrol = WiflyControl(cherrypy.engine)

