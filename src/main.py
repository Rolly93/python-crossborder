import os
import time
import webview
import asyncio
from modules.shipment import Shipment
from modules.backend_js import Capture
class BorderCrossingApp:
    def __init__(self):
        self.login_html = None
        self.capture_window = None
        self.bordercross_window = None
        
        self.api_capture = Capture()
        self.html_root = os.path.join(os.path.dirname(__file__), 'web')

    def _load_html(self, filename):
        return os.path.abspath(os.path.join(self.html_root, filename))

    def display_capture_shipment(self, e):
        print("Capture shipment")
        html_capture = self._load_html('capture_shipment.html')
        self.capture_window = webview.create_window(
            "Capture Shipment",
            html_capture,
            width=256,
            height=480,
            frameless=True,
            draggable=True,
            js_api=self.api_capture
        )
        self._setup_capture_window_events()
    def get_html_file_name(html_file):
        #file_name = os.path.basename(html_file)
        asyncio.sleep(2)
        html_file.destroy()
        
        
    def display_bordercrossing(self , e):
        
        print("Border Table")
        html_border = self._load_html("bordercross.html")
        self.bordercross_window = webview.create_window("Track Border Crossing",html_border)
        time.sleep(2)
        self.login_html.destroy()
        if self.bordercross_window:
            btn_capture_ship = self.bordercross_window.dom.get_element("#btn-cature-shipment")
            if btn_capture_ship:
                btn_capture_ship.on('click', lambda e: self.display_capture_shipment(e))
        
    def _before_close_capture_shipment(self, button):
        
        # i need to reload my table 
        print("table reload it")
        
        self.capture_window.destroy()
            
    
    def _setup_capture_window_events(self):
        if self.capture_window:
            btn_close = self.capture_window.dom.get_element('#cancel')
            
            btn_capture = self.capture_window.dom.get_element('#capture')
            btn_capture.events.click += self._before_close_capture_shipment
            
            if btn_close:
                btn_close.on('click', lambda e: self.capture_window.destroy())
            

    def _setup_capture_shipment_window_events(self, window):
        if window:
            btn_capture_ship = window.dom.get_element("#btn-cature-shipment")
            
            if btn_capture_ship:
                btn_capture_ship.on('click', lambda e: self.display_capture_shipment(e))
                
    def _insert_data(self, data_shipmet ,):
        self.main_window.show()
        time.sleep(1)
    
    def _setup_main_window_events(self,window):
        if window:
            btn_login = window.dom.get_element("#login")
            if btn_login:
                
                btn_login.events.click += self.display_bordercrossing

        
    def run(self):
        html_path = self._load_html('login.html')
        self.login_html = webview.create_window("Loging", html_path , frameless=False,draggable=True)
        webview.start(self._setup_main_window_events, self.login_html)

if __name__ == '__main__':
    app = BorderCrossingApp()
    app.run()