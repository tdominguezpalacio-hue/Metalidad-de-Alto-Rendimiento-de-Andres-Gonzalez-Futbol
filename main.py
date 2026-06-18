import os

print("PYTHON STARTED")

from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

HOST = "0.0.0.0"
PORT = int(os.environ.get("PORT", 8000))

class AppHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"HELLO FROM RAILWAY")

server = ThreadingHTTPServer((HOST, PORT), AppHandler)

print("SERVER STARTING ON", PORT)

server.serve_forever()




