import customtkinter as ctk
from datetime import datetime
from Database.db import add_weight


class WeightPage(ctk.CTkFrame):

    def __init__(self, master):
        super().__init__(master)

        ctk.CTkLabel(
            self,
            text="体重記録"
        ).pack(pady=10)

        self.weight_entry = ctk.CTkEntry(
            self,
            placeholder_text="体重(kg)"
        )
        self.weight_entry.pack(pady=10)

        ctk.CTkButton(
            self,
            text="登録",
            command=self.save_weight
        ).pack(pady=10)

    def save_weight(self):

        weight = float(
            self.weight_entry.get()
        )

        add_weight(
            datetime.now().strftime("%Y-%m-%d"),
            weight
        )

        self.weight_entry.delete(0, "end")