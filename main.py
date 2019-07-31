import threading
from threading import Thread
import apimethod
from flask import flash

def monitor(webhookurl, handles):

	#creates array from the string inputted by the user
	#this allows each handle to be sent to a different thread
	handles = handles.split(" ")

	#TREADING IS WORKING!
	i = 0
	numthreads = str(len(handles))
	flash(numthreads + " processes starting!")

	def worker():
		apimethod.run(chosenhandle = str(handles[i]), url = webhookurl)
		#chosenhandle = str(handles[i])
		#print("Monitoring @" + chosenhandle)

	while i <= len(handles) - 1:
	  t = Thread(target=worker)
	  t.start()
	  i = i + 1

	flash("All processes started!")
