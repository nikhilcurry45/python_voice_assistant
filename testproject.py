import speech_recognition as sr
import pyttsx3
from os import startfile
import tkinter as tk
from functools import partial
import subprocess
from datetime import date
import requests
import json
import random
api_key = '45f40e0a2a6708c11064faa118afb498'


engine = pyttsx3.init()
rate = engine.getProperty('rate')
engine.setProperty('rate', 175)
r = sr.Recognizer() 
class _speaker:
    def set_male(self):
        voices = engine.getProperty('voices')       
        engine.setProperty('voice', voices[0].id)
    def set_female(self):
        voices = engine.getProperty('voices')
        engine.setProperty('voice',voices[1].id)
    def speaker(self,command):
        engine.say(command) 
        engine.runAndWait()
import speech_recognition as sr

class _listener:
    def listen(self):
        r = sr.Recognizer()
        
        try:
            with sr.Microphone() as source2:
                r.adjust_for_ambient_noise(source2, duration=0.2)
                audio2 = r.listen(source2)
                
                try:
                    MyText = r.recognize_google(audio2)
                    MyText = MyText.lower()
                    return MyText
                except sr.RequestError as e:
                    # API was unreachable or unresponsive
                    return f"RequestError: {e}"
                except sr.UnknownValueError:
                    # Speech was unintelligible
                    return "UnknownValueError: Could not understand the audio"
                except sr.WaitTimeoutError:
                    # Timeout occurred
                    return "WaitTimeoutError: Listening timed out while waiting for phrase to start"
                except sr.AudioDataError:
                    # Issue with the audio data
                    return "AudioDataError: Could not process the audio data"
                except Exception as e:
                    # Catch-all for any other exceptions
                    return f"Exception: {e}"
        
        except sr.MicrophoneUnavailableError:
            # Microphone is not available
            return "MicrophoneUnavailableError: No microphone found"
        except OSError as e:
            # OS-related errors (e.g., hardware issues)
            return f"OSError: {e}"
        except Exception as e:
            # Catch-all for any other exceptions
            return f"Exception: {e}"




        
