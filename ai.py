import pyttsx3
import speech_recognition as sr

class AI():
    __name = ""
    __skill = []

    def __init__(self, name=None):
        self.engine = pyttsx3.init()

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
        self.__name = value

    def say(self, sentence):
        self.engine.say(sentence)
        self.engine.runAndWait()
   
    def elasticListen(self):
        print("listening")
        with self.m as source:
            self.r.adjust_for_ambient_noise(source)
            try:
                audio = self.r.listen(source,timeout=5)
            except:
                return
            print('Audio received')

        try:
            dataDict = self.r.recognize_google(audio, show_all=True, language="en_US")
            if dataDict is not None:
                dataList = dataDict.get('alternative')
                print("listen successful")
                return dataList #list of all alternatives
        except: 
            pass

    def listen(self):
        print("listening")
        with self.m as source:
            self.r.adjust_for_ambient_noise(source)
            try:
                audio = self.r.listen(source, timeout=5)
            except:
                return
            print('Audio received')

        try:
            phrase = self.r.recognize_google(audio, show_all=False, language="en_US")
            if phrase is not None:
                print("listen successful")
                phrase = phrase.lower()
                return phrase
        except:
            pass
            
    
    
            
