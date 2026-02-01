# Nearest Safety Resource Finder

## Overview
This project integrates two public third‑party APIs to create a small application that identifies the nearest emergency resource based on the user’s approximate location. It was developed for the AD311 assignment on API integration.

The application uses:

- ipinfo.io for approximate geolocation  
- OpenStreetMap Overpass API for emergency resource data  

The program calculates the nearest resource and displays the result in a simple web interface.

---

## How the Application Works

The application retrieves the user’s approximate latitude and longitude from the ipinfo.io API.

It sends a query to the Overpass API to retrieve emergency‑related points of interest in the Seattle area.

It calculates:

- The nearest resource  
- Distance in meters  
- Cardinal direction  

The result is displayed in a simple Flask web interface in a readable vertical format.

---

## Setup Instructions

### 1. Clone the repository
```bash
git clone https://github.com/YOUR_USERNAME/nearest-safety-phone-finder
cd nearest-safety-phone-finder
```
### 2. Create and activate a virtual environment
```bash
python -m venv venv
venv\Scripts\activate
```
### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the application
```bash
python app.py
```

### 5. Open the interface
Visit:
```Code
http://127.0.0.1:5000
```
## Requirements
```text
requests
flask
```

## Documentation and Testing

### Testing Overview
The application was tested using a combination of normal and edge case scenarios to ensure reliability, accuracy, and proper error handling. A separate `test_app.py` script was created to manually validate the core logic, including distance calculations, direction determination, and nearest‑resource selection.

---

### Normal Test Cases

#### 1. Standard run using real location data  
Validated that the application correctly identifies the nearest emergency resource based on the user’s actual IP‑derived coordinates.

#### 2. Modified location (hardcoded)  
Simulated a different user location to confirm that the nearest resource changes appropriately.

#### 3. Multiple resources returned  
Ensured that when several emergency resources are available, the application selects the closest one based on distance.

---

### Edge Test Cases

#### 1. No resources returned  
Tested behavior when the Overpass API returns an empty list.  
**Expected:** Graceful message indicating no resources found.  
**Result:** Passed.

#### 2. API failure or invalid response  
Simulated a failure by passing `None` as the resource list.  
**Expected:** Function returns `None` without crashing.  
**Result:** Passed.

#### 3. Invalid or missing location data  
Passed `None` for latitude/longitude to simulate corrupted or missing location data.  
**Expected:** Error is raised and handled cleanly.  
**Result:** Passed.

---

### Test Script
A dedicated test file (`test_app.py`) was created to run all scenarios.  
It includes:

- Mock emergency resource data  
- Normal test cases  
- Edge test cases  
- Printed results for verification  

This ensures the core logic works independently of the Flask interface and external APIs.

## Write‑Up

### API Choice
I selected ipinfo.io because it provides simple, no‑auth geolocation data.  
I selected the Overpass API because it offers open access to emergency‑related map data.

### Functionality
The application retrieves the user’s approximate location, queries emergency resources, calculates the nearest one, and displays the result in a simple UI.

### Challenges
- Understanding Overpass query syntax
- Ensuring fallback categories for emergency resources
- Handling cases where APIs return no data
- Keeping the UI simple and readable

### Outcome
A functional application demonstrating integration of two third‑party APIs, proper data handling, and a simple user interface.
