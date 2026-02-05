import mido
import time

def main():
    tst = 'TestMiddleC.mid'
    mid = mido.MidiFile(tst)

    mapping = {
        "48" : 'C4',
        "52" : 'E4',
        "55" : 'G4',
        "60" : 'C5'
    }

    sheetMusic = makeSheet(mid)

    for note in sheetMusic:
        time.sleep(note.time)
        print(note.type)
    

def makeSheet(mid):
    class Note:
        def __init__(self, type, note, time):
            self.type = type # 'note_on' or 'note_off'
            self.note = note # 'the number value for the note'
            self.time = time

    sheetMusic = []

    for msg in mid:
        if not msg.is_meta:
            sheetMusic.append(Note(msg.type, msg.note, msg.time))
    
    return(sheetMusic)


main()