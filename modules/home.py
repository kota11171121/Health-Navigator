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

    def open_profile(self):
        self.master.show_profile()