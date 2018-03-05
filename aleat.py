#!/usr/bin/python3


import webApp
import random

class URLAleatApp(webapp.webApp):

	def process(self, parsedRequest):
        return ["200 OK", "<html><body><h1><a href='" + str(random.randit(1,10000)) + "' >Dame otra!</a></h1></body></html>"]

if __name__ == "__main__":
	MywebApp = aleatApp("localhost", 1234)
