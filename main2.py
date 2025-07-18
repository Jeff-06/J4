import requests
import datetime

API_KEY = "API-KEY "  # Replace with your actual API key

url = f"https://routes.googleapis.com/directions/v2:computeRoutes?key={API_KEY}"

headers = {
    "Content-Type": "application/json",
    "X-Goog-FieldMask": "routes.duration,routes.distanceMeters,routes.legs",
}

# Add 2 minutes to current UTC time to ensure it's in the future
departure_time = (datetime.datetime.utcnow() + datetime.timedelta(minutes=2)).isoformat("T") + "Z"

body4 = {
    "origin": {
        "location": {
            "latLng": {
                "latitude": 9.9930983,
                "longitude": 76.3584460
            }
        }
    },
    "intermediates": [
        {
            "location": {
                "latLng": {
                    "latitude": 10.0572396,
                    "longitude": 76.3935822
                }
            }
        }
    ],
    "destination": {
        "location": {
            "latLng": {
                "latitude": 10.0894462,
                "longitude": 76.3886449
            }
        }
    },
    "travelMode": "DRIVE",
    "routingPreference": "TRAFFIC_AWARE_OPTIMAL",
    "departureTime": departure_time
}
body1 = {
    "origin": {
        "location": {
            "latLng": {
                "latitude": 9.9930983,
                "longitude": 76.3584460
            }
        }
    },
    "intermediates": [
        {
            "location": {
                "latLng": {
                    "latitude": 10.1004225,
                    "longitude": 76.3503436
                }
            }
        }
    ],
    "destination": {
        "location": {
            "latLng": {
                "latitude": 10.0894462,
                "longitude": 76.3886449
            }
        }
    },
    "travelMode": "DRIVE",
    "routingPreference": "TRAFFIC_AWARE_OPTIMAL",
    "departureTime": departure_time
}

for body in [body4,body1]:
    response = requests.post(url, headers=headers, json=body)

    if response.status_code == 200:
        data = response.json()
        route = data["routes"][0]
        total_distance = route["distanceMeters"]
        total_duration_seconds = int(route["duration"].rstrip("s"))

        print(f"Total Distance: {total_distance / 1000:.2f} km")
        print(f"Estimated Time with Traffic: {str(datetime.timedelta(seconds=total_duration_seconds))}")

        print("\nLeg-wise Breakdown:")
        for i, leg in enumerate(route["legs"]):
            leg_distance = leg["distanceMeters"]
            leg_duration = int(leg["duration"].rstrip("s"))
            print(f"  Leg {i+1}: {leg_distance / 1000:.2f} km in {str(datetime.timedelta(seconds=leg_duration))}")

    else:
        print("Error:", response.text)
