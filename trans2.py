#pip install translate
from translate import Translator
file = open('projects.txt')
new_content = file.read()
translator = Translator(to_lang ='spanish')
translation = translator.translate(new_content)
print(translation)