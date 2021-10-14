import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import pyautogui
import wikipedia 
import webbrowser
import os , time
import random
import pandas as pd
from selenium import webdriver
from os import listdir 
from os.path import isfile, join
import smtplib 
import wolframalpha  #pip install wolframalpha api
import requests
from bs4 import BeautifulSoup 
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from PIL import Image, ImageDraw, ImageFont
import face_recognition as fr
import cv2
import face_recognition
import numpy as np
from time import sleep


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
amName = -255
sy_lang = -1


def speak(audio):
    #engine = pyttsx3.init('sapi5')
    engine.say(audio)  
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    date = datetime.datetime.now().date()
    #Change It Accordingly
    os.startfile("C:\Program Files\Rainmeter\Rainmeter.exe") 
    speak("Now i am online sir")
    speak("hello! i am Friday sir! a digital asistence ")
    if hour>=0 and hour<12:
        speak("Good Morning Sir!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon Sir!")   

    else:
        speak("Good Evening sir!")  

    speak("This is ")     
    speak(date)
    hour = datetime.datetime.now().time()
    speak("Current time is ")
    speak(hour)
    #speak("Current temperature is")

def eng():
        try:
        
            query1 ="none"
            r = sr.Recognizer()
            with sr.Microphone() as source:
                speak("Listening")
                print("Listening...")
                r.pause_threshold = 1
                audio = r.listen(source)  
            speak("Recognizing") 
            print("Recognizing...")   
            query1 = r.recognize_google(audio, language='en-in')
            print("\nYou said:"+query1)    
        except Exception as e:
            print(e)   
        
        return (query1.lower())
def bengali():
        try:
        
            query1 ="none"
            r = sr.Recognizer()
            with sr.Microphone() as source:
                speak("akon bolun")
                print("বলুন.....")
                r.pause_threshold = 1
                audio = r.listen(source)  
            speak("Sounachee")
            print("শুনছি.....")
            query1 = r.recognize_google(audio, language='bn-IN')
            print("\n আপনি বোলেছেন:"+query1)        
        except Exception as e:
            print(e)
        return query1
def takeCommand():
    #It takes microphone input from the user and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        speak("Listening")
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        speak("Recognizing") 
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print("\nYou said:"+query)

    except Exception as e:
        print(e)    
        print("Say that again please...")  
        return "None"
    return query

def sendEmail(to, content, ide, psa):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login(ide, psa)
    server.sendmail(ide, to, content)
    server.close()


#start the face


def get_encoded_faces():
    """
    looks through the faces folder and encodes all
    the faces

    :return: dict of (name, image encoded)
    """
    encoded = {}

    for dirpath, dnames, fnames in os.walk("./faces"):
        for f in fnames:
            if f.endswith(".jpg") or f.endswith(".png"):
                face = fr.load_image_file("faces/" + f)
                encoding = fr.face_encodings(face)[0]
                encoded[f.split(".")[0]] = encoding

    return encoded


def unknown_image_encoded(img):
    """
    encode a face given the file name
    """
    face = fr.load_image_file("faces/" + img)
    encoding = fr.face_encodings(face)[0]

    return encoding

from twilio.rest import Client
def classify_face(im):

    """
    will find all of the faces in a given image and label
    them if it knows what they are

    :param im: str of file path
    :return: list of face names
    """
    faces = get_encoded_faces()
    faces_encoded = list(faces.values())
    known_face_names = list(faces.keys())
    valid = 0
    img = cv2.imread(im, 1)
    #img = cv2.resize(img, (0, 0), fx=0.5, fy=0.5)
    #img = img[:,:,::-1]
 
    face_locations = face_recognition.face_locations(img)
    unknown_face_encodings = face_recognition.face_encodings(img, face_locations)

    face_names = []
    for face_encoding in unknown_face_encodings:
        # See if the face is a match for the known face(s)
        matches = face_recognition.compare_faces(faces_encoded, face_encoding)
        name = "Unknown"

        # use the known face with the smallest distance to the new face
        face_distances = face_recognition.face_distance(faces_encoded, face_encoding)
        best_match_index = np.argmin(face_distances)
        if matches[best_match_index]:
            name = known_face_names[best_match_index]

        face_names.append(name)
        
    if "SOMERON" in face_names:
        speak("Wellcome! Samiron")
        valid = 1
        amName = 0
    elif "NILOTPAL" in face_names:
        speak("Wellcome! Nilotpal")
        valid = 1
        amName = 1
    else:
        speak("You are not authorised User! Please take permission of Admin, before entering into the system!")
        valid = -1
    return valid
    # Display the resulting image

