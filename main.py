import pyttsx3 as p
import pywhatkit
import speech_recognition as sr


listener = sr.Recognizer()
engine = p.init()
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source:
            print("listening...")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if "bot" in command:
                command = command.replace("bot", "")
                print(command)

    except:
        pass
    return command


def run_bot():
    command = take_command()
    print(command)
    if "play" in command:
        song = command.replace("play", "")
        talk("playing"+song)
        pywhatkit.playonyt(song)
    elif "Hi" and "bot" in command:
        talk("Hi sir what song do you want to listen")
    else:
        talk("sorry i cant hear you")

while True:
    run_bot()

