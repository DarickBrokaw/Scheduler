from pathlib import Path

from constraint_solver import solve_schedule
from utils import load_json, save_json

DATA_DIR = Path(__file__).resolve().parent.parent / "data"


def main():
    therapists = load_json(DATA_DIR / "therapists.json")
    patients = load_json(DATA_DIR / "patients.json")
    schedule = solve_schedule(therapists, patients)
    save_json(schedule, DATA_DIR / "schedule_output.json")


if __name__ == "__main__":
    main()