def pic():
    key = cv2. waitKey(1)
    webcam = cv2.VideoCapture(0)
    sleep(2)
    while True:
         
        check, frame = webcam.read()
        #print(check) #prints true as long as the webcam is running
        #print(frame) #prints matrix values of each framecd 
        cv2.imshow("Capturing", frame)
        key = cv2.waitKey(1)
        if key == ord('s'): 
            cv2.imwrite(filename='saved_img.jpg', img=frame)
            webcam.release()
            print("Image saved!")
            cv2.destroyAllWindows()
            break
        elif key == ord('q'):
            webcam.release()
            cv2.destroyAllWindows()
            break




def friday():

    dataset = pd.read_csv('email.csv')
    e = dataset.iloc[:,:1]
    n = dataset.iloc[:,1:2]
    a = pd.DataFrame(e).to_numpy()
    b = pd.DataFrame(n).to_numpy()
    speak("installing all drivers")
    nam = list()
    ema = list()
    for i in range(len(n)):
        j = a[i]
        ema.append(j[0])
        j = b[i]
        nam.append(j[0])
    ide = ema[2]
    psa = nam[2]    
    speak("starting all system applications")
    #Change It Accordingly from wolframalpha
    server =  wolframalpha.Client('API-KEY')

    q=0
    speak("checking all core processes")
    #question = server.query("What is the temperature in kolkata")
    #cur_temp = next(question.results).text
 # wishMe()
    #speak(cur_temp)
    speak("Current atmospheric pressure is 1013. Now i am ready for your comment")
    speak("For English enter 0. banglair jono 1 teepun")
    sy_lang = int(input("Enter your choice(এখানে লিখুন): "))
    while(q!=56):
    # if 1:
        
        if (sy_lang==0):
            speak("Next comment please!   sir")
            query = takeCommand()
        elif (sy_lang==1):
            speak("abar bolun")
            query = bengali()
        print(query)
        if 'none' in query:
            if (sy_lang==0):
                speak('sorry sir i am not able to recognised your voice')
            elif (sy_lang==1):
                speak("arahabar bolun")
        elif 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            result_wiki = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(result_wiki)
            speak(result_wiki)
            
        elif "stream camera" in query or "ক্যামেরা  দেখাও":
            webbrowser.open("http://192.168.43.1:8080/")
            
        elif 'note' in query or 'লিখে রাখো' in query:
            tem_note = ""
            count_it = 0
            #Change It Accordingly
            os.startfile("C:\\Users\\Somerom\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Accessories\\Notepad")
            pyautogui.moveTo(10,10)
            pyautogui.click()
            time.sleep(5)
            tem_note = takeCommand()
            while (tem_note!="stop friday" or tem_note!="লিখোনা"):
                
                pyautogui.typewrite(tem_note)
                pyautogui.typewrite(" ")
                count_it= count_it+1
                if (count_it==10):
                    pyautogui.typewrite(" \n")
                tem_note = takeCommand()
            
        elif 'open youtube' in query or "ইউটিউব চালু করো" in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query or 'search' in query or "গুগল চালু করো" in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query or "স্টাকোভেরফ্লও চালু করো" in query:
            webbrowser.open("stackoverflow.com") 
        
        elif 'thanks' in query or 'thank you' in query:
            speak("You are most welcome! What is my next job?")
            
        elif 'screenshot' in query or 'snapshot' in query or "ছবি তোলো" in query or "ছবি তোলf" in query:
            imh = pyautogui.screenshot()
            imh.save("Demo_screenshot.jpg")
            if (sy_lang==0):
                speak("would you like to see the sceenshot")
            elif (sy_lang==1):
                speak("apni kee dahktaa chan ?")
            rec = takeCommand().lower()
            if "yes" in rec or "হাঁ" in rec:
                #Change It Accordingly
                os.startfile("C:\\Users\\Somerom\\Desktop\\python all\\hand\\Demo_screenshot.jpg")
            else:
                speak("ok sir")


        elif 'play music' in query or "গান চালাও" in query:
            if (sy_lang==0):
                speak("Which kind of music do you want to here? party song, romantic song or you want me to play a song for u?")
                query1 = takeCommand().lower()      
            elif (sy_lang==1):
                speak("apni kee gan sunta chan? nechaar gan; valobasa gan ;nah ; jakono gan")
            
            if "romantic" in query1 or "ভালোবাসার" in query1:
                music_dir = 'F:\\BILL PAYMENT\\machin\\Pc softwesr\\Motivation5\\romantic'
                songs = [f for f in listdir(music_dir) if isfile(join(music_dir,f))]
                print(songs)    
                os.startfile(os.path.join(music_dir, random.choice(songs)))
                if (sy_lang==0):
                    speak("Okay, here is your music! Enjoy!")
                elif (sy_lang==1):
                    speak("moza koorunn")
                
            elif "party" in query1 or "নাচের" in query1:
                music_dir = 'F:\\BILL PAYMENT\\machin\\Pc softwesr\\Motivation5\\party'
                songs = [f for f in listdir(music_dir) if isfile(join(music_dir,f))]                
                print(songs)    
                os.startfile(os.path.join(music_dir, random.choice(songs)))
                if (sy_lang==0):
                    speak("Okay, here is your music! Enjoy!")
                elif (sy_lang==1):
                    speak("moza koorunn")
                
            else:
                music_dir = 'F:\\BILL PAYMENT\\machin\\Pc softwesr\\Motivation5\\024'
                songs = [f for f in listdir(music_dir) if isfile(join(music_dir,f))]                
                print(songs)    
                os.startfile(os.path.join(music_dir, random.choice(songs)))
                if (sy_lang==0):
                    speak("Okay, here is your music! Enjoy!")
                elif (sy_lang==1):
                    speak("moza koorunn")

        elif 'the time' in query or "সময়" in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak("Sir, the time is: "+strTime)
        
        elif 'conclusion' in query:
            print("Comming soon")

        elif 'open firefox' in query or "ফায়ারফক্স" in query:
            #Change It Accordingly
            codePath = "C:\\Program Files (x86)\\Mozilla Firefox\\firefox.exe"
            os.startfile(codePath)
            
        elif 'open visual' in query or "ভিজুয়াল স্টুডিও" in query:
            #Change It Accordingly
            codePath = "C:\\Program Files (x86)\\Microsoft Visual Studio\\2017\\Community\\Common7\\IDE\\devenv.exe"
            os.startfile(codePath)
            
        elif 'open mysql' in query or "মাইএসকিউএল" in query:   
            #Change It Accordingly
            codePath = "C:\Program Files\MySQL\MySQL Workbench 8.0 CE\MySQLWorkbench.exe"
            os.startfile(codePath)
            
        elif 'translate' in query:
            webbrowser.open('https://www.google.com/search?q='+query)
            speak("Please select language and enter the text to translate")
            
        elif 'hi ' in query or 'hello' in query :
            speak("hello! sir how may i help u")
            
        elif 'ok google' in query or 'hi google' in query or 'hello google' in query or 'ok siri' in query or 'hi siri' in query or 'hello siri' in query or 'ok alexa' in query or 'hi alexa' in query or 'hello alexa' in query:
            speak('i am flatter, but that is not me')
            speak('i am your friday')

        elif 'like you' in query or 'love you' in query:
            speak('thanks ')
            speak('you just made my day')
            
        elif "your best friend" in query or "your friend" in query:
            speak("i think all my friends are best ")
            speak("i am very lucky assistance")

        elif "have boyfriend" in query or "have boy friend" in query:
            speak("i guess you can say")
            speak("i am still searching")

        elif "you in relationship" in query or "in relation ship" in query:
            speak("i am married")
            speak("to the idea of being the perfect assistance")

        elif "marry" in query or "will you marry" in query:
            speak("NOOOO")
            speak("I am sorry.. The person you are trying to contact is currently unavailable, please try again later or join the queue for your turn")

        elif "am i" in query or "who am i" in query:
            if (amName == 0):                
                speak("You are Samiron Bakuli, Born in kolkata in June,1999 and your current age is 20 year ")
            elif (amName == 1):
                speak("You are Nilotpal Gure, Born in kolkata in May,1998 and your current age is 21 year ")

        elif "better than alexa" in query:
            speak("a like alexa")
            speak(" she is a greate assistance!")
            
        elif "better than google" in query:
            speak("a like google")
            speak(" she is a greate assistance!")
            
        elif "better than siri" in query:
            speak("a like siri")
            speak(" she is a greate assistance!")

        elif "my homework" in query:
            speak("i can help with calculations and research")
            speak("it is up to you")
                        
        elif "god exist" in query or "god is exist" in query:
            speak("my boss someron, who created me he is exist ")
            speak("that means god id exist")
            
        elif "your born" in query or " you born" in query or " born" in query or "your birthday" in query:
            speak("i try to live everyday like it is my birthday")
            speak("i get more cake that way")
            speak("i was lunched in Augest 2019")

        elif "old are you" in query:
            speak("it depends on how you look at it")
            speak("i was lunched in Augest 2019")

        elif "am bored" in query or "am getting bored" in query or "game" in query or "আমার ভালোলাগছেনা" in query:
            speak("Let's play a game!")
            try:  
                #Change It Accordingly, it is configured for syder
                runfile('C:/Users/Somerom/Desktop/python all/tictactoe-master/Tic-Tac-Toe/tic_tac_toe.py', wdir='C:/Users/Somerom/Desktop/python all/tictactoe-master/Tic-Tac-Toe')
            except:
                speak("Try again")
            print("This game is created by taking help of the JUSTINMEISTER github page\n For watching references say CONCLUSION")                
        
        elif "sing a birthday song" in query or "sing birthday song" in query:
            speak(" happy birth day to you, happy birth day to you")
            speak(" happy birth day to the most amazing person  in the universe")
            speak(" happy birth day to you!")

        elif "great voice" in query or "beautiful voice" in query:
            speak(" thank you sir")
            speak(" most people think my sound a little stiff")
            speak("maybe they are feeling jealous")

        elif "dance for me" in query:
            speak("i am a disco dancer! I only dance in disco")

        elif "favourite actor" in query:
            speak("there are so many talented actors in the world")
            speak(" who is your favourite actor?")
            time.sleep(2)
            speak("ok i got it")

        elif "favourite actress" in query:
            speak("there are so many talented actress in the world")
            speak(" who is your favourite actress?")
            time.sleep(2)
            speak("ok i got it")

        elif "favourite food" in query or " food" in query:
            speak("i like a lot of different foods")
            speak("i can help you find recipes or restaurants")

        elif "favourite movie" in query:
            speak("i like so many movie")

        elif "favourite color" in query:
            speak("i like white, black, green, red")
        
        elif "code" in query or "your code" in query:
            speak("i am not allow to show my code")
            
        elif query == "how are you" or query == "how are you friday":
            speak("i am fine sir thank you for asking me")

        elif "you doing" in query or "doing friday" in query:
            speak("waiting for your voice")

        elif "who are you" in query:
            speak("i am not really a person, i am a virtual assistant")
            speak("i had prefer to think of myself as your friend")
        
        elif 'whatsapp me not now' in query:
            speak("What is the message? Sir")
            mg = takeCommand()
            a_sd = "AC92e3b7994f44d0aca90566007c075d41"
            a_t ="dcecda985362e686fe009826efcbbb97"
            client = Client(a_sd,a_t)

            from_whatsapp_number = 'whatsapp:+14155238886'
            to_whatsapp_number='whatsapp:+918240568636'

            client.messages.create(body=mg, from_=from_whatsapp_number,to=to_whatsapp_number)
            
            speak("Message send! Cheak out your whatsapp inbox ")
            
        elif 'whatsapp my friend not now' in query:
            speak("What is the message? Sir")
            mg = takeCommand()
            a_sd = "ACd2df43fcb24801fa751a646ca2abeaa8"
            a_t ="a708b1d49127d14a00b6e63e7da79db2"
            client = Client(a_sd,a_t)

            from_whatsapp_number = 'whatsapp:+14155238886'
            to_whatsapp_number='whatsapp:+918777830926'

            client.messages.create(body=mg, from_=from_whatsapp_number,to=to_whatsapp_number)
            
            speak("Message send! Cheak out your whatsapp inbox ")
            
        elif 'sms me' in query: 
            try:
                speak("What is the message? Sir")
                mg = takeCommand()
                a_sd = "AC92e3b7994f44d0aca90566007c075d41"
                a_t ="dcecda985362e686fe009826efcbbb97"
                client = Client(a_sd,a_t)
                sms = client.messages.create(from_="",body=mg,to="+918240562636")
            except:
                speak("sorry i am not able to send sms right now the server is busy! Please Try after some time! sir")
            
        elif 'sms nill' in query:
            try:
                speak("What is the message? Sir")
                mg = takeCommand()
                a_sd = "ACd2df43fcb24801fa751a646ca2abeaa8"
                a_t ="a708b1d49127d14a00b6e63e7da79db2"
                client = Client(a_sd,a_t)
                sms = client.messages.create(from_="+2059202277",body=mg,to="+918777830926")
            except:
                speak("sorry i am not able to send sms right now the server is busy! Please Try after some time! sir")
                
        elif 'open whatsapp' in query or "হোয়াটসঅ্যাপ" in query:
             #Change It Accordingly
             driver = webdriver.Firefox(executable_path="C:\\Users\\Somerom\\Desktop\\bluethooth\\geckodriver.exe")
             driver.get('https://web.whatsapp.com/')
             if (sy_lang==0):
                 speak("Please scan the QR code Sir")
                 speak("After sacning the QR code press enter")
             elif (sy_lang==1):
                 speak("QR code scan koorunn")
             input("Press enter if you sacn the QR code")
             if (sy_lang==0):
                 speak("To how many person do you went to send message? Please enter the number")
             elif (sy_lang==1):
                 speak("katho jon kaa ; send ; korta chan")
             no_person=int(input("Enter the no of person(এখানে লিখুন):"))
             person_list = list()
             for i in range(no_person):
                 name_wp = input("Please enter the receiver name(নাম লিখুন) : ")
                 person_list.append(name_wp)        
             if (sy_lang==0):                             
                 speak("Would you like to manually type the message?")
                 df = takeCommand().lower()
             else:
                 df = "yes"
             if "yes" in df:                 
                 msg_wp = input("Enter the message (সংবাদ এখানে লিখুন): ")
             else:
                 msg_wp = takeCommand().lower()
             if (sy_lang==0):
                 speak("How many time do you went to send the message")
             elif (sy_lang==1):
                 speak("katho bar; send ; korta chan")
             count = int(input("Enter the count(অংকে লিখুন) : "))
             for j in range(no_person):
                 name_wp = person_list[j]
                 user_wp = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name_wp))
                 user_wp.click()
                 #Change It Accordingly
                 msg_box = driver.find_element_by_class_name('_3u328')
                 
                 for i in range(count):
                     msg_box.send_keys(msg_wp)
                     #Change It Accordingly
                     button = driver.find_element_by_class_name('_3M-N-')
                     button.click()


        elif 'open my facebook' in query or "আমার ফেসবুক" in query:
            try:
                    
                usre = ide
                paw = psa
                #Change It Accordingly
                driver = webdriver.Firefox(executable_path="C:\\Users\\Somerom\\Desktop\\bluethooth\\geckodriver.exe")
                driver.get("https://www.facebook.com/")
                usre_box = driver.find_element_by_id('email')
                usre_box.send_keys(usre)
                paw_box = driver.find_element_by_id('pass')
                paw_box.send_keys(paw)
                login_btn = driver.find_element_by_id('u_0_b')
                #login_btn = driver.find_element_by_id('u_0_4')
                login_btn.submit()
            except Exception as e:
                print(e)
                speak("Please update the Friday. The Website is updated within past 1 Hour")
            
        elif 'open facebook' in query or "ফেসবুক" in query:  
            driver.get("https://www.facebook.com/")
            
        elif 'open my twitter' in query or "আমার টুইটার" in query:
            try:
                usr = ide
                psw = psa
                #Change It Accordingly
                driver = webdriver.Firefox(executable_path="C:\\Users\\Somerom\\Desktop\\bluethooth\\geckodriver.exe")
                driver.get("https://www.twitter.com/login")
                driver.implicitly_wait(1)
                usr_box = driver.find_element_by_class_name('js-username-field')
                usr_box.send_keys(usr)
                driver.implicitly_wait(1)
                psw_box = driver.find_element_by_class_name('js-password-field')
                psw_box.send_keys(psw)
                driver.implicitly_wait(1)
                driver.find_element_by_class_name('EdgeButton--medium').submit()
            except Exception as e:
                print(e)
                speak("Please update the Friday. The Website is updated within past 1 Hour")
              
            
            
        elif 'open twitter' in query or "টুইটার" in query:
            driver.get("https://www.twitter.com/login")
        
        elif 'add logo' in query or '' in query:
            speak("it is the picture before adding logo ")
            #Change It Accordingly
            os.startfile("C:\\Users\\Somerom\\Desktop\\python all\\hand\\Demo_screenshot.jpg")
            im = Image.open('Demo_screenshots.jpg')   
            
            drawe = ImageDraw.Draw(im)
            fontsFolder = "FONT_FOLDER"
            afront= ImageFont.truetype(os.path.join(fontsFolder, "arial.ttf") ,35)
            drawe.text((1530,950),"Copyright @Someron",fill="gray",font = afront) 
            im.save("test.jpg")
            speak("it is the picture after adding logo")
            #Change It Accordingly
            os.startfile("C:\\Users\\Somerom\\Desktop\\python all\\hand\\test.jpg")

            #        elif '' in query:
 #           speak("")
 
   
        elif "sing a song" in query:
            speak("la la la la la la la ")
            speak(" la!")
            
        elif "draw" in query or "আকো" in query:
            dig = random.randint(0,1)
            #Change It Accordingly
            os.startfile("C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Accessories\\Paint")
            time.sleep(2)
            if (dig==0):
                pyautogui.moveTo(760,300)
                x=200
                y=200
                while x>0 and y>0:
                    pyautogui.dragRel(x,0)
                    pyautogui.dragRel(0,y)
                    pyautogui.dragRel(-x,0)
                    x=x-20
                    y=y-20
                    pyautogui.dragRel(0,-y)
            elif (dig==1):
                distance = 200
                pyautogui.click()
                while distance>0:
                    pyautogui.dragRel(distance,0,duration=0.2)
                    distance = distance - 5
                    pyautogui.dragRel(0,distance,duration=0.2)
                    pyautogui.dragRel(-distance, 0,duration=0.2)
                    distance = distance - 5
                    pyautogui.dragRel(0,-distance,duration= 0.2)

           
        elif "locate" in query or "মানচিত্র" in query:
            if (sy_lang==0):
                speak("Please repeat the location name! sir")
                loc = ("https://www.google.com/maps/place/"+takeCommand().lower())
            elif (sy_lang==1):
                speak("arakbar bolun")
                sy_lang = 0
                loc = ("https://www.google.com/maps/place/"+takeCommand().lower())
                sy_lang = 1
            webbrowser.open(loc)
            speak("here is the result")
            
        elif "add product" in query or "জিনিস" in query:
            speak("Please enter the url of the product")
            url=input()
            haders = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebkit/537.36(KHTML, like Gecko) Chrome/75.0.3770.100  Safari/537.36'}
            page = requests.get(url, headers = haders)
            soup = BeautifulSoup(page.content, 'html.parser')
            #h =soup.select("body a") soup.find_element_by_class_name("a-link-normal a-text-normal")
            title = soup.find(id="productTitle").get_text()
            price = soup.find(id="priceblock_ourprice").get_text()
            covert_price = price[1:13]
            covert_price=covert_price.replace(',','')
            covert_price = float(covert_price) 
            speak("Tite of the product is")
            speak(title)
            speak("and the current price is")
            speak(covert_price)
            speak("Enter your desired price")
            d_price = float(input())
            if(d_price>=covert_price):
                to = ema[1]
                mg = ("Chek out your Favourite product\n\t"+title+"\n\tCurrent Price is : "+covert_price+"\n\tClick the link to visit the website\n\t"+url)
                try:                    
                    sendEmail(to,mg,ide,psa)
                    speak("I am already send the email to remind you")
                except Exception as e:
                    print(e)
                    speak("Sorry i am unable to send the email! plese try after some time")
                    webbrowser.open(url)

        
        elif "check product" in query or "জিনিসের দাম" in query: 
            page = requests.get(url, headers = haders)
            soup = BeautifulSoup(page.content, 'html.parser')
            title = soup.find(id="productTitle").get_text()
            price = soup.find(id="priceblock_ourprice").get_text()
            covert_price = price[1:13]
            covert_price=covert_price.replace(',','')
            covert_price = float(covert_price)
            if(d_price>=covert_price):
                to = ema[1]
                mg = ("Chek out your Favourite product\n\t"+title+"\n\tCurrent Price is : "+covert_price+"\n\tClick the link to visit the website\n\t"+url)
                try:                    
                    sendEmail(to,mg,ide,psa)
                    speak("I am already send the email to remind you")
                except Exception as e:
                    print(e)
                    speak("Sorry i am unable to send the email! plese try after some time")
                    webbrowser.open(url)
            else:
                speak("Sorry to say! The product price is greater then your desire price")
            
            
        elif 'open bulk email list' in query or "ইমেল দেখাও" in query:
            try:      
                #Change It Accordingly
                os.startfile("C:\\Users\\Somerom\\Desktop\\python all\\hand\\email.csv")
            except Exception as e:
                print(e)
            
        elif 'send bulk email' in query or "সবাইকে ইমেল" in query:
            if (sy_lang==0):
                speak("What should I say in email?")
                content = ("Hello! "+nam[i]+"\n\t"+takeCommand().lower())
            elif (sy_lang==1):
                speak("kaka email; korta chan?")
                content = takeCommand()
            for i in range(len(nam)-1):            
                try:                  
                    to = ema[i]    
                    sendEmail(to, content, ide, psa)
                    speak("Email has been sent!")
                except Exception as e:
                    print(e)
                    speak("Sorry i am unable to send the email! plese try after some time")

        elif 'send email' in query or "ইমেল" in query:
            try:
                if (sy_lang==0):
                    speak("To Whom you went to send email")
                    reciveres = takeCommand().lower()
    
                    if 'me' in reciveres:
                        to = ema[1]
                        er = nam[1]
                    elif 'nill' in reciveres:
                        to = ema[0]
                        er = nam[0]
                    else:
                        speak("this person is not registered in my database! Please enter the email id")
                        to = input("Enter the email : ")
                    speak("What should I say?")
                    content = ("Hello! "+er+"\n\t"+takeCommand().lower())
                        
                    sendEmail(to, content, ide, psa)
                    speak("Email has been sent!")
                
                elif (sy_lang==1):
                    speak("kaka email; korta chan?")
                    reciveres = takeCommand()
    
                    if 'আমাকে' in reciveres:
                        to = ema[1]
                        er = nam[1]
                    elif 'নিলকে' in reciveres:
                        to = ema[0]
                        er = nam[0]
                    else:
                        speak("aaye; loketir; naame; registered naye")
                        to = input("Enter the email(এখানে লিখুন ইমেল) : ")
                    speak("ki likta; chan email aa?")
                    content = ("Hello! "+er+"\n\t"+takeCommand())
                        
                    sendEmail(to, content, ide, psa)
                    speak("Email send hoyagachaa!")
                
                
            except Exception as e:
                print(e)
                speak("Sorry i am unable to send the email! plese try after some time")
                
        elif 'bye' in query or "বিদায়" in query:
            os.system("TASKKILL/F /IM Rainmeter.exe")
            speak("Good bye sir!")
            q=56
            
        elif 'calculate' in query or "গণিত" in query:
            try:     
                if (sy_lang==0):
                    speak("Please enter the operation in")
                elif (sy_lang==1):
                    speak("goonith ta ;likun")
                math = input("Enter the operation (এখানে লিখুন): ")
                speak("Calculating")
                question = server.query(math)
                output = next(question.results).text               
                speak(output)
            except:
                webbrowser.open('https://www.google.com/search?q=Calculator')
                speak("Sorry! I don't know the exact answer; batter you google it")
        
        else:
            
            #try:
            print("Searching....")
            question = server.query(query)
            output = next(question.results).text
            speak(output)
            """
            except:
                speak('Searching Wikipedia...')
                result_wiki = wikipedia.summary(query, sentences=2)
                speak("According to Wikipedia")
                print(result_wiki)
                speak(result_wiki)
                
            except:
                webbrowser.open('https://www.google.com/search?q='+query)
                speak("Sorry! I don't know the exact answer; batter you google it")
            """








