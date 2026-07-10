import customtkinter as ctk
from modules.csv_manager import save_profile, load_profile


class ProfileFrame(ctk.CTkFrame):

    def __init__(self, master):
        super().__init__(master)

        self.pack(fill="both", expand=True, padx=20, pady=20)

        ctk.CTkLabel(self, text="プロフィール入力",
                     font=("Yu Gothic", 24, "bold")).pack(pady=20)

        self.entries = {}

        items = [
            "名前",
            "年齢",
            "性別",
            "身長(cm)",
            "体重(kg)"
        ]

        for item in items:

            frame = ctk.CTkFrame(self)
            frame.pack(fill="x", pady=5)

            ctk.CTkLabel(frame, text=item, width=120).pack(side="left")

            entry = ctk.CTkEntry(frame)
            entry.pack(side="left", padx=10)

            self.entries[item] = entry

        ctk.CTkButton(
            self,
            text="保存",
            command=self.save
        ).pack(pady=20)

        self.load()

    def save(self):

        data = [
            self.entries["名前"].get(),
            self.entries["年齢"].get(),
            self.entries["性別"].get(),
            self.entries["身長(cm)"].get(),
            self.entries["体重(kg)"].get()
        ]

        save_profile(data)

    def load(self):

        data = load_profile()

        if data:

            keys = [
                "名前",
                "年齢",
                "性別",
                "身長(cm)",
                "体重(kg)"
            ]

            for key, value in zip(keys, data):
                self.entries[key].insert(0, value)