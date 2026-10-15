from flask import Flask, request, render_template_string
from datetime import date

app = Flask(__name__)

appointments = []

HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Clinic Appointment Booking</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background: #eef5ff;
            margin: 0;
            padding: 30px 15px;
        }
        .container {
            background: white;
            max-width: 520px;
            margin: auto;
            padding: 25px;
            border-radius: 14px;
            box-shadow: 0 4px 15px #ccd5e0;
        }
        h1 { color: #1769aa; text-align: center; }
        p { text-align: center; color: #555; }
        label { display: block; margin-top: 14px; font-weight: bold; }
        input, select, button {
            width: 100%;
            padding: 11px;
            margin-top: 6px;
            box-sizing: border-box;
            border: 1px solid #ccc;
            border-radius: 6px;
        }
        button {
            background: #1769aa;
            color: white;
            border: none;
            margin-top: 20px;
            cursor: pointer;
            font-weight: bold;
        }
        button:hover { background: #0d4f85; }
        .message {
            background: #e2f7e8;
            color: #176b35;
            padding: 12px;
            border-radius: 6px;
            text-align: center;
        }
        .total { text-align: center; margin-top: 20px; }
    </style>
</head>
<body>
    <div class="container">
        <h1>Clinic Appointment Booking</h1>
        <p>Book your clinic visit online</p>

        {% if message %}
        <div class="message">{{ message }}</div>
        {% endif %}

        <form method="POST">
            <label>Patient Name</label>
            <input name="patient" required maxlength="100"
                   placeholder="Enter your full name">

            <label>Email Address</label>
            <input name="email" type="email" required
                   placeholder="Enter your email">

            <label>Select Doctor</label>
            <select name="doctor" required>
                <option value="">Choose a doctor</option>
                <option>General Physician</option>
                <option>Cardiologist</option>
                <option>Dermatologist</option>
            </select>

            <label>Appointment Date</label>
            <input name="date" type="date" min="{{ today }}" required>

            <label>Appointment Time</label>
            <input name="time" type="time" required>

            <button type="submit">Book Appointment</button>
        </form>

        <div class="total">
            Total bookings this session: <strong>{{ total }}</strong>
        </div>
    </div>
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def home():
    message = ""

    if request.method == "POST":
        patient = request.form["patient"].strip()
        email = request.form["email"].strip()
        doctor = request.form["doctor"]
        appointment_date = request.form["date"]
        appointment_time = request.form["time"]

        if appointment_date < date.today().isoformat():
            message = "Please select today or a future date."
        else:
            appointments.append({
                "patient": patient,
                "email": email,
                "doctor": doctor,
                "date": appointment_date,
                "time": appointment_time
            })
            message = "Appointment booked successfully!"

    return render_template_string(
        HTML,
        message=message,
        total=len(appointments),
        today=date.today().isoformat()
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
