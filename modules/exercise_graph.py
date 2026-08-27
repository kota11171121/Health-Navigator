import customtkinter as ctk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import pandas as pd

from modules.csv_manager import load_exercise


class ExerciseGraphFrame(ctk.CTkFrame):

    def __init__(self, master):

        super().__init__(master)

        self.master = master

        self.configure(
            fg_color="#EAF6FF"
        )

        self.pack(
            fill="both",
            expand=True
        )

        title = ctk.CTkLabel(
            self,
            text="📈 運動記録のグラフ",
            font=("Hiragino Sans", 28, "bold"),
            text_color="#222222"
        )

        title.pack(
            pady=(20, 5)
        )

        self.status_label = ctk.CTkLabel(
            self,
            text="運動記録を読み込み中...",
            font=("Hiragino Sans", 13),
            text_color="#666666"
        )

        self.status_label.pack(
            pady=(0, 10)
        )

        graph_card = ctk.CTkFrame(
            self,
            corner_radius=18,
            fg_color="white",
            border_width=1,
            border_color="#D8D8D8"
        )

        graph_card.pack(
            fill="both",
            expand=True,
            padx=30,
            pady=10
        )

        self.graph_area = ctk.CTkFrame(
            graph_card,
            fg_color="white"
        )

        self.graph_area.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=20
        )

        home_button = ctk.CTkButton(
            self,
            text="⌂  ホームへ戻る",
            height=40,
            command=self.master.show_home
        )

        home_button.pack(
            padx=40,
            pady=(5, 15)
        )

        self.after(500, self.show_graph)

    def show_graph(self):

        print("===== グラフ読み込み開始 =====")

        # 以前の表示を削除
        for widget in self.graph_area.winfo_children():
            widget.destroy()

        try:

            df = load_exercise()

            print("読み込んだデータ:")
            print(df)

        except Exception as e:

            print("CSV読み込みエラー:", e)

            self.status_label.configure(
                text="運動記録の読み込み中にエラーが発生しました"
            )

            self.show_message(
                f"エラーが発生しました。\n\n{e}"
            )

            return

        if df is None:

            self.status_label.configure(
                text="exercise.csv が見つかりません"
            )

            self.show_message(
                "まだ運動記録がありません。\n\n"
                "「運動記録」から徒歩時間を入力して保存してください。"
            )

            return

        if df.empty:

            self.status_label.configure(
                text="運動記録が0件です"
            )

            self.show_message(
                "まだ運動記録がありません。"
            )

            return

        print("CSVの列名:", df.columns.tolist())

        if "日付" not in df.columns:

            self.status_label.configure(
                text="CSVの日付データが見つかりません"
            )

            self.show_message(
                f"「日付」列がありません。\n\n現在の列名:\n{df.columns.tolist()}"
            )

            return

        if "徒歩(分)" not in df.columns:

            self.status_label.configure(
                text="CSVの徒歩時間データが見つかりません"
            )

            self.show_message(
                f"「徒歩(分)」列がありません。\n\n現在の列名:\n{df.columns.tolist()}"
            )

            return

        df["日付"] = pd.to_datetime(
            df["日付"],
            errors="coerce"
        )

        df["徒歩(分)"] = pd.to_numeric(
            df["徒歩(分)"],
            errors="coerce"
        )

        df = df.dropna(
            subset=["日付", "徒歩(分)"]
        )

        print("グラフに使用できるデータ:")
        print(df)

        if df.empty:

            self.status_label.configure(
                text="グラフに使用できるデータがありません"
            )

            self.show_message(
                "日付または徒歩時間を正しく読み込めませんでした。\n\n"
                "徒歩時間には「30」のように数字を入力してください。"
            )

            return

        df = df.sort_values("日付")

        self.status_label.configure(
            text=f"{len(df)}件の運動記録を表示しています"
        )

        fig = plt.Figure(
            figsize=(6, 4),
            dpi=100
        )

        ax = fig.add_subplot(111)

        ax.plot(
            df["日付"],
            df["徒歩(分)"],
            marker="o"
        )

        ax.set_title("Walking Time")

        ax.set_xlabel("Date")

        ax.set_ylabel("Minutes")

        ax.grid(True)

        fig.autofmt_xdate()

        fig.tight_layout()

        self.canvas = FigureCanvasTkAgg(
            fig,
            master=self.graph_area
        )

        self.canvas.draw()

        canvas_widget = self.canvas.get_tk_widget()

        canvas_widget.pack(
            fill="both",
            expand=True
        )

        print("===== グラフ表示完了 =====")

    def show_message(self, message):

        label = ctk.CTkLabel(
            self.graph_area,
            text=message,
            font=("Hiragino Sans", 15),
            text_color="#666666",
            justify="center"
        )

        label.pack(
            expand=True
        )