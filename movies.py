import random , subprocess
import webbrowser
import sys
import os
import time
import playsound
import speech_recognition as sr
from gtts import gTTS
#chromedir= "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
movie = [ 'The Lord of the Rings: The Fellowship of the Ring',
		  'The Sixth Sense','Saving Private Ryan','Titanic','Fargo','Toy Story',
		  'Forrest Gump','The Shawshank Redemption',
		  'Pulp Fiction','Schindler\'s List','Unforgiven','The Silence of the Lambs',
		  'Goodfellas','Dances with Wolves','Do the Right Thing',
		  'Platoon','Amadeus','Sophie\'s Choice','Blade Runner',
		  'Tootsie','E.T. the Extra-Terrestrial','Raiders of the Lost Ark'
		  'Raging Bull','Apocalypse Now','The Deer Hunter','Close Encounters of the Third Kind',
		  'Annie Hall','Star Wars','All the President\'s Men','Rocky',
		  'Network','Taxi Driver','Nashville','Jaws','One Flew Over the Cuckoo\'s Nest',
		  'The Godfather Part II','Chinatown','American Graffiti','Cabaret',
		  'The Godfather','The Last Picture Show','The French Connection',
		  'A Clockwork Orange','Patton','MASH',
		  'Easy Rider','The Wild Bunch','Butch Cassidy and the Sundance Kid',
		  'Midnight Cowboy','2001: A Space Odyssey','In the Heat of the Night',
		  'Guess Who\'s Coming to Dinner','Bonnie and Clyde']
def speak(text):
	number = random.randint(0, 1000)
	tts = gTTS(text=text, slow=False)
	filename = str(number)+".mp3"
	tts.save(filename)
	playsound.playsound(filename)
	os.remove(filename)
speak('Count of films: {0}'.format(len(movie)))
print('Count of films: {0}'.format(len(movie)))
input("Press Enter if you want to pick a movie...")
watch = random.choice(movie)
speak("Do you wanna watch"+watch+"?")
print(watch)
number = 'Yes'
otricanie = 'No'
exit = 'end'
running = True
while running:
	guess = input('Would you like to watch this movie? (Yes/No, end if want to exit) : ')
	if guess == number:
		speak("Here we go!")
		webbrowser.open_new_tab('https://www.google.com/search?q='+watch+' watch free')
		running = False # это останавливает цикл while
	elif guess == otricanie:
		random.shuffle(movie)
		watch = random.choice(movie)
		speak("Maybe"+watch+"?")
		print(watch)
	elif guess == exit:
		running = False