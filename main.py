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
	def post(self): 
		name = self.request.get("name")
		email = self.request.get("email")
		message = self.request.get("message")
		phone = self.request.get("phone")
		mail.send_mail(sender=" <connectreeuser@gmail.com>",
												  to= "<connect@connectree.in>",
												subject="Website Contact Form:" + self.request.get("name"),
												body = "You have received a new message from your website contact form.\n\nHere are the details:\n\nName:"+ name + "\n\nEmail: " + email + "\n\nPhone: "+ phone + " \n\nMessage:\n" + message)

		
			

app = webapp2.WSGIApplication([('/', HomePageHandler),])