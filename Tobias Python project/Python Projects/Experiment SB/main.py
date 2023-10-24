from tk import Tkframe
import keyboard

if __name__ == "__main__":
    tkframe = Tkframe()

    if keyboard.is_pressed('enter'):
        tkframe.speak()
