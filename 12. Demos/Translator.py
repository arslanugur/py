# Library: pip install googletrans or googletrans==3.1.0a0

from googletrans import Translator
translator = Translator(service_urls = ['translate.googleapis.com'])
bool = True
while bool:
   wrd = input("Word: q-Quit: ")
   if(wrd=="q"):
      bool = False
      print("Quitted")
   else:
      translation = translator.translate(wrd, src = 'tr', dest = 'en')
      print(f"{translation.origin} ===> {translation.text}")



