import time
import webview
import threading

from api_server import start_server, API_PORT 


def run_pywebview():
    """
    Launches the pywebview window, pointing it to the Flask server's URL.
    """
    # The URL is the local address where the Flask server is running
    app_url = f'http://127.0.0.1:{API_PORT}'
    print(f"Pywebview loading content from: {app_url}")

    window = webview.create_window(
        'Gestión de Cruces',  # The title of the desktop window
        url=app_url,
        width=1200,
        height=800,
        min_size=(800, 600)
    )
    # webview.start() is a blocking call and must be the last command in the main thread
    webview.start()

if __name__ == '__main__':
    # 1. Start the Flask server in a background thread.
    # daemon=True ensures the server stops when the main pywebview window is closed.
    server_thread = threading.Thread(target=start_server, daemon=True)
    server_thread.start()
    
    # 2. Wait for a moment (1 second) to ensure Flask has fully initialized before pywebview connects
    time.sleep(1)
    
    # 3. Launch the pywebview window
    run_pywebview()
