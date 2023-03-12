import speech_recognition as aa
import pyttsx3

listener = aa.Recognizer()

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('rate', 150)
engine.setProperty('voice', "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\MSTTS_V110_enCA_LindaM")
engine.say('The quick brown fox jumped over the lazy dog.')
engine.runAndWait()

def talk(text):
    engine.say(text)
    engine.runAndWait()

def input_instruction():
    global instruction
    try:
        with aa.Microphone() as origin:
            print("listening")
            speech = listener.listen(origin)
            instruction = listener.recognize_google(speech)
            instruction = instruction.lower()
            if"athena" in instruction:
                instruction = instruction.replace('athena', '')
            else:
                instruction = ""
                   
            

    except:
        pass
    return instruction

def play_Athena():

    instruction = input_instruction()
    print(instruction)
    if'how are you' in instruction:
        talk("I'm good!")
        print("ok")
  
while 1:
    play_Athena()
    instruction = ""
