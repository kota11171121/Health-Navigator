import customtkinter as ctk

class HomeFrame(ctk.CTkFrame):

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
            text="🩺 ヘルスナビゲーター",
            font=("Hiragino Sans", 32, "bold")
        )

        title.pack(
            pady=(25, 5)
        )

        subtitle = ctk.CTkLabel(
            self,
            text="健康管理アプリ",
            font=("Hiragino Sans", 15)
        )

        subtitle.pack(
            pady=(0, 20)
        )


        profile_card = ctk.CTkFrame(
            self,
            corner_radius=18,
            fg_color="white",
            border_width=1,
            border_color="#D8D8D8"
        )

        profile_card.pack(
            fill="x",
            padx=40,
            pady=8
        )

        profile_button = ctk.CTkButton(
            profile_card,
            text="👤  プロフィール入力     ＞",
            height=55,
            corner_radius=15,
            fg_color="white",
            hover_color="#F0F0F0",
            text_color="#222222",
            font=("Hiragino Sans", 16, "bold"),
            anchor="w",
            command=self.open_profile
        )

        profile_button.pack(
            fill="x",
            padx=10,
            pady=(10, 2)
        )

        profile_description = ctk.CTkLabel(
            profile_card,
            text="基本情報を登録する",
            font=("Hiragino Sans", 12),
            text_color="gray40",
            anchor="w"
        )

        profile_description.pack(
            fill="x",
            padx=25,
            pady=(0, 10)
        )


        exercise_card = ctk.CTkFrame(
            self,
            corner_radius=18,
            fg_color="white",
            border_width=1,
            border_color="#D8D8D8"
        )

        exercise_card.pack(
            fill="x",
            padx=40,
            pady=8
        )

        exercise_button = ctk.CTkButton(
            exercise_card,
            text="🚶  運動記録             ＞",
            height=55,
            corner_radius=15,
            fg_color="white",
            hover_color="#F0F0F0",
            text_color="#222222",
            font=("Hiragino Sans", 16, "bold"),
            anchor="w",
            command=self.open_exercise
        )

        exercise_button.pack(
            fill="x",
            padx=10,
            pady=(10, 2)
        )

        exercise_description = ctk.CTkLabel(
            exercise_card,
            text="毎日の運動を記録する",
            font=("Hiragino Sans", 12),
            text_color="gray40",
            anchor="w"
        )

        exercise_description.pack(
            fill="x",
            padx=25,
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
            fill="x",
            padx=40,
            pady=8
        )

        graph_button = ctk.CTkButton(
            graph_card,
            text="📈  運動記録のグラフ     ＞",
            height=55,
            corner_radius=15,
            fg_color="white",
            hover_color="#F0F0F0",
            text_color="#222222",
            font=("Hiragino Sans", 16, "bold"),
            anchor="w",
            command=self.open_exercise_graph
        )

        graph_button.pack(
            fill="x",
            padx=10,
            pady=(10, 2)
        )

        graph_description = ctk.CTkLabel(
            graph_card,
            text="記録した運動量をグラフで確認する",
            font=("Hiragino Sans", 12),
            text_color="gray40",
            anchor="w"
        )

        graph_description.pack(
            fill="x",
            padx=25,
            pady=(0, 10)
        )


        advice_card = ctk.CTkFrame(
            self,
            corner_radius=18,
            fg_color="white",
            border_width=1,
            border_color="#D8D8D8"
        )

        advice_card.pack(
            fill="x",
            padx=40,
            pady=8
        )

        advice_button = ctk.CTkButton(
            advice_card,
            text="🤖  健康アドバイス     ＞",
            height=55,
            corner_radius=15,
            fg_color="white",
            hover_color="#F0F0F0",
            text_color="#222222",
            font=("Hiragino Sans", 16, "bold"),
            anchor="w",
            command=self.open_advice
        )

        advice_button.pack(
            fill="x",
            padx=10,
            pady=(10, 2)
        )

        advice_description = ctk.CTkLabel(
            advice_card,
            text="AIが生活改善を提案",
            font=("Hiragino Sans", 12),
            text_color="gray40",
            anchor="w"
        )

        advice_description.pack(
            fill="x",
            padx=25,
            pady=(0, 10)
        )


    def open_profile(self):

        self.master.show_profile()


    def open_exercise(self):

        self.master.show_exercise()


    def open_exercise_graph(self):

        self.master.show_exercise_graph()


    def open_advice(self):

        self.master.show_advice()