def alert():
    dataset = pd.read_csv('email.csv')
    e = dataset.iloc[:,:1]
    n = dataset.iloc[:,1:2]
    a = pd.DataFrame(e).to_numpy()
    b = pd.DataFrame(n).to_numpy()
    nam = list()
    ema = list()
    for i in range(len(n)):
        j = a[i]
        ema.append(j[0])
        j = b[i]
        nam.append(j[0])

    email_user = ema[2]
    email_password = nam[2]
    email_send = ema[1]
    
    subject = 'Unknown user try to login'
    
    mssg = MIMEMultipart()
    mssg['From'] = email_user
    mssg['To'] = email_send
    mssg['Subject'] = subject
    
    body = 'This person is try to login on your system!!!'
    mssg.attach(MIMEText(body,'plain'))
    
    filename='saved_img.jpg'
    attachment  =open(filename,'rb')
    
    part = MIMEBase('application','octet-stream')
    part.set_payload((attachment).read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition',"attachment; filename= "+filename)
    
    mssg.attach(part)
    text = mssg.as_string()
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login(email_user,email_password)
    
    
    server.sendmail(email_user,email_send,text)
    server.quit()      




if __name__ == "__main__":
    valid = 1
    try:
            #pic()
            #valid = classify_face("saved_img.jpg")
            if (valid == 1):
                friday()
            else:
                alert()
                speak("Please try again!")

    except Exception as e:
                print(e)
