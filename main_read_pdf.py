import tkinter
from tkinter import filedialog as fd
import tkinter.messagebox
from PyPDF2 import PdfFileReader
import time
import threading
import TextToSpeech

window = tkinter.Tk()
window.title("Python GUI - PDF to Speech App")
window.config(width=640, height=480, padx=50, pady=50)

def select_file():

    filename = fd.askopenfilename(
        title='Open a file',
        filetypes=(('Pdf file', '*.pdf'),))
    print(f"Opening file {filename}")

    thread_init = threading.Thread(target=readPDF, args=(filename,))
    thread_init.start()


frameInput = tkinter.Frame(borderwidth=20)
inputText = tkinter.Text(frameInput, width=140, height=40, font=("Courier", 9))
open_button = tkinter.Button(text="Open File", command=select_file)

frameInput.pack()
inputText.pack()
open_button.pack()

def readPDF(filename):
    with open(filename, "rb") as filehandle:
        pdf = PdfFileReader(filehandle)
        info = pdf.getDocumentInfo()
        print(info)
        pages = pdf.getNumPages()

        for page in range(pages):
            print(f"Read Page {page}")
            page1 = pdf.getPage(page)
            text_content = page1.extractText()
            setTextInput(text_content)

            textToSpeech(text_content)
            time.sleep(1)

def setTextInput(text):
    inputText.delete(1.0, tkinter.END)
    inputText.insert(1.0, text)


def textToSpeech(text):
    print(f"text : \"{text}\"")
    try_to_speech = 0
    while (try_to_speech < 3):
        try:
            if (try_to_speech>0):
                print(f"trying {try_to_speech+1} times")
            playsound(text)
            break
        except:
            try_to_speech+=1

def playsound(text:str):
    TextToSpeech.play_sound(text)

if __name__ == '__main__':
    window.mainloop()