
'''
Middleware for controller to contain all the modules
'''
import tornado.web
import tornado.escape
import time
import  tornado.gen
from  .Recognizer import Simple_Faces_Compare,Foreced_Faces_Compare
					