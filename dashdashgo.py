#!/usr/bin/env python
from __future__ import print_function

import base64
import json
import socket
import tornado
import tornado.gen
import tornado.web
import tornado.websocket

class WebServerHandler(tornado.web.RequestHandler):

    def initialize(self, webserver):
        '''
        '''
        self._webserver = webserver

    @tornado.web.asynchronous
    @tornado.gen.coroutine
    def get(self, uri):
        '''
        '''
        self._webserver.handle(self)


class WebServer:

    def __init__(self, port=2001):
        '''
        '''
        self._port = port

    def start(self):
        '''
        '''

        ip = socket.gethostbyname('')
        port = self._port

        webapp = tornado.web.Application([
            (r'/knopf/(.*)', WebServerHandler, dict(webserver=self))
        ])

        webapp.listen(port)
        print('Starting DASHDASHGO at \033[93mhttp://' + ip + ':' + str(port) + '\033[0m')
        tornado.ioloop.IOLoop.instance().start()

    @tornado.gen.coroutine
    def handle(self, handler):
        '''
        '''
        splitted_request = handler.request.uri.split('/')
        event = json.loads(base64.b64decode(splitted_request[2]))
        
        #
        # parse the Dash event
        #
        battery_voltage = event['batteryVoltage']
        serial_number = event['serialNumber']
        click_type = event['clickType']

        if click_type == 'SINGLE':
            #
            # TODO ACTION ON SINGLE CLICK
            #
            print('Single push.')
        elif click_type == 'DOUBLE':
            #
            # TODO ACTION ON DOUBLE CLICK
            #
            print('Double push.')
        elif click_type == 'LONG':
            #
            # TODO ACTION ON LONG CLICK
            #
            print('Long push.')

        handler.set_header('Access-Control-Allow-Origin', '*')
        handler.set_header('Content-Type', 'text/html')
        handler.set_status(200)
        handler.write('DASHDASHBOOM!')

#
# entry point
#
if __name__ == "__main__":

    ws = WebServer()
    ws.start()


