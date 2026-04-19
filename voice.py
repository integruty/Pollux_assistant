import speech_recognition as sr

r = sr.Recognizer()

def listen():
    with sr.Microphone() as source:
        audio = r.listen(source)
    try:
        return r.recognize_google(audio, language="ru-RU")
    except:
        return ""