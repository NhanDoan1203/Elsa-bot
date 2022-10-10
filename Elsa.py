import speech_recognition as sr
import playsound
from gtts import gTTS
import random
from datetime import datetime
from datetime import time
import webbrowser
import ssl
import certifi
import os
from PIL import Image
import subprocess
import pyautogui
import pyttsx3
import yfinance as yf
import subprocess
import os.path
import wikipedia
import time
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
import math
import sounddevice
from scipy.io.wavfile import write

x = datetime.now()
Time = int(x.strftime("%H"))
if 0 <= Time <= 12:
    Y = "good morning"
elif 12 < Time <= 13:
    Y = "good afternoon,"
elif 13 < Time <= 17:
    Y = " good evening"
elif 17 < Time < 23:
    Y = "What a lovely night "
elif Time >= 23:
    Y = "You have to go to sleep"

class person:
    name = ''
    def username(self, name):
        self.name = name

def user(terms):
    for term in terms:
        if term in user_data:
            return True

def com_mouth(text):
    text = str(text)
    engine.say(text)
    engine.runAndWait()

r = sr.Recognizer()
def recorder(ask=False):
    with sr.Microphone() as source:
        if ask:
            com_mouth(ask)
        audio = r.record(source, duration=4)
        user_data = ''
        print("Elsa:...")
        try:
            user_data = r.recognize_google(audio)
        except sr.UnknownValueError:
            com_mouth('i cannot hear you, try again')
        except sr.RequestError:
            com_mouth("i don't understand")
        print(f"You: {user_data.lower()}")
        return user_data.lower()

def com_mouth(audio_string):
    audio_string = str(audio_string)
    tts = gTTS(text=audio_string, lang='en')
    r = random.randint(1, 20000000)
    audio_file = 'audio' + str(r) + '.mp3'
    tts.save(audio_file)
    playsound.playsound(audio_file)
    print(f"Elsa: {audio_string}")
    os.remove(audio_file)

def note(text):
    date = datetime.now()
    file_name = str(date).replace(":", "-") + "-note.txt"
    with open(file_name, "w") as f:
        f.write(text)
        subprocess.Popen(["notepad.exe", file_name])

