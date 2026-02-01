# test_app.py
# Simple manual test runner for the Nearest Safety Resource Finder project

from main import find_nearest_resource


# ---------------------------------------------------------
# Helper: Mock resources for testing
# ---------------------------------------------------------
mock_resources = [
    {"lat": 47.7000, "lng": -122.3300, "name": "Emergency Phone A"},
    {"lat": 47.7100, "lng": -122.3200, "name": "Emergency Phone B"},
    {"lat": 47.7200, "lng": -122.3100, "name": "Emergency Phone C"},
]


# ---------------------------------------------------------
# Normal Test Cases
# ---------------------------------------------------------
def test_normal_real_location():
    user_lat = 47.7005
    user_lon = -122.3290
    nearest = find_nearest_resource(user_lat, user_lon, mock_resources)
    print("Normal Test 1 – Real location:", nearest)

def test_normal_modified_location():
    user_lat = 47.7150
    user_lon = -122.3150
    nearest = find_nearest_resource(user_lat, user_lon, mock_resources)
    print("Normal Test 2 – Modified location:", nearest)

def test_normal_multiple_resources():
    user_lat = 47.7050
    user_lon = -122.3250
    nearest = find_nearest_resource(user_lat, user_lon, mock_resources)
    print("Normal Test 3 – Multiple resources:", nearest)

# ---------------------------------------------------------
# Edge Test Cases
# ---------------------------------------------------------
def test_edge_no_resources():
    empty_list = []
    nearest = find_nearest_resource(47.7000, -122.3300, empty_list)
    print("Edge Test 1 – No resources:", nearest)

def test_edge_api_failure():
    try:
        # Simulate failure by passing None
        nearest = find_nearest_resource(47.7000, -122.3300, None)
        print("Edge Test 2 – API failure:", nearest)
    except Exception as e:
        print("Edge Test 2 – API failure handled:", str(e))

def test_edge_invalid_location():
    try:
        nearest = find_nearest_resource(None, None, mock_resources)
        print("Edge Test 3 – Invalid location:", nearest)
    except Exception as e:
        print("Edge Test 3 – Invalid location handled:", str(e))

# ---------------------------------------------------------
# Run all tests
# ---------------------------------------------------------
if __name__ == "__main__":
    print("\n--- Running Normal Test Cases ---")
    test_normal_real_location()
    test_normal_modified_location()
    test_normal_multiple_resources()

    print("\n--- Running Edge Test Cases ---")
    test_edge_no_resources()
    test_edge_api_failure()
    test_edge_invalid_location()

    print("\nAll tests completed.\n")
