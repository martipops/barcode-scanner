from http.server import BaseHTTPRequestHandler, HTTPServer
from json import loads
from pyautogui import typewrite, hotkey, press
from socket import gethostname, gethostbyname
from time import sleep

server_port = 8869

hostname = gethostname()
ip_address = gethostbyname(hostname)

def receive_data(text):
    if text.startswith("T-"):
        hotkey('ctrl', 'l')
        hotkey('ctrl', 'a')
        text = "https://entertainmentrestoration.repairdesk.co/index.php?r=ticket/index&ticket[keyword]=" + text
        typewrite(text)
        press('enter')
        sleep(3)
        hotkey('ctrl', 'l')
        hotkey('ctrl', 'a')
        js = "editticket"
        typewrite(js)
        press('enter')

    else:
        typewrite(text)



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



def run(server_class=HTTPServer, handler_class=SimpleHTTPRequestHandler, port=server_port):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f'Starting server...')
    print(f"IP Address: {hostname}.local:{port}")
    if (not ip_address.startswith('127.')):
        print(f"Alternate IP Address: {ip_address}:{port}")
    httpd.serve_forever()

if __name__ == '__main__':
    run()

