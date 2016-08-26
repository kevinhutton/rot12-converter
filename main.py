# Copyright 2016 Google Inc.
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

import webapp2
import os
import jinja2

template_dir = os.path.join(os.path.dirname(__file__), 'templates' )
jinja_env = jinja2.Environment( loader = jinja2.FileSystemLoader(template_dir))


class MainPage(webapp2.RequestHandler):
    def get(self):
        template = jinja_env.get_template('frontend.html')
        self.response.write(template.render())
    def post(self):
        template = jinja_env.get_template('frontend.html')
        encryptedText = self.request.get('text')
        self.response.write(template.render(encryptedText=self.encrypt(encryptedText)))
    def encrypt(self,inputString):

        newString = []
        for i in range(0,len(inputString)):
            currentCharacter = inputString[i]
            if currentCharacter.isalpha():

                if (currentCharacter.isupper() and  ord(currentCharacter) + 13) > ord('Z'):
                        asciiLetter = (12 - (ord('Z') - ord(currentCharacter)) ) + ord('A')
                        newString.append(chr(asciiLetter))
                elif (currentCharacter.islower() and  ord(currentCharacter) + 13) > ord('z'):
                        asciiLetter = (12 - (ord('z') - ord(currentCharacter)) ) + ord('a')
                        newString.append(chr(asciiLetter))
                else:
                    newString.append(chr(ord(currentCharacter) + 13))
            else:
                newString.append(currentCharacter)

        return ''.join(newString)


app = webapp2.WSGIApplication([
    ('/', MainPage),
], debug=True)
