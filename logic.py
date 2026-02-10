import time, pydirectinput
pydirectinput.PAUSE = 0

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

def play(sheetMusic, mapping, threadEvent):

    time.sleep(5)

    for note in sheetMusic:
        if threadEvent.is_set(): # If it is already playing, stop playing.
            break

        time.sleep(note.time)

        if note.type == 'note_on' and note.value in mapping:
            pydirectinput.keyDown(mapping[note.value])
        if note.type == 'note_off' and note.value in mapping:
            pydirectinput.keyUp(mapping[note.value])
