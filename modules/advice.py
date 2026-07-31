import customtkinter as ctk

from modules.gemini_api import get_health_advice
from modules.csv_manager import load_profile
from modules.csv_manager import load_exercise


class AdviceFrame(ctk.CTkFrame):

    def __init__(self, master):

        super().__init__(master)

        self.master = master

        self.pack(fill="both", expand=True)

        title = ctk.CTkLabel(
            self,
            text="健康アドバイス",
            font=("Yu Gothic", 24, "bold")
        )

        title.pack(pady=20)

        self.textbox = ctk.CTkTextbox(
            self,
            width=500,
            height=300
        )

        self.textbox.pack(padx=20, pady=20)

        ctk.CTkButton(
            self,
            text="アドバイスを取得",
            command=self.get_advice
        ).pack(pady=10)

        ctk.CTkButton(
            self,
            text="ホームへ戻る",
            command=self.master.show_home
        ).pack(pady=10)

    def get_advice(self):

        profile = load_profile()

        height = float(profile[3])
        weight = float(profile[4])

        bmi = round(weight / ((height / 100) ** 2), 1)

        exercise = load_exercise()

        latest = exercise.iloc[-1]

        walk = latest["徒歩(分)"]
        other = latest["その他の運動"]

        prompt = f"""
    あなたは管理栄養士です。

    BMIは{bmi}

    徒歩時間は{walk}分

    その他の運動

    {other}

    最初の挨拶を省略し、
    生活習慣病予防のための
    アドバイスを箇条書きで、高校生でもわかるような文で何個か出してください
    また、改行を入れて読みやすいようにしてください
    ですます調にして丁寧な言葉遣いを心がけてください。
    """

        advice = get_health_advice(prompt)

        self.textbox.delete("1.0", "end")

        self.textbox.insert("1.0", advice)