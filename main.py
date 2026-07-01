import customtkinter as ctk


class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Buckshot")
        self.geometry("1000x600")
        self.resizable(False,False)
        self.grid_rowconfigure(0,weight=1)
        self.grid_columnconfigure(0,weight=1)
        

app = App()
app.mainloop()