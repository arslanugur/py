import pyttsx3
import PyPDF2

book = open('yours.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages

speaker = pyttsx3.init()

for num in range(7, pages): # just switch the start range index from 7 to 0
  page = pdfReader.getPage(num)
  text = page.extractText()
  speaker.say(text)
  speaker.runAndWait()
  
  
  
