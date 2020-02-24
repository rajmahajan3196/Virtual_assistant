from gtts import gTTS
import speech_recognition as sr
import os
import webbrowser
import smtplib
import sys
import datetime
from playsound import playsound


def talkToMe(audio):
    print(audio)
    tts = gTTS(text=audio, lang='en-us')
    tts.save('audio.mp3')
    # os.system('mpg321 audio.mp3')
    playsound('audio.mp3')

# listens


def myCommand():

    r = sr.Recognizer()

    with sr.Microphone() as source:
        print('_Proton command listerner active_')
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)

    try:
        command = r.recognize_google(audio)
        print('You said: ' + command + '/n')
        return command

    except sr.UnknownValueError:
        couldntUnderstand()
    command = 'False'
    return command


def couldntUnderstand():
    print('Please speak')


def assistant(command):
    if 'False' in command:
        assistant(myCommand())

    if 'search Google' in command:
        talkToMe('Okay!')
        command = command.split(" ")
        location = command[2]
        url = 'https://www.google.com/search?q='+location
        webbrowser.get('/usr/bin/google-chrome --no-sandbox %s').open_new(url)

    if 'hello' in command:
        talkToMe('Hello Sir')

    if 'bye' in command:
        talkToMe('You cant shut me like that!')

    if 'what is today\'s date' in command:
        time = datetime.datetime.now()
        year = str(time.year)
        month = str(time.strftime("%B"))
        day = str(time.day)
        talkToMe("Today's date is " + day + " of " + month + " "+year)

    if 'weather' in command or 'how is today\'s weather' in command or 'what is today\'s weather' in command:
        talkToMe('You can google that..')

    if "where is" in command:
        command = command.split(" ")
        if command[3] is None:
            location = command[2]
        else:
            location = command[2]+' '+command[3]+' '+command[4]
        talkToMe("Hold on, I will show you where " + location + " is.")
        url = 'https://www.google.nl/maps/place/'+location
        chrome_path = '/usr/bin/google-chrome --no-sandbox %s'
        webbrowser.get(chrome_path).open(url)

    if "email" in command:
        talkToMe(' To whom? ')
        recipient = myCommand()

        if 'Dev' in recipient:
            talkToMe('What is the subject?')
            subject = myCommand()
            talkToMe('What should I say?')
            body = myCommand()
            body = body + '\n \n \n \n \n \n \n' + 'Send by Proton, Raj\'s virtual assistant'
            message = 'To: {}\r\nSubject: {}\r\n\r\n{}'.format(
                'mahajandev68@gmail.com', subject, body)
            smtp = smtplib.SMTP('smtp.gmail.com', 587)
            smtp.ehlo()
            smtp.starttls()
            smtp.login('protonassistant@gmail.com', 'protonraj123')
            smtp.sendmail('protonassistant@gmail.com', [
                          'mahajandev68@gmail.com', ''], message)
            smtp.quit()
            talkToMe('Email Sent')

        if 'Raj' or 'myself' in recipient:
            talkToMe('What is the subject?')
            subject = myCommand()
            talkToMe('What should I say?')
            body = myCommand()
            body = body + '\n \n \n \n \n \n \n' + 'Send by Proton, Raj\'s virtual assistant'
            message = 'To: {}\r\nSubject: {}\r\n\r\n{}'.format(
                'rajmj3113@gmail.com', subject, body)
            smtp = smtplib.SMTP('smtp.gmail.com', 587)
            smtp.ehlo()
            smtp.starttls()
            smtp.login('protonassistant@gmail.com', 'protonraj123')
            smtp.sendmail('protonassistant@gmail.com', [
                          'rajmj3113@gmail.com', ''], message)
            smtp.quit()
            talkToMe('Email Sent')


talkToMe('Hello Sir, What would you like to do today?')

while True:
    assistant(myCommand())