s = _speaker()
l = _listener()
l3 = _listener()
l4 = _listener()
class do_tasks:
    def main(self): 
        s.speaker("what can i do for you?")
        task = l3.listen()
        if(task == 'exit'):
            s.speaker("thankyou.... see you again!")
            exit()
        elif(task == 'open chrome'):                #ELIFS FOR OPENING APPLICATIONS
            s.speaker("opening chrome")
            print( startfile(r"C:\Program Files\Google\Chrome\Application\chrome.exe"))
        elif(task == 'open edge'):
            s.speaker("opening edge")
            print( startfile(r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"))
        elif(task == 'open spotify'):
            s.speaker("opening spotify")
            print( startfile(r"C:\Users\nikhi\AppData\Roaming\Spotify\spotify.exe"))
        elif(task == 'open code blocks'):
            s.speaker("opening code blocks")
            print( startfile(r"C:\Program Files\CodeBlocks\CodeBlocks.exe"))
        elif(task == 'open vs code'):
            s.speaker("opening vs code")
            print( startfile(r"C:\Users\nikhi\AppData\Local\Programs\Microsoft VS Code\code.exe"))
        elif(task == 'open illustrator'):
            s.speaker("opening adobe illustrator")
            print( startfile(r"C:\Program Files\Adobe\Adobe Illustrator 2020\Support Files\Contents\Windows\Illustrator.exe"))
        elif(task == 'open photoshop'):
            s.speaker("opening adobe photoshop")
            print( startfile(r"D:\cdrivebackups\Adobe\Adobe Photoshop 2023\Photoshop.exe"))
        elif(task == 'open steam'):
            s.speaker("opening steam")
            print( startfile(r"C:\Program Files (x86)\Steam\steam.exe"))
        elif(task == 'open epic games'):
            s.speaker("opening epic games")
            print( startfile(r"D:\epic\Epic Games\Launcher\Portal\Binaries\Win32\EpicGamesLauncher.exe"))
        elif(task == 'open command prompt'):    #ELIFS FOR OPENING SYSTEM APPS
            s.speaker("opening command prompt")
            print( startfile(r"C:\WINDOWS\system32\cmd.exe"))
        elif(task == 'open calculator'):    
            s.speaker("opening calculator")
            print( startfile("calc.exe"))
        elif task == 'open camera':
            s.speaker("opening Camera")
            subprocess.Popen(["start", "microsoft.windows.camera:", "//"], shell=True)
        elif task == 'open settings':
            s.speaker("opening Settings")
            subprocess.Popen(["start", "ms-settings:", "//"], shell=True)
        elif task == 'tell date':    #other tasks
            today = date.today()
            x = str(today)
            l1 = x.split('-')
            dic = {'01':'january','02':'february','03':'march','04':'april','05':'may','06':'june','07':'july','08':'august','09':'september','10':'october','11':'november','12':'december'}
            for i in dic:
                if l1[1] == i:
                    l1[1] = dic[i]
            s.speaker("today's date is.... "+l1[2]+"..."+l1[1]+"..."+l1[0])
        elif task == 'tell weather':
            s.speaker("ofcourse!.....of which city you want the weather details?")
            city = l4.listen()
            weather_data = requests.get(
                       f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=imperial&APPID={api_key}")
            if weather_data.json()['cod'] == '404':
                 s.speaker("No City Found")
            else:
                weather = weather_data.json()['weather'][0]['main']
                f=int(weather_data.json()['main']['temp'])
                c = 5/9*(f - 32)
                temp = str(int(c))
                s.speaker("the temperature of "+city+" is "+temp+" degree celcius and its mostly "+ weather)
        elif task == 'tell news':
            s.speaker("ofcourse!.... what type of news ? choose from the following..... general.... business.....technology......entertainment.....sports.....health.....science.....politics")
            news = l4.listen()
            try:
                url = f"https://newsapi.org/v2/top-headlines?country=in&category={news}&apiKey=dce0f36528484660b9b0707acba02e43"

                r = requests.get(url)
                a = r.json()["articles"]
                for i in range(5):
                    s.speaker(a[i]["title"])
            except IndexError:
                s.speaker("sorry no news found about that")
        else:
            self.chatbot(task)

    def chatbot(self,task):
                dic = {
                    ("hi", "hello", "hi there", "whats up"): [
                        "Hi there! Hope you are doing good.",
                        "Hey, greetings!",
                        "Good day!"
                    ],
                    ("how are you", "how are you doing"): [
                        "I'm just a bot, but I'm functioning as expected!",
                        "Doing great, thanks for asking! How about you?",
                        "I'm here to help you, so I'm doing well!"
                    ],
                    ("what is your name", "who are you"): [
                        "I'm your friendly chatbot!",
                        "I'm ,"+assistant+" your virtual assistant.",
                        "You can call me "+assistant+"."
                    ],
                    ("what can you do", "what are your capabilities"): [
                        "I can help answer your questions, provide information, and have a chat with you.",
                        "I'm here to assist you with a variety of tasks and answer your queries.",
                        "I can chat with you, provide information, and help with many tasks."
                    ],
                    ("bye", "goodbye", "see you"): [
                        "Goodbye! Have a great day!",
                        "See you later!",
                        "Take care! Until next time."
                    ],
                    ("thank you", "thanks", "appreciate it"): [
                        "You're welcome!",
                        "No problem at all!",
                        "Happy to help!"
                    ],
                    ("help", "assist me", "i need help"): [
                        "Sure, I'm here to help! What do you need assistance with?",
                        "How can I assist you today?",
                        "I'm here to help you. Please tell me what you need."
                    ],
                    ("joke", "tell me a joke", "make me laugh"): [
                        "Why don't scientists trust atoms? Because they make up everything!",
                        "Why did the scarecrow win an award? Because he was outstanding in his field!",
                        "Why don't some couples go to the gym? Because some relationships don't work out!"
                    ]
                   }
                for i in dic:
                    if task in i:
                        x = int(len(dic[i]))
                        r = random.randint(0,x-1)
                        s.speaker(dic[i][r])
                        break
                else:
                    s.speaker("please speak that again")
    
    
def setup():  
    c = "who do you want your assistant to be?.... jarvis..... or ..alexa, or say exit ,to exit"
    s.speaker(c)
    n=l.listen()
    return n

#voice test
task = do_tasks()
n=setup()
assistant = ''
if(n=='jarvis'):
    s.set_male()
    assistant = 'Jarvis'
    c="Hi there, I am your assistant..."+assistant+"....press the button to speak"
    s.speaker(c)
elif(n=='alexa'):
    s.set_female()
    assistant = 'Alexa'
    c="Hi there, I am your assistant..."+assistant+".... press the button to speak"
    s.speaker(c)
elif(n=='exit'):
    s.speaker("thankyou ! see you again")
    exit()
elif(n=='error'):
    c = "I am sorry, can you speak again?"
    s.speaker(c)
    setup()
else:
    c = "I am sorry, can you speak again"
    s.speaker(c)
    setup()

#gui
m = tk.Tk()
m.title("VOICE ASSISTANT")
m.geometry("500x500")
m.configure(bg="#041527")
w = tk.Label(m,text="YOUR OWN VOICE ASSISTANT",font=("Arial",15))
button = tk.Button(text = "click to speak",height="14",width="26",bg="#041527",fg="white",font=("Arial",12),command=partial(task.main))
w.pack(pady="10")
button.pack(pady="150")
m.mainloop()

    
    
