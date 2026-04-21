import random
import time
from datetime import datetime
import csv

# -----------------------------
# CONFIGURATION
# -----------------------------

MACHINES = ["M1", "M2", "M3"]

DEFECT_CODES = ["NONE", "D1", "D2", "D3"]

OUTPUT_FILE = "machine_data.csv"

# -----------------------------
# MACHINE SIMULATION LOGIC
# -----------------------------

def generate_production():
    """
    Simulate production count with realistic variability
    """
    base = random.randint(5, 15)

    # simulate occasional boost or drop
    variation = random.choice([-3, -2, 0, 1, 2, 3])

    return max(0, base + variation)


def generate_defect():
    """
    Simulate defect occurrence (biased towards no defect)
    """
    weights = [0.7, 0.1, 0.1, 0.1]
    return random.choices(DEFECT_CODES, weights=weights)[0]


def generate_downtime():
    """
    Simulate machine downtime (rare event)
    """
    return 1 if random.random() < 0.05 else 0


def generate_event():
    """
    Generate a single machine event
    """
    return {
        "id_machine": random.choice(MACHINES),
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "production_count": generate_production(),
        "defect_code": generate_defect(),
        "downtime": generate_downtime()
    }


# -----------------------------
# DATA STREAM SIMULATION
# -----------------------------

def stream_data(interval=2):
    """
    Simulate real-time data stream
    """
    print("Starting industrial data stream...")

    # create file + header if not exists
    with open(OUTPUT_FILE, mode="a", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=[
            "id_machine",
            "timestamp",
            "production_count",
            "defect_code",
            "downtime"
        ])

        # write header only if file is empty
        file.seek(0, 2)
        if file.tell() == 0:
            writer.writeheader()

        while True:
            event = generate_event()

            writer.writerow(event)

            print(event)

            time.sleep(interval)


# -----------------------------
# MAIN
# -----------------------------

if __name__ == "__main__":
    stream_data(interval=2)