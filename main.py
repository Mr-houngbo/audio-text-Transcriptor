#!/usr/bin/env python
#_______________________________Transcription de texte en audio_________________________

import pyttsx3
import PyPDF2

droid=pyttsx3.init()
voices=droid.getProperty("voices")
rate=droid.getProperty("rate")
droid.setProperty("voice",voices[1].id)
droid.setProperty("rate",rate-10)
droid.say("Hello ! My name is Gord , a droid of the third generation programmed by raoul")


"""livre=open("doc.pdf","rb")
lecture=PyPDF2.PdfReader(livre)
debutlecture=lecture.pages[0]
texte=debutlecture.extract_text()
droid.say(texte)
droid.runAndWait()
"""


#________________________Transcription d'audio en texte__________________________
"""
import pyaudio 
import speech_recognition as sr
r=sr.Recognizer()
with sr.Microphone() as source:
    print("Parlez maintenant...")
    audio=r.listen(source)
try:
    text=r.recognize_sphinx(audio,language='fr-FR',acoustic_parameters='path',language_model='path')
    print("Vous avez dit : " + text)
except sr.UnknownValueError:
    print("Je n'arrive pas a comprendre ce que vous avez dit")
except sr.RequestError as e:
    print("Erreur de connexion .... : {0}".format(e))
    """