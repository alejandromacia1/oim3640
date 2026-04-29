
from flask import Flask, render_template, request
from main import find_stop_near

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    error = None

    if request.method == "POST":
        place = request.form.get("place", "").strip()
        if place:
            station, wheelchair_status = find_stop_near(place)
            if station:
                result = {"place": place, "station": station, "accessible": wheelchair_status}
            else:
                error = f"No results found for '{place}'. Try a different address."

    return render_template("index.html", result=result, error=error)

if __name__ == "__main__":
    app.run(debug=True)