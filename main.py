import mido, pyautogui, time, json

def main():
    tst = 'TestMiddleC.mid'
    mid = mido.MidiFile(tst)

    with open('mapping.json', 'r') as file:
        data = file.read()

    mapping = json.loads(data)

    sheetMusic = makeSheet(mid)
    play(sheetMusic, mapping)
    

def makeSheet(mid):
    class Note:
        def __init__(self, type, note_no, time):
            self.type = type # 'note_on' or 'note_off'
            self.note_no = note_no # 'the number value for the note'
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
            pyautogui.keyDown(mapping[note.note_no])
        if note.type == 'note_off':
            pyautogui.keyUp(mapping[note.note_no])

main()