import customtkinter as ctk


class HomeFrame(ctk.CTkFrame):

    def __init__(self, master):
        super().__init__(master)

        self.master = master

        # 背景色
        self.configure(fg_color="#EAF6FF")
        self.pack(fill="both", expand=True)

        # ==========================
        # タイトル
        # ==========================

        title = ctk.CTkLabel(
            self,
            text="🩺 健康管理アプリ",
            font=("Hiragino Sans", 32, "bold")
        )
        title.pack(pady=(20, 5))

        subtitle = ctk.CTkLabel(
            self,
            text="Lifestyle Disease Prevention",
            font=("Hiragino Sans", 15)
        )
        subtitle.pack(pady=(0, 25))

        # ==========================
        # プロフィールカード
        # ==========================

        self.create_card(
            icon="👤",
            title="プロフィール",
            description="基本情報を登録・変更します。",
            color="#4CAF50",
            command=self.open_profile
        )

        # ==========================
        # 運動記録カード
        # ==========================

        self.create_card(
            icon="🚶",
            title="運動記録",
            description="毎日の運動時間を記録します。",
            color="#2196F3",
            command=self.open_exercise
        )

        # ==========================
        # AI健康アドバイスカード
        # ==========================

        self.create_card(
            icon="🤖",
            title="健康アドバイス",
            description="Gemini AIが生活改善を提案します。",
            color="#9C27B0",
            command=self.open_advice
        )

    # ==========================
    # カード作成関数
    # ==========================

    def create_card(self, icon, title, description, color, command):

        card = ctk.CTkFrame(
            self,
            corner_radius=18,
            border_width=1,
            border_color="#D8D8D8",
            fg_color="white",
            height=90
        )

        card.pack(
            fill="x",
            padx=30,
            pady=10
        )

        # 左側（アイコン＋タイトル＋説明）
        left = ctk.CTkFrame(card, fg_color="transparent")
        left.pack(side="left", padx=15, pady=10)

        title_label = ctk.CTkLabel(
            left,
            text=f"{icon}  {title}",
            font=("Hiragino Sans", 18, "bold"),
            text_color=color
        )

        title_label.pack(anchor="w")

        desc_label = ctk.CTkLabel(
            left,
            text=description,
            font=("Hiragino Sans", 13),
            text_color="gray40"
        )

        desc_label.pack(anchor="w")

        # 右側ボタン
        button = ctk.CTkButton(
            card,
            text="▶",
            width=45,
            height=45,
            corner_radius=25,
            fg_color=color,
            hover_color=color,
            command=command
        )

        button.pack(side="right", padx=20)

    # ==========================
    # 画面遷移
    # ==========================

    def open_profile(self):
        self.master.show_profile()

    def open_exercise(self):
        self.master.show_exercise()

    def open_advice(self):
        self.master.show_advice()