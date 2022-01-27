import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer()

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty("voice", voices[1].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()

def takeCommand():
    try:
        with sr.Microphone(device_index=0) as source:
            listener.adjust_for_ambient_noise(source, duration=1)
            print("Listening...")
            talk("listening")

            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            print(command)

            command = command.replace("alexa", " ")

            # if "alexa" in command:
            #     command = command.replace("alexa", "")
            # else:
            #     command = "This is an invalid command"
            #     talk("This is an invalid command")
    except:
        command = "can't connect to microphone"
    return command;

def runAlexa():
    command = takeCommand();
    print(command)
    if "time" in command:
        time = datetime.datetime.now().strftime("%I:%M %p")
        print("The current time is " + time)
        talk("The current time is " + time)
    elif "play" in command:
        song = command.replace("play", " ")
        talk("Playing " + song )
        pywhatkit.playonyt(song)
    elif "who is" in command:
        story = command.replace("who is", " ")
        try:
            info = wikipedia.summary(story)
            print(info)
            talk(info)
        except:

            talk("sorry we couldn't find your search")
    elif "joke" in command:
        joke = pyjokes.get_joke()
        print(joke)
        talk(joke)

    else:
        talk("say that command again")

while True:
    runAlexa()