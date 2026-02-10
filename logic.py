import time
import pydirectinput
pydirectinput.PAUSE = 0 #Disables pause for pydirectinput to preserve timing accuracy

class Note:
    def __init__(self, type, value, time):
        self.type = type # 'note_on' or 'note_off'
        self.value = value # 'the number value for the note'
        self.time = time

def makeSheet(mid):

    sheet_music = []

    for msg in mid:
        if not msg.is_meta:
            sheet_music.append(Note(msg.type, str(msg.note), msg.time)) # msg.note into string as json file only takes srings as keys
    
    return(sheet_music)

def play(sheet_music, mapping, thread_event):

    time.sleep(5) #Gives user time to switch to program/game

    for note in sheet_music:
        if thread_event.is_set(): # If it is already playing, stop playing.
            break

        time.sleep(note.time)

        if note.type == 'note_on' and note.value in mapping:
            pydirectinput.keyDown(mapping[note.value])
        if note.type == 'note_off' and note.value in mapping:
            pydirectinput.keyUp(mapping[note.value])
