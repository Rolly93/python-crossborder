import os
import json
from flask import Flask, jsonify, send_from_directory

# Define the port and the path to the data file
API_PORT = 5000 

# --- 1. SETUP FLASK APPLICATION ---
# Point Flask to the React build 'dist' folder for serving the frontend
app = Flask(__name__, static_folder='dist', static_url_path='')


# --- 3. FLASK SERVING STATIC FILES (REACT) ---
@app.route('/')
def serve_index():
    """
    The main route serves the built index.html from the 'dist' folder.
    This is what pywebview will load when it hits the root URL.
    """
    return send_from_directory(app.static_folder, 'index.html')


# --- 4. SERVER START FUNCTION ---
def start_server():
    """
    Runs the Flask server. This function is called from the main launcher file.
    """
    print(f"Flask server starting on http://127.0.0.1:{API_PORT}")
    # Runs the server locally, accessible only from the machine
    # We use app=app and host/port defined globally for simplicity in this decoupled structure
    app.run(host='127.0.0.1', port=API_PORT, threaded=True, debug=False)

if __name__ == '__main__':
    # Allows running this file directly for API development/testing
    #start_server()
        app.run(host='127.0.0.1', port=API_PORT, threaded=True, debug=True)