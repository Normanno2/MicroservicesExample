#!/usr/bin/env python

import sys
import datetime
import signal
import tornado.ioloop
from tornado.options import options, define
from hello import HelloWordApp

define("port", default=8080, help="listen_port", type=int)

def signal_handler(signal, frame):
    print("Exit on "+str(datetime.now()))
    sys.exit(0)


if __name__ == '__main__':
    application = HelloWordApp()
    app = application.make_app()
    app.listen(options.port)
    tornado.ioloop.IOLoop.current().start()
    signal.signal(signal.SIGINT, signal_handler())