def volumn_setting(user_data):
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(
    IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = cast(interface, POINTER(IAudioEndpointVolume))
    volume.SetMasterVolumeLevelScalar(user_data/100,None)

def recording(user_data):
    time= user_data
    fs = 44100
    device = devices.rec(int(timepy *fs), samplerate = fs, channels = 2)
    devices.wait()
    write("Myrecording.wav",fs,record_device)

def respond(user_data):
    if user(['hey', 'hi', 'hello']):
        greetings = [Y + f"How can i help you {person_obj.name}",
                     Y +f"what do you want{person_obj.name}", f"I'm listening {person_obj.name}"]
        greet = greetings[random.randint(0, len(greetings) - 1)]
        com_mouth(greet)

    if user(["what is your name", "what's your name", "tell me your name"]):
        if person_obj.name:
            com_mouth("my name is Elsa")
        else:
            com_mouth("my name is Elsa. what's your name?")

    if user(["my name is"]):
        person_name = user_data.split("is")[-1].strip()
        com_mouth(f"okay, i will remember that {person_name}")
        person_obj.username(person_name)

    if user(["how are you", "how are you doing"]):
        com_mouth(f"I'm very well, thanks for asking {person_obj.name}")

    if user(["what's the time", "tell me the time", "what time is it"]):
        now = datetime.now()
        com_mouth(now.strftime("%H hours %M minutes %S seconds"))

    if user(["what's the date", "tell me the date", "today"]):
        today = datetime.today()
        com_mouth(today.strftime("%B %d, %Y"))

    if user(["make a rest", "you should take a nap"]):
        com_mouth('Yay')
        time.sleep(10)

    if user(["i have to go now", "shutdown the computer"]):
        os.system('shutdown -s')
        com_mouth("Bye Human")

    if user(["restart"]):
        os.system('shutdown -r')
        com_mouth("i will come back for you Human")

    if user(["search for"]) and 'youtube' not in user_data:
        search_term = user_data.split("for")[-1]
        url = "https://google.com/search?q=" + search_term
        webbrowser.get().open(url)
        com_mouth("Here is what I found for" + search_term + "on google")

    if user(["open google"]) and 'youtube' not in user_data:
        search_term = user_data.replace("open", "")
        url = "https://google.com/search?q=" + search_term
        webbrowser.get().open(url)
        com_mouth(" opening google ")

    if user(["youtube"]):
        search_term = user_data.split("for")[-1]
        search_term = search_term.replace("on youtube", "").replace("search", "")
        url = "https://www.youtube.com/results?search_query=" + search_term
        webbrowser.get().open(url)
        com_mouth("Here is what I found for " + search_term + "on youtube")

    if user(["weather"]):
        search_term = user_data.split("for")[-1]
        url = "https://www.google.com/search?sxsrf=ACYBGNSQwMLDByBwdVFIUCbQqya-ET7AAA%3A1578847393212&ei=oUwbXtbXDN-C4-EP-5u82AE&q=weather&oq=weather&gs_l=psy-ab.3..35i39i285i70i256j0i67l4j0i131i67j0i131j0i67l2j0.1630.4591..5475...1.2..2.322.1659.9j5j0j1......0....1..gws-wiz.....10..0i71j35i39j35i362i39._5eSPD47bv8&ved=0ahUKEwiWrJvwwP7mAhVfwTgGHfsNDxsQ4dUDCAs&uact=5"
        webbrowser.get().open(url)
        com_mouth("Here is what I found for on google")
    
    if user(["game"]):
        user_data = recorder("choose among rock paper or scissor")
        moves = ["rock", "paper", "scissor"]
        cmove = random.choice(moves)
        umove = user_data
        com_mouth("The computer chose " + cmove)
        com_mouth("You chose " + umove)
        if umove == cmove:
            com_mouth("the match is draw")
        elif umove == "rock" and cmove == "scissor":
            com_mouth("you win , damnne so lucky")
        elif umove == "rock" and cmove == "paper":
            com_mouth("I win, you are a looser human, haha!")
        elif umove == "paper" and cmove == "rock":
            com_mouth("you win , damnne so lucky")
        elif umove == "paper" and cmove == "scissor":
            com_mouth("I win, you are a looser human, haha!")
        elif umove == "scissor" and cmove == "paper":
            com_mouth("you win , damnne so lucky")
        elif umove == "scissor" and cmove == "rock":
            com_mouth("I win, you are a looser human, haha!")

    if user(["toss", "flip", "coin"]):
        moves = ["head", "tails"]
        cmove = random.choice(moves)
        com_mouth("The computer chose " + cmove)

    if user(["capture", "my screen", "screenshot"]):
        myScreenshot = pyautogui.screenshot()
        myScreenshot.save('D:/screenshot/screen.png')
        myScreenshot.save('D:/screenshot/screen.png')

    if user(["price of"]):
        search_term = user_data.lower().split(" of ")[-1].strip()
        stocks = {
            "apple": "AAPL",
            "microsoft": "MSFT",
            "facebook": "FB",
            "tesla": "TSLA",
            "bitcoin": "BTC-USD"
        }
        try:
            stock = stocks[search_term]
            stock = yf.Ticker(stock)
            price = stock.info["regularMarketPrice"]

            com_mouth(f'price of {search_term} is {price} {stock.info["currency"]} {person_obj.name}')
        except:
            com_mouth('oops, something went wrong')

    if user(["set the volume at"]):
        volume_data = int(user_data.split("at")[-1])
        volumn_setting(volume_data)
        com_mouth(f'I have set your volume at {volume_data} %')

    if user(["what is my exact location"]):
        url = "https://www.google.com/maps/search/Where+am+I+?/"
        webbrowser.get().open(url)
        com_mouth(f"You must be somewhere near here, as per Google maps, {person_obj.name}")

    if user(["find location for"]):
        search_term = user_data.split("for")[-1]
        url = 'https://www.google.com/maps/search/' + search_term
        webbrowser.get().open(url)
        com_mouth("I have found your place on google map")
        
    if user(["make a note", "write down", "remember this"]):
        com_mouth("what would you like me write down?")
        note_text = recorder()
        note(note_text)
        com_mouth("I've made a note for that.")

    if user(["thank you","love you"]):
        say = ["you welcome",f"I love hearing that, {person_obj.name}" , f"it's very nice of you to say so, {person_obj.name}"]
        elsa = random.choice(say)
        com_mouth(elsa)

    if user(["definition for"]):
        search_term = user_data.split("for")[-1]
        url= 'https://en.wikipedia.org/wiki/' + search_term
        webbrowser.get().open(url)
        print (wikipedia.summary(search_term))
        com_mouth(f'this is what I found for' + search_term + wikipedia.summary(search_term))

    if user(['make a recording']):
        com_mouth('How many seconds do you want')
        if user(['seconds']):
            record_time = user_data.split('seconds')[-1]
            com_mouth('Recording')
            recording(record_time)
            com_mouth('Recording is done please check the file')

    if user(["exit", "quit", "goodbye"]):
        com_mouth("I just pretend to be nice the whole time, now get the hell out of here")
        exit()


time.sleep(1)

person_obj = person()
person_obj.name = ""
engine = pyttsx3.init()

while (1):
    user_data = recorder()
    respond(user_data)
