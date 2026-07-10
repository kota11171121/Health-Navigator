import customtkinter as ctk

from modules.home import HomeFrame
from modules.profile import ProfileFrame

ctk.set_appearance_mode("Light")
ctk.set_default_color_theme("blue")


class App(ctk.CTk):

    def __init__(self):
        super().__init__()

        self.title("健康管理アプリ")
        self.geometry("500x500")

        self.current_frame = None

        self.show_home()

    def change_frame(self, frame_class):

        if self.current_frame is not None:
            self.current_frame.destroy()

        self.current_frame = frame_class(self)

    def show_home(self):
        self.change_frame(HomeFrame)

    def show_profile(self):
        self.change_frame(ProfileFrame)


app = App()
app.mainloop()