import customtkinter as ctk
from datetime import datetime
#from Database.db import add_bp


class BloodPressurePage(ctk.CTkFrame):

    def __init__(self, master):
        super().__init__(master)

        ctk.CTkLabel(
            self,
            text="血圧記録"
        ).pack(pady=10)

        self.sys_entry = ctk.CTkEntry(
            self,
            placeholder_text="最高血圧"
        )

        self.dia_entry = ctk.CTkEntry(
            self,
            placeholder_text="最低血圧"
        )

        self.sys_entry.pack(pady=5)
        self.dia_entry.pack(pady=5)

        ctk.CTkButton(
            self,
            text="登録",
            #command=self.save_bp
        ).pack(pady=10)

    """

    def save_bp(self):

        add_bp(
            datetime.now().strftime("%Y-%m-%d"),
            int(self.sys_entry.get()),
            int(self.dia_entry.get())
        )

        self.sys_entry.delete(0, "end")
        self.dia_entry.delete(0, "end")

    """