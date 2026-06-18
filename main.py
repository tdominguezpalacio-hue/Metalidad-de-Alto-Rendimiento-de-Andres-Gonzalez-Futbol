import os
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

PORT = int(os.environ.get("PORT", 8080))

class AppHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("REQUEST:", self.path)

        self.send_response(200)
        self.send_header("Content-Type", "text/plain")
        self.end_headers()
        self.wfile.write(b"HELLO FROM RAILWAY")

server = ThreadingHTTPServer(("0.0.0.0", PORT), AppHandler)

print("LISTENING ON", PORT)

server.serve_forever()
