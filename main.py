import random
import ctypes
import time
import os


def change():
    print("Successfully done.")
    path = os.path.split(os.path.realpath(__file__))[0]+"/data"
    file = os.listdir(path)  # open the file directory of storaged img files.
    while True:
        # open the file directory of storaged img files.
        file = os.listdir(path)
        # random choices any picture path.
        filepath = path + "\\" + random.choice(file)
        print(filepath)
        ctypes.windll.user32.SystemParametersInfoW(
            20, 0, filepath, 0)  # set the desk wallpaper.
        time.sleep(30 * 60)  # switch once every hour.


if __name__ == "__main__":
    change()
