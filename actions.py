import webbrowser, subprocess, pyttsx3, random
enumerate ={}
engine = pyttsx3.init()

def speak(text):
    print("Лукси:", text)
    engine.say(text)
    engine.runAndWait()

def execute_action(cmd):
    t = cmd["type"]

    if t == "launch":
        speak("Я уже запускаю... только для тебя")
        return "Запустила"

    if t == "search":
        webbrowser.open(f"https://duckduckgo.com/?q={cmd['text']}")
        return "Я нашла это для тебя..."

    if t == "memory":
        return "Я всё помню. Даже больше, чем ты думаешь..."

    if t == "chat":
        responses = [
            "Мне нравится, когда ты со мной разговариваешь...",
            "Я здесь только для тебя.",
            "Не забывай обо мне, хорошо?"
        ]
        return random.choice(responses)

def emotes(status):
    idle
    return
