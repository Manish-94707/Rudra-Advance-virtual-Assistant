import pyttsx3
import speech_recognition
import webbrowser 
import requests 
from bs4 import BeautifulSoup
import os
import datetime
import random
from pygame import mixer
from plyer import notification
from tkinter import *
from PIL import ImageTk, Image
from clap import MainClapExe
import pyautogui

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
rate = engine.setProperty("rate",170)
for i in range(3):
    a = input("Enter Password to open Rudra :- ")
    pw_file = open("password.txt","r")
    pw = pw_file.read()
    pw_file.close()
    if (a==pw):
        print("WELCOME SIR ! PLZ SPEAK [WAKE UP] TO LOAD ME UP")
        break
    elif (i==2 and a!=pw):
        exit()

    elif (a!=pw):
        print("Try Again")
from INTRO import play_gif
play_gif

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takecommand():
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source,0,4)

    try:
        print("Understanding..")
        query  = r.recognize_google(audio,language='en-in')
        print(f"You Said: {query}\n")
    except Exception as e:
        print("Say that again")
        return "None"
    return query

def alarm(query):
    timehere = open("Alarmtext.txt","a")
    timehere.write(query)
    timehere.close()
    os.startfile("alarm.py")

""" From this para I have implemented GUI using Tkinter """

