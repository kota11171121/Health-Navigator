import csv
import os

WEIGHT_FILE = "data/weight.csv"
BP_FILE = "data/blood_pressure.csv"


def init_csv():

    os.makedirs("data", exist_ok=True)

    if not os.path.exists(WEIGHT_FILE):
        with open(
            WEIGHT_FILE,
            "w",
            newline="",
            encoding="utf-8"
        ) as f:

            writer = csv.writer(f)
            writer.writerow([
                "date",
                "weight"
            ])

    if not os.path.exists(BP_FILE):
        with open(
            BP_FILE,
            "w",
            newline="",
            encoding="utf-8"
        ) as f:

            writer = csv.writer(f)
            writer.writerow([
                "date",
                "systolic",
                "diastolic"
            ])

def add_weight(date, weight):

    with open(
        WEIGHT_FILE,
        "a",
        newline="",
        encoding="utf-8"
    ) as f:

        writer = csv.writer(f)

        writer.writerow([
            date,
            weight
        ])