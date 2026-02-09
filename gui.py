import customtkinter

def button_callback():
    print("Button Pressed")

app = customtkinter.CTk()
app.title("Midi To Keyboard")
app.geometry("400x150")

button = customtkinter.CTkButton(app, text="My Button", command = button_callback)
button.grid(row = 0, column = 0, padx = 20, pady = 20)


app.mainloop()