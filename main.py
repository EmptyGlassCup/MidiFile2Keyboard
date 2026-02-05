import mido
import time

def main():
    tst = 'TestMiddleC.mid'
    mid = mido.MidiFile(tst)

    for msg in mid:
        time.sleep(msg.time)
        if not msg.is_meta:
            print(msg)