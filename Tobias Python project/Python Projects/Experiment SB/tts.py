import pyttsx3


class TextToSpeech:
    def __init__(self):
        self.engine = pyttsx3.init()

    def speak(self, message, rate = 150):
        self.engine.stop()
        self.engine.setProperty('rate', rate)
        self.engine.say(message)
        self.engine.runAndWait()


#engine = init()
#engine.say(text)
#engine.runAndWait()


#engine: String ID of the engine
#rate: Integer speech rate in words per minute
#volume: Floating point volume of speech in the range [0.0, 1.0]