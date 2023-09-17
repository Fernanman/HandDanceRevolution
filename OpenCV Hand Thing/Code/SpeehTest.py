import speech_recognition as sr
from time import sleep

r = sr.Recognizer()

with sr.Microphone() as source:
    # print("Say something")
    # sleep(0.5)
    # try:
    #     audio = r.listen(source, 0.7)
    #     text = r.recognize_google(audio)
    #     print(text)
    # except:
    #     print("Something went wrong.")

    for i in range(1000):
        try:
            audio = r.listen(source, 0.7)
            text = r.recognize_google(audio)
            print(f"On second {i}, word was {text}")
        except:
            print(f"On second {i}, there was no text")