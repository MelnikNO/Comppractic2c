from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs
import datetime
import json

MOODLE_LOGIN = "1149288"

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def load_html(self, filename):
        try:
            with open(f'templates/{filename}', 'r', encoding='utf-8') as f:
                return f.read()
        except FileNotFoundError:
            return "<h1>Error: File not found</h1>"

    def do_GET(self):
        path = self.path
        if path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/html; charset=utf-8')
            self.end_headers()
            form = self.load_html('form.html')
            self.wfile.write(form.encode('utf-8'))

        else:
            self.send_response(404)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b"Not found")

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length).decode('utf-8')
        data = parse_qs(post_data)
        login = MOODLE_LOGIN
        time = datetime.datetime.now().isoformat()

        # Сохраняем данные в файл
        with open('index.json', 'a') as f:
            json.dump({'login': login, 'time': time}, f)
            f.write('\n')

        self.send_response(200)
        self.send_header('Content-type', 'text/html; charset=utf-8')
        self.end_headers()
        success_message = self.load_html('success.html').format(login=login, time=time)
        self.wfile.write(success_message.encode('utf-8'))


port = 8080
httpd = HTTPServer(('', port), SimpleHTTPRequestHandler)
print (f"Сервер запущен на порту {port}")
try:
    httpd.serve_forever()
except KeyboardInterrupt:
    print ("Сервер остановлен")