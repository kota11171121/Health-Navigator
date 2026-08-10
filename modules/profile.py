import customtkinter as ctk
from tkinter import messagebox

from modules.csv_manager import save_profile, load_profile

class ProfileFrame(ctk.CTkFrame):

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
            text="👤 プロフィール入力",
            font=("Hiragino Sans", 28, "bold"),
            text_color="#222222"
        )

        title.pack(
            pady=(20, 5)
        )

        subtitle = ctk.CTkLabel(
            self,
            text="あなたの基本情報を登録します",
            font=("Hiragino Sans", 14),
            text_color="#666666"
        )

        subtitle.pack(
            pady=(0, 20)
        )

        # ==========================================
        # 注意・説明カード
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
                "名前・年齢・性別・身長・体重などの\n"
                "基本情報を登録することができます。\n\n"
                "登録した身長と体重は、BMIの計算や\n"
                "健康アドバイスに利用されます。"
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
        # 入力フォームカード
        # ==========================================

        form_card = ctk.CTkFrame(
            self,
            corner_radius=18,
            fg_color="#FFFFFF",
            border_width=1,
            border_color="#D8D8D8"
        )

        form_card.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=5
        )

        self.entries = {}

        items = [
            "名前",
            "年齢",
            "性別",
            "身長(cm)",
            "体重(kg)"
        ]

        # ==========================================
        # 入力欄
        # ==========================================

        for item in items:

            row = ctk.CTkFrame(
                form_card,
                fg_color="transparent"
            )

            row.pack(
                fill="x",
                padx=25,
                pady=7
            )

            label = ctk.CTkLabel(
                row,
                text=item,
                width=110,
                anchor="w",
                font=("Hiragino Sans", 13, "bold"),
                text_color="#333333"
            )

            label.pack(
                side="left"
            )

            entry = ctk.CTkEntry(
                row,
                height=38,
                corner_radius=10,
                font=("Hiragino Sans", 13)
            )

            entry.pack(
                side="left",
                fill="x",
                expand=True,
                padx=(10, 0)
            )

            self.entries[item] = entry

        # ==========================================
        # 保存ボタン
        # ==========================================

        save_button = ctk.CTkButton(
            self,
            text="💾  保存する",
            height=45,
            corner_radius=14,
            font=("Hiragino Sans", 15, "bold"),
            command=self.save
        )

        save_button.pack(
            fill="x",
            padx=40,
            pady=(15, 8)
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
            pady=(0, 15)
        )

        # ==========================================
        # 保存されているプロフィールを読み込む
        # ==========================================

        self.load()

    # ==========================================
    # プロフィール保存
    # ==========================================

    def save(self):

        data = [
            self.entries["名前"].get(),
            self.entries["年齢"].get(),
            self.entries["性別"].get(),
            self.entries["身長(cm)"].get(),
            self.entries["体重(kg)"].get()
        ]

        # ======================================
        # 入力チェック
        # ======================================

        if not data[0]:

            messagebox.showwarning(
                "入力確認",
                "名前を入力してください。"
            )

            return

        if not data[1]:

            messagebox.showwarning(
                "入力確認",
                "年齢を入力してください。"
            )

            return

        if not data[2]:

            messagebox.showwarning(
                "入力確認",
                "性別を入力してください。"
            )

            return

        if not data[3]:

            messagebox.showwarning(
                "入力確認",
                "身長を入力してください。"
            )

            return

        if not data[4]:

            messagebox.showwarning(
                "入力確認",
                "体重を入力してください。"
            )

            return

        # ======================================
        # 身長・体重の数値チェック
        # ======================================

        try:

            height = float(data[3])
            weight = float(data[4])

        except ValueError:

            messagebox.showwarning(
                "入力確認",
                "身長と体重は数字で入力してください。"
            )

            return

        if height <= 0 or weight <= 0:

            messagebox.showwarning(
                "入力確認",
                "身長と体重には0より大きい数字を入力してください。"
            )

            return

        # ======================================
        # 保存
        # ======================================

        save_profile(data)

        messagebox.showinfo(
            "保存完了",
            "プロフィールを保存しました。"
        )

    # ==========================================
    # プロフィール読み込み
    # ==========================================

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
