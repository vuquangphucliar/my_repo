import pyttsx3
import PyPDF2

book = open("EB.pdf", "rb")
pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages
print(pages)

bot = pyttsx3.init()
voices = bot.getProperty('voices')
bot.setProperty('voices', voices[0].id)

start = int(input("Start page: "))
end = int(input("End page: "))

for num in range(start - 1, end - 1):
    page = pdfReader.getPage(num)
    text = page.extractText()
    bot.say(text)
    bot.runAndWait()