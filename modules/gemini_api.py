from google import genai
from modules.csv_manager import load_profile
from modules.csv_manager import load_exercise

api_key = ""

if api_key != "":
    client = genai.Client(api_key=api_key)

def get_health_advice(prompt):

    if api_key != "":
        response = client.models.generate_content(model="gemini-3.5-flash-lite",contents=prompt)
        return response.text

    else:  # APIキーがない場合のアドバイス

        advice_list = []
        profile = load_profile()

        if not profile or len(profile) < 5:
            return "プロフィール情報を登録してください。"

        try:
            height = float(profile[3])
            weight = float(profile[4])
            bmi = round(weight / ((height / 100) ** 2),1)

        except (ValueError, TypeError):

            return "身長と体重を正しく入力してください。"
        advice_list.append(f"・現在のBMIは {bmi} です。")

        if bmi < 18.5:
            advice_list.append("・BMIが低めです。バランスの良い食事を意識しましょう。")

        elif bmi < 25:
            advice_list.append("・BMIは標準的な範囲です。現在の生活習慣を維持しましょう。")

        else:
            advice_list.append("・BMIが高めです。食事や運動の習慣を少しずつ見直してみましょう。")

        exercise = load_exercise()

        if exercise is None or exercise.empty:
            advice_list.append("・運動記録がありません。まずは短い散歩などから始めてみましょう。")

            return "\n\n".join(advice_list)

        try:
            exercise["徒歩(分)"] = exercise["徒歩(分)"].astype(float)
            average_walk = exercise["徒歩(分)"].mean()

        except (ValueError, TypeError):
            advice_list.append("・運動記録を正しく読み取れませんでした。")

            return "\n\n".join(advice_list)

        advice_list.append(f"・記録されている平均徒歩時間は "f"{round(average_walk, 1)}分です。")

        if average_walk < 10:
            advice_list.append("・運動量が少ない傾向があります。まずは1日10分程度歩くことから始めてみましょう。")

        elif average_walk < 30:
            advice_list.append("・適度に運動できています。少しずつ運動時間を増やしてみましょう。")

        else:
            advice_list.append("・十分な運動を続けられています。これからも無理のない範囲で継続しましょう。")

        return "\n\n".join(advice_list)