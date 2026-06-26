import customtkinter as ctk
from UI.dashboard import Dashboard

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("健康管理アプリ")
app.geometry("1000x700")

dashboard = Dashboard(app)
dashboard.pack(fill="both", expand=True)

app.mainloop()