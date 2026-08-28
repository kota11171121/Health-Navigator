import customtkinter as ctk

from modules.gemini_api import get_health_advice
from modules.csv_manager import load_profile
from modules.csv_manager import load_exercise

class AdviceFrame(ctk.CTkFrame):


    def __init__(self, master):

        super().__init__(master)

        self.master = master

        self.configure(fg_color="#EAF6FF")

        self.pack(fill="both",expand=True,padx=20,pady=20)

        title = ctk.CTkLabel(
            self,
            text="🤖 健康アドバイス",
            font=("Hiragino Sans", 30, "bold"))

        title.pack(pady=(10, 5))

        subtitle = ctk.CTkLabel(
            self,
            text="AIがあなたの健康記録をもとにアドバイスします",
            font=("Hiragino Sans", 14))

        subtitle.pack(pady=(0, 15))

        data_card = ctk.CTkFrame(
            self,
            corner_radius=18,
            border_width=1,
            border_color="#D8D8D8",
            fg_color="white")

        data_card.pack(fill="x",padx=20,pady=10)

        data_title = ctk.CTkLabel(
            data_card,
            text="🩺 現在の健康データ",
            font=("Hiragino Sans", 18, "bold"),
            text_color="#2196F3")

        data_title.pack(anchor="w",padx=25,pady=(15, 10))

        self.data_label = ctk.CTkLabel(
            data_card,
            text="健康データを読み込んでいます...",
            font=("Hiragino Sans", 14),
            justify="left",
            anchor="w")

        self.data_label.pack(fill="x",padx=25,pady=(0, 20))

        advice_button = ctk.CTkButton(
            self,
            text="🤖 アドバイスを取得",
            width=280,
            height=50,
            corner_radius=15,
            fg_color="#4CAF50",
            hover_color="#388E3C",
            font=("Hiragino Sans", 16, "bold"),
            command=self.get_advice)

        advice_button.pack(pady=(15, 10))

        advice_card = ctk.CTkFrame(
            self,
            corner_radius=18,
            border_width=1,
            border_color="#D8D8D8",
            fg_color="white")

        advice_card.pack(fill="both",expand=True,padx=20,pady=10)

        advice_title = ctk.CTkLabel(
            advice_card,
            text="💡 AIからの健康アドバイス",
            font=("Hiragino Sans", 18, "bold"),
            text_color="#2196F3")

        advice_title.pack(anchor="w",padx=20,pady=(15, 10))

        self.textbox = ctk.CTkTextbox(advice_card,height=130,font=("Hiragino Sans", 14),corner_radius=10)

        self.textbox.pack(fill="both",expand=True,padx=20,pady=(0, 15))

        home_button = ctk.CTkButton(
            self,
            text="🏠 ホームへ戻る",
            width=280,
            height=45,
            corner_radius=15,
            fg_color="#607D8B",
            hover_color="#455A64",
            font=("Hiragino Sans", 14, "bold"),
            command=self.master.show_home)

        home_button.pack(pady=(5, 15))
        self.show_health_data()

    def show_health_data(self):
        profile = load_profile()
        exercise = load_exercise()

        bmi_text = "未登録"

        if profile:
            try:
                height = float(profile[3])
                weight = float(profile[4])

                if height > 0:
                    bmi = round(weight / ((height / 100) ** 2),1)
                    bmi_text = str(bmi)
            except (ValueError, IndexError, TypeError):

                bmi_text = "計算できません"

        walk_text = "未登録"
        other_text = "未登録"

        if exercise is not None and not exercise.empty:
            try:
                latest = exercise.iloc[-1]
                walk_text = str(latest["徒歩(分)"])
                other_text = str(latest["その他の運動"])
            except (KeyError, IndexError):

                pass

        data_text = (
            f"📊 BMI：{bmi_text}\n\n"
            f"🚶 最新の徒歩時間：{walk_text} 分\n\n"
            f"🏃 その他の運動：{other_text}")

        self.data_label.configure(text=data_text)

    def get_advice(self):

        profile = load_profile()

        if not profile:
            self.textbox.delete("1.0","end")
            self.textbox.insert(
                "1.0",
                "⚠ プロフィールが登録されていません。\n\n"
                "先にプロフィール画面から\n"
                "身長と体重を登録してください。")

            return

        try:
            height = float(profile[3])
            weight = float(profile[4])
            bmi = round(weight / ((height / 100) ** 2),1)

        except (ValueError, IndexError, TypeError, ZeroDivisionError):

            self.textbox.delete("1.0","end")
            self.textbox.insert("1.0","⚠ 身長または体重のデータが正しくありません。")

            return

        exercise = load_exercise()

        if exercise is None or exercise.empty:
            walk = "記録なし"
            other = "記録なし"

        else:
            try:
                latest = exercise.iloc[-1]
                walk = latest["徒歩(分)"]
                other = latest["その他の運動"]

            except (KeyError, IndexError):

                walk = "記録なし"
                other = "記録なし"

        prompt = f"""
    ```

    あなたは管理栄養士です。

    以下はユーザーの健康記録です。

    BMI：{bmi}

    徒歩時間：{walk}分

    その他の運動：
    {other}

    あなたは栄養管理士です。
    この健康記録を参考にして、
    生活習慣病予防のための具体的なアドバイスを作成してください。

    最初の挨拶は省略してください。

    高校生でも理解できるような、
    わかりやすい文章にしてください。

    アドバイスは箇条書きで何個か出してください。

    それぞれのアドバイスの間には
    改行を入れて読みやすくしてください。

    ですます調で、丁寧な言葉遣いを心がけてください。

    医療行為や診断をするのではなく、
    日常生活で取り組める一般的な健康アドバイスをしてください。
    絵文字を使いすぎないでください。
    """

        self.textbox.delete("1.0","end")
        self.textbox.insert("1.0","🤖 AIが健康記録を分析しています...\n\n""少しお待ちください。")
        self.update()

        try:
            advice = get_health_advice(prompt)
            self.textbox.delete("1.0","end")
            self.textbox.insert("1.0",advice)
            self.show_health_data()

        except Exception as e:

            self.textbox.delete("1.0","end")
            self.textbox.insert(
                "1.0",
                "⚠ アドバイスの取得中にエラーが発生しました。\n\n"
                f"エラー内容：\n{e}")

