
'''
The main server file
'''
from tornado.web import RequestHandler, Application
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
import os
import torn

from routes import *
settings = dict(
		debug=torn.Debug(),
		template_path=os.path.join(os.path.dirname(__file__),"templates"),
		static_path=os.path.join(os.path.dirname(__file__),"static")
	)

application = Application(route, **settings)

if __name__ == "__main__":
	server = HTTPServer(application)
	server.listen(int(os.environ.get("PORT", 8000)))
	IOLoop.current().start()

					
