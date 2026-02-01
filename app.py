from flask import Flask, render_template_string, request
from main import get_user_location, get_emergency_phones, distance_meters, get_direction

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>Nearest Safety Resource</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background: #fafafa;
            margin: 0;
            padding: 0;
        }
        .container {
            max-width: 600px;
            margin: 40px auto;
            background: white;
            padding: 25px;
            border-radius: 10px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.08);
        }
        h2 {
            margin-top: 0;
            color: #333;
        }
        button {
            background: #0078ff;
            color: white;
            padding: 10px 18px;
            border: none;
            border-radius: 6px;
            cursor: pointer;
            font-size: 15px;
        }
        button:hover {
            background: #005fcc;
        }
        .result {
            margin-top: 20px;
            padding: 15px;
            background: #f1f5fb;
            border-radius: 8px;
            line-height: 1.6;
        }
        .label {
            font-weight: bold;
            color: #222;
        }
    </style>
</head>

<body>
    <div class="container">
        <h2>Nearest Safety Resource Finder</h2>

        <form method="POST">
            <button type="submit">Find Nearest Resource</button>
        </form>

        {% if result %}
            <div class="result">
                <div><span class="label">Name:</span> {{ result.name }}</div>
                <div><span class="label">Distance:</span> {{ result.distanceMeters }} meters</div>
                <div><span class="label">Direction:</span> {{ result.direction }}</div>
                <div><span class="label">Latitude:</span> {{ result.coordinates.lat }}</div>
                <div><span class="label">Longitude:</span> {{ result.coordinates.lng }}</div>
            </div>
        {% endif %}
    </div>
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def index():
    result = None

    if request.method == "POST":
        try:
            user_lat, user_lng = get_user_location()
            phones = get_emergency_phones()

            if phones:
                nearest = min(
                    phones,
                    key=lambda p: distance_meters(user_lat, user_lng, p["lat"], p["lng"])
                )

                dist = distance_meters(user_lat, user_lng, nearest["lat"], nearest["lng"])
                direction = get_direction(user_lat, user_lng, nearest["lat"], nearest["lng"])

                result = {
                    "name": nearest["name"],
                    "distanceMeters": round(dist),
                    "direction": direction,
                    "coordinates": {
                        "lat": nearest["lat"],
                        "lng": nearest["lng"]
                    }
                }
            else:
                result = {"error": "No emergency resources found."}

        except Exception as e:
            result = {"error": str(e)}

    return render_template_string(HTML, result=result)

if __name__ == "__main__":
    app.run(debug=True)
