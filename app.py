from flask import Flask, jsonify, request
import random

app = Flask(__name__)

# Global variable to store the tracking state
is_tracking_active = False

@app.route('/api/tracking', methods=['POST'])
def update_tracking():
    global is_tracking_active
    data = request.get_json()
    is_tracking_active = data.get('tracking', False)
    
    # You can trigger your ESP32 or hardware scripts to start/stop here
    print(f"Tracking state updated: {is_tracking_active}")
    
    return jsonify({"success": True, "tracking": is_tracking_active})

@app.route('/api/data')
def get_sensor_data():
    # If the user hasn't clicked "Start Tracking", return an idle state
    if not is_tracking_active:
        return jsonify({
            "status": "Idle",
            "heart_rate": "--",
            "exercise": "Resting",
            "reps": 0,
            "form_feedback": "N/A"
        })

    # Generate mock data only when tracking is active
    exercises = ["Bicep Curl", "Bench Press", "Jumping Jacks", "Resting"]
    current_exercise = random.choice(exercises)
    
    # Simulate form feedback based on whether they are resting or active
    form_feedback = "N/A"
    if current_exercise != "Resting":
        form_feedback = random.choice(["Perfect form", "Too fast", "Extend fully", "Elbows flaring"])
        
    return jsonify({
        "status": "Connected (ESP32 Mock)",
        "heart_rate": random.randint(65, 145), # Mocking MAX30102
        "exercise": current_exercise,
        "reps": random.randint(0, 15),
        "form_feedback": form_feedback
    })

if __name__ == '__main__':
    # Using 127.0.0.1 is fine if Nginx on the Pi is reverse-proxying to port 5000. 
    # Change to '0.0.0.0' if Nginx needs to hit it via the local network IP.
    app.run(host='127.0.0.1', port=5000)
