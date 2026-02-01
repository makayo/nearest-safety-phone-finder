Nearest Safety Resource Finder
Overview
This project integrates two public third‑party APIs to create a small application that identifies the nearest emergency resource based on the user’s approximate location. It was developed for the AD311 assignment on API integration.

The application uses:

ipinfo.io  for approximate geolocation

OpenStreetMap Overpass API for emergency resource data

The program calculates the nearest resource and displays the result in a simple web interface.

How the Application Works
The application retrieves the user’s approximate latitude and longitude from the ipinfo.io  API.

It sends a query to the Overpass API to retrieve emergency‑related points of interest in the Seattle area.

It calculates:

The nearest resource

Distance in meters

Cardinal direction

The result is displayed in a simple Flask web interface in a readable vertical format.

Setup Instructions
1. Clone the repository
bash
git clone https://github.com/YOUR_USERNAME/nearest-safety-phone-finder
cd nearest-safety-phone-finder
2. Create and activate a virtual environment
bash
python -m venv venv
venv\Scripts\activate
3. Install dependencies
bash
pip install -r requirements.txt
4. Run the application
bash
python app.py
5. Open the interface
Visit:

Code
http://127.0.0.1:5000
Requirements
Code
requests
flask
Documentation and Testing
Testing
Normal Test Cases
Standard run using real location data

Modified location (temporarily hardcoded) to verify different nearest results

Multiple resources returned → nearest one selected correctly

Edge Test Cases
No resources returned → displays appropriate message

API failure or timeout → error handled

Invalid or missing location data → handled gracefully

Write‑Up
API Choice
I selected ipinfo.io  because it provides simple, no‑auth geolocation data.
I selected the Overpass API because it offers open access to emergency‑related map data.

Functionality
The application retrieves the user’s approximate location, queries emergency resources, calculates the nearest one, and displays the result in a simple UI.

Challenges
Understanding Overpass query syntax

Ensuring fallback categories for emergency resources

Handling cases where APIs return no data

Keeping the UI simple and readable

Outcome
A functional application demonstrating integration of two third‑party APIs, proper data handling, and a simple user interface.