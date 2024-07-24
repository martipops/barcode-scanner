import tkinter as tk
import threading
import time
from http.server import BaseHTTPRequestHandler, HTTPServer
from json import loads
from pyautogui import typewrite, hotkey, press
from socket import gethostname, gethostbyname
import webbrowser
import configparser
import os

server_port = 8869

hostname = gethostname()
ip_address = gethostbyname(hostname)

advanced_features = True
config_file = 'settings.ini'

def create_default_config():
    config = configparser.ConfigParser()
    config['Settings'] = {'advanced_features': 'false'}
    with open(config_file, 'w') as file:
        config.write(file)

def load_config(variable):
    global advanced_features
    config = configparser.ConfigParser()
    if not os.path.exists(config_file):
        create_default_config()
    config.read(config_file)
    advanced_features = config.getboolean('Settings', variable)
    return advanced_features


def update_config(variable, new_value):
    global advanced_features
    config = configparser.ConfigParser()
    if not os.path.exists(config_file):
        create_default_config()
    config.read(config_file)
    config.set('Settings', variable, new_value)
    with open(config_file, 'w') as file:
        config.write(file)

def open_help():
    webbrowser.open_new_tab('https://gist.github.com/martipops/cf0df5bcd92844905722e57efe266365')

def receive_data(text):
    print("ADVANCED:", advanced_features)
    if (not text.startswith("T-")) or (not advanced_features):
        typewrite(text)
    else:
        hotkey('ctrl', 'l')
        hotkey('ctrl', 'a')
        text = "https://entertainmentrestoration.repairdesk.co/index.php?r=ticket/index&ticket[keyword]=" + text
        typewrite(text)
        press('enter')
        time.sleep(3)
        hotkey('ctrl', 'l')
        hotkey('ctrl', 'a')
        js = "editticket"
        typewrite(js)
        press('enter')

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        data = loads(post_data)
        print(f"Received data: {data}")
        
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(b'POST request received!')

        receive_data(data['text'])


def run_server():
    server_address = ('', server_port)
    httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)
    print(f'Starting server...')
    print(f"IP Address: {hostname}.local:{server_port}")
    if (not ip_address.startswith('127.')):
        print(f"Alternate IP Address: {ip_address}:{server_port}")
    httpd.serve_forever()


def infinite_loop(checkbox_var):
    while True:
        state = "enabled" if checkbox_var.get() else "disabled"
        print(f"Running in the background... {state}")
        time.sleep(1)


def create_app():
    global advanced_features
    def on_checkbutton_toggle():
        # This function will be called whenever the checkbox is toggled
        global advanced_features
        if checkbox_var.get():
            advanced_features = True
            print("Advanced features enabled")
        else:
            advanced_features = False
            print("Advanced features disabled")
        update_config('advanced_features', str(advanced_features).lower())

    # Create the main window
    root = tk.Tk()
    root.title("Barcode Scanner Server")

    checkbox_var = tk.BooleanVar(value=advanced_features)
    label_var = tk.StringVar(value="Advanced features disabled")

    motd_label = tk.Label(root, text="Server Started!")
    ip_text = f"IP Address:  {hostname}.local:{server_port}"
    if (not ip_address.startswith('127.')):
        ip_text +=  f"\nAlternate IP:  {ip_address}:{server_port}"
    ip_label = tk.Label(root, text=ip_text)


    help_button = tk.Button(root, text="Helpful Info", command=open_help)
    quit_button = tk.Button(root, text="Quit", command=root.quit)

    checkbox = tk.Checkbutton(root, text="Advanced Features", variable=checkbox_var, command=on_checkbutton_toggle)

    motd_label.pack(padx=10, pady=10)
    ip_label.pack(padx=10, pady=10)
    checkbox.pack(padx=10, pady=10)
    help_button.pack(padx=10, pady=10)
    quit_button.pack(padx=10, pady=10)

    loop_thread = threading.Thread(target=run_server)
    loop_thread.daemon = True  # Daemonize thread to close with the main program
    loop_thread.start()

    root.mainloop()


if __name__ == "__main__":
    config_file = 'config.ini'
    advanced_features = load_config('advanced_features')
    print(f'Advanced Feature: {advanced_features}')
    create_app()
