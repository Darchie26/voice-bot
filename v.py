import webbrowser
import speech_recognition as sr
import time
import webbrowser

r = sr.Recognizer()

def record_audio(ask = False):

    with sr.Microphone() as source:
        if ask:
          print(ask)
        

        audio = r.listen(source)
        voice_data = ''
    try:
        voice_data = r.recognize_google(audio)
        print(voice_data)
    except sr.UnknownValueError:
            print('Sorry, I did not get that')
    except sr.RequestError:
            print('Sorry, my speech service is down')
    return voice_data


def respond(voice_data):
  if 'what is your name' in voice_data:
      print('My name is Curtis')
  if 'What time is it' in voice_data:
    print(time.ctime())
  if 'search' in voice_data:
      search = record_audio('What do you want to search for?')
      url = 'https://google.com/search?q=' + search
      webbrowser.get().open(url)
      print('Here what I found for' + search)

print('How can I help you?')
voice_data = record_audio()
respond(voice_data)