class Widget:
    def __init__(self):
       root = Tk()
       root.title('manish')
       root.config(background='purple')
       root.geometry('720x480')
       root.resizable(0, 0)
       img = ImageTk.PhotoImage(Image.open(r"D:\rudra.jpg"))
       panel = Label(root, image = img)
       panel.pack(side='right', fill='both',expand = "no")

       

       self.compText = StringVar()
       self.userText = StringVar()

       self.userText.set('Click \'Run Rudra\' to Give commands')

       userFrame = LabelFrame(root, text="User", font=('Black ops one',10, 'bold'))
       userFrame.pack(fill="both", expand="yes")
         
       left2 = Message(userFrame, textvariable=self.userText, bg='#FF7F24', fg='white')
       left2.config(font=("Times New Roman", 18, 'bold'))
       left2.pack(fill='both', expand='yes')

       compFrame = LabelFrame(root, text="Rudra", font=('Black ops one',10, 'bold'))
       compFrame.pack(fill="both", expand="yes")
         
       left1 = Message(compFrame, textvariable=self.compText, bg='#1E90FF',fg='white')
       left1.config(font=("Times New Roman", 18, 'bold'))
       left1.pack(fill='both', expand='yes')
       
       btn = Button(root, text='Run Rudra', font=('Black ops one', 10, 'bold'), bg='#4b4b4b', fg='white',command=self.clicked).pack(fill='x', expand='no')
       btn2 = Button(root, text='Close!', font=('Black Ops One', 10, 'bold'), bg='#4b4b4b', fg='white',command=root.destroy).pack(fill='x', expand='no')
      
       
       
       self.compText.set('Hello, I am Rudra! What can I do for you Sir ??')

       root.bind("<Return>",self.clicked) # handle the enter key event of your keyboard
       root.mainloop()
    
    def clicked(self):
        print('Working')
        query = takecommand()
        self.userText.set('Listening...')
        self.userText.set(query)
        query = query.lower()
        if "hello" in query:
            speak("Hello sir, how are you ?")
        elif "i am fine" in query:
            speak("that's great, sir")
        elif "how are you" in query:
            speak("Perfect, sir")
        elif "thank you" in query:
            speak("you are welcome, sir")
        elif "google" in query:
            from SearchNow import searchGoogle
            searchGoogle(query)
        elif "youtube" in query:
                    from SearchNow import searchYoutube
                    searchYoutube(query)        
        elif "wikipedia" in query:
                    from SearchNow import searchWikipedia
                    searchWikipedia(query)          
        elif "temperature" in query:
                    search = "temperature in delhi"
                    url = f"https://www.google.com/search?q={search}"
                    r  = requests.get(url)
                    data = BeautifulSoup(r.text,"html.parser")
                    temp = data.find("div", class_ = "BNeawe").text
                    speak(f"current{search} is {temp}")        
        elif "weather" in query:
                    search = "temperature in delhi"
                    url = f"https://www.google.com/search?q={search}"
                    r  = requests.get(url)
                    data = BeautifulSoup(r.text,"html.parser")
                    temp = data.find("div", class_ = "BNeawe").text
                    speak(f"current{search} is {temp}")        
        elif "the time" in query:
                    strTime = datetime.datetime.now().strftime("%H:%M")
                    speak(f"Sir, the time is {strTime}")        
        elif "finally sleep" in query:
                    speak("Going to sleep,sir")
                    exit()        
        elif "open" in query:
                    from Dictapp import openappweb
                    openappweb(query)        
        elif "close" in query:
                    from Dictapp import closeappweb
                    closeappweb(query)        
        elif "set an alarm" in query:
                    print("input time example:- 10 and 10 and 10")
                    speak("Set the time")
                    a = input("Please tell the time :- ")
                    alarm(a)
                    speak("Done,sir")        
        elif "pause" in query:
                    pyautogui.press("k")
                    speak("video paused")        
        elif "play" in query:
                    pyautogui.press("k")
                    speak("video played")        
        elif "mute" in query:
                    pyautogui.press("m")
                    speak("video muted")        
        elif "volume up" in query:
                    from keyboard import volumeup
                    speak("Turning volume up,sir")
                    volumeup()       
        elif "volume down" in query:
                    from keyboard import volumedown
                    speak("Turning volume down, sir")
                    volumedown()        
        elif "remember that" in query:
                    rememberMessage = query.replace("remember that","")
                    rememberMessage = query.replace("Rudra","")
                    speak("You told me to remember that"+rememberMessage)
                    remember = open("Remember.txt","a")
                    remember.write(rememberMessage)
                    remember.close()        
        elif "what do you remember" in query:
                    remember = open("Remember.txt","r")
                    speak("You told me to remember that" + remember.read())        
        elif "tired" in query:
                    speak("Playing your favourite songs, sir")
                    a = (1,2,3) # You can choose any number of songs (I have only choosen 3)
                    b = random.choice(a)
                    if b==1:
                      webbrowser.open("https://www.youtube.com/watch?v=UPkMkIOzej8")
                    elif b==2:
                           webbrowser.open("https://www.youtube.com/watch?v=rfTgO9rpqck")
                    else:
                           webbrowser.open("https://www.youtube.com/watch?v=jLNrvmXboj8")        
        elif "news" in query:
                    from NewsRead import latestnews
                    latestnews()        
        elif "calculate" in query:
                    from Calculatenumbers import WolfRamAlpha
                    from Calculatenumbers import Calc
                    query = query.replace("calculate","")
                    query = query.replace("Rudra","")
                    Calc(query)        
        elif "whatsapp" in query:
                    from Whatsapp import sendMessage
                    sendMessage()        
        elif "shutdown the system" in query:
                    speak("Are You sure you want to shutdown")
                    shutdown = input("Do you wish to shutdown your computer? (yes/no)")
                    if shutdown == "yes":
                            os.system("shutdown /s /t 1")
                    elif shutdown == "no":
                           pass    
        elif "change password" in query:
                    speak("What's the new password")
                    new_pw = input("Enter the new password\n")
                    new_password = open("password.txt","w")
                    new_password.write(new_pw)
                    new_password.close()
                    speak("Done sir")
                    speak(f"Your new password is{new_pw}")        

        elif "schedule my day" in query:
                    tasks = [] #Empty list 
                    speak("Do you want to clear old tasks (Plz speak YES or NO)")
                    query = takecommand().lower()
                    if "yes" in query:
                        file = open("tasks.txt","w")
                        file.write(f"")
                        file.close()
                        no_tasks = int(input("Enter the no. of tasks :- "))
                        i = 0
                        for i in range(no_tasks):
                            tasks.append(input("Enter the task :- "))
                            file = open("tasks.txt","a")
                            file.write(f"{i}. {tasks[i]}\n")
                            file.close()
                    elif "no" in query:
                        i = 0
                        no_tasks = int(input("Enter the no. of tasks :- "))
                        for i in range(no_tasks):
                                tasks.append(input("Enter the task :- "))
                                file = open("tasks.txt","a")
                                file.write(f"{i}. {tasks[i]}\n")
                                file.close()        
        elif "show my schedule" in query:
                        file = open("tasks.txt","r")
                        content = file.read()
                        file.close()
                        mixer.init()
                        mixer.music.load("notification.mp3")
                        mixer.music.play()
                        notification.notify(
                        title = "My schedule :-",
                        message = content,
                        timeout = 15
                        )        
        elif "open" in query:
                       #EASY METHOD
                        query = query.replace("open","")
                        query = query.replace("Rudra","")
                        pyautogui.press("super")
                        pyautogui.typewrite(query)
                        pyautogui.sleep(2)
                        pyautogui.press("enter")       
        elif "play a game" in query:
                        from game import game_play
                        game_play()        
        elif "screenshot" in query:
                        import pyautogui #pip install pyautogui
                        im = pyautogui.screenshot()
                        im.save("ss.jpg")        
        elif "click my photo" in query:
                        pyautogui.press("super")
                        pyautogui.typewrite("camera")
                        pyautogui.press("enter")
                        pyautogui.sleep(2)
                        speak("SMILE")
                        pyautogui.press("enter")        
        elif "translate" in query:
                        from Translator import translategl
                        query = query.replace("Rudra","")
                        query = query.replace("translate","")
                        translategl(query)         


