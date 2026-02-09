import time, pydirectinput, mido

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
    time.sleep(5)

    for note in sheetMusic:
        time.sleep(note.time)

        if note.type == 'note_on':
            pydirectinput.keyDown(mapping[note.value])
            print(mapping[note.value])
        if note.type == 'note_off':
            pydirectinput.keyUp(mapping[note.value])
