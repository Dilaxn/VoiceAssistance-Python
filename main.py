import pyttsx3
import speech_recognition as sr

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
# voiceFemales = filter(lambda v: v.gender == 'VoiceGenderFemale', voices)
# for v in voiceFemales:
#     engine.setProperty('voice', v.id)
#     print(v.id)
#     engine.say('Good Afternoon from ' + v.name)
#     engine.runAndWait()

def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print("listening....")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            print(command)
            command = command.lower()
            if 'jarvis' and 'password' and '5738' in command:
                # command = command.replace('jarvis', '')
                talk("You have a access What kind of help do you want")
                voice = listener.listen(source)
                command1 = listener.recognize_google(voice)
                if 'memory' in command1:
                    talk("your last memory is Artificial Intelligence")
                command = "This is your secret"
                print(command)
            elif 'jarvis' and 'password' in command:
                command = "Your Password is wrong"
                print(command)
            else:
                command = "I cannot hear you"


    except:
        pass
    return command


def run_jarvis():
    command = take_command()
    talk(command)


run_jarvis()
