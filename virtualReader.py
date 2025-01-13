
import pyttsx3
import PyPDF2

book =  open('bookb.pdf', 'rb') 
pdfReader = PyPDF2.PdfReader(book)
pages = pdfReader.numpages

print(f"Total pages of your book: {pages}")

friend = pyttsx3.init()
for num in range(1,10):
 page = pdfReader.pages[79]  
 text = page.extractText()  
    
 friend.say(text)
 friend.runAndWait()

