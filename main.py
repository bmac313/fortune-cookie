#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import random

def getRandomFortune():
	fortunes = [
		"I see much code in your future.",
		"Consider eating more fortune cookies.",
		"I sense you will bring balance to the Force.",
		"You have tamed the mighty Python, now you must free it onto the Great Web.",
		"Invite more C# into your life, and great things will happen.",
		"I see a great Apprenticeship in your future.",
		"You will become frustrated because of a silly problem in your code. Remember to relax and remember the principles of Code Zen."
	] 
		
	rand_num = random.randrange(0, len(fortunes))
	
	return fortunes[rand_num]

class MainHandler(webapp2.RequestHandler):
	def get(self):
		header = "<h1>Fortune Cookie</h1>"
		
		fortune = "<strong>" + getRandomFortune() + "</strong>"
		fortune_message = "<p>Your fortune: " + fortune + "</p>"
		
		lucky_num = random.randint(1, 100)
		num_message = "<p>Your lucky number: <strong>" + str(lucky_num) + "</strong></p>"
		
		cookie_again_btn = "<a href='.'>New fortune</a>"
		
		content = header + fortune_message + num_message + cookie_again_btn
		
		self.response.write(content)
		
class LoginHandler(webapp2.RequestHandler):
	def get(self):
		self.response.write("Thanks for trying to log in!")

routes = [
	('/', MainHandler),
	('/login', LoginHandler)
]
		
app = webapp2.WSGIApplication(routes, debug=True)
