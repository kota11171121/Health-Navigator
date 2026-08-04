import customtkinter as ctk
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

        # ==========================
        # 画面全体
        # ==========================

        self.configure(
            fg_color="#EAF6FF"
        )

        self.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=20
        )

        # ==========================
        # タイトル
        # ==========================

        title = ctk.CTkLabel(
            self,
            text="🚶 運動記録",
            font=("Hiragino Sans", 30, "bold")
        )

        title.pack(
            pady=(10, 5)
        )

        subtitle = ctk.CTkLabel(
            self,
            text="毎日の運動量を記録します",
            font=("Hiragino Sans", 14)
        )

        subtitle.pack(
            pady=(0, 15)
        )

        # ==========================
        # 入力カード
        # ==========================

        input_card = ctk.CTkFrame(
            self,
            corner_radius=18,
            border_width=1,
            border_color="#D8D8D8",
            fg_color="white"
        )

        input_card.pack(
            fill="x",
            padx=20,
            pady=10
        )

        # ==========================
        # 日付
        # ==========================

        date_label = ctk.CTkLabel(
            input_card,
            text="📅 記録する日付",
            font=("Hiragino Sans", 16, "bold")
        )

        date_label.pack(
            anchor="w",
            padx=25,
            pady=(20, 8)
        )

        self.date_entry = DateEntry(
            input_card,
            width=18,
            date_pattern="yyyy-mm-dd",
            locale="ja_JP",
            font=("Hiragino Sans", 12)
        )

        self.date_entry.pack(
            anchor="w",
            padx=25,
            pady=(0, 15)
        )

        # ==========================
        # 徒歩
        # ==========================

        walk_label = ctk.CTkLabel(
            input_card,
            text="🚶 徒歩（分）",
            font=("Hiragino Sans", 16, "bold")
        )

        walk_label.pack(
            anchor="w",
            padx=25,
            pady=(5, 8)
        )

        self.walk_entry = ctk.CTkEntry(
            input_card,
            placeholder_text="例：30",
            height=40,
            font=("Hiragino Sans", 14)
        )

        self.walk_entry.pack(
            fill="x",
            padx=25
        )

        walk_unit = ctk.CTkLabel(
            input_card,
            text="徒歩した時間を分単位で入力してください",
            font=("Hiragino Sans", 12),
            text_color="gray40"
        )

        walk_unit.pack(
            anchor="w",
            padx=25,
            pady=(3, 15)
        )

        # ==========================
        # その他の運動
        # ==========================

        other_label = ctk.CTkLabel(
            input_card,
            text="🏃 その他の運動",
            font=("Hiragino Sans", 16, "bold")
        )

        other_label.pack(
            anchor="w",
            padx=25,
            pady=(5, 8)
        )

        self.other_text = ctk.CTkTextbox(
            input_card,
            height=90,
            font=("Hiragino Sans", 14)
        )

        self.other_text.pack(
            fill="x",
            padx=25,
            pady=(0, 20)
        )

        # ==========================
        # 保存ボタン
        # ==========================

        save_button = ctk.CTkButton(
            self,
            text="💾 運動記録を保存",
            width=280,
            height=50,
            corner_radius=15,
            fg_color="#4CAF50",
            hover_color="#388E3C",
            font=("Hiragino Sans", 16, "bold"),
            command=self.save
        )

        save_button.pack(
            pady=(15, 10)
        )

        # ==========================
        # ホームへ戻る
        # ==========================

        home_button = ctk.CTkButton(
            self,
            text="🏠 ホームへ戻る",
            width=280,
            height=45,
            corner_radius=15,
            fg_color="#607D8B",
            hover_color="#455A64",
            font=("Hiragino Sans", 14, "bold"),
            command=self.master.show_home
        )

        home_button.pack(
            pady=(0, 15)
        )

        # ==========================
        # グラフカード
        # ==========================

        graph_card = ctk.CTkFrame(
            self,
            corner_radius=18,
            border_width=1,
            border_color="#D8D8D8",
            fg_color="white"
        )

        graph_card.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=(5, 20)
        )

        graph_title = ctk.CTkLabel(
            graph_card,
            text="📈 徒歩時間の推移",
            font=("Hiragino Sans", 18, "bold"),
            text_color="#2196F3"
        )

        graph_title.pack(
            pady=(15, 5)
        )

        # グラフを表示する場所
        self.graph_frame = ctk.CTkFrame(
            graph_card,
            fg_color="white"
        )

        self.graph_frame.pack(
            fill="both",
            expand=True,
            padx=15,
            pady=10
        )

        # ==========================
        # 起動時にグラフを表示
        # ==========================

        self.show_graph()

    # ==================================================
    # グラフを表示
    # ==================================================

    def show_graph(self):

        df = load_exercise()

        # データが存在しない場合
        if df is None:

            print("exercise.csv がありません")

            return

        # データが空の場合
        if df.empty:

            print("exercise.csv にデータがありません")

            return

        print("読み込んだデータ")
        print(df)

        # ==========================
        # 日付をdatetimeに変換
        # ==========================

        df["日付"] = pd.to_datetime(
            df["日付"],
            errors="coerce"
        )

        # ==========================
        # 徒歩時間を数値に変換
        # ==========================

        df["徒歩(分)"] = pd.to_numeric(
            df["徒歩(分)"],
            errors="coerce"
        )

        # ==========================
        # 不正なデータを削除
        # ==========================

        df = df.dropna(
            subset=[
                "日付",
                "徒歩(分)"
            ]
        )

        # データがなくなった場合
        if df.empty:

            print("グラフに使用できるデータがありません")

            return

        # ==========================
        # 日付順に並べる
        # ==========================

        df = df.sort_values(
            "日付"
        )

        # ==========================
        # グラフ作成
        # ==========================

        fig = plt.Figure(
            figsize=(6, 3),
            dpi=100
        )

        ax = fig.add_subplot(111)

        ax.plot(
            df["日付"],
            df["徒歩(分)"],
            marker="o"
        )

        ax.set_xlabel(
            "日付",
            fontname="Hiragino Sans"
        )

        ax.set_ylabel(
            "徒歩時間（分）",
            fontname="Hiragino Sans"
        )

        ax.set_title(
            "日ごとの徒歩時間",
            fontname="Hiragino Sans"
        )

        # 日付を見やすくする
        fig.autofmt_xdate()

        # ==========================
        # 以前のグラフを削除
        # ==========================

        if hasattr(self, "canvas"):

            self.canvas.get_tk_widget().destroy()

        # ==========================
        # グラフを作成
        # ==========================

        self.canvas = FigureCanvasTkAgg(
            fig,
            master=self.graph_frame
        )

        self.canvas.draw()

        # ==========================
        # グラフを表示
        # ==========================

        self.canvas.get_tk_widget().pack(
            fill="both",
            expand=True,
            padx=10,
            pady=10
        )

    # ==================================================
    # 運動記録を保存
    # ==================================================

    def save(self):

        # ==========================
        # 入力内容を取得
        # ==========================

        date = self.date_entry.get_date().strftime(
            "%Y-%m-%d"
        )

        walk = self.walk_entry.get()

        other = self.other_text.get(
            "1.0",
            "end"
        ).strip()

        # ==========================
        # CSVへ保存
        # ==========================

        save_exercise(
            date,
            walk,
            other
        )

        # ==========================
        # グラフを更新
        # ==========================

        self.show_graph()

        print("運動記録を保存しました")
