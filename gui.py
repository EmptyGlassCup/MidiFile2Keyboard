import customtkinter
import mido
import json
import threading
from logic import play, makeSheet

# GUI Appearance
customtkinter.set_appearance_mode("Dark")
customtkinter.set_default_color_theme("blue")


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__() 

        # Setup
        self.title("Midi to Keyboard")
        self.geometry("500x200")
        self.resizable(False, False) # Disables Full Screen

        self.song_chosen = False

        self.playing = False
        self.stop_event = threading.Event()

        # Frame configuration
            # Frame for buttons
        self.interactive_frame = customtkinter.CTkFrame(self)
        self.interactive_frame.grid(row = 2, column = 0, sticky = 'ew', padx = 20, pady=(10, 5))
        self.interactive_frame.grid_columnconfigure(0, weight=1)
        self.interactive_frame.grid_columnconfigure(3, weight=1)
            # Frame for info
        self.info_frame = customtkinter.CTkFrame(self)
        self.info_frame.grid(row = 3, column = 0, sticky = 'ew', padx = 20)


        self.grid_columnconfigure(0, weight = 1) #Centres widgets on Window
        #Widgets on Window
                #Main Header
        self.title_label = customtkinter.CTkLabel(self, text = "Midi To Keyboard", font = customtkinter.CTkFont(size = 20, weight = 'bold'))
        self.title_label.grid(row=0, column=0)

                #Sub Header
        self.sub_label = customtkinter.CTkLabel(self, text = "By EmptyCup", font = customtkinter.CTkFont(size = 17, weight = 'normal'))
        self.sub_label.grid(row=1, column=0)

        #Widgets in Interactive Frame
                #Choose File button
        self.file_button = customtkinter.CTkButton(self.interactive_frame, text="Choose File", command = self.file_select)
        self.file_button.grid(row = 0, column = 1, pady = 10, padx = 5)

                #Playback Button
        self.play_button = customtkinter.CTkButton(self.interactive_frame, text="Play", command=self.playback)
        self.play_button.grid(row = 0, column = 2)

        #Widgets in Information Frame
            # 'Current File: ' Text
        self.current_file = customtkinter.CTkLabel(self.info_frame, text = 'Current File: None')
        self.current_file.grid(row =0, column = 0, padx=(5,0))

            #Text for Countdown
        self.countdown = customtkinter.CTkLabel(self.info_frame, text = '')
        self.countdown.grid(row=1, column = 0, sticky = 'w', padx=(5,0))

    #Functions    
        #Function for choosing a file
    def file_select(self):
        self.file = customtkinter.filedialog.askopenfilename(filetypes=[("Midi File", "*.mid")]) # Allows the user to choose a midi file
        if self.file == '': #If the user exits the file explorer window
            self.current_file.configure(text = 'Current File: None')
        else:
            self.current_file.configure(text = f"Current File: {self.file}")
            self.song_chosen = True

        
        # Function for playing back Keyboard Inputs
    def playback(self):

        if self.song_chosen:  #Has a file been chosen by the user?
            if not self.playing:
                #Preperation
                mid = mido.MidiFile(self.file) # Turn midi file into mido object

                with open('mapping.json', 'r') as file: # Default is Heartopia Mapping
                    data = file.read()
                mapping = json.loads(data) #turn read json into python dictionary

                # Modify playing information
                self.playing = True
                self.play_button.configure(text = "Stop") 
                self.stop_event.clear() # Allows playback thread to run
                self.countdown.configure(text = "Starting in 5 seconds. [Switch to your desired program!]")

                # Playback
                sheet_music = makeSheet(mid)

                thread = threading.Thread(target = play, args=(sheet_music, mapping, self.stop_event), daemon=True)
                thread.start()
 
            else:
                self.playing = False
                self.play_button.configure(text = "Play")
                self.countdown.configure(text = '')
                self.stop_event.set() #Stops playback
        else:
            self.current_file.configure(text = "Current File: NO FILE CHOSEN")