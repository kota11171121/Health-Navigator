import customtkinter as ctk
from modules.profile import ProfileFrame

ctk.set_appearance_mode("Light")
ctk.set_default_color_theme("blue")


class App(ctk.CTk):

    def __init__(self):
        super().__init__()

        self.title("健康管理アプリ")

        self.geometry("500x500")

        ProfileFrame(self)


app = App()
app.mainloop()