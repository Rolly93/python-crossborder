import os
import webview
import threading
from src.app import app

def run_flask():
    app.run(debug = False, port=5000)
    

if __name__ == "__main__":
    
    run_flask()
    flask_thread = threading.Thread(target = run_flask)
    flask_thread.daemon = True
    flask_thread.start()
    
    window = webview.create_window("Border Crossing App", "https://python-crossborder.onrender.com",height = 950)
    
    webview.start()
    
   