import time
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

STATE = {
    "on": False,
    "hex": "#ff0000",
    "r": 255,
    "g": 0,
    "b": 0,
    "brightness": 120,
    "updated_at": time.time()
}

def clamp(v, lo, hi):
    return max(lo, min(hi, v))

def hex_to_rgb(hex_str):
    s = hex_str.strip().lstrip("#")
    if len(s) != 6:
        return 255, 0, 0
    r = int(s[0:2], 16)
    g = int(s[2:4], 16)
    b = int(s[4:6], 16)
    return r, g, b

@app.get("/")
def home():
    return jsonify({
        "ok": True,
        "message": "Flask LED API running on Render",
        "routes": ["/api/state (GET)", "/api/set (POST)", "/api/off (POST)"]
    })

@app.get("/api/state")
def get_state():
    return jsonify({"ok": True, "state": STATE})

@app.post("/api/set")
def set_state():
    data = request.get_json(silent=True) or {}

    on = bool(data.get("on", True))
    hex_color = str(data.get("hex", "#ff0000"))
    brightness = int(data.get("brightness", STATE["brightness"]))
    brightness = clamp(brightness, 0, 255)

    r, g, b = hex_to_rgb(hex_color)

    STATE["on"] = on
    STATE["hex"] = hex_color
    STATE["r"] = r
    STATE["g"] = g
    STATE["b"] = b
    STATE["brightness"] = brightness
    STATE["updated_at"] = time.time()

    return jsonify({"ok": True, "state": STATE})

@app.post("/api/off")
def set_off():
    STATE["on"] = False
    STATE["updated_at"] = time.time()
    return jsonify({"ok": True, "state": STATE})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
