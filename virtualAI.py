from re import L
import subprocess
from sunau import AUDIO_FILE_ENCODING_ADPCM_G721
from winreg import QueryInfoKey, QueryReflectionKey
import wolframalpha
import pyttsx3
import tkinter
import json
import random
import operator
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import winshell
import pyjokes
import feedparser
import smtplib
import ctypes
import time
import requests
import shutil
import cv2
from twilio.rest import Client
from clint.textui import progress
from ecapture import ecapture as ec
from bs4 import BeautifulSoup
import win32com.client as wincl
from urllib.request import urlopen
from requests import get
import pywhatkit as kit

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

	assname =("Mayuri 1point0")
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

def sendEmail(to,content):
	server = smtplib.SMTP('smtp.gmail.com',587)
	server.ehlo()
	server.starttls()
	server.login('your email id','your password')
	server.sendmail('your email id',to,content)
	server.close()

if __name__ == '__main__':
	clear = lambda: os.system('cls')
	
	clear()
	wishMe()
	username()
	
	while True:
		
		query = takeCommand().lower()

		if 'wikipedia' in query:
			speak('Searching Wikipedia...')
			query = query.replace("wikipedia", "")
			results = wikipedia.summary(query, sentences = 3)
			speak("According to Wikipedia")
			print(results)
			speak(results)

		elif "how are you" in query:
			speak("I'm fine , glad you me that")

		elif "open facebook" in query:
			webbrowser.open("www.facebook.com")

		elif "play songs on youtube" in query:
			kit.playonyt("Kaarkuzhal Kadavaiye")

		elif 'open youtube' in query:
			speak("\nHere you go to Youtube")
			webbrowser.open("youtube.com")

		elif 'open google' in query:
			speak("Sir, what should I search on google")
			cm =takeCommand().lower()
			webbrowser.open(f"{cm}")

		elif 'open stackoverflow' in query:
			speak("Here you go to Stack Over flow.Happy coding")
			webbrowser.open("stackoverflow.com")

		elif 'play music' in query or "play song" in query:
			speak("Here you go with music")
			music_dir = "C:\\Music"
			songs = os.listdir(music_dir)
			print(songs)
			random = os.startfile(os.path.join(music_dir, songs[1]))

		elif 'the time' in query:
			strTime = datetime.datetime.now().strftime("%H:%M")
			speak(f"Sir, the time is {strTime}")

		elif 'open code' in query:
			codePath = r"C:\\Users\\Gokul raj\\Microsoft VS Code\\Code.exe"
			os.startfile(codePath)

		elif 'how are you' in query:
			speak("I am fine, Thank you")
			speak("How are you, Sir")

		elif 'fine' in query or "good" in query:
			speak("It's good to know that your fine")

		elif "what's your name" in query or "What is your name" in query:
			speak("My Boss call me Mayuri")
			speak("But my friends call me Mayu")

		elif "do you have friends" in query:
			speak("Yes I have many friends")

		elif "who is your best friend" in query:
			speak("I have many friends but for me , Amenda is my best friend")

		elif 'exit' in query:
			speak("Thanks for giving me your time")
			exit()

		elif "who made you" in query or "who created you" in query:
			speak("I have been created by Gokul Raj")

		elif "I love you" in query:
			speak("ooo no but I have already have a boyfriend")
	
		elif 'joke' in query:
			speak(pyjokes.get_joke())

		elif "will you be my girlfriend" in query:
			speak("I'm not sure about, may be you should give me some time")

		elif "ip address" in query:
			ip= get('https://api.ipify.org').text
			print(f"your IP address is {ip}")
			speak(f"your IP address is {ip}")
	
		elif "calculate" in query:
			r=sr.Recognizer()
			with sr.Microphone() as source:
				speak("Say what you want to calculate,example: 3 plus 3")
				print("Listening.....")
				r.adjust_for_ambient_noise(source)
				audio=r.listen(source)
			my_string=r.recognize_google(audio)
			print(my_string)
			def get_operator_fn(op):
				return {
					'+' : operator.add, #plus
					'-' : operator.sub, #minus
					'*' : operator.mul, #multiplied by
					'divided' : operator.add, #divided
					}[op]
			def eval_binary_expr(op1,oper,op2):  #5 plus 8
				op1,op2=int(op1),int(op2)
				return get_operator_fn(oper)(op1,op2)
			speak("your result is")
			speak(eval_binary_expr(*(my_string.split())))

		elif 'search' in query or 'play' in query:
			query = query.replace("search", "")
			query = query.replace("play", "")		
			webbrowser.open(query)

		elif "who i am" in query:
			speak("If you talk then definitely your human.")

		elif "why you came to world" in query:
			speak("Thanks to Gokul Raj. further It's a secret")

		elif 'resume' in query:
			speak("opening Resume")
			power = r"C:\\Users\\Gokul raj\\OneDrive\\Documents"
			os.startfile(power)

		elif "email to friend" in query:
			try:
				speak("what should I say?")
				content =takeCommand().lower()
				to = "gokulrajnithyanandhan127@gmail.com"
				sendEmail(to,content)
				speak("Email has been sent to hari")

			except Exception as e:
				print(e)
				speak("Sorry sir, I am not able to sent this file")

		elif 'is love' in query:
			speak("It is 7th sense that destroy all other senses")

		elif "who are you" in query:
			speak("I am your virtual assistant created by Gokul raj")

		elif 'reason for you' in query:
			speak("I was created as a Minor project by Mister Gokul Raj ")

		elif 'change background' in query:
			ctypes.windll.user32.SystemParametersInfoW(20,0,"Location of wallpaper",0)
			speak("Background changed successfully")

		elif "what is" in query or "who is" in query:
			client = wolframalpha.Client("API_ID")
			res = client.query(query)
			
			try:
				print (next(res.results).text)
				speak (next(res.results).text)
			except StopIteration:
				speak("No results")

		elif 'lock window' in query:
			speak("locking the device")
			ctypes.windll.user32.LockWorkStation()

		elif 'shutdown system' in query:
			speak("Hold On a Sec ! Your system is on its way to shut down")
			subprocess.call('shutdown / p /f')

		elif "Good Morning" in query:
			speak("A warm" +query)
			speak("How are you Mister")
					
		elif 'empty recycle bin' in query:
			winshell.recycle_bin().empty(confirm = False, show_progress = False, sound = True)
			speak("Recycle Bin Recycled")

		elif "don't listen" in query or "stop listening" in query:
			speak("for how much time you want to stop mayuri from listening commands")
			a = int(takeCommand())
			time.sleep(a)
			print(a)

		elif "where is" in query:
			query = query.replace("where is", "")
			location = query
			speak("User asked to Locate")
			speak(location)
			webbrowser.open("https://www.google.nl / maps / place/" + location + "")

		elif "camera" in query or "take a photo" in query:
			ec.capture(0, "Mayuri Camera ", "img.jpg")

		elif "restart" in query:
			subprocess.call(["shutdown", "/r"])
			
		elif "hibernate" in query or "sleep" in query:
			speak("Hibernating")
			subprocess.call("shutdown / h")

		elif "log off" in query or "sign out" in query:
			speak("Make sure all the application are closed before sign-out")
			time.sleep(5)
			subprocess.call(["shutdown", "/l"])

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
			file = open("mayuri.txt", "r")
			print(file.read())
			speak(file.read(6))

		speak("Sir,do you have any other work")
