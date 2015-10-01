"""
Notes:
http://docs.cherrypy.org/stable/concepts/config.html
http://tools.cherrypy.org/wiki/RestfulDispatch
http://www.ics.uci.edu/~fielding/pubs/dissertation/evaluation.htm


"""
import cherrypy
import spc_plugin
import os


class Root():

    def __init__(self):
        spc = cherrypy.engine.wiflycontrol.subscribe()
    @cherrypy.expose
    def index(self):
        return "Well Hello there from the Pi"
        self.spc.callme()
        cherrypy.engine.wiflycontrol.start()
        cherrypy.engine.wiflycontrol.callme()

    @cherrypy.expose
    def default(self, handle_id):
        if not handle_id.isdigit():
            raise cherrypy.NotFound()
        else: 
            return "Are you lost?"


"""
handlers = {
    'SIGTERM': self.bus.exit,
    'SIGHUP': self.handle_SIGHUP,
    'SIGUSR1': self.bud.graceful,
}
"""
conf = {
    'global': {
        'server.socket_host': '0.0.0.0',
        'server.socket_port': 8080,
        'server.thread_pool': 20,
        'tools.staticdir.root': os.getcwd() + '/site',
        'engine.wiflycontrol.on': True,

        'tools.log_headers.on': True,
        'log.error_file': os.getcwd() + '/log/error.log',
        'log.access_file': os.getcwd() + '/log/access.log'
    },
    '/': {
        'tools.trailing_slash.on': False,

    }
}



if __name__ == '__main__':
    cherrypy.quickstart(Root(), '/', config=conf)

