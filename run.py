from app import app
from flask import jsonify
from app.view.views import app


if __name__ == "__main__":
    app.run(debug=True)