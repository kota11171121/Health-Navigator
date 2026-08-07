import customtkinter as ctk

import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

import pandas as pd

from modules.csv_manager import load_exercise

class ExerciseGraphFrame(ctk.CTkFrame):


    def __init__(self, master):

        super().__init__(master)

        self.master = master

        # ==========================================
        # 画面全体
        # ==========================================

        self.configure(
            fg_color="#EAF6FF"
        )

        self.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=20
        )

        # ==========================================
        # タイトル
        # ==========================================

        title = ctk.CTkLabel(
            self,
            text="📈 運動記録のグラフ",
            font=("Hiragino Sans", 28, "bold"),
            text_color="#222222"
        )

        title.pack(
            pady=(20, 5)
        )

        subtitle = ctk.CTkLabel(
            self,
            text="記録した運動量をグラフで確認できます",
            font=("Hiragino Sans", 14),
            text_color="#666666"
        )

        subtitle.pack(
            pady=(0, 20)
        )

        # ==========================================
        # 説明カード
        # ==========================================

        info_card = ctk.CTkFrame(
            self,
            corner_radius=18,
            fg_color="#FFFFFF",
            border_width=1,
            border_color="#D8D8D8"
        )

        info_card.pack(
            fill="x",
            padx=20,
            pady=(0, 15)
        )

        info_title = ctk.CTkLabel(
            info_card,
            text="💡 この機能について",
            font=("Hiragino Sans", 16, "bold"),
            text_color="#222222"
        )

        info_title.pack(
            anchor="w",
            padx=20,
            pady=(15, 5)
        )

        info_text = ctk.CTkLabel(
            info_card,
            text=(
                "「運動記録」で保存した徒歩時間を、\n"
                "日付ごとのグラフで確認できます。\n\n"
                "毎日の運動量の変化を確認してみましょう。"
            ),
            font=("Hiragino Sans", 12),
            text_color="#666666",
            justify="left",
            anchor="w"
        )

        info_text.pack(
            fill="x",
            padx=20,
            pady=(0, 15)
        )

        # ==========================================
        # グラフカード
        # ==========================================

        graph_card = ctk.CTkFrame(
            self,
            corner_radius=18,
            fg_color="#FFFFFF",
            border_width=1,
            border_color="#D8D8D8"
        )

        graph_card.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=5
        )

        graph_title = ctk.CTkLabel(
            graph_card,
            text="🚶 徒歩時間の推移",
            font=("Hiragino Sans", 16, "bold"),
            text_color="#222222"
        )

        graph_title.pack(
            anchor="w",
            padx=20,
            pady=(15, 5)
        )

        # ==========================================
        # グラフ表示エリア
        # ==========================================

        self.graph_area = ctk.CTkFrame(
            graph_card,
            fg_color="transparent"
        )

        self.graph_area.pack(
            fill="both",
            expand=True,
            padx=10,
            pady=10
        )

        # ==========================================
        # ホームへ戻る
        # ==========================================

        home_button = ctk.CTkButton(
            self,
            text="⌂  ホームへ戻る",
            height=40,
            corner_radius=12,
            fg_color="#FFFFFF",
            hover_color="#F0F0F0",
            text_color="#333333",
            border_width=1,
            border_color="#D0D0D0",
            font=("Hiragino Sans", 13),
            command=self.master.show_home
        )

        home_button.pack(
            fill="x",
            padx=40,
            pady=(10, 15)
        )

        # ==========================================
        # グラフ表示
        # ==========================================

        self.show_graph()

    # ==========================================
    # グラフ
    # ==========================================

    def show_graph(self):

        df = load_exercise()

        # ------------------------------------------
        # データがない場合
        # ------------------------------------------

        if df is None:

            self.show_no_data()

            return

        if df.empty:

            self.show_no_data()

            return

        # ------------------------------------------
        # 必要な列があるか確認
        # ------------------------------------------

        if "日付" not in df.columns:

            self.show_no_data()

            return

        if "徒歩(分)" not in df.columns:

            self.show_no_data()

            return

        # ------------------------------------------
        # 日付を変換
        # ------------------------------------------

        df["日付"] = pd.to_datetime(
            df["日付"],
            errors="coerce"
        )

        # ------------------------------------------
        # 徒歩時間を数値に変換
        # ------------------------------------------

        df["徒歩(分)"] = pd.to_numeric(
            df["徒歩(分)"],
            errors="coerce"
        )

        # ------------------------------------------
        # 不正なデータを削除
        # ------------------------------------------

        df = df.dropna(
            subset=[
                "日付",
                "徒歩(分)"
            ]
        )

        if df.empty:

            self.show_no_data()

            return

        # ------------------------------------------
        # 日付順に並べ替え
        # ------------------------------------------

        df = df.sort_values(
            "日付"
        )

        # ------------------------------------------
        # グラフ作成
        # ------------------------------------------

        fig = plt.Figure(
            figsize=(7, 4),
            dpi=100
        )

        ax = fig.add_subplot(111)

        ax.plot(
            df["日付"],
            df["徒歩(分)"],
            marker="o"
        )

        # ------------------------------------------
        # グラフ設定
        # ------------------------------------------

        #ax.set_title(
            #""
        #)

        ax.set_xlabel(
            "date"
        )

        ax.set_ylabel(
            "walking time (minutes)"
        )

        ax.grid(
            True,
            alpha=0.3
        )

        fig.autofmt_xdate()

        # ------------------------------------------
        # グラフをTkinterに表示
        # ------------------------------------------

        self.canvas = FigureCanvasTkAgg(
            fig,
            master=self.graph_area
        )

        self.canvas.draw()

        self.canvas.get_tk_widget().pack(
            fill="both",
            expand=True,
            padx=10,
            pady=10
        )

    # ==========================================
    # データがない場合
    # ==========================================

    def show_no_data(self):

        no_data_label = ctk.CTkLabel(
            self.graph_area,
            text=(
                "📊 まだ運動記録がありません。\n\n"
                "「運動記録」から運動した日を登録すると、\n"
                "ここにグラフが表示されます。"
            ),
            font=("Hiragino Sans", 15),
            text_color="#666666",
            justify="center"
        )

        no_data_label.pack(
            expand=True
        )
