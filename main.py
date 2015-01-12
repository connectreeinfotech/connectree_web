#oggpnosn 
#hkhr 

#connectree website 


import webapp2
import random 
import jinja2
import os 
from google.appengine.api import mail
from google.appengine.api import users
from google.appengine.ext import ndb

env = jinja2.Environment(loader=jinja2.FileSystemLoader(os.path.join(os.path.dirname(__file__),'html')), extensions=['jinja2.ext.autoescape'], autoescape=True)

class HomePageHandler(webapp2.RequestHandler):
	def get(self):
		filename = "index.html"
		self.response.headers['Content-Type'] = 'text/html'
		#template = env.get_template(filename)
		text = open(filename).read()
		self.response.write(text)

app = webapp2.WSGIApplication([('/', HomePageHandler),])