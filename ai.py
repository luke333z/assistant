import pyttsx3
import speech_recognition as sr

class AI():
    __name = ""
    __skill = []

    def __init__(self, name=None):
        self.engine = pyttsx3.init()
        voices = self.engine.getProperty('voices')
        self.engine.setProperty('voice', 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\MSTTS_V110_enCA_LindaM')
        self.r = sr.Recognizer()
        self.m = sr.Microphone()

        if name is not None:
            self.__name = name

        print("listening") 
        with self.m as source:
            self.r.adjust_for_ambient_noise(source)

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        sentence = "Hello, my name is" + self.__name
        self.__name = value
        self.engine.say(sentence)
        self.engine.runAndWait()

    def say(self, sentence):
        self.engine.say(sentence)
        self.engine.runAndWait()
   
    def listen(self):
        print("say something")
        with self.m as source:
            self.r.adjust_for_ambient_noise(source)
            try:
                audio = self.r.listen(source,timeout=5)
            except:
                return
            print('got it')
        try:
            print("okok")
            data = self.r.recognize_google(audio, show_all=True, language="en_US")
            if data is not None:
                data = data.get('alternative')
            print("listen successful")
            return data
        except:
            pass
    
    
            