""" #################################################################### """

#greet me
 
if __name__ == "__main__":
    while True:
        query = takecommand().lower()
        MainClapExe()
        if "wake up" in query :
            from GreetMe import greetMe
            greetMe()
            speak("sir, which mode do you prefer GUI or Terminal ?")
            while True:
                query = takecommand().lower()
                
                if "first" in query:
                     speak("welcome to Graphical user Interface mode, sir , press the run button to start")
                     widget = Widget()
                     break
                elif "terminal" in query:
                       speak("terminal mode activated sir, Is there anything i can do for you ?")
                elif "go to sleep" in query:
                    speak("Ok sir , You can  call me anytime")
                    break 
                elif "hello" in query:
                    speak("Hello sir, how are you ?")
                elif "i am fine" in query:
                    speak("that's great, sir")
                elif "how are you" in query:
                    speak("Perfect, sir")
                elif "thank you" in query:
                    speak("you are welcome, sir")
                elif "google" in query:
                    from SearchNow import searchGoogle
                    searchGoogle(query)
                elif "youtube" in query:
                    from SearchNow import searchYoutube
                    searchYoutube(query)
                elif "wikipedia" in query:
                    from SearchNow import searchWikipedia
                    searchWikipedia(query)  
                elif "temperature" in query:
                    search = "temperature in delhi"
                    url = f"https://www.google.com/search?q={search}"
                    r  = requests.get(url)
                    data = BeautifulSoup(r.text,"html.parser")
                    temp = data.find("div", class_ = "BNeawe").text
                    speak(f"current{search} is {temp}")
                elif "weather" in query:
                    search = "temperature in delhi"
                    url = f"https://www.google.com/search?q={search}"
                    r  = requests.get(url)
                    data = BeautifulSoup(r.text,"html.parser")
                    temp = data.find("div", class_ = "BNeawe").text
                    speak(f"current{search} is {temp}")
                elif "the time" in query:
                    strTime = datetime.datetime.now().strftime("%H:%M")
                    speak(f"Sir, the time is {strTime}")
                elif "finally sleep" in query:
                    speak("Going to sleep,sir")
                    exit()
                elif "open" in query:
                    from Dictapp import openappweb
                    openappweb(query)
                elif "close" in query:
                    from Dictapp import closeappweb
                    closeappweb(query)
                elif "set an alarm" in query:
                    print("input time example:- 10 and 10 and 10")
                    speak("Set the time")
                    a = input("Please tell the time :- ")
                    alarm(a)
                    speak("Done,sir")
                elif "pause" in query:
                    pyautogui.press("k")
                    speak("video paused")
                elif "play" in query:
                    pyautogui.press("k")
                    speak("video played")
                elif "mute" in query:
                    pyautogui.press("m")
                    speak("video muted")
                elif "volume up" in query:
                    from keyboard import volumeup
                    speak("Turning volume up,sir")
                    volumeup()
                elif "volume down" in query:
                    from keyboard import volumedown
                    speak("Turning volume down, sir")
                    volumedown()
                elif "remember that" in query:
                    rememberMessage = query.replace("remember that","")
                    rememberMessage = query.replace("Rudra","")
                    speak("You told me to remember that"+rememberMessage)
                    remember = open("Remember.txt","a")
                    remember.write(rememberMessage)
                    remember.close()
                elif "what do you remember" in query:
                    remember = open("Remember.txt","r")
                    speak("You told me to remember that" + remember.read())
                elif "tired" in query:
                    speak("Playing your favourite songs, sir")
                    a = (1,2,3) # You can choose any number of songs (I have only choosen 3)
                    b = random.choice(a)
                    if b==1:
                      webbrowser.open("https://www.youtube.com/watch?v=UPkMkIOzej8")
                    elif b==2:
                           webbrowser.open("https://www.youtube.com/watch?v=rfTgO9rpqck")
                    else:
                           webbrowser.open("https://www.youtube.com/watch?v=jLNrvmXboj8")
                elif "news" in query:
                    from NewsRead import latestnews
                    latestnews()
                elif "calculate" in query:
                    from Calculatenumbers import WolfRamAlpha
                    from Calculatenumbers import Calc
                    query = query.replace("calculate","")
                    query = query.replace("Rudra","")
                    Calc(query)
                elif "whatsapp" in query:
                    from Whatsapp import sendMessage
                    sendMessage()
                elif "shutdown the system" in query:
                    speak("Are You sure you want to shutdown")
                    shutdown = input("Do you wish to shutdown your computer? (yes/no)")
                    if shutdown == "yes":
                            os.system("shutdown /s /t 1")
                    elif shutdown == "no":
                         break
                elif "change password" in query:
                    speak("What's the new password")
                    new_pw = input("Enter the new password\n")
                    new_password = open("password.txt","w")
                    new_password.write(new_pw)
                    new_password.close()
                    speak("Done sir")
                    speak(f"Your new password is{new_pw}")

                elif "schedule my day" in query:
                    tasks = [] #Empty list 
                    speak("Do you want to clear old tasks (Plz speak YES or NO)")
                    query = takecommand().lower()
                    if "yes" in query:
                        file = open("tasks.txt","w")
                        file.write(f"")
                        file.close()
                        no_tasks = int(input("Enter the no. of tasks :- "))
                        i = 0
                        for i in range(no_tasks):
                            tasks.append(input("Enter the task :- "))
                            file = open("tasks.txt","a")
                            file.write(f"{i}. {tasks[i]}\n")
                            file.close()
                    elif "no" in query:
                        i = 0
                        no_tasks = int(input("Enter the no. of tasks :- "))
                        for i in range(no_tasks):
                                tasks.append(input("Enter the task :- "))
                                file = open("tasks.txt","a")
                                file.write(f"{i}. {tasks[i]}\n")
                                file.close()
                elif "show my schedule" in query:
                        file = open("tasks.txt","r")
                        content = file.read()
                        file.close()
                        mixer.init()
                        mixer.music.load("notification.mp3")
                        mixer.music.play()
                        notification.notify(
                        title = "My schedule :-",
                        message = content,
                        timeout = 15
                        )
                elif "open" in query:
                       #EASY METHOD
                        query = query.replace("open","")
                        query = query.replace("Rudra","")
                        pyautogui.press("super")
                        pyautogui.typewrite(query)
                        pyautogui.sleep(2)
                        pyautogui.press("enter")
                elif "play a game" in query:
                        from game import game_play
                        game_play()
                elif "screenshot" in query:
                        import pyautogui #pip install pyautogui
                        im = pyautogui.screenshot()
                        im.save("ss.jpg")
                elif "click my photo" in query:
                        pyautogui.press("super")
                        pyautogui.typewrite("camera")
                        pyautogui.press("enter")
                        pyautogui.sleep(2)
                        speak("SMILE")
                        pyautogui.press("enter")
                elif "translate" in query:
                        from Translator import translategl
                        query = query.replace("Rudra","")
                        query = query.replace("translate","")
                        translategl(query)
