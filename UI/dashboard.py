import customtkinter as ctk

from UI.weight_page import WeightPage
from UI.blood_pressure_page import BloodPressurePage
from Logic.health_logic import calculate_bmi


class Dashboard(ctk.CTkFrame):

    def __init__(self, master):
        super().__init__(master)

        title = ctk.CTkLabel(
            self,
            text="健康管理アプリ",
            font=("Arial", 24)
        )
        title.pack(pady=20)

        bmi = calculate_bmi(
            weight=65,
            height_cm=170
        )

        bmi_label = ctk.CTkLabel(
            self,
            text=f"BMI: {bmi}"
        )
        bmi_label.pack(pady=10)

        self.weight_page = WeightPage(self)
        self.weight_page.pack(
            fill="x",
            padx=20,
            pady=10
        )

        self.bp_page = BloodPressurePage(self)
        self.bp_page.pack(
            fill="x",
            padx=20,
            pady=10
        )