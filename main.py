import customtkinter as ctk
from screeninfo import get_monitors

monitor = get_monitors()[0]

HEIGHT = monitor.height
WIDTH = monitor.width

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Buckshot")
        self.geometry(f"{WIDTH // 2}x{HEIGHT // 2}")
        self.resizable(False,False)
        self.grid_rowconfigure(0,weight=1)
        self.grid_columnconfigure(0,weight=1)
        login_frame = LoginFrame(self)
        login_frame.grid(row=0, column=0)
        
class LoginFrame(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)

        app_width = WIDTH // 2
        app_height = HEIGHT // 2

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        
        self.entry_frame = ctk.CTkFrame(
            self,
            fg_color="black",
            width=(app_width // 2),
            height=(app_height // 2)
        )
        self.entry_frame.grid(row=0, column=0, sticky="nsew")

        self.entry_frame.grid_propagate(False)

        self.entry_frame.grid_rowconfigure(0,weight=1)
        self.entry_frame.grid_columnconfigure(0, weight=1)

        self.header_lbl = ctk.CTkLabel(
            self.entry_frame,
            text="Buckshot",
            font=("Segoe UI", 30, "bold"),
        )
        self.header_lbl.grid(row=0, column=0, sticky="nswe")

        

app = App()
app.mainloop()
