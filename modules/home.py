import customtkinter as ctk


class HomeFrame(ctk.CTkFrame):

    def __init__(self, master):
        super().__init__(master)

        self.master = master

        self.pack(fill="both", expand=True)

        title = ctk.CTkLabel(
            self,
            text="健康管理アプリ",
            font=("Yu Gothic", 28, "bold")
        )
        title.pack(pady=40)

        profile_button = ctk.CTkButton(
            self,
            text="プロフィール入力",
            width=250,
            height=40,
            command=self.open_profile
        )
        profile_button.pack(pady=20)

        #7月17日追加
        exercise_button = ctk.CTkButton(
            self,
            text="運動記録",
            width=250,
            height=40,
            command=self.open_exercise
        )

        exercise_button.pack(pady=10)

    def open_profile(self):
        self.master.show_profile()

    #7月17日追加
    def open_exercise(self):
        self.master.show_exercise()