import csv
import os
import pandas as pd

DATA_FILE = "data/profile.csv"
EXERCISE_FILE = "data/exercise.csv"


def save_profile(data):
    os.makedirs("data", exist_ok=True)

    with open(DATA_FILE, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)

        writer.writerow([
            "名前",
            "年齢",
            "性別",
            "身長",
            "体重"
        ])

        writer.writerow(data)

#7月17日追加
def save_exercise(date, walk, other):

    os.makedirs("data", exist_ok=True)

    file_exists = os.path.exists(EXERCISE_FILE)

    with open(EXERCISE_FILE, "a", newline="", encoding="utf-8") as f:

        writer = csv.writer(f)

        if not file_exists:
            writer.writerow([
                "日付",
                "徒歩(分)",
                "その他の運動"
            ])

        writer.writerow([
            date,
            walk,
            other
        ])


def load_profile():

    if not os.path.exists(DATA_FILE):
        return None

    with open(DATA_FILE, "r", encoding="utf-8") as f:
        reader = csv.reader(f)

        next(reader)

        return next(reader)
    
#7月17日追加
def load_exercise():

    if not os.path.exists(EXERCISE_FILE):
        return None

    return pd.read_csv(EXERCISE_FILE)