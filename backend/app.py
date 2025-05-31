from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

from routes import *

if __name__ == '__main__':
    app.run(debug=True)
    import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=False, host="0.0.0.0", port=port)
