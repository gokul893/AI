from re import L
from sunau import AUDIO_FILE_ENCODING_ADPCM_G721
from winreg import QueryInfoKey, QueryReflectionKey
import wolframalpha
import pyttsx3
import operator
import speech_recognition as sr
import datetime
import webbrowser
import os
import winshell
import pyjokes
import ctypes
import shutil
from ecapture import ecapture as ec
from urllib.request import urlopen
from requests import get
import pywhatkit as kit
import yagmail
import requests
from bs4 import BeautifulSoup
import speedtest
import pyautogui

from INTRO import play_gif
play_gif

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

#speak function
def speak(audio):
	engine.say(audio)
	engine.runAndWait()

#Wishing the user
def wishMe():
	hour = int(datetime.datetime.now().hour)
	if hour>= 0 and hour<12:
		speak("Good Morning Sir !")
	elif hour>= 12 and hour<18:
		speak("Good Afternoon Sir !")
	else:
		speak("Good Evening Sir !")
	assname = ("Voice Assistmant")
	speak("I am your Assistant")
	speak(assname)

#getting user name
def username():
	speak("What should i call you sir")
	uname = takeCommand()
	speak("Welcome Mister")
	speak(uname)
	columns = shutil.get_terminal_size().columns
	print("Welcome Mr.", uname)
	speak("How can i Help you, Sir")

#Taking commands from user
def takeCommand():
	r = sr.Recognizer()
	with sr.Microphone() as source:
		print("Listening...")
		r.pause_threshold = 1
		audio = r.listen(source)
	try:
		print("Recognizing...")
		query = r.recognize_google(audio, language ='en-in')
		print(f"User said: {query}\n")
	except Exception as e:
		print(e)
		print("Unable to Recognize your voice.")
		return "None"
	return query

