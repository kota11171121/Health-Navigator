import customtkinter as ctk
<<<<<<< HEAD
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
=======
from UI.dashboard import Dashboard

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("健康管理アプリ")
app.geometry("1000x700")

dashboard = Dashboard(app)
dashboard.pack(fill="both", expand=True)

>>>>>>> eee847bd44eefcf80adfa26e588bedcc1025951f
app.mainloop()