from pygame import mixer

# Initialize the mixer
mixer.init()

# Load the audio file
mixer.music.load("TextToSpeech.wav")

mixer.init(devicename='CABLE Input (VB-Audio Virtual Cable)') #Initialize it with the correct deviceREVENT + 8)

# Play the audio
mixer.music.play()

# Wait for the audio to finish
while mixer.music.get_busy():
    pass

# Quit the mixer
mixer.quit()