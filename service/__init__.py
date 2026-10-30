import sys
from flask import Flask
from flask_talisman import Talisman
from flask_cors import CORS

app = Flask(__name__)

# Initialize Talisman for Security Headers
talisman = Talisman(app)

# Initialize CORS
CORS(app)

@app.route("/")
def index():
    return {"status": "OK", "message": "Account service is running successfully"}, 200