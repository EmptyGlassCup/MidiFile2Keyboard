import customtkinter, mido, json
from logic import play, makeSheet

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__() 

        # Decoration!
        self.title("Midi to Keyboard")
        self.geometry("400x150")

        # Widgets
        self.grid_columnconfigure(0, weight = 1) #Centres widgets

            #Main Header
        self.title_label = customtkinter.CTkLabel(self, text = "Midi To Keyboard", font = customtkinter.CTkFont(size = 20, weight = 'bold'))
        self.title_label.grid(row=0, column=0)

            #Sub Header
        self.sub_label = customtkinter.CTkLabel(self, text = "By EmptyCup", font = customtkinter.CTkFont(size = 17, weight = 'normal'))
        self.sub_label.grid(row=1, column=0)

            #Choose File button
        self.file_button = customtkinter.CTkButton(self, text="Choose File", command = self.file_select)
        self.file_button.grid(row = 2, column = 0, pady=10)

            #Playback Button
        self.play_button = customtkinter.CTkButton(self, text="Play", command=self.playback)
        self.play_button.grid(row = 3, column = 0)
    
    #Function for choosing a file
    def file_select(self):
        self.file = customtkinter.filedialog.askopenfilename(filetypes=[("Midi File", "*.mid")]) # Allows the user to choose a midi file
        print(self.file)
        
    # Function for playing back Keyboard Inputs
    def playback(self):

       # Preperation
        mid = mido.MidiFile(self.file) # Turn midi file into mido object

        with open('mapping.json', 'r') as file: #Read keymapping from json file
            data = file.read()
        mapping = json.loads(data) #turn read json into python dictionary

        # Playback
        sheet_music = makeSheet(mid)
        play(sheet_music, mapping)