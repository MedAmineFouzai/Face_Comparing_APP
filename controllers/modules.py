
'''
Middleware for controller to contain all the modules
'''
import tornado.web
import tornado.escape
import time
import  tornado.gen
from  .recognizer import simple_faces_compare,foreced_faces_compare
					