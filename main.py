import customtkinter as ctk

from modules.home import HomeFrame
from modules.profile import ProfileFrame
from modules.exercise import ExerciseFrame
from modules.exercise_graph import ExerciseGraphFrame
from modules.advice import AdviceFrame

ctk.set_appearance_mode("Light")
ctk.set_default_color_theme("blue")


class App(ctk.CTk):

    def __init__(self):
        super().__init__()

        self.title("ヘルスナビゲーター")
        self.geometry("500x700")
        self.minsize(500, 650)

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

    def show_exercise(self):
        self.change_frame(ExerciseFrame)

    def show_exercise_graph(self):
        self.change_frame(ExerciseGraphFrame)

    def show_advice(self):
        self.change_frame(AdviceFrame)


app = App()
app.mainloop()