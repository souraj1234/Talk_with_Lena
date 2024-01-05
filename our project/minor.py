




from PIL import ImageTk,Image
from tkinter import *
import tkinter as tk
from PIL import Image
import pyautogui
import pywhatkit
import requests
from speech_recognition import Microphone, Recognizer, UnknownValueError
import pyttsx3
import webbrowser
import datetime
import pyjokes
import wikipedia
import os
import time

# Create the main window
root = Tk()
root.title("Voice Assistant")
img = Image.open("lena_final.jpg")
photo = ImageTk.PhotoImage(img)
root.geometry('520x360')

image_label = tk.Label(root, image=photo)
image_label.pack()

# Create a function to recognize and process speech
def sptext():
    recognizer = Recognizer()
    with Microphone() as source:
        print("Listening....")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        try:
            print("Recognizing")
            data = recognizer.recognize_google(audio)
            print(data)
            return data  # Return the recognized text
        except UnknownValueError:
            print("Not Understood")
            return ""

def speechtx(x): # AI generated voice
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    engine.getProperty('rate')
    engine.setProperty('rate', 200)
    engine.say(x)
    engine.runAndWait()

def initialize_both_functions():
    data1 = sptext()  # Get user's speech
    if 'ok lena' in data1.lower():
        while True:
            data1 = sptext().lower()
            if "your name" in data1:
                name = "my name is alexa"
                speechtx(name)
            elif "old are you" in data1:
                age = "i am twenty years old"
                speechtx(age)
            elif "do you love with me" in data1:
                love = "yes i do love with you"
                speechtx(love)
            elif "youtube" in data1:
                webbrowser.open("https://www.youtube.com/")
            elif "web" in data1:
                webbrowser.open("https://www.google.com/")
            elif 'play' in data1:
                song = data1.replace('play', '')
                speechtx(song)
                pywhatkit.playonyt(song)
            elif 'jokes' in data1:
                joke = pyjokes.get_joke(language='en',category='neutral')
                print(joke)
                speechtx(joke)
            elif "calculator" in data1:
                webbrowser.open("https://www.online-calculator.com/")
                speechtx("opening....")
            elif "weather" in data1:
                apikey = "0961aed733a8daec3ddf7ac7da0bb5d3"
                baseURL = "https://api.openweathermap.org/data/2.5/weather?q=kolkata&appid=0961aed733a8daec3ddf7ac7da0bb5d3"
                completeURL = baseURL + "&appid" +apikey
                response = requests.get(completeURL)
                simple = response. json()
                # print(simple)
                value = simple['main']['temp']
                def kelvin_to_celsius(kelvin):
                    return kelvin - 273.15


                # Printing the temperatures in Celsius
                print("Current temperature: {:.2f}".format(kelvin_to_celsius(value)))
                print("Current temperature feels like: {:.2f}".format(kelvin_to_celsius(simple['main']['feels_like'])))
                print("Maximum temperature: {:.2f}".format(kelvin_to_celsius(simple['main']['temp_max'])))
                print("Minimum temperature: {:.2f}".format(kelvin_to_celsius(simple['main']['temp_min'])))
                speechtx("current temp")
                speechtx(simple['main'] ['temp'])
                speechtx("current temp feels")
                speechtx(simple['main'] ['feels_like'])
                speechtx("current temp max")
                speechtx(simple['main'] ['temp_max'])
                speechtx("current temp min")
                speechtx(simple['main']['temp_min'])
            elif "spotify1" in data1:
                webbrowser.open("https://open.spotify.com/")
                speechtx("opening...")
            elif "spotify" in data1:
                os.system("spotify")
                time.sleep(5)
                pyautogui.hotkey('ctrl', 'l')
                pyautogui.write(data1, interval = 0.1)
                for key in ['enter','pagedown','tab','enter','enter']:
                    time.sleep(2)
                    pyautogui.press(key)
                speechtx("playing")

            elif "tell" in data1:
                wikipedia.set_lang("en")
                ask = (data1)
                speechtx(ask)
                print(wikipedia.summary(ask))
                speechtx(wikipedia.summary(ask))

            elif "exit" in data1:
                speechtx("thank you")
                break
                time.sleep(5)
             # ... (rest of your conditions)
    else:
        print("Thanks")

def exit_program():
    root.destroy()


exit_button = tk.Button(root, text="Exit", command=exit_program,width=24,height=2)
exit_button.place(x=7, y=170)


# Create a button that calls the wrapper function
listen_button = Button(root, text="Listen", command=initialize_both_functions,width=24,height=2)
listen_button.place(x=7, y=100)
# listen_button.pack()

# Start the GUI main loop
root.mainloop()