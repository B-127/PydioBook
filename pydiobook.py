import pyttsx3                                      #Python text-to-speech conversion library
import PyPDF2

book = open(r"C:\Users\Asus\Desktop\LSEG\mit_is_pl2___acceptable_usage_policy__ver_2.5__new.pdf", 'rb')
pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages

speaker = pyttsx3.init()
voices = speaker.getProperty('voices') 
speaker.setProperty('voice', voices[1].id)          #voices[0] for male voice
for num in range(6, pages):
    page = pdfReader.getPage(num)
    text = page.extractText().lower()
    speaker.say(text)
    speaker.runAndWait()