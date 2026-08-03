import customtkinter as ctk
from modules.csv_manager import save_profile, load_profile

class ProfileFrame(ctk.CTkFrame):

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
            text="👤 プロフィール",
            font=("Hiragino Sans", 30, "bold")
        )

        title.pack(
            pady=(10, 5)
        )

        subtitle = ctk.CTkLabel(
            self,
            text="基本情報を登録・変更します",
            font=("Hiragino Sans", 14)
        )

        subtitle.pack(
            pady=(0, 20)
        )

        # ==========================
        # 入力欄を入れるカード
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
        # 入力項目
        # ==========================

        self.entries = {}

        items = [
            "名前",
            "年齢",
            "性別",
            "身長(cm)",
            "体重(kg)"
        ]

        for item in items:

            # 1つの項目をまとめるフレーム
            frame = ctk.CTkFrame(
                input_card,
                fg_color="transparent"
            )

            frame.pack(
                fill="x",
                padx=25,
                pady=7
            )

            # 項目名
            label = ctk.CTkLabel(
                frame,
                text=item,
                width=110,
                anchor="w",
                font=("Hiragino Sans", 14, "bold")
            )

            label.pack(
                side="left"
            )

            # 入力欄
            entry = ctk.CTkEntry(
                frame,
                height=40,
                font=("Hiragino Sans", 14)
            )

            entry.pack(
                side="left",
                fill="x",
                expand=True,
                padx=(10, 0)
            )

            self.entries[item] = entry

        # ==========================
        # BMI表示
        # ==========================

        self.bmi_label = ctk.CTkLabel(
            input_card,
            text="BMI：--",
            font=("Hiragino Sans", 16, "bold"),
            text_color="#2196F3"
        )

        self.bmi_label.pack(
            pady=(10, 20)
        )

        # ==========================
        # 保存ボタン
        # ==========================

        save_button = ctk.CTkButton(
            self,
            text="💾 保存",
            width=280,
            height=50,
            corner_radius=15,
            fg_color="#4CAF50",
            hover_color="#388E3C",
            font=("Hiragino Sans", 16, "bold"),
            command=self.save
        )

        save_button.pack(
            pady=(20, 10)
        )

        # ==========================
        # ホームへ戻るボタン
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
            pady=(0, 20)
        )

        # ==========================
        # 保存済みデータを読み込む
        # ==========================

        self.load()

    # ==================================================
    # プロフィールを保存
    # ==================================================

    def save(self):

        data = [
            self.entries["名前"].get(),
            self.entries["年齢"].get(),
            self.entries["性別"].get(),
            self.entries["身長(cm)"].get(),
            self.entries["体重(kg)"].get()
        ]

        # CSVへ保存
        save_profile(data)

        # BMIを計算
        try:

            height = float(
                self.entries["身長(cm)"].get()
            )

            weight = float(
                self.entries["体重(kg)"].get()
            )

            if height <= 0 or weight <= 0:
                raise ValueError

            bmi = weight / ((height / 100) ** 2)

            bmi = round(
                bmi,
                1
            )

            self.bmi_label.configure(
                text=f"BMI：{bmi}",
                text_color="#2196F3"
            )

        except (ValueError, ZeroDivisionError):

            self.bmi_label.configure(
                text="BMI：身長・体重を正しく入力してください",
                text_color="#F44336"
            )

    # ==================================================
    # 保存済みプロフィールを読み込む
    # ==================================================

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

                self.entries[key].delete(
                    0,
                    "end"
                )

                self.entries[key].insert(
                    0,
                    value
                )

            # 読み込んだデータからBMIを計算
            try:

                height = float(
                    self.entries["身長(cm)"].get()
                )

                weight = float(
                    self.entries["体重(kg)"].get()
                )

                if height > 0 and weight > 0:

                    bmi = weight / ((height / 100) ** 2)

                    bmi = round(
                        bmi,
                        1
                    )

                    self.bmi_label.configure(
                        text=f"BMI：{bmi}",
                        text_color="#2196F3"
                    )

            except (ValueError, ZeroDivisionError):

                pass



        