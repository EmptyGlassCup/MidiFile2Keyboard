import time, pyautogui

def makeSheet(mid):
    class Note:
        def __init__(self, type, value, time):
            self.type = type # 'note_on' or 'note_off'
            self.value = value # 'the number value for the note'
            self.time = time

    sheetMusic = []

    for msg in mid:
        if not msg.is_meta:
            sheetMusic.append(Note(msg.type, str(msg.note), msg.time)) # msg.note into string as json file only takes srings as keys
    
    return(sheetMusic)

def play(sheetMusic, mapping):

    for note in sheetMusic:
        time.sleep(note.time)

        if note.type == 'note_on':
            pyautogui.keyDown(mapping[note.value])
            print(mapping[note.value])
        if note.type == 'note_off':
            pyautogui.keyUp(mapping[note.value])
