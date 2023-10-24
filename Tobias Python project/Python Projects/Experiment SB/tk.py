import tkinter as tk
import pyttsx3

class Tkframe:
    def __init__(self):
        self.engine = pyttsx3.init()

        self.saving = False

        self.window = tk.Tk()
        self.window.geometry('325x225')
        self.window.configure(bg='#0D1117')
        self.window.title("Voice Player")

        self.to_say_label = tk.Label(self.window, text="Enter Text to Speak:", bg='#0D1117', fg='white')
        self.to_say = tk.Entry(self.window, width=50)
        self.rate_label = tk.Label(self.window, text="Speech Rate (words per minute):", bg='#0D1117', fg='white')
        self.rate = tk.Entry(self.window, width=10)
        self.button = tk.Button(self.window, text="Speak", bg='white', width=10, height=2, command=self.speak)
        self.save_button = tk.Button(self.window, text="Save", bg='white',width=10,height=2, command=self.save_to_file)

        self.to_say_label.grid(row=0, column=0, pady=10, padx=10, columnspan=2)
        self.to_say.grid(row=1, column=0, padx=10, columnspan=2)
        self.rate_label.grid(row=2, column=0, padx=10, pady=5, columnspan=2)
        self.rate.grid(row=3, column=0, columnspan=2)
        self.button.grid(row=4, column=0, columnspan=1, padx= 30, pady=15)
        self.save_button.grid(row=4, column=1, pady=10, padx=0, sticky='w')

        self.voice_var = tk.StringVar()
        self.voice_dict = {}

        self.get_voices()

        self.window.bind("<Return>", self.speak)
        self.window.bind("<Shift-Return>", self.save_to_file)

        self.window.mainloop()

    def speak(self, event=None):
        self.set_voice(self.voice_var)
        to_say = self.to_say.get()

        try:
            rate = float(self.rate.get())
        except:
            rate = 200

        self.engine.setProperty('rate', rate)

        if not self.saving:
            self.engine.say(to_say)
            self.engine.runAndWait()

        else:
            filename = ""
            self.engine.save_to_file(to_say, f"saves//{to_say}.wav")
            self.engine.runAndWait()
            self.saving = False

    def get_voices(self):
        voices = self.engine.getProperty('voices')

        for voice in voices:
            voice_id = voice.id
            voice_name = voice.name
            self.voice_dict[voice_name] = voice_id

        self.voice_var.set(list(self.voice_dict.keys())[0])
        self.voice_menu = tk.OptionMenu(self.window, self.voice_var, *self.voice_dict.keys())
        self.voice_menu.grid(row=5, column=0, columnspan=2, pady=0)

    def set_voice(self, voice):
        nVoice = self.voice_dict[voice.get()]
        self.engine.setProperty('voice', nVoice)


    def save_to_file(self, event=None):
        self.saving = True
        self.speak()
