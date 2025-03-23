from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import parse_qs
import datetime

MOODLE_LOGIN = "1149288"

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-Type', 'text/plain; charset=utf-8')
        self.end_headers()

        now = datetime.datetime.now()
        formatted_date_time = now.strftime("%d.%m.%y %H:%M:%S")

        response = f"{MOODLE_LOGIN}, {formatted_date_time}\n"

        self.wfile.write(response.encode('utf-8'))

httpd = HTTPServer(('0.0.0.0', 8080), SimpleHTTPRequestHandler)
print('serving')
try:
    httpd.serve_forever()
except KeyboardInterrupt:
    print("\nServer stopped.")