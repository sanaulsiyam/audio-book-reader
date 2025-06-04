import pyttsx3
from PyPDF2 import PdfReader
book = open("python_DS_ML.pdf","rb")
pdfReader = PdfReader(book)

#Number of pages
pages= len(pdfReader.pages)
print(f"Total Pages : {pages}")

audio = pyttsx3.init()
#changing voice
voices = audio.getProperty('voices')
audio.setProperty('voice',voices[14].id)

#For slower speech rate
rate = audio.getProperty('rate')
audio.setProperty('rate',170)

#input of starting page
n = int(input("Enter the starting page number : "))

page = pdfReader.pages[n]
text = page.extract_text()

audio.say(text)
audio.runAndWait()
