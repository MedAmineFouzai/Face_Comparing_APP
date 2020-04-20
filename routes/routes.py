
from controllers import *
from  tornado.web import url
route = [
		url(
			r"/",
			home.homeHandler
		)
]
					