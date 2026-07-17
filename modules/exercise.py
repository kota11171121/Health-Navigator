import customtkinter as ctk
from datetime import datetime
from tkcalendar import DateEntry
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from modules.csv_manager import load_exercise
from modules.csv_manager import save_exercise
import pandas as pd


class ExerciseFrame(ctk.CTkFrame):

    def __init__(self, master):

        super().__init__(master)

        self.master = master

        self.pack(fill="both", expand=True, padx=20, pady=20)

        title = ctk.CTkLabel(
            self,
            text="運動記録",
            font=("Yu Gothic", 24, "bold")
        )

        title.pack(pady=20)

        # 日付
        ctk.CTkLabel(self, text="日付").pack()

        self.date_entry = DateEntry(
            self,
            width=18,
            date_pattern="yyyy-mm-dd",
            locale="ja_JP"
        )

        self.date_entry.pack(pady=5)

        # 徒歩
        ctk.CTkLabel(self, text="徒歩（分）").pack(pady=(15, 0))

        self.walk_entry = ctk.CTkEntry(self, width=200)

        self.walk_entry.pack()

        # その他
        ctk.CTkLabel(
            self,
            text="その他の運動"
        ).pack(pady=(15, 0))

        self.other_text = ctk.CTkTextbox(
            self,
            width=300,
            height=120
        )

        self.other_text.pack()

        ctk.CTkButton(
            self,
            text="保存",
            command=self.save
        ).pack(pady=20)

        ctk.CTkButton(
            self,
            text="ホームへ戻る",
            command=self.master.show_home
        ).pack()


    #7月17日追加
    def show_graph(self):

        df = load_exercise()

        if df is None:
            return

        df["日付"] = pd.to_datetime(df["日付"])
        df = df.sort_values("日付")

        df["徒歩(分)"] = pd.to_numeric(df["徒歩(分)"], errors="coerce")
        df = df.dropna()

        fig = plt.Figure(figsize=(6,3), dpi=100)

        ax = fig.add_subplot(111)

        ax.plot(
            df["日付"],
            df["徒歩(分)"],
            marker="o"
        )

        ax.set_title("徒歩時間の推移")
        ax.set_xlabel("日付")
        ax.set_ylabel("分")

        if hasattr(self, "canvas"):
            self.canvas.get_tk_widget().destroy()

        self.canvas = FigureCanvasTkAgg(fig, self)

        self.canvas.draw()

        self.canvas.get_tk_widget().pack(
            pady=20,
            fill="both",
            expand=True
        )
    
    def save(self):

        save_exercise(
            self.date_entry.get_date().strftime("%Y-%m-%d"),
            self.walk_entry.get(),
            self.other_text.get("1.0", "end").strip()
        )

        self.show_graph()