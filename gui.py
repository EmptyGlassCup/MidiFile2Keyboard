import customtkinter, mido, json
from logic import play, makeSheet

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # Decor
        self.title("Midi to Keyboard")
        self.geometry("400x150")
        self.grid_columnconfigure((0, 1), weight=1)

        #UI elements
        self.button = customtkinter.CTkButton(self, text="Play", command=self.playback)
        self.button.grid(row = 0, column = 0, padx = 0, pady = 0)
        
    def playback(self):
        # Prep
        tst = "TestMiddleC.mid"
        mid = mido.MidiFile(tst)

        with open('mapping.json', 'r') as file: #Read keymapping from json file
            data = file.read()

        mapping = json.loads(data) #turn read json into python dictionary


        sheetMusic = makeSheet(mid)
        play(sheetMusic, mapping)