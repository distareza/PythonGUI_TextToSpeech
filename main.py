import tkinter
import time
import threading
import tkinter.messagebox
from tkinter.ttk import Progressbar

import TextToSpeech

window = tkinter.Tk()
window.title("Python GUI - Text to Speech App")
window.config(width=640, height=480, padx=50, pady=50)

frameInput = tkinter.Frame(borderwidth=20)
inputText = tkinter.Text(frameInput, width=30, height=5, font=("Courier", 14))
Progress_Bar = Progressbar(window, orient= tkinter.HORIZONTAL, length=250, mode='determinate')

frameInput.pack()
inputText.pack()
Progress_Bar.pack()

start_time = time.perf_counter()

def startCounter():
    global start_time
    start_time = time.perf_counter()

def key_press(event):
    try :
        startCounter()
    except Exception as ex:
        print(ex)

def textToSpeech(text):
    print(f"text : \"{text}\"")
    playsound(text)

def wipeTextThread():
    while True:
        delta_time = time.perf_counter() - start_time
        if delta_time > 5:
            text = inputText.get("1.0", tkinter.END).strip()
            inputText.delete('1.0', tkinter.END)
            inputText.focus()
            Progress_Bar['value'] = 0

            if text:
                print("More that 5 second Idle, start Speach")
                textToSpeech(text)

        else:
            Progress_Bar['value'] = 100 - int(delta_time) * 20
            print(f"{int(delta_time)} second idle")
        time.sleep(1)

def playsound(text:str):
    TextToSpeech.play_sound(text)

inputText.bind('<Key>', key_press)
thread_init = threading.Thread(target=wipeTextThread)
thread_init.start()

if __name__ == '__main__':
    inputText.focus()
    window.mainloop()