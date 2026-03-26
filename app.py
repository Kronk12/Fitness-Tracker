from flask import Flask, jsonify
import random

app = Flask(__name__)

@app.route('/api/data')
def get_sensor_data():
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
    app.run(host='127.0.0.1', port=5000)
