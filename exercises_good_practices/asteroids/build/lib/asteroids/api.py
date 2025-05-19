import requests

def get_asteroids(date):
    API_KEY = "DEMO_KEY"
    url = "https://api.nasa.gov/neo/rest/v1/feed"
    params = {
        "start_date": date,
        "end_date": date,
        "api_key": API_KEY
    }

    response = requests.get(url, params=params)
    data = response.json()

    closest = None

    for neo in data["near_earth_objects"].get(date, []):
        name = neo["name"]
        distance = float(neo["close_approach_data"][0]["miss_distance"]["kilometers"])
        candidate = {
            "name": name,
            "distance_km": round(distance)
        }

        if closest is None or candidate["distance_km"] < closest["distance_km"]:
            closest = candidate

    return {"asteroid": closest}
