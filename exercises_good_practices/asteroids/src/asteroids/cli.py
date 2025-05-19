import argparse
from .api import get_asteroids

def main():
    parser = argparse.ArgumentParser(description="Get the closest asteroid to Earth on a given date")
    parser.add_argument("--date", required=True, help="Date in YYYY-MM-DD format")
    args = parser.parse_args()

    result = get_asteroids(args.date)
    asteroid = result["asteroid"]

    print(f"\nThe closest asteroid to Earth on {args.date} was:")
    print(f"- {asteroid['name']}, {asteroid['distance_km']:,} km from Earth")