if __name__ == '__main__':
	clear = lambda: os.system('cls')
	clear()
	wishMe()
	username()
	
	while True:
		query = takeCommand().lower()
		#Asking contents in google 
		if "google" in query:
			from SearchNow import searchGoogle
			searchGoogle(query)
		
		#Greeting1
		elif "hello" in query:
			speak("Hello master   How are you ? ")
		
		#Greeting2
		elif "i am fine" in query:
			speak("That great   Master!")
		
		#Greeting3
		elif "how are you" in query:
			speak("Perfect as always Master")
		
		#Greeting4
		elif "Thank you" in query:
			speak("At your service Master")
		
		#Asking contents in wikipedia
		elif "wikipedia" in query:
			from SearchNow import searchWikipedia
			searchWikipedia(query)

		#Seeing video in youtube
		elif "youtube" in query:
			from SearchNow import searchYoutube
			searchYoutube(query)

		#Sending email using voice
		elif "send email" in query:
			recognizer=sr.Recognizer()
			with sr.Microphone() as source:
				speak("Clearing Background noise..")
				recognizer.adjust_for_ambient_noise(source,duration=1)
				speak("Waiting for your message...")
				recordedaudio=recognizer.listen(source)
				speak("Done Recording..!")
			try:
				speak("Printing the message..")
				text=recognizer.recognize_google(recordedaudio,language='en-US')
				speak("your message:{}".format(text))

			except Exception as ex:
				print(ex)
			reciever='mohang124777@gmail.com'
			message=text
			sender=yagmail.SMTP('gokulrajnithyanandhan127@gmail.com')
			sender.send(to=reciever,subject='This is an automated mail',contents=message)
			speak("Your email is sent successfully")

		#latest news in various category (business,technology,sports,science,entertainment,health)
		elif "latest news" in query:
			from NewsRead import latestnews
			latestnews()

		#Temperature in chennai
		elif "temperature" in query:
			search = "temperature in chennai"
			url = f"https://www.google.com/search?q={search}"
			r  = requests.get(url)
			data = BeautifulSoup(r.text,"html.parser")
			temp = data.find("div", class_ = "BNeawe").text
			speak(f"current{search} is {temp}")

		#Weather in chennai
		elif "weather" in query:
			search = "temperature in chennai"
			url = f"https://www.google.com/search?q={search}"
			r  = requests.get(url)
			data = BeautifulSoup(r.text,"html.parser")
			temp = data.find("div", class_ = "BNeawe").text
			speak(f"current{search} is {temp}")

		#Playing a game (stone,paper,scissors)
		elif "play a game" in query:
			from game import game_play
			game_play() 

		#Opening facebook
		elif "open facebook" in query:
			webbrowser.open("www.facebook.com")

		#opening chrome
		elif 'open chrome' in query:
			speak("Sir, what should I search on chrome")
			cm =takeCommand().lower()
			webbrowser.open(f"{cm}")

		#Opening the stack overflow
		elif 'open stackoverflow' in query or 'overflow' in query:
			speak("Here you go to Stack Over flow.Happy coding")
			webbrowser.open("stackoverflow.com")

		#Playing Music in local folder
		elif 'play music' in query or "play song" in query:
			speak("Here you go with music")
			music_dir = "C:\\Users\\Gokul raj\\Music"
			songs = os.listdir(music_dir)
			print(songs)
			random = os.startfile(os.path.join(music_dir, songs[1]))

		#telling the time
		elif 'the time' in query:
			strTime = datetime.datetime.now().strftime("%H:%M")
			speak(f"Sir, the time is {strTime}")

		#Stopping the youtube video
		elif "stop" in query:
			pyautogui.press("k")
			speak("video paused")

		#Playing songs in Youtube
		elif "play" in query:
			pyautogui.press("k")
			speak("video played")

		#Full screen enabled in youtube	
		elif "full kscreen" in query:
			pyautogui.press("f")
			speak("Full screen enabled")

		#Open code
		elif 'open code' in query:
			codePath = r"C:\\Users\\Gokul raj\\Microsoft VS Code\\Code.exe"
			os.startfile(codePath)

		#telling Jokes
		elif 'joke' in query:
			speak(pyjokes.get_joke())

		#Telling your ip address
		elif "ip address" in query:
			ip= get('https://api.ipify.org').text
			print(f"your IP address is {ip}")
			speak(f"your IP address is {ip}")
	
		#voice calculator
		elif "calculate" in query:
			r = sr.Recognizer()
			with sr.Microphone() as source:
				speak("Say what you want to calculate ")
				print("Listening....")
				r.adjust_for_ambient_noise(source)
				audio = r.listen(source)
			my_string=r.recognize_google(audio)
			print(my_string)
			def get_operator_fn(op):
				return {
					'+' : operator.add, #plus
					'-' : operator.sub, #minus
					'x' : operator.mul, #multiplied
					'divided by' : operator.__truediv__, #divided
				}[op]
			def eval_binary_expr(op1,oper,op2):
				op1,op2 = int(op1), int(op2)
				return get_operator_fn(oper)(op1,op2)
			speak("Your result is")
			speak(eval_binary_expr(*(my_string.split())))

		#searching on google:1
		elif 'search' in query or 'play' in query:
			query = query.replace("search", "")
			query = query.replace("play", "")		
			webbrowser.open(query)

		#opening whatsapp and send message
		elif "whatsapp" in query:
			from Whatsapp import sendMessage
			sendMessage()

		#checking internet speed
		elif "internet speed" in query:
			wifi  = speedtest.Speedtest()
			upload_net = wifi.upload()/1048576
			download_net = wifi.download()/1048576
			print("Wifi Upload Speed is", upload_net)
			print("Wifi download speed is ",download_net)
			speak(f"Wifi download speed is {download_net}")
			speak(f"Wifi Upload speed is {upload_net}")

		#changing Background
		elif 'change background' in query:
			ctypes.windll.user32.SystemParametersInfoW(20,0,"Location of wallpaper",0)
			speak("Background changed successfully")

		#screenshoot function
		elif "screenshot" in query:
			import pyautogui
			im = pyautogui.screenshot()
			im.save("ss.jpg")

		#Searching in google:2
		elif "what is" in query or "who is" in query:
			client = wolframalpha.Client("WRPK8A-AHKGG5HA9L")
			res = client.query(query)
			try:
				print (next(res.results).text)
				speak (next(res.results).text)
			except StopIteration:
				speak("No results")

		#Lock window
		elif 'lock window' in query:
			speak("locking the device")
			ctypes.windll.user32.LockWorkStation()

		#deleting recycle bin
		elif 'delete recycle bin' in query:
			winshell.recycle_bin().empty(confirm = False, show_progress = False, sound = True)
			speak("Recycle Bin Recycled")

		#Taking a photo
		elif "camera" in query:
			pyautogui.press("super")
			pyautogui.typewrite("camera")
			pyautogui.press("enter")
			pyautogui.sleep(2)
			speak("SMILE")
			pyautogui.press("enter")

		#Creating a note function	
		elif "write a note" in query:
			speak("What should i write, sir")
			note = takeCommand()
			file = open('jarvis.txt', 'w')
			speak("Sir, Should i include date and time")
			snfm = takeCommand()
			if 'yes' in snfm or 'sure' in snfm:
				strTime = datetime.datetime.now().strftime("% H:% M:% S")
				file.write(strTime)
				file.write(" :- ")
				file.write(note)
			else:
				file.write(note)
		
		#showning notes
		elif "show note" in query:
			speak("Showing Notes")
			file = open("jarvis.txt","r")
			print(file.read())
			speak(file.read(6))

		#opening any app using pyautogui
		elif "open" in query:
			query = query.replace("open","")
			query = query.replace("jarvis","")
			pyautogui.press("super")
			pyautogui.typewrite(query)
			pyautogui.sleep(2)
			pyautogui.press("enter")
		
		#translate function
		elif "translate" in query:
			from Translator import translategl
			query = query.replace("jarvis","")
			query = query.replace("translate","")
			translategl(query)

		#Volume down function
		elif "volume up" in query:
			from keyboard import volumeup
			speak("Turning volume up,sir")
			volumeup()

		#Volume down function
		elif "volume down" in query:
			from keyboard import volumedown
			speak("Turning volume down, sir")
			volumedown()
		
		#closing the program
		elif 'exit' in query:
			speak("Thanks for giving me your time")
			exit()
