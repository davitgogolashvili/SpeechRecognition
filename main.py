
import speech_recognition as sr
import os
import sys
import webbrowser

def talk(words):
	print(words)
	os.system("say " + words)


talk("გამარჯობა მე ვარ დავითი")


def command():
	r = sr.Recognizer()


	with sr.Microphone() as source:
		print("ისაუბრეთ")
		r.pause_threshold = 1

		r.adjust_for_ambient_noise(source, duration=1)

		audio = r.listen(source)

	try:

		zadanie = r.recognize_google(audio, language="ka_Ge").lower()

		print("თქვენ თქვით: " + zadanie)

	except sr.UnknownValueError:

		talk("ვერ გავიგე")
		zadanie = command()

	return zadanie

def makeSomething(zadanie):

	if 'საიტის გახსნა' in zadanie:

		talk("უკვე ვხსნი")

		url = 'https://mws.ge'

		webbrowser.open(url)

	elif 'გაჩერდი' in zadanie:

		talk("ახლავე")

		sys.exit()

	elif 'სახელი' in zadanie:
		talk("მე მქვია პროგრამა")


while True:
	makeSomething(command())