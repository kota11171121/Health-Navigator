import customtkinter as ctk

from tkinter import messagebox
from tkcalendar import DateEntry

from modules.csv_manager import save_exercise

class ExerciseFrame(ctk.CTkFrame):

    def __init__(self, master):

        super().__init__(master)

        self.master = master


        self.configure(
            fg_color="#EAF6FF"
        )

        self.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=20
        )


        title = ctk.CTkLabel(
            self,
            text="🚶 運動記録",
            font=("Hiragino Sans", 28, "bold"),
            text_color="#222222"
        )

        title.pack(
            pady=(20, 5)
        )

        subtitle = ctk.CTkLabel(
            self,
            text="毎日の運動量を記録します",
            font=("Hiragino Sans", 14),
            text_color="#666666"
        )

        subtitle.pack(
            pady=(0, 20)
        )


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
                "日付ごとに、徒歩やその他の運動を記録できます。\n"
                "記録した内容は「運動記録のグラフ」から確認できます。\n\n"
                "毎日の運動量を記録して、生活習慣の改善に役立てましょう。"
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


        form_card = ctk.CTkFrame(
            self,
            corner_radius=18,
            fg_color="#FFFFFF",
            border_width=1,
            border_color="#D8D8D8"
        )

        form_card.pack(
            fill="x",
            padx=20,
            pady=5
        )


        date_label = ctk.CTkLabel(
            form_card,
            text="📅 記録する日付",
            font=("Hiragino Sans", 14, "bold"),
            text_color="#333333"
        )

        date_label.pack(
            anchor="w",
            padx=25,
            pady=(20, 5)
        )

        self.date_entry = DateEntry(
            form_card,
            width=18,
            date_pattern="yyyy-mm-dd",
            locale="ja_JP"
        )

        self.date_entry.pack(
            padx=25,
            pady=(0, 10),
            anchor="w"
        )


        walk_label = ctk.CTkLabel(
            form_card,
            text="🚶 徒歩（分）",
            font=("Hiragino Sans", 14, "bold"),
            text_color="#333333"
        )

        walk_label.pack(
            anchor="w",
            padx=25,
            pady=(10, 5)
        )

        self.walk_entry = ctk.CTkEntry(
            form_card,
            height=38,
            width=220,
            corner_radius=10,
            placeholder_text="例：30",
            font=("Hiragino Sans", 13)
        )

        self.walk_entry.pack(
            padx=25,
            pady=(0, 10),
            anchor="w"
        )


        other_label = ctk.CTkLabel(
            form_card,
            text="🏃 その他の運動",
            font=("Hiragino Sans", 14, "bold"),
            text_color="#333333"
        )

        other_label.pack(
            anchor="w",
            padx=25,
            pady=(10, 5)
        )

        self.other_text = ctk.CTkTextbox(
            form_card,
            width=350,
            height=90,
            corner_radius=10,
            font=("Hiragino Sans", 13)
        )

        self.other_text.pack(
            padx=25,
            pady=(0, 20),
            anchor="w"
        )


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


    def save(self):

        date = self.date_entry.get_date().strftime(
            "%Y-%m-%d"
        )

        walk = self.walk_entry.get()

        other = self.other_text.get(
            "1.0",
            "end"
        ).strip()


        if not walk:

            walk = "0"

        try:

            walk_value = float(walk)

        except ValueError:

            messagebox.showwarning(
                "入力確認",
                "徒歩時間は数字で入力してください。"
            )

            return

        if walk_value < 0:

            messagebox.showwarning("入力確認","徒歩時間は0以上で入力してください。")

            return


        save_exercise(
            date,
            str(walk_value),
            other
        )

        messagebox.showinfo("保存完了","運動記録を保存しました。")

        self.walk_entry.delete(0,"end")

        self.other_text.delete("1.0","end")

