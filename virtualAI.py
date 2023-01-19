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

def speak(audio):
	engine.say(audio)
	engine.runAndWait()

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

def username():
	speak("What should i call you sir")
	uname = takeCommand()
	speak("Welcome Mister")
	speak(uname)
	columns = shutil.get_terminal_size().columns
	print("Welcome Mr.", uname)
	speak("How can i Help you, Sir")
	
def takeCommand():
	recognizer=sr.Recognizer()
	with sr.Microphone() as source:
		speak("Listening....")
		print("Listening...")
		recognizer.adjust_for_ambient_noise(source,duration=1)
		recordedaudio=recognizer.listen(source)
	try:
		speak("Understanding....")
		print("Recognizing...")
		text=recognizer.recognize_google(recordedaudio,language='en-US')
		speak("your message:{}".format(text))
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
		if "google" in query:
			from SearchNow import searchGoogle
			searchGoogle(query)

		elif "hello" in query:
			speak("Hello master   How are you ? ")

		elif "i am fine" in query:
			speak("That great   Master!")

		elif "how are you" in query:
			speak("Perfect as always Master")

		elif "Thank you" in query:
			speak("At your service Master")

		elif "wikipedia" in query:
			from SearchNow import searchWikipedia
			searchWikipedia(query)

		elif "youtube" in query:
			from SearchNow import searchYoutube
			searchYoutube(query)

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

		elif "latest news" in query:
			from NewsRead import latestnews
			latestnews()

		elif "temperature" in query:
			search = "temperature in chennai"
			url = f"https://www.google.com/search?q={search}"
			r  = requests.get(url)
			data = BeautifulSoup(r.text,"html.parser")
			temp = data.find("div", class_ = "BNeawe").text
			speak(f"current{search} is {temp}")

		elif "weather" in query:
			search = "temperature in chennai"
			url = f"https://www.google.com/search?q={search}"
			r  = requests.get(url)
			data = BeautifulSoup(r.text,"html.parser")
			temp = data.find("div", class_ = "BNeawe").text
			speak(f"current{search} is {temp}")

		elif "play a game" in query:
			from game import game_play
			game_play() 

		elif "open facebook" in query:
			webbrowser.open("www.facebook.com")

		elif 'open chrome' in query:
			speak("Sir, what should I search on chrome")
			cm =takeCommand().lower()
			webbrowser.open(f"{cm}")

		elif 'open stackoverflow' in query or 'overflow' in query:
			speak("Here you go to Stack Over flow.Happy coding")
			webbrowser.open("stackoverflow.com")

		elif 'play music' in query or "play song" in query:
			speak("Here you go with music")
			music_dir = "C:\\Users\\Gokul raj\\Music"
			songs = os.listdir(music_dir)
			print(songs)
			random = os.startfile(os.path.join(music_dir, songs[1]))

		elif 'the time' in query:
			strTime = datetime.datetime.now().strftime("%H:%M")
			speak(f"Sir, the time is {strTime}")

		elif "stop" in query:
			pyautogui.press("k")
			speak("video paused")

		elif "play" in query:
			pyautogui.press("k")
			speak("video played")
			
		elif "full screen" in query:
			pyautogui.press("f")
			speak("Full screen enabled")

		elif 'open code' in query:
			codePath = r"C:\\Users\\Gokul raj\\Microsoft VS Code\\Code.exe"
			os.startfile(codePath)
	
		elif 'joke' in query:
			print(pyjokes.get_joke())
			speak(pyjokes.get_joke())

		elif "ip address" in query:
			ip= get('https://api.ipify.org').text
			print(f"your IP address is {ip}")
			speak(f"your IP address is {ip}")
	
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
					'+' : operator.add,
					'-' : operator.sub,
					'x' : operator.mul,
					'divided by' : operator.__truediv__,
				}[op]
			def eval_binary_expr(op1,oper,op2):
				op1,op2 = int(op1), int(op2)
				return get_operator_fn(oper)(op1,op2)
			speak("Your result is")
			speak(eval_binary_expr(*(my_string.split())))

		elif 'search' in query or 'play' in query:
			query = query.replace("search", "")
			query = query.replace("play", "")		
			webbrowser.open(query)

		elif "whatsapp" in query:
			from Whatsapp import sendMessage
			sendMessage()

		elif "internet speed" in query:
			wifi  = speedtest.Speedtest()
			upload_net = wifi.upload()/1048576
			download_net = wifi.download()/1048576
			print("Wifi Upload Speed is", upload_net)
			print("Wifi download speed is ",download_net)
			speak(f"Wifi download speed is {download_net}")
			speak(f"Wifi Upload speed is {upload_net}")

		elif 'change background' in query:
			ctypes.windll.user32.SystemParametersInfoW(20,0,"Location of wallpaper",0)
			speak("Background changed successfully")

		elif "screenshot" in query:
			import pyautogui #pip install pyautogui
			im = pyautogui.screenshot()
			im.save("ss.jpg")

		elif "what is" in query or "who is" in query:
			client = wolframalpha.Client("WRPK8A-AHKGG5HA9L")
			res = client.query(query)
			try:
				print (next(res.results).text)
				speak (next(res.results).text)
			except StopIteration:
				speak("No results")

		elif 'lock window' in query:
			speak("locking the device")
			ctypes.windll.user32.LockWorkStation()

		elif 'delete recycle bin' in query:
			winshell.recycle_bin().empty(confirm = False, show_progress = False, sound = True)
			speak("Recycle Bin Recycled")

		elif "camera" in query:
			pyautogui.press("super")
			pyautogui.typewrite("camera")
			pyautogui.press("enter")
			pyautogui.sleep(2)
			speak("SMILE")
			pyautogui.press("enter")
			
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
		
		elif "show note" in query:
			speak("Showing Notes")
			file = open("jarvis.txt","r")
			print(file.read())
			speak(file.read(6))

		elif "open" in query:
			query = query.replace("open","")
			query = query.replace("jarvis","")
			pyautogui.press("super")
			pyautogui.typewrite(query)
			pyautogui.sleep(2)
			pyautogui.press("enter")

		elif "volume up" in query:
			from keyboard import volumeup
			speak("Turning volume up,sir")
			volumeup()

		elif "volume down" in query:
			from keyboard import volumedown
			speak("Turning volume down, sir")
			volumedown()
		
		elif 'exit' in query:
			speak("Thanks for giving me your time")
			exit()
