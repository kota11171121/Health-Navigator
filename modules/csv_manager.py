import csv
import os

DATA_FILE = "data/profile.csv"


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


def load_profile():

    if not os.path.exists(DATA_FILE):
        return None

    with open(DATA_FILE, "r", encoding="utf-8") as f:
        reader = csv.reader(f)

        next(reader)

        return next(reader)