import tornado.web
import tornado.ioloop
from hello_handler import HelloMateHandler, SimpleHelloHandler
from hello_db_handler import HelloDBHandler, HelloNewDBHandler

class HelloWordApp:

    def make_app(self):
        return tornado.web.Application([
            (r"/", SimpleHelloHandler),
            (r"/hello", SimpleHelloHandler),
            (r"/hello/([^ / ]*)", HelloMateHandler),
            (r"/hello-all", HelloDBHandler),
            (r"/hello/new/([^ / ]*)", HelloNewDBHandler),
        ])