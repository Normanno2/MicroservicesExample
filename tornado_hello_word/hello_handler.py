from tornado.web import RequestHandler

class SimpleHelloHandler(RequestHandler):

    def get(self):
        print("Get")
        self.write("Hello Word")


class HelloMateHandler(RequestHandler):

    def get(self, mate):
        print("Get")
        self.write("Hello "+str(mate))
