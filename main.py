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
