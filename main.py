import requests
import math
import json

# -----------------------------
# 1. Get user location (ipinfo.io)
# -----------------------------
def get_user_location():
    url = "https://ipinfo.io/json"
    response = requests.get(url).json()

    print("DEBUG:", response)  # Shows your detected location

    if "loc" not in response:
        raise Exception("Could not get location. Full response: " + str(response))

    lat_str, lon_str = response["loc"].split(",")
    return float(lat_str), float(lon_str)


# -----------------------------
# 2. Query Overpass API for emergency resources
# -----------------------------
def get_emergency_phones():
    overpass_url = "https://overpass-api.de/api/interpreter"

    query = """
    [out:json];
    (
      node["amenity"="police"](47.50,-122.45,47.80,-122.20);
      node["amenity"="telephone"](47.50,-122.45,47.80,-122.20);
      node["emergency"="phone"](47.50,-122.45,47.80,-122.20);
      node["emergency"="call_point"](47.50,-122.45,47.80,-122.20);
      node["amenity"="emergency_phone"](47.50,-122.45,47.80,-122.20);
    );
    out;
    """

    response = requests.get(overpass_url, params={"data": query})
    data = response.json()

    phones = []
    for element in data.get("elements", []):
        phones.append({
            "lat": element["lat"],
            "lng": element["lon"],
            "name": element["tags"].get("emergency", element["tags"].get("amenity", "Emergency Resource"))
        })

    return phones


# -----------------------------
# 3. Distance calculation (Haversine)
# -----------------------------
def distance_meters(lat1, lon1, lat2, lon2):
    R = 6371000
    phi1, phi2 = math.radians(lat1), math.radians(lat2)
    dphi = math.radians(lat2 - lat1)
    dlambda = math.radians(lon2 - lon1)

    a = math.sin(dphi/2)**2 + math.cos(phi1)*math.cos(phi2)*math.sin(dlambda/2)**2
    return 2 * R * math.atan2(math.sqrt(a), math.sqrt(1 - a))


# -----------------------------
# 4. Determine direction
# -----------------------------
def get_direction(lat1, lon1, lat2, lon2):
    dlat = lat2 - lat1
    dlon = lon2 - lon1

    if abs(dlat) > abs(dlon):
        return "North" if dlat > 0 else "South"
    else:
        return "East" if dlon > 0 else "West"


# -----------------------------
# 5. Main logic (CLI version)
# -----------------------------
def main():
    user_lat, user_lng = get_user_location()
    phones = get_emergency_phones()

    if not phones:
        print("No emergency resources found in this area.")
        return

    nearest = min(
        phones,
        key=lambda p: distance_meters(user_lat, user_lng, p["lat"], p["lng"])
    )

    dist = distance_meters(user_lat, user_lng, nearest["lat"], nearest["lng"])
    walk_time = f"{round(dist / 80)} minute(s)"
    direction = get_direction(user_lat, user_lng, nearest["lat"], nearest["lng"])

    result = {
        "nearestSafetyPhone": {
            "name": nearest["name"],
            "distanceMeters": round(dist),
            "walkTime": walk_time,
            "direction": direction,
            "coordinates": {
                "lat": nearest["lat"],
                "lng": nearest["lng"]
            }
        },
        "message": f"Closest safety resource is {round(dist)} meters away. Walk {direction}."
    }

    print(json.dumps(result, indent=4))


if __name__ == "__main__":
    main()
